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

  // ------------------------------------------------------------------ finding
  let hits = [], at = -1, open = false, lastQ = '';
  const main = () => $('#paper');
  function textHits(q) {
    const out = [];
    const root = main(); if (!root) return out;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: n => n.parentNode.closest('mjx-container, .qbadge, .anchor, .fold-btn, button') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT });
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
    const out = [];
    $$('#paper mjx-container[data-tex]').forEach(f => { if (texHas(f.dataset.tex, q)) out.push({ el: f }); });
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
    hits.forEach(h => { if (!h.range) h.el.classList.add('find-f'); });
  }
  function clear() {
    if (window.CSS && CSS.highlights) { CSS.highlights.delete('conifer-find'); CSS.highlights.delete('conifer-find-now'); }
    $$('#paper .find-f, #paper .find-f-now').forEach(f => f.classList.remove('find-f', 'find-f-now'));
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
    if (!h.range) h.el.classList.add('find-f-now');
    const el = h.range ? (h.range.startContainer.nodeType === 3 ? h.range.startContainer.parentElement : h.range.startContainer) : h.el;
    const r = h.range ? h.range.getBoundingClientRect() : el.getBoundingClientRect();
    const bar = $('#bar'); const top = (bar ? bar.getBoundingClientRect().bottom : 0) + 12;
    if (r.top < top || r.bottom > window.innerHeight - 24) window.scrollTo({ top: window.scrollY + r.top - top - window.innerHeight * 0.3, behavior: first ? 'auto' : 'smooth' });
    count();
  }

  // ------------------------------------------------------------------ the field in the bar
  let timer = null;
  function show(on) {
    open = on;
    const row = $('#bar-row'), find = $('#find-row'); if (!row || !find) return;
    row.hidden = on; find.hidden = !on;
    if (on) { const f = $('#find-input'); f.value = lastQ; f.focus(); f.select(); if (lastQ) run(lastQ); }
    else { clear(); count(); }
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
