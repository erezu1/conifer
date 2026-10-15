// Conifer: search in the paper, after Epsilon's rules. Words are found in the text as a browser finds them; a query
// with TeX in it (\phi, x^2, \frac{1}{2}) is looked for in the formulas' TeX (each drawn formula carries its TeX as
// data-tex); a symbol by name (phi, \phi) or typed (φ) is found in every formula that draws it; spellings that mean
// the same are one (\le and \leq, \to and \rightarrow, \epsilon and \varepsilon, <= and \leq); \left, \right and
// sizes do not count; a letter asked for plainly is found in any font, with any accent or prime; ? stands for any one
// symbol and {?} for anything in braces; $...$ searches the formulas only. Enter and the arrows step through the
// places found; Escape closes.
(function () {
  'use strict';
  const $ = (s, el) => (el || document).querySelector(s);
  const $$ = (s, el) => Array.from((el || document).querySelectorAll(s));
  const reEsc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const GREEK = { 'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta', 'ϵ': 'epsilon', 'ε': 'varepsilon', 'ζ': 'zeta', 'η': 'eta', 'θ': 'theta', 'ϑ': 'vartheta',
    'ι': 'iota', 'κ': 'kappa', 'λ': 'lambda', 'μ': 'mu', 'ν': 'nu', 'ξ': 'xi', 'π': 'pi', 'ρ': 'rho', 'σ': 'sigma', 'ς': 'varsigma', 'τ': 'tau', 'υ': 'upsilon',
    'ϕ': 'phi', 'φ': 'varphi', 'χ': 'chi', 'ψ': 'psi', 'ω': 'omega', 'Γ': 'Gamma', 'Δ': 'Delta', 'Θ': 'Theta', 'Λ': 'Lambda', 'Ξ': 'Xi', 'Π': 'Pi', 'Σ': 'Sigma',
    'Υ': 'Upsilon', 'Φ': 'Phi', 'Ψ': 'Psi', 'Ω': 'Omega', 'ℓ': 'ell', 'ℏ': 'hbar', '∂': 'partial', '∇': 'nabla', '∞': 'infty' };
  const NAMES = new Set(Object.values(GREEK));
  const SAME = { le: 'leq', ge: 'geq', ne: 'neq', rightarrow: 'to', leftarrow: 'gets', varepsilon: 'epsilon', varphi: 'phi', vartheta: 'theta', varrho: 'rho',
    varsigma: 'sigma', varpi: 'pi', varkappa: 'kappa', dfrac: 'frac', tfrac: 'frac', hslash: 'hbar', varnothing: 'emptyset', lvert: '|', rvert: '|' };
  const UNI = { '≤': '\\leq ', '≥': '\\geq ', '≠': '\\neq ', '→': '\\to ', '←': '\\gets ', '×': '\\times ', '·': '\\cdot ', '±': '\\pm ', '∑': '\\sum ', '∫': '\\int ',
    '√': '\\sqrt', '∞': '\\infty ', '∂': '\\partial ', '∇': '\\nabla ', '≈': '\\approx ', '∼': '\\sim ', '≡': '\\equiv ', '∈': '\\in ', '⊂': '\\subset ', '−': '-',
    '≪': '\\ll ', '≫': '\\gg ', '≃': '\\simeq ', '∝': '\\propto ', '⟨': '\\langle ', '⟩': '\\rangle ', '⋅': '\\cdot ', '∘': '\\circ ', '†': '\\dagger ', '⊗': '\\otimes ', '⊕': '\\oplus ', '∧': '\\wedge ', '∨': '\\vee ', '¬': '\\neg ', 'ℝ': '\\mathbb{R}', 'ℤ': '\\mathbb{Z}', 'ℂ': '\\mathbb{C}', '²': '^2', '³': '^3', '⁴': '^4', '⁰': '^0', '¹': '^1', '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 'ⁿ': '^n', 'ᵢ': '_i', 'ⱼ': '_j' };
  const SIZES = /\\(left|right|big|Big|bigg|Bigg|bigl|bigr|Bigl|Bigr|biggl|biggr|Biggl|Biggr|,|;|!|quad|qquad|displaystyle|textstyle|scriptstyle|nolimits|limits)(?![A-Za-z])/g;
  const FONTS = 'mathcal|mathbb|mathfrak|mathscr|boldsymbol|bm|mathbf|mathsf|mathtt|mathit|mathrm|operatorname|text|textrm';
  const ACCS = 'hat|bar|tilde|vec|dot|ddot|check|breve|acute|grave|widehat|widetilde|overline|underline|mathring';
  const FONTED = new RegExp('\\\\(' + FONTS + ')\\{([^{}]*)\\}', 'g'), ACCENTED = new RegExp('\\\\(' + ACCS + ')\\{([^{}]*)\\}', 'g');
  const HAS_FONT = new RegExp('\\\\(' + FONTS + ')\\{'), HAS_ACC = new RegExp('\\\\(' + ACCS + ')\\{');
  const PRIMED = /'+|\^\\prime(?![A-Za-z])|\\prime(?![A-Za-z])/g;
  const GROUP = '\\{(?:[^{}]|\\{(?:[^{}]|\\{[^{}]*\\})*\\})*\\}', TOKEN = '(?:\\\\[A-Za-z]+|' + GROUP + '|[^{}\\\\])';

  function uniTeX(q) {                              // typed symbols as TeX
    return q.replace(/[^\x00-\x7f]/g, ch => GREEK[ch] ? '\\' + GREEK[ch] + ' ' : UNI[ch] || ch);
  }
  const normed = new Map();
  function texNorm(t) {
    t = t || '';
    if (normed.has(t)) return normed.get(t);
    let s = uniTeX(t).replace(/<=/g, '\\leq ').replace(/>=/g, '\\geq ').replace(/!=/g, '\\neq ').replace(SIZES, '');
    s = s.replace(/\\([A-Za-z]+)(?![A-Za-z])/g, (x, n) => n === 'lt' ? '<' : n === 'gt' ? '>' : SAME[n] ? '\\' + SAME[n] : x);
    s = s.replace(/\\frac(?![A-Za-z])\s*(\d|\\[A-Za-z]+|[^{\\\s])\s*(\d|\\[A-Za-z]+|[^{\\\s])/g, '\\frac{$1}{$2}');    // \frac12: \frac{1}{2}
    s = s.replace(/(\\[A-Za-z]+)\s+(?=[A-Za-z])/g, '$1\u0001').replace(/\s+/g, '').replace(/\u0001/g, ' ');
    s = s.replace(/([_^])\{([^{}\\]|\\[A-Za-z]+)\}/g, '$1$2');
    s = s.replace(/\\sqrt(?![A-Za-z])(\[[^\]]*\])?(\\[A-Za-z]+|[^{\\\s])/g, '\\sqrt$1{$2}');
    if (normed.size > 20000) normed.clear();
    normed.set(t, s);
    return s;
  }
  function plainly(t, q) {                          // the formula's TeX as a plain query reads it
    if (!HAS_FONT.test(q)) t = t.replace(FONTED, '$2');
    if (!HAS_ACC.test(q)) for (let k = 0; k < 3; k++) t = t.replace(ACCENTED, '$2');
    if (!/'|\\prime/.test(q)) t = t.replace(PRIMED, '');
    return t.replace(/([_^])\{([^{}\\]|\\[A-Za-z]+)\}/g, '$1$2');
  }
  function texHas(tex, q) {
    q = texNorm(q);
    const t = plainly(texNorm(tex), q);
    if (q.indexOf('?') >= 0) {
      return new RegExp(q.split('{?}').map(part => part.split('?').map(reEsc).join(TOKEN)).join(GROUP)).test(t);
    }
    let i = t.indexOf(q);
    while (i >= 0) {
      if (!(/\\[A-Za-z]+$/.test(q) && /[A-Za-z]/.test(t.charAt(i + q.length)))) return true;    // \phi is not the start of \phiup
      i = t.indexOf(q, i + 1);
    }
    return false;
  }
  // what a query asks for: words in the text, TeX in the formulas, or both
  function what(q) {
    q = q.trim();
    if (!q) return null;
    const dm = /^\\\[([\s\S]*)\\\]$/.exec(q);
    if (dm) q = '$' + dm[1] + '$';
    const parts = []; let last = 0, fm; const FORM = /\$([^$]+)\$/g;
    while ((fm = FORM.exec(q))) { if (q.slice(last, fm.index).trim()) parts.push({ t: q.slice(last, fm.index).trim() }); parts.push({ f: fm[1] }); last = FORM.lastIndex; }
    if (q.slice(last).trim() && parts.length) parts.push({ t: q.slice(last).trim() });
    if (parts.length > 1) return { mixed: parts };
    if (q.charAt(0) === '$') {                      // "$...": the formulas only
      q = q.slice(1).replace(/\$$/, '').trim();
      if (!q) return null;
      q = uniTeX(q).trim();
      if (NAMES.has(q)) q = '\\' + q;
      return { tex: q };
    }
    if (GREEK[q]) return { tex: '\\' + GREEK[q], text: null };
    const u = uniTeX(q).trim();
    const cmd = /^\\([A-Za-z]+)$/.exec(u);
    if (cmd) return { tex: u };
    if (/[\\^_{}]/.test(u)) return { tex: u };
    const w = { text: q.replace(/[^A-Za-z]/g, '').length >= 3 || (/[^A-Za-z\s]/.test(q) && q.length >= 2) ? q.toLowerCase() : null };
    if (NAMES.has(q)) w.tex = '\\' + q;             // "phi": the word, and the symbol
    else if (/[^A-Za-z\s]/.test(q)) w.tex = q.replace(/\s+/g, '');   // "O(N)", "a+b": in the text, and in the formulas
    if (!w.text && !w.tex) return null;
    return w;
  }

  // ------------------------------------------------------------------ a symbol where it stands in a formula
  // (Epsilon's rule) A single symbol, or a short run of TeX, is found in each formula's drawing, glyph by glyph (MathJax
  // writes each glyph's code as data-c), and marked just where it stands; longer or stranger TeX marks the formulas
  // whose TeX has it, whole. A letter asked for plainly is found in any font; an accent or a prime not asked for is
  // passed over (B>1 finds \bar{B}>1 and B'>1).
  const GLYPH = { alpha: '1D6FC', beta: '1D6FD', gamma: '1D6FE', delta: '1D6FF', epsilon: '1D716', varepsilon: '1D700', zeta: '1D701',
    eta: '1D702', theta: '1D703', vartheta: '1D717', iota: '1D704', kappa: '1D705', varkappa: '1D718', lambda: '1D706', mu: '1D707',
    nu: '1D708', xi: '1D709', pi: '1D70B', varpi: '1D71B', rho: '1D70C', varrho: '1D71A', sigma: '1D70E', varsigma: '1D70D',
    tau: '1D70F', upsilon: '1D710', phi: '1D719', varphi: '1D711', chi: '1D712', psi: '1D713', omega: '1D714', Gamma: '393',
    Delta: '394', Theta: '398', Lambda: '39B', Xi: '39E', Pi: '3A0', Sigma: '3A3', Upsilon: '3A5', Phi: '3A6', Psi: '3A8',
    Omega: '3A9', ell: '2113', hbar: '210F', hslash: '210F', partial: '1D715', nabla: '2207', infty: '221E', aleph: '2135',
    emptyset: '2205', varnothing: '2205' };
  const OPS = { cdot: '22C5', times: 'D7', pm: 'B1', mp: '2213', sum: '2211', int: '222B', prod: '220F', oint: '222E', sqrt: '221A',
    langle: '27E8', rangle: '27E9', dagger: '2020', ldots: '2026', cdots: '22EF', to: '2192', rightarrow: '2192', leftarrow: '2190', gets: '2190',
    leq: '2264', le: '2264', geq: '2265', ge: '2265', neq: '2260', ne: '2260', approx: '2248', sim: '223C', simeq: '2243', equiv: '2261',
    propto: '221D', otimes: '2297', oplus: '2295', wedge: '2227', vee: '2228', cap: '2229', cup: '222A', in: '2208', ll: '226A', gg: '226B',
    subset: '2282', mid: '2223', prime: '2032', star: '22C6', ast: '2217', circ: '2218', bullet: '2219' };
  const QUIET = /^(frac|dfrac|tfrac|mathrm|mathit|mathbf|mathsf|text|textrm|operatorname|left|right|big|Big|bigg|Bigg|bigl|bigr|Bigl|Bigr|,|;|!|quad|qquad|displaystyle|textstyle|scriptstyle|nolimits|limits)$/;
  const SYM = { '+': '2B', '-': '2212', '=': '3D', '(': '28', ')': '29', '[': '5B', ']': '5D', ',': '2C', ';': '3B', ':': '3A', '!': '21',
    '/': '2F', '<': '3C', '>': '3E', '|': '7C', "'": '2032', '*': '2217', '.': '2E' };
  const OPNAME = /^(log|ln|lg|exp|sin|cos|tan|cot|sec|csc|sinh|cosh|tanh|coth|arcsin|arccos|arctan|det|dim|ker|deg|hom|lim|liminf|limsup|max|min|sup|inf|arg|gcd|Pr|Tr|tr)$/;
  const FONTCMD = /^(mathcal|mathbb|mathfrak|mathscr|boldsymbol|bm|mathbf|mathsf|mathtt|mathit|mathrm|operatorname)$/;
  const ODD = { mathbb: { C: '2102', H: '210D', N: '2115', P: '2119', Q: '211A', R: '211D', Z: '2124' },
    mathfrak: { C: '212D', H: '210C', I: '2111', R: '211C', Z: '2128' },
    mathscr: { B: '212C', E: '2130', F: '2131', H: '210B', I: '2110', L: '2112', M: '2133', R: '211B', e: '212F', g: '210A', o: '2134' } };
  const FROM = { mathbb: [0x1D538, 0x1D552, 0x1D7D8], mathfrak: [0x1D504, 0x1D51E], mathscr: [0x1D49C, 0x1D4B6],
    mathbf: [0x1D400, 0x1D41A, 0x1D7CE], boldsymbol: [0x1D468, 0x1D482, 0x1D7CE], bm: [0x1D468, 0x1D482, 0x1D7CE],
    mathsf: [0x1D5A0, 0x1D5BA, 0x1D7E2], mathtt: [0x1D670, 0x1D68A, 0x1D7F6] };
  const hex = c => c.toString(16).toUpperCase();
  function alts(name) {                             // the codes a command may draw (\epsilon: ϵ and ε; \le: ≤)
    const one = SAME[name] || name, out = [];
    [one].concat(Object.keys(SAME).filter(k => SAME[k] === one)).forEach(n => { const c = GLYPH[n] || OPS[n]; if (c && out.indexOf(c) < 0) out.push(c); });
    return out;
  }
  function fontGlyph(font, c) {
    const k = c.charCodeAt(0), plain = hex(k), at = c <= '9' ? 2 : c < 'a' ? 0 : 1, base = FROM[font] && FROM[font][at];
    const codes = [plain], off = k - (at === 2 ? 48 : at === 0 ? 65 : 97);
    if (ODD[font] && ODD[font][c]) codes.push(ODD[font][c]);
    else if (base) codes.push(hex(base + off));
    if (font === 'boldsymbol' || font === 'bm') codes.push(hex(FROM.mathbf[at] + off));
    if (font === 'mathit' && at < 2) codes.push(hex((at ? 0x1D44E : 0x1D434) + off));
    return codes;
  }
  function glyphsOf(q) {                            // the glyphs q draws, in order; null when it has something this cannot tell
    const out = []; let i = 0, m, fontTo = -1, font = '';
    const groupEnd = from => { let d = 0, e = from; for (; e < q.length; e++) { if (q.charAt(e) === '{') d++; else if (q.charAt(e) === '}' && !--d) break; } return e; };
    while (i < q.length) {
      const c = q.charAt(i);
      if ((m = /^\\([A-Za-z]+|.)/.exec(q.slice(i)))) {
        const name = m[1]; i += m[0].length;
        if (FONTCMD.test(name)) {
          font = name === 'operatorname' ? 'mathrm' : name;
          fontTo = q.charAt(i) === '{' ? groupEnd(i) : i + 1;
          continue;
        }
        if (name === 'sqrt') {                      // a root is drawn with what is under it first, then the sign (then its index)
          let idx = '', body;
          if (q.charAt(i) === '[') { const cl = q.indexOf(']', i); if (cl < 0) return null; idx = q.slice(i + 1, cl); i = cl + 1; }
          if (q.charAt(i) === '{') { const e = groupEnd(i); body = q.slice(i + 1, e); i = e + 1; }
          else if ((m = /^(\\[A-Za-z]+|.)/.exec(q.slice(i)))) { body = m[1]; i += m[0].length; }
          const bg = body ? glyphsOf(body) : [], ig = idx ? glyphsOf(idx) : [];
          if (!bg || !ig) return null;
          out.push(...bg, alts('sqrt'), ...ig);
          continue;
        }
        if (GLYPH[name]) out.push(alts(name));
        else if (OPNAME.test(name)) { for (const ch of name) out.push([hex(ch.charCodeAt(0))]); }
        else if (OPS[name]) out.push(alts(name));
        else if (name === '{' || name === '}') out.push([hex(name.charCodeAt(0))]);
        else if (!QUIET.test(name)) return null;
        continue;
      }
      i++;
      if (c === '?') { out.push(['*']); continue; }
      if (i - 1 < fontTo && /[A-Za-z0-9]/.test(c)) { out.push(fontGlyph(font, c)); continue; }
      if (/[A-Za-z]/.test(c)) {
        const k = c.charCodeAt(0), it = c === 'h' ? '210E' : hex(c < 'a' ? 0x1D434 + k - 65 : 0x1D44E + k - 97);
        out.push([it, hex(k)].concat(Object.keys(FROM).map(f => fontGlyph(f, c)[1])));   // (and in any font)
      } else if (/[0-9]/.test(c)) out.push([hex(c.charCodeAt(0))]);
      else if (SYM[c]) out.push([SYM[c]].concat(c === '-' ? ['2D'] : c === '|' ? ['2223'] : []));
      else if (/[\s_^{}&~]/.test(c)) continue;
      else return null;
    }
    return out.length ? out : null;
  }
  const ACC_C = /^(5E|7E|AF|2C9|2D9|A8|2C7|2D8|B4|60|2C6|2DC|20D7)$/;
  // the places q is drawn in a formula: each a run of its glyph elements; [] when none, null when q is not glyph-searchable
  function glyphRuns(f, q) {
    const qn = texNorm(q), seq = glyphsOf(qn);
    if (!seq) return null;
    const plainAcc = !HAS_ACC.test(qn), plainPrime = !/'|\\prime/.test(qn), single = seq.length === 1;
    const over = c => (plainAcc && ACC_C.test(c)) || (plainPrime && c === '2032');
    const gl = f.querySelectorAll('[data-c]'), all = Array.from(gl, g => g.getAttribute('data-c'));
    const idx = []; for (let k = 0; k < all.length; k++) if (single || !over(all[k])) idx.push(k);
    const codes = idx.map(k => all[k]), runs = [];
    for (let i = 0; i + seq.length <= codes.length; i++) {
      let ok = true;
      for (let j = 0; j < seq.length && ok; j++) ok = seq[j][0] === '*' || seq[j].indexOf(codes[i + j]) >= 0;
      if (!ok && seq.length > 2) {                  // the same glyphs in another order (a script's two parts)
        const left = seq.slice(); ok = true;
        for (let jj = 0; jj < seq.length && ok; jj++) {
          let at = -1;
          for (let kk = 0; kk < left.length; kk++) if (left[kk][0] === '*' || left[kk].indexOf(codes[i + jj]) >= 0) { at = kk; break; }
          if (at < 0) ok = false; else left.splice(at, 1);
        }
      }
      if (!ok) continue;
      runs.push(Array.prototype.slice.call(gl, idx[i], idx[i + seq.length - 1] + 1));
      i += seq.length - 1;
    }
    return runs;
  }
  // a soft box behind the given glyphs, drawn inside the formula's own picture (behind its glyphs, at least as tall as
  // the text round it), so it scrolls and scales with the formula
  function markGlyphs(f, gs) {
    try {
      const svg = f.querySelector('svg'); if (!svg) return null;
      let L = Infinity, T = Infinity, R = -Infinity, B = -Infinity;
      gs.forEach(g => { const r = g.getBoundingClientRect(); L = Math.min(L, r.left); T = Math.min(T, r.top); R = Math.max(R, r.right); B = Math.max(B, r.bottom); });
      if (!(R > L)) return null;
      const fs = parseFloat(getComputedStyle(f).fontSize) || 16, cy = (T + B) / 2, hh = Math.max(B - T + 2, fs * 1.05);
      T = cy - hh / 2; B = cy + hh / 2; L -= 2; R += 2;
      const M = svg.getScreenCTM().inverse(), pt = svg.createSVGPoint();
      pt.x = L; pt.y = T; const a = pt.matrixTransform(M);
      pt.x = R; pt.y = B; const b = pt.matrixTransform(M);
      const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rect.setAttribute('class', 'find-g');
      rect.setAttribute('x', a.x); rect.setAttribute('y', a.y); rect.setAttribute('width', b.x - a.x); rect.setAttribute('height', b.y - a.y);
      const rx = Math.min(b.x - a.x, b.y - a.y) * 0.18; rect.setAttribute('rx', rx); rect.setAttribute('ry', rx);
      svg.insertBefore(rect, svg.firstChild);
      return rect;
    } catch (e) { return null; }
  }

  // ------------------------------------------------------------------ finding
  let hits = [], at = -1, open = false, lastQ = '';
  const main = () => $('#paper');
  function textHits(q) {
    const out = [];
    const root = main(); if (!root) return out;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: n => n.parentNode.closest('mjx-container, .mjx-hl, .qbadge, .anchor, .fold-btn, button') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT });
    const parts = []; let text = '', node;
    while ((node = walker.nextNode())) { parts.push({ node, start: text.length }); text += node.nodeValue; }
    const hay = text.toLowerCase();
    const needle = q.toLowerCase().replace(/\s+/g, ' ');
    const at = pos => { let lo = 0, hi = parts.length - 1; while (lo < hi) { const mid = (lo + hi + 1) >> 1; if (parts[mid].start <= pos) lo = mid; else hi = mid - 1; } return { node: parts[lo].node, off: pos - parts[lo].start }; };
    let i = hay.indexOf(needle);
    while (i >= 0 && out.length < 2000) {
      const a = at(i), b = at(i + needle.length);
      const r = document.createRange(); r.setStart(a.node, a.off); r.setEnd(b.node, b.off);
      out.push({ range: r, el: a.node.parentElement });
      i = hay.indexOf(needle, i + Math.max(1, needle.length));
    }
    return out;
  }
  function texHits(q) {
    const out = [], seq = glyphsOf(texNorm(q)), single = !!seq && seq.length === 1;
    $$('#paper mjx-container[data-tex]').forEach(f => {
      // a single symbol: wherever it is drawn (a paper's own macros for it too); more TeX: in formulas whose TeX has it
      if (!single && !texHas(f.dataset.tex, q)) return;
      const runs = seq ? glyphRuns(f, q) : null;
      if (runs && runs.length) runs.forEach(gs => out.push({ el: f, glyphs: gs }));
      else if (!single || texHas(f.dataset.tex, q)) out.push({ el: f });   // the formula as a whole
    });
    return out;
  }
  function order(list) {
    const pos = h => h.range ? h.range.startContainer : h.el;
    return list.sort((x, y) => { const a = pos(x), b = pos(y); if (a === b) return 0; return a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1; });
  }
  function run(q) {
    clear();
    lastQ = q;
    const w = what(q);
    if (!w) { count(); return; }
    let list = [];
    if (w.mixed) {                                   // "the trace $\mathrm{Tr}\,\rho$ is": every text part, where a formula part is near
      w.mixed.forEach(p => { if (p.t) list = list.concat(textHits(p.t)); else list = list.concat(texHits(p.f)); });
    } else {
      if (w.text) list = list.concat(textHits(w.text));
      if (w.tex) list = list.concat(texHits(w.tex));
    }
    hits = order(list);
    paint();
    if (hits.length) go(0, true); else count();
  }
  function paint() {
    if (window.Highlight && CSS.highlights) {
      CSS.highlights.set('conifer-find', new Highlight(...hits.filter(h => h.range).map(h => h.range)));
    }
    hits.forEach(h => { if (h.range) return; if (h.glyphs) h.mark = markGlyphs(h.el, h.glyphs); else h.el.classList.add('find-f'); });
  }
  function clear() {
    if (window.CSS && CSS.highlights) { CSS.highlights.delete('conifer-find'); CSS.highlights.delete('conifer-find-now'); }
    $$('#paper .find-f, #paper .find-f-now').forEach(f => f.classList.remove('find-f', 'find-f-now'));
    $$('#paper .find-g').forEach(g => g.remove());
    hits = []; at = -1;
  }
  function count() {
    const c = $('#find-count'); if (!c) return;
    c.textContent = !lastQ.trim() ? '' : hits.length ? (at + 1) + ' of ' + hits.length : 'none';
  }
  function go(k, first) {
    if (!hits.length) return;
    at = (k + hits.length) % hits.length;
    const h = hits[at];
    if (window.Highlight && CSS.highlights) CSS.highlights.set('conifer-find-now', new Highlight(...(h.range ? [h.range] : [])));
    $$('#paper .find-f-now').forEach(f => f.classList.remove('find-f-now'));
    $$('#paper .find-g.now').forEach(g => g.classList.remove('now'));
    if (h.mark) h.mark.classList.add('now'); else if (!h.range) h.el.classList.add('find-f-now');
    const el = h.range ? (h.range.startContainer.nodeType === 3 ? h.range.startContainer.parentElement : h.range.startContainer) : h.el;
    const closed = el.closest && el.closest('.fold[data-state="closed"]'); if (closed && window.ConiferFolds) ConiferFolds.open(closed.dataset.key);
    const r = h.range ? h.range.getBoundingClientRect() : (h.mark || el).getBoundingClientRect();
    const bar = $('#bar'); const top = (bar ? bar.getBoundingClientRect().bottom : 0) + 12;
    if (r.top < top || r.bottom > window.innerHeight - 24) window.scrollTo({ top: window.scrollY + r.top - top - window.innerHeight * 0.3, behavior: first ? 'auto' : 'smooth' });
    count();
  }

  // ------------------------------------------------------------------ the field in the bar
  let timer = null;
  const reduced = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function show(on) {
    if (open === on) return;
    open = on;
    const row = $('#bar-row'), find = $('#find-row'); if (!row || !find) return;
    if (on) {
      row.hidden = true; find.hidden = false; find.classList.remove('closing'); find.classList.add('opening');
      const f = $('#find-input'); f.value = lastQ; f.focus(); f.select(); if (lastQ) run(lastQ);
    } else {
      clear(); count();
      const f = $('#find-input'); if (f && document.activeElement === f) f.blur();
      const done = () => { find.hidden = true; find.classList.remove('closing'); row.hidden = false; row.classList.add('opening'); setTimeout(() => row.classList.remove('opening'), 250); };
      if (reduced()) done(); else { find.classList.remove('opening'); find.classList.add('closing'); setTimeout(done, 170); }
    }
  }
  window.ConiferSearch = {
    open: () => show(true), close: () => show(false), toggle: () => show(!open), isOpen: () => open,
    refresh: () => { if (open && lastQ) run(lastQ); },
  };
  document.addEventListener('input', e => {
    if (e.target.id !== 'find-input') return;
    clearTimeout(timer);
    const q = e.target.value;
    timer = setTimeout(() => run(q), 180);
  });
  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && !e.altKey && !e.shiftKey && e.key.toLowerCase() === 'f') { e.preventDefault(); show(true); return; }   // Ctrl+F / Cmd+F is this search
    if (!open) return;
    if (e.key === 'Escape') { e.preventDefault(); show(false); return; }
    if (e.target.id === 'find-input' && e.key === 'Enter') { e.preventDefault(); go(at + (e.shiftKey ? -1 : 1)); }
  });
  document.addEventListener('click', e => {
    const t = e.target.closest('[data-find]'); if (!t) return;
    const a = t.dataset.find;
    if (a === 'open') show(true); else if (a === 'close') show(false); else if (a === 'next') go(at + 1); else if (a === 'prev') go(at - 1);
  });
})();
