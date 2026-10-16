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
  const GIST = IDX.gist ?? 0, BRIEF = IDX.brief ?? 1, SKIM = IDX.skim, PAPER = IDX.paper ?? LEVELS.length - 2, FULL = IDX.full ?? Infinity;      // (no tree declares an Everything level now: a fold opens by itself, never by depth)
  const LEVEL_HASH = LEVELS.map(l => ({ gist: 'gist', brief: 'summary', skim: 'skim', paper: 'paper', full: 'everything' })[l.key] || l.key);
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
  const ledesOn = () => state.ledes === true;                    // briefs are folded unless the reader opens them all
  const chipsOn = () => state.chips === true || (state.chips === 'auto' && state.audience !== 'specialist');
  function load() { try { const s = JSON.parse(localStorage.getItem('conifer-reader') || '{}'); ['ledes', 'chips', 'level', 'theme', 'audience'].forEach(k => { if (k in s && (k !== 'ledes' || s.lv === 2)) state[k] = s[k]; });
      if (!(state.level >= 0 && state.level < LEVELS.length)) state.level = Math.min(Math.max(+state.level || 0, 0), LEVELS.length - 1); } catch (e) {} }
  function save() { try { localStorage.setItem('conifer-reader', JSON.stringify({ lv: 2, level: state.level, ledes: state.ledes, chips: state.chips, theme: state.theme, audience: state.audience })); } catch (e) {} }
  function applyTheme() { const r = document.documentElement; if (state.theme === 'light' || state.theme === 'dark') r.dataset.theme = state.theme; else delete r.dataset.theme; }

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
  const circle = (act, key, open) => `<button type="button" class="fold-btn" data-act="toggle" data-key="${key}" title="${open ? 'Fold' : 'Open'}" aria-label="${open ? 'Fold' : 'Open'}" aria-expanded="${open}">${open ? '&minus;' : '+'}</button>`;

  // THE FOLD PATTERN (one for everything that folds: a section's brief, a background note, an appendix, a proof).
  // A fold is a head that never moves and a body under it. The head is the same whether the fold is open or closed:
  // a circled +/− at the left and the title beside it; the whole head is the control. Only the body eases open
  // (its grid track goes from nothing to its size, so nothing is measured or redrawn) and wears the fold's box (a
  // rule at the left for a note). The head is a heading when the fold is a section (an appendix, a brief's section).
  function secHead(n, ctx, lead, foldKey) {
    const hl = Math.min(1 + depth(n.id), 5);
    const anchor = ctx.prefix ? '' : `<button type="button" class="anchor" data-copy="${n.id}" title="Copy a link to this section" aria-label="Copy a link to this section">&#182;</button>`;
    return n.title ? `<h${hl} class="sec-h" data-node="${n.id}"${foldKey ? ` data-fold="${foldKey}"` : ''}>${lead}<span class="secnum">${esc(n.number || '')}</span><span class="sec-t">${titleOf(n)}${qbadge(n, false, ctx)}${anchor}</span></h${hl}>` : '';
  }
  function foldBlock(n, open, L, ctx) {
    const key = ctx.prefix + n.id;
    const bg = n.kind === 'background';
    const lead = ctx.prefix ? '' : circle('toggle', key, open), fk = ctx.prefix ? '' : key;
    let head;
    if (n.kind === 'appendix' && n.children) head = secHead(n, ctx, lead, fk);
    else {
      const name = bg ? 'Background' : n.kind === 'appendix' ? esc('Appendix ' + (n.number || '')) : esc(n.title || BOX[n.kind] || 'More');
      const who = bg ? `<span class="fold-who">for ${esc((n.audience || []).map(a => audLabel(a).toLowerCase() + 's').join(' and '))}</span>` : '';
      const detail = bg ? `<span class="fold-title">${esc(n.title)} ${who}</span>` : `<span class="fold-detail">${n.kind === 'appendix' ? titleOf(n) : n.gist ? pick(n.gist).html : `${words(n.body || '')} words`}</span>`;
      head = `<div class="fold-head"${fk ? ` data-fold="${fk}"` : ''}>${lead}<span class="fold-name">${name}</span>${detail}${bg ? '' : who}</div>`;
    }
    const inner = n.children ? wrap(n, L, ctx, true) : leaf(n, ctx, n.kind === 'proof');
    return `<div class="node fold${bg ? ' fold-bg' : ''}" data-state="${open ? 'open' : 'closed'}" data-id="${n.id}" data-key="${key}"${ctx.prefix ? '' : ` id="${n.id}"`}>${head}<div class="fold-wrap"><div class="fold-body">${inner}</div></div></div>`;
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
    // the section's brief, at Paper depth: a fold under the title, as every fold is (a circled +/− at the left of the
    // title, which folds it as a whole); open by the reader's setting unless this one was folded or opened by hand.
    // In a peek, and inside an appendix (whose title's circle is the appendix's), the brief stands open as it is.
    const briefed = n.brief && L === PAPER && n.id !== DOC.root.id && n.title;
    const ledeKey = ctx.prefix + 'lede:' + n.id, foldable = briefed && !ctx.prefix && !inFold;
    const ledeOpen = foldable ? (ctx.over.has(ledeKey) ? ctx.over.get(ledeKey) >= 3 : ledesOn()) : ledesOn();
    const head = inFold ? '' : secHead(n, ctx, foldable ? circle('toggle', ledeKey, ledeOpen) : '', foldable ? ledeKey : '');
    const lede = foldable ? `<div class="node fold fold-lede" data-state="${ledeOpen ? 'open' : 'closed'}" data-key="${ledeKey}"><div class="fold-wrap"><div class="fold-body">${ledeBlock(n, ctx)}</div></div></div>`
      : briefed && ledeOpen ? ledeBlock(n, ctx) : '';
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
      return foldBlock(n, eff >= 3, Math.max(inh, PAPER), ctx);
    }
    if (!n.children) return leaf(n, ctx);
    return wrap(n, Math.max(inh, PAPER), ctx);
  }
  function actions(from) {
    const b = [];
    if (from < BRIEF) b.push(`<button type="button" class="btn primary" data-setlevel="${BRIEF}">Read the summary</button>`);
    if (SKIM !== undefined && from < SKIM && !skimHidden()) b.push(`<button type="button" class="btn${from === BRIEF ? ' primary' : ''}" data-setlevel="${SKIM}">Skim the paper</button>`);
    b.push(`<button type="button" class="btn${from >= BRIEF && (SKIM === undefined || from >= SKIM) ? ' primary' : ''}" data-setlevel="${PAPER}">Open the paper</button>`);
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
    if (y0 != null) { const after = locate(keepKey); if (after) window.scrollBy(0, after.getBoundingClientRect().top - y0); }
    drawDial(); barTitle();
    if (window.ConiferSearch) ConiferSearch.refresh();
  }
  function moveInd(group) {                       // the chosen option's pill glides to it (the dial, a segmented setting)
    const ind = group.querySelector('.sel-ind'), on = group.querySelector('[aria-checked="true"]');
    if (!ind || !on) return;
    const first = !ind.classList.contains('placed');          // the first placing is a set, not a glide: the pill is where it belongs when the group appears
    ind.style.width = on.offsetWidth + 'px';
    ind.style.transform = 'translateX(' + on.offsetLeft + 'px)';
    if (first) { void ind.offsetWidth; requestAnimationFrame(() => ind.classList.add('placed')); }
  }
  // a fold opens or closes where it stands: only its state flips, the stylesheet eases the rest
  function setFold(key, open) {
    state.over.set(key, open ? 3 : 2); commit();
    const el = $(`#paper .fold[data-key="${CSS.escape(key)}"]`);
    if (!el) { draw(); return; }
    el.dataset.state = open ? 'open' : 'closed';
    $$(`#paper .fold-btn[data-key="${CSS.escape(key)}"]`).forEach(b => {      // the circle turns: + to −, and back
      b.setAttribute('aria-expanded', String(open)); b.innerHTML = open ? '&minus;' : '+'; b.title = b.ariaLabel = open ? 'Fold' : 'Open';
    });
    if (!open && el.getBoundingClientRect().top < barH()) scrollTo(el);      // folded from below its top: the line is kept in sight
    barTitle();
  }
  const openFoldAt = key => setFold(key, true), closeFoldAt = key => setFold(key, false);
  const toggleFold = key => { const el = $(`#paper .fold[data-key="${CSS.escape(key)}"]`); setFold(key, !(el && el.dataset.state === 'open')); };
  window.ConiferFolds = { open: openFoldAt };
  function drawDial() {
    const dial = $('#dial');
    if (!dial.querySelector('button')) dial.innerHTML = '<span class="sel-ind" aria-hidden="true"></span>' + LEVELS.map((l, i) => `<button type="button" role="radio" aria-checked="${i === state.level}" data-setlevel="${i}" title="${esc(l.hint || '')}"><span>${esc(l.label)}</span></button>`).join('');
    $$('button', dial).forEach((b, i) => { b.setAttribute('aria-checked', String(i === state.level)); b.hidden = i === SKIM && skimHidden(); });
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
  // Scrolling to a place. Blocks far from the screen are not laid out (content-visibility, see viewer.css) and stand
  // at an estimated height until they are seen, so where a place is changes while the page scrolls towards it. A long
  // way is therefore taken in one jump and then corrected, frame by frame, until the place stays where it was
  // aimed; a short way scrolls smoothly and is corrected after. The reader's own wheel, touch or key ends it.
  function landAt(want, smooth) {
    const far = Math.abs(want() - window.scrollY) > window.innerHeight * 2.5;
    window.scrollTo({ top: Math.max(0, want()), behavior: smooth && !far && !reduced() ? 'smooth' : 'instant' });
    let stop = false, n = 0, calm = 0;
    const end = () => { stop = true; ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(t => window.removeEventListener(t, end)); };
    ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(t => window.addEventListener(t, end, { passive: true }));
    const fix = () => {
      if (stop) return;
      if (++n > 40) { end(); return; }
      const d = Math.max(0, want()) - window.scrollY;
      if (Math.abs(d) > 3) { calm = 0; window.scrollTo({ top: Math.max(0, want()), behavior: 'instant' }); } else calm++;
      if (calm >= 3) { end(); return; }
      requestAnimationFrame(fix);
    };
    setTimeout(() => requestAnimationFrame(fix), smooth && !far && !reduced() ? 500 : 0);
  }
  window.ConiferScroll = { land: landAt };
  function scrollTo(el) { landAt(() => el.getBoundingClientRect().top + window.scrollY - barH() - 16, true); }
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
    if (reduced()) { sh.hidden = true; $('#scrim').hidden = true; return; }
    sh.classList.add('closing'); $('#scrim').classList.add('closing');
    setTimeout(() => { sh.hidden = true; sh.classList.remove('closing'); $('#scrim').hidden = true; $('#scrim').classList.remove('closing'); }, 190);
  }
  function closePop() {
    const pop = $('#pop'); if (pop.hidden) return;
    if (reduced()) { pop.hidden = true; return; }
    pop.classList.add('closing'); setTimeout(() => { pop.hidden = true; pop.classList.remove('closing'); }, 160);
  }
  function closeAll() { closeSheet(); closePeek(); closePop(); }

  // ------------------------------------------------------------------ the peek (after Epsilon's)
  // A second view below the page: a panel rising from the bottom while the reading stays where it is above, with no
  // veil over it. Its head is a grip: dragged, the peek follows the finger or the mouse, and let go it settles at a
  // third, a half or two thirds of the screen (and remembers which); let go low it closes, pulled up to the bar it
  // becomes the page (as its title's link does). A link inside it moves the peek (its back arrow steps back); a long
  // press or a right click on one goes there in the page. In the page, a long press or a right click on a link opens
  // the peek; a tap on a summary's sentence, a note or a citation does too.
  const PEEK_SNAPS = [0.34, 0.5, 0.66];
  let peekFrac = (() => { try { const v = parseFloat(localStorage.getItem('conifer-peek')); return v > 0.2 && v < 0.9 ? v : 0.5; } catch (e) { return 0.5; } })();
  const peekStack = [];
  const peekAvail = () => window.innerHeight - barH();
  const peekMax = () => peekAvail() - 40;
  const peekIsOpen = () => { const pk = $('#peek'); return !!pk && !pk.hidden && !pk.classList.contains('closing'); };
  function peekSetH(h) {
    h = Math.max(120, Math.min(peekMax(), Math.round(h)));
    $('#peek').style.height = h + 'px';
    document.body.style.paddingBottom = (h + 24) + 'px';        // (room under the page, to read its end above the peek)
    return h;
  }
  function openPeek(title, html, inPeek) {
    closePop();
    if (!$('#sheet').hidden) closeSheet();
    const pk = $('#peek'), body = $('#peek-body');
    if (inPeek && peekIsOpen()) peekStack.push({ title: $('#peek-title').innerHTML, html: body.innerHTML, y: body.scrollTop });
    else peekStack.length = 0;
    $('#peek-title').innerHTML = title; body.innerHTML = html; body.scrollTop = 0;
    $('[data-peekback]', pk).hidden = !peekStack.length;
    if (!peekIsOpen()) { pk.classList.remove('closing'); pk.hidden = false; peekSetH(peekAvail() * peekFrac); }
  }
  function closePeek() {
    const pk = $('#peek'); if (!peekIsOpen()) return;
    $$('.gs.peeking, .skim.peeking').forEach(x => x.classList.remove('peeking'));
    peekStack.length = 0;
    const done = () => { pk.hidden = true; pk.classList.remove('closing'); document.body.style.paddingBottom = ''; };
    if (reduced()) { done(); return; }
    pk.classList.add('closing'); setTimeout(() => { if (pk.classList.contains('closing')) done(); }, 200);
  }
  function peekBack() {
    const prev = peekStack.pop(); if (!prev) return;
    $('#peek-title').innerHTML = prev.title; $('#peek-body').innerHTML = prev.html; $('#peek-body').scrollTop = prev.y;
    $('[data-peekback]').hidden = !peekStack.length;
  }
  function peekGo() { const a = $('#peek-title .peek-from'); if (a) a.click(); }    // the peek becomes the page: its title's link
  (function peekDrag() {
    const pk = $('#peek'); if (!pk) return;
    const head = $('.peek-head', pk); let drag = null;
    head.addEventListener('pointerdown', e => {
      if (e.button !== 0 || e.target.closest('button, a')) return;
      e.preventDefault();
      drag = { y: e.clientY, h: pk.getBoundingClientRect().height, at: null, id: e.pointerId };
      pk.classList.add('dragging'); head.setPointerCapture(e.pointerId);
    });
    head.addEventListener('pointermove', e => {
      if (!drag || e.pointerId !== drag.id) return;
      if (e.clientY <= barH() + 2) { drag = null; pk.classList.remove('dragging'); peekGo(); return; }   // pulled up to the bar
      drag.at = Math.max(40, Math.min(peekAvail(), drag.h + drag.y - e.clientY));
      pk.style.height = drag.at + 'px';
    });
    const end = e => {
      if (!drag || e.pointerId !== drag.id) return;
      const h = drag.at == null ? drag.h : drag.at; drag = null; pk.classList.remove('dragging');
      const avail = peekAvail();
      if (h < avail * 0.17) { closePeek(); return; }                 // let go low: it goes
      peekFrac = PEEK_SNAPS.reduce((a, b) => Math.abs(b * avail - h) < Math.abs(a * avail - h) ? b : a);
      try { localStorage.setItem('conifer-peek', String(peekFrac)); } catch (err) {}
      peekSetH(avail * peekFrac);
    };
    head.addEventListener('pointerup', end); head.addEventListener('pointercancel', end);
    window.addEventListener('resize', () => { if (peekIsOpen()) peekSetH(peekAvail() * peekFrac); });
  })();
  const peekCtx = () => ({ prefix: 'peek|', over: new Map(), plain: true, allOpen: true });
  // the paragraphs a sentence stands for
  function peekCovered(span, inPeek) {
    const ids = span.dataset.covers.split(/\s+/).filter(id => byId.has(id));
    if (!ids.length) return;
    const ctx = peekCtx();
    const html = ids.map(id => render(byId.get(id), PAPER, ctx)).join('');
    const places = [...new Set(ids.map(id => (titled(id) || {}).id).filter(Boolean))];
    const from = places.map(p => `<a href="#${esc(ids.find(i => (titled(i) || {}).id === p))}" class="peek-from" data-reveal="${esc(ids.find(i => (titled(i) || {}).id === p))}" title="Open the paper here">${placeHtml(p)}</a>`).join(', ');
    $$('.gs.peeking').forEach(s => s.classList.remove('peeking')); span.classList.add('peeking');
    openPeek(`<span class="peek-label">From</span> ${from}`, html, inPeek);
  }
  function peekAnchor(a, inPeek) {
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
    openPeek(`<span class="peek-label">${what}</span> <span class="peek-in">in</span> ${link}`, html, inPeek);
    if (mark) { const m = $('#peek-body #' + CSS.escape(mark)); if (m) { m.scrollIntoView({ block: 'center' }); flash(m); } }
    return true;
  }
  function peekNode(id, inPeek) {
    const n = byId.get(id); if (!n) return false;
    const link = `<a href="#${esc(id)}" class="peek-from" data-reveal="${esc(id)}" title="Open the paper here">${placeHtml(id)}</a>`;
    openPeek(`<span class="peek-label">From</span> ${link}`, render(n, PAPER, peekCtx()), inPeek);
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
      `<div class="set-group"><span class="set-head">Section briefs in the Paper view</span>${seg('ledes', [['auto', 'Folded'], ['true', 'Open']], state.ledes === true ? 'true' : 'auto')}<p class="set-note">The circle beside a section's title opens its brief, or folds it again.</p></div>` +
      `<div class="set-group"><span class="set-head">Who wrote each summary</span>${seg('chips', [['auto', 'By reader'], ['true', 'Show'], ['false', 'Hide']], state.chips)}<div class="legend" style="margin-top:.5rem"><div><span class="chip">author</span> written by the author</div><div><span class="chip ai-approved">AI draft · approved</span> drafted by the AI reader, checked by the author</div><div><span class="chip ai-draft">AI draft · unreviewed</span> not yet checked</div><div><span class="chip reader">from a reader</span> a question a reader sent in</div></div></div>` +
      `<div class="set-group"><span class="set-head">Appearance</span>${seg('theme', [['system', 'System'], ['light', 'Light'], ['dark', 'Dark']], state.theme)}</div>`;
    openSheet('Settings', html, 'sheet-set');
    $$('#sheet .seg').forEach(moveInd);
  }

  // ------------------------------------------------------------------ events
  document.addEventListener('click', e => {
    const pb = e.target.closest('[data-peekclose], [data-peekback]');
    if (pb) { if (pb.hasAttribute('data-peekclose')) closePeek(); else peekBack(); return; }
    const foldHead = e.target.closest('[data-fold]');                           // the whole head of a fold is its control, open or closed
    if (foldHead && !e.target.closest('a, .anchor, .qwords, .qbadge, [data-def]')) { toggleFold(foldHead.dataset.fold); return; }
    const t = e.target.closest('[data-act], [data-setlevel], .gs, [data-peek], [data-go], .qbadge, .qwords, [data-def], a[href^="#"], [data-open], [data-set], [data-reveal], [data-copy], .scrim, [data-close], #back');
    if (!t) { if (!e.target.closest('#pop')) closePop(); return; }
    if (t.matches('.scrim, [data-close]')) { closeAll(); return; }
    if (t.id === 'back') { goBack(); return; }
    if (t.dataset.copy) { copyLink(t.dataset.copy); return; }
    if (t.dataset.open) { if (t.dataset.open === 'contents') openContents(); else if (t.dataset.open === 'search') { closeAll(); if (window.ConiferSearch) ConiferSearch.open(); } else openSettings(); return; }
    if (t.dataset.set) {
      const [k, v] = t.dataset.set.split(':');
      if (k === 'ledes' || k === 'chips') state[k] = v === 'auto' ? 'auto' : v === 'true'; else if (k === 'theme') state.theme = v;
      else if (k === 'audience') { state.audience = v; if (skimHidden() && state.level === SKIM) state.level = BRIEF; }
      const g = t.closest('.seg'); if (g) { $$('button', g).forEach(b => b.setAttribute('aria-checked', String(b === t))); moveInd(g); }
      applyTheme(); save(); draw();
      if (k === 'audience') { const note = $('#aud-note'); if (note) note.textContent = (AUD.find(a => a.key === v) || {}).hint || ''; }
      return;
    }
    if (t.dataset.setlevel !== undefined) { setLevel(+t.dataset.setlevel); return; }
    if (t.dataset.act) { toggleFold(t.dataset.key); return; }
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
      const inPeek = !!t.closest('#peek');
      if (anchorHost.has(a) && ['footnotes', 'references'].includes(byId.get(anchorHost.get(a)).kind)) { e.preventDefault(); peekAnchor(a, inPeek); return; }   // a note, a citation: a peek, as in Epsilon
      if (byId.has(a)) { e.preventDefault(); if (inPeek) peekNode(a, true); else if (state.level < PAPER && !t.closest('#sheet') && byId.get(a).kind !== 'section' && byId.get(a).kind !== 'appendix') peekNode(a); else reveal(a); return; }
      if (anchorHost.has(a)) {
        e.preventDefault();
        if (inPeek) { if (!peekAnchor(a, true)) peekNode(anchorHost.get(a), true); }
        else if (state.level < PAPER || t.closest('#sheet')) { if (!peekAnchor(a)) reveal(anchorHost.get(a), { flash: a }); }
        else reveal(anchorHost.get(a), { flash: a });               // in the paper a tap travels, as in Epsilon; a long press peeks
      }
      return;
    }
  });
  let longPressed = false, lpTimer = null;
  const HOLDABLE = '#paper a[href^="#"], #paper [data-go], #peek-body a[href^="#"]';
  function hold(el) {                                // a long press or a right click on a link
    const id = el.dataset.go || decodeURIComponent(el.getAttribute('href').slice(1));
    if (LEVEL_HASH.includes(id)) return false;
    if (el.closest('#peek')) {                       // from the peek: the page goes there
      if (byId.has(id)) reveal(id); else if (anchorHost.has(id)) reveal(anchorHost.get(id), { flash: id }); else return false;
      return true;
    }
    if (byId.has(id)) return peekNode(id);
    if (anchorHost.has(id)) return peekAnchor(id) || peekNode(anchorHost.get(id));
    return false;
  }
  document.addEventListener('pointerdown', e => {
    const a = e.target.closest && e.target.closest(HOLDABLE); if (!a || e.button !== 0) return;
    clearTimeout(lpTimer); longPressed = false;
    const x = e.clientX, y = e.clientY;
    const move = ev => { if (Math.abs(ev.clientX - x) + Math.abs(ev.clientY - y) > 10) { clearTimeout(lpTimer); document.removeEventListener('pointermove', move); } };
    document.addEventListener('pointermove', move, { passive: true });
    lpTimer = setTimeout(() => { document.removeEventListener('pointermove', move); if (hold(a)) { longPressed = true; if (navigator.vibrate) { try { navigator.vibrate(12); } catch (err) {} } } }, 480);
  });
  ['pointerup', 'pointercancel'].forEach(ev => document.addEventListener(ev, () => clearTimeout(lpTimer)));
  document.addEventListener('contextmenu', e => {      // a right click (or the browser's own long press) on a link peeks
    const a = e.target.closest && e.target.closest(HOLDABLE); if (!a) return;
    e.preventDefault();
    if (longPressed) return;                          // (the long press has opened it already)
    clearTimeout(lpTimer);
    hold(a);                                          // (a right click makes no click after it: nothing to swallow)
  });
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
  draw();
  const h = decodeURIComponent(location.hash.slice(1));
  if (h) goHash(h, false);
  commit();
})();
