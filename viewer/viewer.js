// Conifer viewer. The dial chooses which document is read (gist, summary, paper, everything); each is a clean linear
// text. A tap on something in the text opens a peek (a sheet) with the related material: the paragraphs a summary
// sentence stands for, a definition, a footnote, an equation. The peek's header is the link into the paper, and
// travelling leaves a way back. Inline expansion exists only for folds (appendices, proofs, background notes).
(function () {
  'use strict';
  const $ = (s, el) => (el || document).querySelector(s);
  const $$ = (s, el) => Array.from((el || document).querySelectorAll(s));
  const esc = t => String(t == null ? '' : t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const DOC = JSON.parse($('#conifer-doc').textContent);
  const LEVELS = DOC.levels;
  const IDX = Object.fromEntries(LEVELS.map((l, i) => [l.key, i]));
  const GIST = IDX.gist ?? 0, BRIEF = IDX.brief ?? 1, SKIM = IDX.skim, PAPER = IDX.paper ?? LEVELS.length - 2, FULL = IDX.full ?? LEVELS.length - 1;
  const LEVEL_HASH = LEVELS.map(l => ({ gist: 'gist', brief: 'summary', skim: 'skim', paper: 'paper', full: 'everything' })[l.key] || l.key);
  const WPM = 230;
  const BOX = { theorem: 'Theorem', definition: 'Definition', remark: 'Remark', proof: 'Proof', lemma: 'Lemma' };
  const HEADED = { references: 'References', footnotes: 'Footnotes', abstract: 'Abstract' };
  const titleOf = n => n.titleHtml || esc(n.title || '');
  const reduced = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ------------------------------------------------------------------ the index
  const byId = new Map(), parentOf = new Map();
  (function walk(n, p) { byId.set(n.id, n); parentOf.set(n.id, p); (n.children || []).forEach(c => walk(c, n.id)); })(DOC.root, null);
  const defs = new Map((DOC.defs || []).map(d => [d.id, d]));
  const qsAt = new Map();
  (DOC.questions || []).forEach(q => { const k = q.at.node; if (!qsAt.has(k)) qsAt.set(k, []); qsAt.get(k).push(q); });
  const descendants = id => { const out = []; (function w(n) { out.push(n.id); (n.children || []).forEach(w); })(byId.get(id)); return out; };
  const questionsUnder = id => descendants(id).flatMap(i => qsAt.get(i) || []);
  const ancestors = id => { const out = []; let p = parentOf.get(id); while (p) { out.unshift(p); p = parentOf.get(p); } return out; };
  const depth = id => ancestors(id).length;
  const titled = id => { let n = byId.get(id); while (n && !n.title) n = byId.get(parentOf.get(n.id)); return n; };
  const anchorHost = new Map();          // an id inside a body (equation, footnote, figure, reference) -> the node holding it
  byId.forEach(n => { if (n.body) for (const m of n.body.matchAll(/ id="([^"]+)"/g)) anchorHost.set(m[1], n.id); });
  const words = h => (String(h || '').replace(/<[^>]+>/g, ' ').match(/[A-Za-z0-9Ͱ-Ͽ][^\s]*/g) || []).length;
  const texText = t => String(t || '').replace(/\\(?:mathcal|mathbb|mathrm|text|textrm|bf|rm)\{([^}]*)\}/g, '$1').replace(/\\([A-Za-z]+)/g, '$1').replace(/[${}]/g, '');
  const shortLabel = n => !n ? '' : n.number ? (n.kind === 'appendix' ? 'App. ' : '§') + n.number : (n.title || n.id);
  function placeName(id) { const t = titled(id); if (!t) return id; return texText(t.number ? shortLabel(t) + ' ' + t.title : t.title); }
  function placeHtml(id) { const t = titled(id); if (!t) return esc(id); return (t.number ? esc(shortLabel(t)) + ' ' : '') + titleOf(t); }
  const isFold = n => !!n.fold || n.kind === 'background';

  // ------------------------------------------------------------------ the state
  const AUD = DOC.audiences || [];
  const state = { level: 0, over: new Map(), ledes: 'auto', chips: 'auto', theme: 'system',
    audience: (DOC.meta && DOC.meta.defaultAudience) || (AUD[0] && AUD[0].key) || '' };
  const audLabel = k => { const a = AUD.find(x => x.key === k); return a ? a.label : k; };
  const pick = t => (t && t.variants && t.variants[state.audience]) || t;
  const forMe = n => !n.audience || n.audience.includes(state.audience);
  const openByDefault = n => state.audience === 'student' && forMe(n);
  const skimHidden = () => SKIM !== undefined && state.audience === 'student';
  const ledesOn = () => state.ledes === true || (state.ledes === 'auto' && state.audience !== 'specialist');
  const chipsOn = () => state.chips === true || (state.chips === 'auto' && state.audience !== 'specialist');
  function load() { try { const s = JSON.parse(localStorage.getItem('conifer-reader') || '{}'); ['ledes', 'chips', 'level', 'theme', 'audience'].forEach(k => { if (k in s) state[k] = s[k]; }); } catch (e) {} }
  function save() { try { localStorage.setItem('conifer-reader', JSON.stringify({ level: state.level, ledes: state.ledes, chips: state.chips, theme: state.theme, audience: state.audience })); } catch (e) {} }
  function applyTheme() { const r = document.documentElement; if (state.theme === 'light' || state.theme === 'dark') r.dataset.theme = state.theme; else delete r.dataset.theme; }
  let EST = [];
  let estimating = false;
  let lastOpened = null;                 // a fold just opened, for its animation

  // terms: a mention of a defined term is a link only for the readers it is meant for
  const audienceDefs = html => html.replace(/<a data-def="([^"]+)">([\s\S]*?)<\/a>/g, (m, id, txt) => { const d = defs.get(id); return d && d.audience && !d.audience.includes(state.audience) ? txt : m; });

  // ------------------------------------------------------------------ rendering (HTML strings)
  function chip(t) {
    if (!chipsOn() || !t || !t.status) return '';
    const M = { author: ['author', 'Written by the author'], 'ai-approved': ['AI draft · approved', 'Drafted by the AI reader and checked by the author'], 'ai-draft': ['AI draft · unreviewed', 'Drafted by the AI reader; the author has not checked it yet'] };
    const m = M[t.status]; if (!m) return '';
    return `<span class="chip ${t.status}" title="${esc(m[1])}">${esc(m[0])}</span>`;
  }
  // a sentence of a summary and what it stands for: no mark in the text, a peek on a tap
  function withSpans(html, ctx) {
    if (ctx.plain) return html.replace(/<span data-covers="[^"]+">/g, '<span>');
    return html.replace(/<span data-covers="([^"]+)">/g, (m, c) => `<span class="gs" data-covers="${c}" role="button" tabindex="0" title="Show the part of the paper this stands for">`);
  }
  const stripIds = html => html.replace(/ id="([^"]*)"/g, ' id="peek-$1"');
  function qbadge(n, deep, ctx) {
    return '';
  }
  function qwords(id, deep) {
    const qs = deep ? questionsUnder(id) : (qsAt.get(id) || []);
    if (!qs.length) return '';
    return `<button type="button" class="qwords" data-q="${id}" data-deep="${deep ? 1 : 0}">${qs.length} question${qs.length > 1 ? 's' : ''}</button>`;
  }
  function qbadgeOld(n, deep, ctx) {
    if (ctx && ctx.prefix) return '';
    const qs = deep ? questionsUnder(n.id) : (qsAt.get(n.id) || []);
    if (!qs.length) return '';
    return `<button type="button" class="qbadge" data-q="${n.id}" data-deep="${deep ? 1 : 0}" title="Questions about this part" aria-label="${qs.length} question${qs.length > 1 ? 's' : ''} about this part">?<span>${qs.length}</span></button>`;
  }
  const circle = (act, key, open) => `<button type="button" class="fold-btn" data-act="${act}" data-key="${key}" title="${open ? 'Fold' : 'Open'}" aria-label="${open ? 'Fold' : 'Open'}" aria-expanded="${open}">${open ? '&minus;' : '+'}</button>`;

  // a fold, closed: one quiet line
  function foldedLine(n, ctx) {
    const key = ctx.prefix + n.id;
    const bg = n.kind === 'background';
    const name = bg ? 'Background' : n.kind === 'appendix' ? esc('Appendix ' + (n.number || '')) : esc(n.title || BOX[n.kind] || 'More');
    const detail = bg ? esc(n.title) : n.kind === 'appendix' ? titleOf(n) : n.gist ? pick(n.gist).html : `${words(n.body || '')} words`;
    const who = bg ? `<span class="fold-who">for ${esc((n.audience || []).map(a => audLabel(a).toLowerCase() + 's').join(' and '))}</span>` : '';
    return `<div class="node folded${bg ? ' fold-bg' : ''}" data-id="${n.id}" data-key="${key}"${ctx.prefix ? '' : ` id="${n.id}"`}>${circle('open', key, false)}<button type="button" class="fold-line" data-act="open" data-key="${key}"><span class="fold-name">${name}</span><span class="fold-detail">${detail}</span>${who}</button></div>`;
  }
  // a fold, open: a small head with the minus, then the content
  function openFold(n, L, ctx) {
    const key = ctx.prefix + n.id;
    const bg = n.kind === 'background';
    const name = bg ? 'Background' : n.kind === 'appendix' ? '' : esc(n.title || BOX[n.kind] || '');
    const head = n.kind === 'appendix' ? '' : `<div class="fold-head">${ctx.prefix ? '' : circle('close', key, true)}<span>${name}</span>${bg ? `<span class="fold-title">${esc(n.title)}</span>` : ''}</div>`;
    let inner;
    if (n.children) inner = wrap(n, L, ctx, true);
    else inner = leaf(n, ctx, n.kind === 'proof');
    const anim = lastOpened === key ? ' opening' : '';
    return `<div class="node fold-open${bg ? ' fold-bg' : ''}" data-id="${n.id}" data-key="${key}"${ctx.prefix ? '' : ` id="${n.id}"`}>${head}<div class="fold-body${anim}">${inner}</div></div>`;
  }
  function leaf(n, ctx, headless) {
    const key = ctx.prefix + n.id;
    const body = audienceDefs(ctx.prefix ? stripIds(n.body) : n.body);
    const box = BOX[n.kind];
    const inner = box && !headless ? body.replace(/^\s*<p>/, `<p><span class="box-head">${esc(n.title || box)}.</span> `) : box ? body.replace(/^\s*<p>/, `<p><span class="box-head">${esc(n.title || box)}.</span> `) : body;
    const head = HEADED[n.kind] ? `<h2 class="sec-h" data-node="${n.id}">${esc(n.title || HEADED[n.kind])}</h2>` : '';
    return `<div class="node leaf kind-${n.kind}" data-id="${n.id}" data-key="${key}"${ctx.prefix ? '' : ` id="${n.id}"`}>${head}${qbadge(n, false, ctx)}${inner}</div>`;
  }
  function ledeBlock(n, ctx) {
    const t = pick(n.brief);
    const who = t.status === 'author' ? 'by the author' : t.status === 'ai-approved' ? 'AI draft, approved' : t.status === 'ai-draft' ? 'AI draft' : '';
    const q = ctx.prefix ? '' : qwords(n.id, true);
    return `<div class="lede"><div class="lede-head"><span>In brief${who ? ` <span class="lede-who">· ${esc(who)}</span>` : ''}</span>${q}</div><div class="sum-body">${audienceDefs(withSpans(t.html, ctx))}</div></div>`;
  }
  function wrap(n, L, ctx, inFold) {
    const key = ctx.prefix + n.id;
    const hl = Math.min(1 + depth(n.id), 5);
    const minus = inFold && !ctx.prefix ? circle('close', key, true) : '';
    const anchor = ctx.prefix ? '' : `<button type="button" class="anchor" data-copy="${n.id}" title="Copy a link to this section" aria-label="Copy a link to this section">&#182;</button>`;
    const head = n.title ? `<h${hl} class="sec-h" data-node="${n.id}">${minus}<span class="secnum">${esc(n.number || '')}</span>${n.number ? ' ' : ''}${titleOf(n)}${qbadge(n, false, ctx)}${anchor}</h${hl}>` : '';
    const lede = n.brief && L === PAPER && ledesOn() && n.id !== DOC.root.id ? ledeBlock(n, ctx) : '';
    const inner = (n.children || []).map(c => render(c, L, ctx)).join('');
    return `<section class="node sec kind-${n.kind}" data-id="${n.id}" data-key="${key}"${ctx.prefix || inFold ? '' : ` id="${n.id}"`}>${head}${lede}${inner}</section>`;
  }
  function render(n, inh, ctx) {
    const key = ctx.prefix + n.id;
    if (n.id === DOC.root.id && !ctx.prefix) return renderRoot(n, inh, ctx);
    if ((HEADED[n.kind] || n.kind === 'background') && inh < PAPER) return '';
    if (isFold(n)) {
      const base = ctx.allOpen || inh >= FULL || (n.kind === 'background' && openByDefault(n)) ? 3 : 2;
      const eff = ctx.over.has(key) ? ctx.over.get(key) : base;
      return eff >= 3 ? openFold(n, Math.max(inh, PAPER), ctx) : foldedLine(n, ctx);
    }
    if (!n.children) return leaf(n, ctx);
    return wrap(n, Math.max(inh, PAPER), ctx);
  }
  function time(l) { const w = EST[l] || 0; const m = Math.max(1, Math.round(w / WPM)); return `≈ ${m} min`; }
  function actions(from) {
    if (estimating) return '';
    const b = [];
    if (from < BRIEF) b.push(`<button type="button" class="btn primary" data-setlevel="${BRIEF}">Read the summary <small>${time(BRIEF)}</small></button>`);
    if (SKIM !== undefined && from < SKIM && !skimHidden()) b.push(`<button type="button" class="btn${from === BRIEF ? ' primary' : ''}" data-setlevel="${SKIM}">Skim the paper <small>${time(SKIM)}</small></button>`);
    b.push(`<button type="button" class="btn${from >= BRIEF && (SKIM === undefined || from >= SKIM) ? ' primary' : ''}" data-setlevel="${PAPER}">Open the paper <small>${time(PAPER)}</small></button>`);
    return `<div class="gist-actions">${b.join('')}</div>`;
  }
  function renderRoot(n, L, ctx) {
    if (L === GIST && n.gist) {
      const key = DOC.meta.key || {};
      let eq = '';
      if (key.equation && anchorHost.has(key.equation)) { const m = byId.get(anchorHost.get(key.equation)).body.match(new RegExp(`<div class="display"[^>]*id="${key.equation}">[\\s\\S]*?</div>\\s*(?:<span class="eqno">[^<]*</span>\\s*)?</div>`)); if (m) eq = stripIds(m[0]); }
      const fig = key.figure && byId.get(key.figure) ? stripIds(byId.get(key.figure).body) : '';
      const hint = state.audience === 'student' ? `<p class="hint">Words with a dotted line have a definition: tap them. Background notes open for you where the paper assumes something.</p>` : '';
      return `<section class="node gist-card" data-id="${n.id}" data-key="${n.id}"><div class="card-label">The gist</div><div class="sum-body">${audienceDefs(withSpans(pick(n.gist).html, ctx))}</div>${eq ? `<div class="gist-eq">${eq}</div>` : ''}${fig ? `<div class="gist-fig">${fig}</div>` : ''}${hint}${actions(GIST)}<div class="sum-foot">${chip(pick(n.gist))}${qwords(DOC.root.id, true)}</div></section>`;
    }
    if (L === BRIEF && n.brief) {
      return `<section class="node sum-page" data-id="${n.id}" data-key="${n.id}"><div class="card-label">Summary <span class="muted">· tap a sentence to see the part of the paper it stands for</span></div><div class="sum-body">${audienceDefs(withSpans(pick(n.brief).html, ctx))}</div><div class="sum-foot">${chip(pick(n.brief))}${qwords(DOC.root.id, true)}</div>${actions(BRIEF)}</section>`;
    }
    if (L === SKIM) return skimPage(n, ctx);
    return (n.children || []).map(c => render(c, Math.max(L, PAPER), ctx)).join('');
  }
  // the skim: the headings, and one line for every paragraph; a tap on a line shows the paragraph
  function skimPage(root, ctx) {
    const parts = []; let status = null;
    (function w(n) {
      if (n === root) { (n.children || []).forEach(w); return; }
      if (HEADED[n.kind] || n.kind === 'background') return;
      if (n.children) {
        const hl = Math.min(1 + depth(n.id), 5);
        parts.push(`<h${hl} class="sec-h" data-node="${n.id}"><span class="secnum">${esc(n.number || '')}</span>${n.number ? ' ' : ''}${titleOf(n)}</h${hl}>`);
        n.children.forEach(w); return;
      }
      const g = n.gist ? pick(n.gist) : null;
      if (g && !status) status = g.status;
      const line = g ? g.html : (n.kind === 'figure' || n.kind === 'table') ? esc(n.title || 'Figure') : BOX[n.kind] ? esc(n.title || BOX[n.kind]) : '';
      if (line) parts.push(`<p class="skim" data-go="${n.id}" role="button" tabindex="0" title="Read this paragraph in the paper">${audienceDefs(line)}</p>`);
    })(root);
    return `<section class="node skim-page" data-id="${root.id}" data-key="${root.id}"><div class="card-label">Skim <span class="muted">· one line for every paragraph; a tap opens the paper there</span></div>${parts.join('')}<div class="sum-foot">${chip({ status })}</div>${actions(SKIM)}</section>`;
  }

  // ------------------------------------------------------------------ drawing the page
  const locate = key => $(`#paper [data-key="${CSS.escape(key)}"]`);
  const barH = () => ($('#bar') ? $('#bar').getBoundingClientRect().bottom : 0);
  function draw(keepKey) {
    const main = $('#paper');
    const ctx = { prefix: '', over: state.over };
    const before = keepKey ? locate(keepKey) : null;
    const y0 = before ? before.getBoundingClientRect().top : null;
    main.innerHTML = render(DOC.root, state.level, ctx);
    lastOpened = null;
    if (y0 != null) { const after = locate(keepKey); if (after) window.scrollBy(0, after.getBoundingClientRect().top - y0); }
    drawDial(); barTitle();
    if (window.ConiferSearch) ConiferSearch.refresh();
  }
  function moveInd(group) {                       // the chosen option's pill glides to it (the dial, a segmented setting)
    const ind = group.querySelector('.sel-ind'), on = group.querySelector('[aria-checked="true"]');
    if (!ind || !on) return;
    ind.style.width = on.offsetWidth + 'px';
    ind.style.transform = 'translateX(' + on.offsetLeft + 'px)';
    ind.classList.add('placed');
  }
  // a fold, opened or closed where it stands: the node is redrawn alone and its body eases between 0 and its height
  const renderNode = n => render(n, state.level, { prefix: '', over: state.over });
  function swapNode(el, html) { const tmp = document.createElement('div'); tmp.innerHTML = html; const neu = tmp.firstElementChild; el.replaceWith(neu); return neu; }
  function ease(body, from, to, after) {
    body.style.overflow = 'hidden'; body.style.height = from + 'px'; body.style.opacity = from ? '1' : '0';
    void body.offsetWidth;
    body.style.transition = 'height .26s var(--ease-out), opacity .22s var(--ease-out)';
    body.style.height = to + 'px'; body.style.opacity = to ? '1' : '0';
    let done = false;
    const end = () => { if (done) return; done = true; body.style.transition = ''; body.style.overflow = ''; body.style.height = ''; body.style.opacity = ''; after && after(); };
    body.addEventListener('transitionend', end, { once: true }); setTimeout(end, 320);
  }
  function openFoldAt(key) {
    const el = locate(key), n = byId.get(key.split('|').pop());
    state.over.set(key, 3); commit();
    if (!el || !n) { draw(); return; }
    const neu = swapNode(el, renderNode(n)), body = neu.querySelector('.fold-body');
    if (body && !reduced()) ease(body, 0, body.offsetHeight);
    barTitle();
  }
  function closeFoldAt(key) {
    const el = locate(key), n = byId.get(key.split('|').pop());
    const finish = () => { state.over.set(key, 2); commit(); if (el && el.isConnected && n) swapNode(el, renderNode(n)); else draw(); barTitle(); };
    const body = el && el.querySelector('.fold-body');
    if (!body || reduced()) { finish(); return; }
    ease(body, body.offsetHeight, 0, finish);
  }
  function drawDial() {
    const dial = $('#dial');
    if (!dial.querySelector('button')) dial.innerHTML = '<span class="sel-ind" aria-hidden="true"></span>' + LEVELS.map((l, i) => `<button type="button" role="radio" aria-checked="${i === state.level}" data-setlevel="${i}" title="${esc(l.hint || '')}"><span>${esc(l.label)}</span><small>${time(i)}</small></button>`).join('');
    $$('button', dial).forEach((b, i) => { b.setAttribute('aria-checked', String(i === state.level)); b.querySelector('small').textContent = time(i); b.hidden = i === SKIM && skimHidden(); });
    document.documentElement.dataset.depth = LEVELS[state.level].key;
    moveInd(dial);
    const who = $('#who'); if (who) who.textContent = audLabel(state.audience) + ' ▾';
    const back = $('#back'); if (back) { back.hidden = !backStack.length; if (backStack.length) back.textContent = '↩ ' + backStack[backStack.length - 1].label; }
  }
  function swapIn() { const main = $('#paper'); main.classList.remove('swap'); void main.offsetWidth; main.classList.add('swap'); }
  function setLevel(i, silent) {
    if (i === state.level) return;
    if (!silent) push(LEVEL_HASH[i]);
    backStack = [];
    state.level = i; state.over.clear(); closeAll(); save(); draw(); swapIn();
    window.scrollTo({ top: 0, behavior: 'auto' });
    if (!silent) commit();
  }
  let curSection = null;
  function barTitle() {
    const t = $('#bar-title');
    if (state.level === GIST || state.level === BRIEF) { t.innerHTML = esc(LEVELS[state.level].label) + ' · ' + esc(DOC.meta.title); curSection = null; return; }
    const top = barH() + 12;
    let cur = null;
    $$('#paper .sec-h', $('#paper')).forEach(h => { if (h.getBoundingClientRect().top <= top) cur = h; });
    if (cur && cur.dataset.node && byId.has(cur.dataset.node)) { const n = byId.get(cur.dataset.node); t.innerHTML = (n.number ? esc(n.number) + ' ' : '') + titleOf(n); curSection = n.id; }
    else { t.textContent = DOC.meta.title; curSection = null; }
  }
  // the address follows the reader: the section being read, or the document (gist, summary)
  let hashTimer = null;
  function followHash() {
    clearTimeout(hashTimer);
    hashTimer = setTimeout(() => {
      const want = (state.level === GIST || state.level === BRIEF) ? LEVEL_HASH[state.level] : (curSection || LEVEL_HASH[state.level]);
      if (decodeURIComponent(location.hash.slice(1)) !== want) { try { history.replaceState(snapshot(history.state && { from: history.state.from }), '', '#' + want); } catch (e) {} }
    }, 250);
  }

  // ---- landing on a place: scroll, then mark it for a while once the scroll has settled
  function afterScroll(fn) {
    let done = false;
    const go = () => { if (done) return; done = true; window.removeEventListener('scrollend', go); fn(); };
    window.addEventListener('scrollend', go, { once: true });
    setTimeout(go, reduced() ? 50 : 750);
  }
  function flash(el) { if (!el) return; el.classList.remove('flash'); void el.offsetWidth; el.classList.add('flash'); setTimeout(() => el.classList.remove('flash'), 2600); }
  function scrollTo(el) {
    const y = el.getBoundingClientRect().top + window.scrollY - barH() - 16;
    window.scrollTo({ top: Math.max(0, y), behavior: reduced() ? 'auto' : 'smooth' });
  }
  function flashQuote(el, quote) {
    if (!quote) return;
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    const parts = []; let text = '', node;
    while ((node = walker.nextNode())) { parts.push({ node, start: text.length }); text += node.nodeValue; }
    const i = text.indexOf(quote); if (i < 0) return;
    const at = pos => { let p = parts[0]; for (const q of parts) { if (q.start <= pos) p = q; else break; } return { node: p.node, off: pos - p.start }; };
    const a = at(i), b = at(i + quote.length);
    const r = document.createRange(); r.setStart(a.node, a.off); r.setEnd(b.node, b.off);
    if (window.Highlight && CSS.highlights) { CSS.highlights.set('conifer-quote', new Highlight(r)); setTimeout(() => CSS.highlights.delete('conifer-quote'), 3000); return; }
    try { const s = document.createElement('span'); s.className = 'qmark'; r.surroundContents(s); setTimeout(() => s.replaceWith(...s.childNodes), 3000); } catch (e) {}
  }

  // ---- travelling: a jump into the paper remembers where the reader was (the pill), and is a history step too
  let backStack = [];
  const snapshot = extra => Object.assign({ conifer: true, level: state.level, over: [...state.over], y: window.scrollY, from: null }, extra || {});
  function commit() { try { history.replaceState(snapshot(history.state && { from: history.state.from }), '', location.hash || ' '); } catch (e) {} }
  function push(hash, extra) { commit(); try { history.pushState(snapshot(extra), '', hash ? '#' + hash : (location.hash || location.pathname + location.search)); } catch (e) {} }
  function restore(sn) { state.level = sn.level; state.over = new Map(sn.over); save(); draw(); window.scrollTo(0, sn.y || 0); }
  try { history.scrollRestoration = 'manual'; } catch (e) {}
  window.addEventListener('popstate', e => {
    backStack = [];
    if (e.state && e.state.conifer) { restore(e.state); return; }
    const h = decodeURIComponent(location.hash.slice(1));
    if (h) goHash(h, false);
  });
  function goHash(h, pushIt) {
    const li = LEVEL_HASH.indexOf(h);
    if (li >= 0) { setLevel(li, !pushIt); return; }
    if (byId.has(h)) reveal(h, { push: pushIt });
    else if (anchorHost.has(h)) reveal(anchorHost.get(h), { flash: h, push: pushIt });
  }
  const linkTo = id => location.href.split('#')[0] + '#' + id;
  function copyLink(id) {
    const url = linkTo(id);
    const done = () => toast('Link copied');
    const fail = () => openSheet('Link to this place', `<p class="set-note">Copy it from here:</p><input class="link-box" id="link-box" type="text" readonly value="${esc(url)}">`, 'sheet-link');
    try { navigator.clipboard.writeText(url).then(done, fail); } catch (e) { fail(); }
  }
  function toast(text) { const t = $('#toast'); if (!t) return; t.textContent = text; t.hidden = false; t.classList.remove('closing'); clearTimeout(t.timer); t.timer = setTimeout(() => { t.classList.add('closing'); setTimeout(() => { t.hidden = true; t.classList.remove('closing'); }, 200); }, 1500); }
  // show a place in the paper: open what hides it, go there, mark it; remember where the reader came from
  function reveal(id, opts) {
    opts = opts || {};
    if (!byId.has(id)) return;
    const fromLevel = state.level;
    const origin = { label: fromLevel < PAPER ? LEVELS[fromLevel].label : (curSection && byId.has(curSection) ? shortLabel(byId.get(curSection)) : 'Back'), sn: snapshot() };
    if (opts.push !== false) push(opts.flash || id, { from: fromLevel });
    if (state.level < PAPER) { state.level = PAPER; state.over.clear(); save(); }
    ancestors(id).concat([id]).forEach(a => { const n = byId.get(a); if (isFold(n)) state.over.set(a, 3); });
    closeAll();
    draw();
    if (fromLevel !== state.level) swapIn();
    backStack.push(origin); drawDial();
    const el = locate(id); if (!el) return;
    const target = opts.flash ? (el.querySelector('#' + CSS.escape(opts.flash)) || el) : el;
    const mark = target === el && byId.get(id).children ? (el.querySelector('.sec-h') || el) : target;   // a section: its heading is marked, not the whole
    scrollTo(target);
    afterScroll(() => { flash(mark); if (opts.quote) flashQuote(el, opts.quote); commit(); });
  }
  function goBack() {
    const o = backStack.pop(); if (!o) return;
    closeAll();
    const changing = o.sn.level !== state.level;
    restore(o.sn);
    if (changing) swapIn();
    drawDial(); commit();
  }

  // ------------------------------------------------------------------ sheets, peeks and the popover
  function openSheet(title, html, cls) {
    closePop();
    const sh = $('#sheet');
    sh.classList.remove('closing');
    $('#sheet-title').innerHTML = title; $('#sheet-body').innerHTML = html;
    sh.className = 'sheet ' + (cls || ''); sh.hidden = false; $('#scrim').hidden = false;
    $('#sheet-body').scrollTop = 0;
    const box = $('#link-box'); if (box) { box.focus(); box.select(); }
  }
  function closeSheet() {
    const sh = $('#sheet'); if (sh.hidden) return;
    $$('.gs.peeking, .skim.peeking').forEach(s => s.classList.remove('peeking'));
    if (reduced()) { sh.hidden = true; $('#scrim').hidden = true; return; }
    sh.classList.add('closing'); $('#scrim').classList.add('closing');
    setTimeout(() => { sh.hidden = true; sh.classList.remove('closing'); $('#scrim').hidden = true; $('#scrim').classList.remove('closing'); }, 190);
  }
  function closePop() {
    const pop = $('#pop'); if (pop.hidden) return;
    if (reduced()) { pop.hidden = true; return; }
    pop.classList.add('closing'); setTimeout(() => { pop.hidden = true; pop.classList.remove('closing'); }, 160);
  }
  function closeAll() { closeSheet(); closePop(); }
  const peekCtx = () => ({ prefix: 'peek|', over: new Map(), plain: true, allOpen: true });
  // the paragraphs a sentence stands for
  function peekCovered(span) {
    const ids = span.dataset.covers.split(/\s+/).filter(id => byId.has(id));
    if (!ids.length) return;
    const ctx = peekCtx();
    const html = ids.map(id => render(byId.get(id), PAPER, ctx)).join('');
    const places = [...new Set(ids.map(id => (titled(id) || {}).id).filter(Boolean))];
    const from = places.map(p => `<a href="#${esc(ids.find(i => (titled(i) || {}).id === p))}" class="peek-from" data-reveal="${esc(ids.find(i => (titled(i) || {}).id === p))}" title="Open the paper here">${placeHtml(p)}</a>`).join(', ');
    $$('.gs.peeking').forEach(s => s.classList.remove('peeking')); span.classList.add('peeking');
    openSheet(`<span class="peek-label">From</span> ${from}`, html, 'sheet-peek');
  }
  function peekAnchor(a) {
    const host = anchorHost.get(a); if (!host) return false;
    const n = byId.get(host);
    const tmp = document.createElement('div'); tmp.innerHTML = n.body;
    const el = tmp.querySelector('#' + CSS.escape(a)); if (!el) return false;
    const link = `<a href="#${esc(a)}" class="peek-from" data-reveal="${host}" data-flash="${esc(a)}" title="Open the paper here">${placeHtml(host)}</a>`;
    let what, html, mark = null;
    if (n.kind === 'footnotes') { what = 'Note ' + esc(a.replace(/^fn/, '')); html = `<div class="peek-fn">${stripIds(el.innerHTML)}</div>`; }
    else if (n.kind === 'references') { what = 'Reference'; html = `<div class="peek-fn">${stripIds(el.innerHTML)}</div>`; }
    else if (n.kind === 'figure' || n.kind === 'table') { what = esc(n.title || 'Figure'); html = stripIds(n.body); }
    else { const d = el.closest('.display') || el; what = 'Equation ' + esc((d.querySelector('.eqno') || {}).textContent || ''); html = render(n, PAPER, peekCtx()); mark = 'peek-' + (d.id || a); }
    openSheet(`<span class="peek-label">${what}</span> <span class="peek-in">in</span> ${link}`, html, 'sheet-peek');
    if (mark) { const m = $('#sheet-body #' + CSS.escape(mark)); if (m) { m.scrollIntoView({ block: 'center' }); flash(m); } }
    return true;
  }
  function peekNode(id) {
    const n = byId.get(id); if (!n) return false;
    const link = `<a href="#${esc(id)}" class="peek-from" data-reveal="${esc(id)}" title="Open the paper here">${placeHtml(id)}</a>`;
    openSheet(`<span class="peek-label">From</span> ${link}`, render(n, PAPER, peekCtx()), 'sheet-peek');
    return true;
  }
  function openDef(id, anchor) {
    const d = defs.get(id); if (!d) return;
    const at = d.at && byId.get(d.at.node);
    const where = at ? `<a href="#${esc(at.id)}" class="peek-from" data-reveal="${at.id}" data-quote="${esc(d.at.quote || '')}" title="Open the paper where this is defined">Defined in ${placeHtml(at.id)}</a>` : '';
    const html = `<div class="pop-def">${d.html}</div>${where ? `<div class="pop-foot">${where}</div>` : ''}`;
    const title = `${esc(d.term)}${d.symbol ? `<span class="pop-sym">${d.symbol}</span>` : ''}`;
    if (window.innerWidth < 760) { openSheet(title, html, 'sheet-def'); return; }
    closeSheet();
    const pop = $('#pop'); pop.classList.remove('closing');
    pop.innerHTML = `<div class="pop-head"><div class="pop-term">${title}</div><button type="button" class="x-btn" data-close aria-label="Close">&times;</button></div>${html}`;
    pop.hidden = false;
    const r = anchor.getBoundingClientRect(), w = pop.offsetWidth;
    pop.style.top = (r.bottom + window.scrollY + 6) + 'px';
    pop.style.left = Math.max(8, Math.min(r.left + window.scrollX, document.documentElement.clientWidth - w - 8)) + 'px';
  }
  function openQuestions(id, deep) {
    const qs = (deep ? questionsUnder(id) : (qsAt.get(id) || [])).slice().sort((a, b) => (b.audience === state.audience) - (a.audience === state.audience));
    const SRC = { author: ['author', 'chip'], ai: ['AI · approved', 'chip ai-approved'], reader: ['from a reader', 'chip reader'] };
    const items = qs.map(q => {
      const src = q.source === 'ai' && q.status === 'draft' ? ['AI · unreviewed', 'chip ai-draft'] : SRC[q.source] || ['', 'chip'];
      const where = q.at.node !== id ? `<span class="q-where">${placeHtml(q.at.node)}</span>` : '';
      const shows = (q.answeredBy || []).map(a => `<a href="#${esc(a)}" class="peek-from" data-reveal="${a}">${placeHtml(a)}</a>`).join(', ');
      return `<div class="qa"><div class="q">${q.q}${where}</div><div class="a">${q.a}</div><div class="qa-foot"><span class="${src[1]}">${esc(src[0])}</span>${q.audience ? `<span class="chip">for ${esc(audLabel(q.audience).toLowerCase())}s</span>` : ''}${shows ? `<span class="qa-show">Answered in ${shows}</span>` : ''}</div></div>`;
    }).join('') || '<p class="set-note">No questions here yet.</p>';
    const ask = `<form class="ask" id="ask-form" data-node="${id}"><label for="ask-input">Ask about this part</label><div class="ask-row"><input id="ask-input" type="text" autocomplete="off" placeholder="What would you like to know here?"><button type="submit" class="btn">Ask</button></div><p class="ask-note" id="ask-note" hidden></p></form>`;
    openSheet(`<span class="peek-label">Questions</span> ${placeHtml(id)}`, items + ask, 'sheet-q');
  }
  function openContents() {
    const items = [];
    (function w(n, d) { if (n.title && !['figure', 'table', 'background'].includes(n.kind) && !BOX[n.kind]) items.push({ n, d }); (n.children || []).forEach(c => w(c, d + 1)); })(DOC.root, 0);
    const html = `<ol class="toc">${items.map(({ n, d }) => `<li class="toc-d${d}${n.id === curSection ? ' toc-cur' : ''}"><button type="button" data-reveal="${n.id}"><span class="tocnum">${esc(n.number || '')}</span>${titleOf(n)}</button></li>`).join('')}</ol>`;
    openSheet('Contents', html, 'sheet-toc');
  }
  function seg(name, opts, cur) {
    return `<div class="seg" role="radiogroup"><span class="sel-ind" aria-hidden="true"></span>${opts.map(o => `<button type="button" role="radio" aria-checked="${String(o[0]) === String(cur)}" data-set="${name}:${o[0]}">${esc(o[1])}</button>`).join('')}</div>`;
  }
  function openSettings() {
    const who = AUD.length ? `<div class="set-group"><span class="set-head">Reading as</span>${seg('audience', AUD.map(a => [a.key, a.label]), state.audience)}<p class="set-note"><span id="aud-note">${esc((AUD.find(a => a.key === state.audience) || {}).hint || '')}</span>. Summaries are written for you and background notes open where you need them.</p></div>` : '';
    const html = who +
      `<div class="set-group"><span class="set-head">Section summaries in the Paper view</span>${seg('ledes', [['auto', 'By reader'], ['true', 'Show'], ['false', 'Hide']], state.ledes)}<p class="set-note">By reader: shown to everyone but a specialist.</p></div>` +
      `<div class="set-group"><span class="set-head">Who wrote each summary</span>${seg('chips', [['auto', 'By reader'], ['true', 'Show'], ['false', 'Hide']], state.chips)}<div class="legend" style="margin-top:.5rem"><div><span class="chip">author</span> written by the author</div><div><span class="chip ai-approved">AI draft · approved</span> drafted by the AI reader, checked by the author</div><div><span class="chip ai-draft">AI draft · unreviewed</span> not yet checked</div><div><span class="chip reader">from a reader</span> a question a reader sent in</div></div></div>` +
      `<div class="set-group"><span class="set-head">Appearance</span>${seg('theme', [['system', 'System'], ['light', 'Light'], ['dark', 'Dark']], state.theme)}</div>`;
    openSheet('Settings', html, 'sheet-set');
    $$('#sheet .seg').forEach(moveInd);
  }

  // ------------------------------------------------------------------ events
  document.addEventListener('click', e => {
    const t = e.target.closest('[data-act], [data-setlevel], .gs, [data-peek], [data-go], .qbadge, .qwords, [data-def], a[href^="#"], [data-open], [data-set], [data-reveal], [data-copy], .scrim, [data-close], #back');
    if (!t) { if (!e.target.closest('#pop')) closePop(); return; }
    if (t.matches('.scrim, [data-close]')) { closeAll(); return; }
    if (t.id === 'back') { goBack(); return; }
    if (t.dataset.copy) { copyLink(t.dataset.copy); return; }
    if (t.dataset.open) { if (t.dataset.open === 'contents') openContents(); else if (t.dataset.open === 'search') { closeAll(); if (window.ConiferSearch) ConiferSearch.open(); } else openSettings(); return; }
    if (t.dataset.set) {
      const [k, v] = t.dataset.set.split(':');
      if (k === 'ledes' || k === 'chips') state[k] = v === 'auto' ? 'auto' : v === 'true'; else if (k === 'theme') state.theme = v;
      else if (k === 'audience') { state.audience = v; estimate(); if (skimHidden() && state.level === SKIM) state.level = BRIEF; }
      const g = t.closest('.seg'); if (g) { $$('button', g).forEach(b => b.setAttribute('aria-checked', String(b === t))); moveInd(g); }
      applyTheme(); save(); draw();
      if (k === 'audience') { const note = $('#aud-note'); if (note) note.textContent = (AUD.find(a => a.key === v) || {}).hint || ''; }
      return;
    }
    if (t.dataset.setlevel !== undefined) { setLevel(+t.dataset.setlevel); return; }
    if (t.dataset.act) { if (t.dataset.act === 'open') openFoldAt(t.dataset.key); else closeFoldAt(t.dataset.key); return; }
    if (t.classList.contains('gs')) { peekCovered(t); return; }
    if (t.dataset.peek) { $$('.skim.peeking').forEach(x => x.classList.remove('peeking')); t.classList.add('peeking'); peekNode(t.dataset.peek); return; }
    if (t.dataset.go) { if (longPressed) { longPressed = false; return; } reveal(t.dataset.go); return; }
    if (t.classList.contains('qbadge') || t.classList.contains('qwords')) { openQuestions(t.dataset.q, t.dataset.deep === '1'); return; }
    if (t.dataset.def) { e.preventDefault(); openDef(t.dataset.def, t); return; }
    if (t.dataset.reveal) { e.preventDefault(); const q = t.dataset.quote, f = t.dataset.flash; reveal(t.dataset.reveal, { quote: q, flash: f }); return; }
    if (t.matches('a[href^="#"]')) {
      const a = decodeURIComponent(t.getAttribute('href').slice(1));
      if (LEVEL_HASH.includes(a)) { e.preventDefault(); goHash(a, true); return; }
      if (longPressed) { longPressed = false; e.preventDefault(); return; }
      if (anchorHost.has(a) && ['footnotes', 'references'].includes(byId.get(anchorHost.get(a)).kind)) { e.preventDefault(); peekAnchor(a); return; }   // a note, a citation: a peek, as in Epsilon
      if (byId.has(a)) { e.preventDefault(); if (state.level < PAPER && !t.closest('#sheet') && byId.get(a).kind !== 'section' && byId.get(a).kind !== 'appendix') peekNode(a); else reveal(a); return; }
      if (anchorHost.has(a)) {
        e.preventDefault();
        if (state.level < PAPER || t.closest('#sheet')) { if (!peekAnchor(a)) reveal(anchorHost.get(a), { flash: a }); }
        else reveal(anchorHost.get(a), { flash: a });               // in the paper a tap travels, as in Epsilon; a long press peeks
      }
      return;
    }
  });
  let longPressed = false, lpTimer = null;
  document.addEventListener('pointerdown', e => {
    const a = e.target.closest && e.target.closest('#paper a[href^="#"], #paper [data-go]'); if (!a || e.button !== 0) return;
    const id = a.dataset.go || decodeURIComponent(a.getAttribute('href').slice(1));
    clearTimeout(lpTimer);
    lpTimer = setTimeout(() => { longPressed = true; if (navigator.vibrate) { try { navigator.vibrate(12); } catch (err) {} } if (byId.has(id)) peekNode(id); else if (anchorHost.has(id)) peekAnchor(id); }, 480);
  });
  ['pointerup', 'pointercancel', 'pointerleave'].forEach(ev => document.addEventListener(ev, () => clearTimeout(lpTimer)));
  document.addEventListener('contextmenu', e => { if (e.target.closest && e.target.closest('#paper a[href^="#"]') && longPressed) e.preventDefault(); });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeAll();
    if ((e.key === 'Enter' || e.key === ' ') && e.target.classList && (e.target.classList.contains('gs') || e.target.classList.contains('skim'))) { e.preventDefault(); e.target.click(); }
  });
  document.addEventListener('submit', e => {
    const f = e.target.closest('#ask-form'); if (!f) return;
    e.preventDefault();
    const q = $('#ask-input').value.trim(); const note = $('#ask-note');
    if (!q) return;
    const n = byId.get(f.dataset.node);
    const context = descendants(n.id).map(i => byId.get(i)).filter(x => x.body).map(x => x.body.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim()).join('\n\n');
    note.hidden = false;
    note.innerHTML = `In the product this question would go to a reader model grounded in <b>${placeHtml(n.id)}</b>, and the author could adopt the answer into the paper's questions. Nothing is sent from this page. <button type="button" class="btn" id="copy-ctx">Copy the question with its context</button>`;
    $('#copy-ctx').addEventListener('click', ev => {
      const text = `Question about "${DOC.meta.title}", ${placeName(n.id)}:\n${q}\n\nContext (the text of that part; formulas omitted):\n${context}`;
      const done = () => { ev.target.textContent = 'Copied'; };
      try { navigator.clipboard.writeText(text).then(done, () => { ev.target.textContent = 'Could not copy'; }); } catch (err) { ev.target.textContent = 'Could not copy'; }
    });
  });
  let ticking = false;
  window.addEventListener('scroll', () => { if (ticking) return; ticking = true; requestAnimationFrame(() => { barTitle(); followHash(); ticking = false; }); }, { passive: true });
  window.addEventListener('resize', () => { $$('.dial, .seg').forEach(moveInd); });

  // ------------------------------------------------------------------ boot
  load(); applyTheme();
  if (skimHidden() && state.level === SKIM) state.level = BRIEF;
  function estimate() { estimating = true; EST = LEVELS.map((l, i) => words(render(DOC.root, i, { prefix: '', over: new Map() }))); estimating = false; }
  estimate();
  draw();
  const h = decodeURIComponent(location.hash.slice(1));
  if (h) goHash(h, false);
  commit();
})();
