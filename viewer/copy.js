// Conifer: copying, as Epsilon does it. A selection copied from the paper carries each formula as its TeX, $...$ in
// a line and \[...\] on a line of its own, with the paper's own macros written out so that it works anywhere; the
// standard physics and braket commands are left as they are. Nothing else about the text changes.
(function () {
  'use strict';
  const DOC = JSON.parse(document.getElementById('conifer-doc').textContent);
  const MACROS = (DOC.meta && DOC.meta.macros) || {};
  const names = Object.keys(MACROS).sort((a, b) => b.length - a.length);
  // a macro's body and how many arguments it takes, in MathJax's forms: "body" or ["body", n] or ["body", n, "default"]
  const defOf = n => { const m = MACROS[n]; return Array.isArray(m) ? { body: String(m[0]), n: +m[1] || 0, dflt: m[2] } : { body: String(m), n: 0 }; };
  function group(s, i) {                             // the brace group (or single token) starting at i: [text, end]
    while (i < s.length && /\s/.test(s[i])) i++;
    if (s[i] === '{') { let d = 0, j = i; for (; j < s.length; j++) { if (s[j] === '{') d++; else if (s[j] === '}') { d--; if (!d) return [s.slice(i + 1, j), j + 1]; } } return [s.slice(i + 1), s.length]; }
    if (s[i] === '\\') { const m = /^\\([A-Za-z]+|.)/.exec(s.slice(i)); return [m[0], i + m[0].length]; }
    return [s[i] || '', i + 1];
  }
  function expand(tex) {
    if (!names.length) return tex;
    let s = tex;
    for (let pass = 0; pass < 12; pass++) {
      let changed = false, out = '', i = 0;
      while (i < s.length) {
        if (s[i] !== '\\') { out += s[i++]; continue; }
        const m = /^\\([A-Za-z]+)/.exec(s.slice(i));
        if (!m || !MACROS.hasOwnProperty(m[1])) { out += s[i]; i++; continue; }
        const d = defOf(m[1]); let j = i + m[0].length; const args = [];
        if (d.n) {
          let k = 0;
          if (d.dflt !== undefined) { if (/^\s*\[/.test(s.slice(j))) { const e = s.indexOf(']', j); args.push(s.slice(s.indexOf('[', j) + 1, e)); j = e + 1; } else args.push(d.dflt); k = 1; }
          for (; k < d.n; k++) { const g = group(s, j); args.push(g[0]); j = g[1]; }
        }
        out += d.body.replace(/#(\d)/g, (x, q) => args[+q - 1] !== undefined ? args[+q - 1] : x) + (/[A-Za-z]/.test(s[j] || '') && !d.n ? ' ' : '');
        i = j; changed = true;
      }
      s = out;
      if (!changed) break;
    }
    return s;
  }
  function textOf(node) {                            // the text of a copied fragment, formulas as TeX
    if (node.nodeType === 3) return node.nodeValue;
    if (node.nodeType === 11) { let f = ''; node.childNodes.forEach(c => { f += textOf(c); }); return f; }
    if (node.nodeType !== 1) return '';
    if (node.tagName === 'MJX-CONTAINER') {
      const tex = expand(node.getAttribute('data-tex') || '').trim();
      return node.getAttribute('display') === 'true' ? '\n\\[ ' + tex + ' \\]\n' : '$' + tex + '$';
    }
    if (node.tagName === 'BR') return '\n';
    if (node.matches('.qbadge, .anchor, .fold-btn, .x-btn, .eqno, script, style')) return '';
    let t = '';
    node.childNodes.forEach(c => { t += textOf(c); });
    const block = /^(P|DIV|LI|H[1-6]|SECTION|FIGCAPTION|TR|BLOCKQUOTE|PRE|OL|UL|FIGURE)$/.test(node.tagName);
    return block ? t.replace(/\s+$/, '') + '\n\n' : t;
  }
  window.ConiferCopy = { expand, textOf };
  document.addEventListener('copy', e => {
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed || !sel.rangeCount) return;
    const range = sel.getRangeAt(0);
    const within = range.commonAncestorContainer.nodeType === 1 ? range.commonAncestorContainer : range.commonAncestorContainer.parentElement;
    if (!within.closest('#paper, #sheet-body, #pop')) return;
    const frag = range.cloneContents();
    if (!frag.querySelector('mjx-container')) return;        // plain text copies as the browser does
    const text = textOf(frag).replace(/\n{3,}/g, '\n\n').replace(/[ \t]+\n/g, '\n').trim();
    e.clipboardData.setData('text/plain', text);
    e.preventDefault();
  });
})();
