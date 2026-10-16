"""The sample Conifer document: an expository note on Wigner's semicircle law, written in the proposed
data structure (see ../DESIGN.md). build.py turns it into semicircle.tree.json (the document as data, TeX
intact) and into the mockup page (math drawn as SVG).

Conventions used in the HTML strings:
  $...$ and \\[...\\]           inline and display math (TeX), drawn by MathJax at build time
  <span data-covers="a b">     a sentence of a summary and the nodes it summarises (grounding)
  <dfn data-def="x">, <a data-def="x">   the defining occurrence of a term, and later mentions
  <a class="eqref" href="#eq-x">(3)</a>  a reference to an equation (the viewer reveals and flashes it)
  <a class="secref" href="#id">          a reference to a node
  <a class="cite" href="#ref-x">[1]</a>  a citation
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIG1 = (HERE / "figures" / "semicircle.svg").read_text()

FIG2 = r"""<svg class="fig fig-pairings" viewBox="0 0 640 150" role="img" aria-label="The three pairings of four points: two non-crossing, one crossing">
<g font-family="var(--sans)" font-size="13" fill="currentColor" text-anchor="middle">
<g transform="translate(10,0)">
 <path d="M30 100 A25 25 0 0 1 80 100" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
 <path d="M130 100 A25 25 0 0 1 180 100" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
 <g fill="currentColor"><circle cx="30" cy="100" r="4"/><circle cx="80" cy="100" r="4"/><circle cx="130" cy="100" r="4"/><circle cx="180" cy="100" r="4"/></g>
 <text x="30" y="122">1</text><text x="80" y="122">2</text><text x="130" y="122">3</text><text x="180" y="122">4</text>
 <text x="105" y="143">{12}{34} — sphere</text>
</g>
<g transform="translate(220,0)">
 <path d="M30 100 A75 75 0 0 1 180 100" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
 <path d="M80 100 A25 25 0 0 1 130 100" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
 <g fill="currentColor"><circle cx="30" cy="100" r="4"/><circle cx="80" cy="100" r="4"/><circle cx="130" cy="100" r="4"/><circle cx="180" cy="100" r="4"/></g>
 <text x="30" y="122">1</text><text x="80" y="122">2</text><text x="130" y="122">3</text><text x="180" y="122">4</text>
 <text x="105" y="143">{14}{23} — sphere</text>
</g>
<g transform="translate(430,0)">
 <path d="M30 100 A50 50 0 0 1 130 100" fill="none" stroke="var(--warn)" stroke-width="2.5"/>
 <path d="M80 100 A50 50 0 0 1 180 100" fill="none" stroke="var(--warn)" stroke-width="2.5"/>
 <g fill="currentColor"><circle cx="30" cy="100" r="4"/><circle cx="80" cy="100" r="4"/><circle cx="130" cy="100" r="4"/><circle cx="180" cy="100" r="4"/></g>
 <text x="30" y="122">1</text><text x="80" y="122">2</text><text x="130" y="122">3</text><text x="180" y="122">4</text>
 <text x="105" y="143">{13}{24} — torus</text>
</g>
</g></svg>"""


def T(html, status="ai-approved", **kw):
    """A rendition of a node at one level: its text, who wrote it, and (optionally) more."""
    d = {"html": html, "status": status}
    d.update(kw)
    return d


DOC = {
    "format": "conifer-doc",
    "version": 1,
    "meta": {
        "title": "Wigner's semicircle law by the moment method",
        "kicker": "Conifer sample · an expository note",
        "authors": ["Written for the Conifer mockup"],
        "date": "October 2026",
        "note": "The text of this note was written for the mockup; it is standard material, but it has not been refereed.",
        "key": {"equation": "eq-sc", "figure": "fig-semicircle"},
        "source": {"kind": "mockup", "generator": "doc_semicircle.py"},
        "defaultAudience": "physicist",
    },
    "audiences": [
        {"key": "specialist", "label": "Specialist", "hint": "works on random matrices or holography"},
        {"key": "physicist", "label": "Physicist", "hint": "from another field; knows quantum mechanics"},
        {"key": "student", "label": "Student", "hint": "knows linear algebra and some probability"},
    ],
    "levels": [
        {"key": "gist", "label": "Gist", "hint": "the trunk: the three things to know"},
        {"key": "brief", "label": "Summary", "hint": "the branches: one page, every sentence opens"},
        {"key": "paper", "label": "Paper", "hint": "the foliage: the full text, with the roots folded"},
    ],
    "root": {
        "id": "root",
        "kind": "paper",
        "gist": T(
            r"""<ul class="gist-list">
<li><b>Context</b> The eigenvalues of a large random Hermitian matrix are not scattered at random: their density has a universal shape, found by Wigner in the 1950s for nuclear spectra and met again today wherever a Hamiltonian is modelled by a random matrix.</li>
<li><b>Result</b> For the <a data-def="gue">GUE</a> normalised so that $\mathbb E|H_{ij}|^2 = 1/N$, the density of eigenvalues converges, as $N\to\infty$, to the semicircle <a class="eqref" href="#eq-sc">(1)</a> on $[-2,2]$. The proof is a count: the $2n$-th moment of the spectrum tends to the <a data-def="catalan">Catalan number</a> $C_n$, the number of <a data-def="noncrossing">non-crossing pairings</a> of $2n$ points, and the semicircle is the unique density with those moments.</li>
<li><b>Why it matters</b> The same count organises the $1/N$ expansion as a sum over surfaces by genus, the mechanism behind “matrix model = sum over surfaces” that underlies two-dimensional gravity and JT gravity. The semicircle is the first entry of that dictionary.</li>
</ul>""",
            status="author",
            variants={
                "specialist": T(r"""<ul class="gist-list">
<li><b>Context</b> The moment method for the GUE, written out with the genus expansion made explicit.</li>
<li><b>Result</b> $\mathbb E\,m_{2n}^{(N)} = \sum_{g}\varepsilon_g(n)\,N^{-2g}$ with $\varepsilon_0(n) = C_n$; the semicircle then follows from the determinacy of the moment problem and from $O(N^{-2})$ concentration. Harer–Zagier gives $\varepsilon_1(n) = (2n)!/(12\,n!\,(n-2)!)$.</li>
<li><b>Why it matters</b> Nothing here is new. The note is a reference for the structure (polygon gluings, Euler characteristic, Catalan recursion) that double-scales into the matrix integral of JT gravity.</li>
</ul>""", status="author"),
                "student": T(r"""<ul class="gist-list">
<li><b>Context</b> Take a large matrix whose entries are random numbers, symmetric enough to have real eigenvalues. Where do its eigenvalues lie?</li>
<li><b>Result</b> Not just anywhere. For an $N\times N$ matrix with entries of size $1/\sqrt N$, almost all eigenvalues fall between $-2$ and $2$, with a density shaped like a semicircle (equation (1) and Figure 1). The proof computes the averages of $\lambda^2, \lambda^4, \lambda^6, \dots$ over the eigenvalues and finds that they become the Catalan numbers $1, 2, 5, 14, \dots$, which are exactly the moments of a semicircle.</li>
<li><b>Why it matters</b> This is the first result of random matrix theory, which describes the energy levels of complex quantum systems, from nuclei to black holes. The counting behind it, a sum over surfaces sorted by their number of handles, reappears throughout theoretical physics.</li>
</ul>""", status="ai-approved"),
            },
        ),
        "brief": T(
            r"""<p><span data-covers="intro">In 1955 Wigner proposed to model the Hamiltonian of a heavy nucleus by a large random Hermitian matrix, and noticed that although its eigenvalues are random their density is not: for large $N$ it settles on a semicircle, whatever the details of the distribution of the entries.</span> <span data-covers="intro-p2">For the Gaussian unitary ensemble with $\mathbb E|H_{ij}|^2 = 1/N$ the statement is that the empirical density $\rho_N(x) = \frac1N\sum_i\delta(x-\lambda_i)$ converges to $\rho_{\rm sc}(x) = \frac{1}{2\pi}\sqrt{4-x^2}$ on $[-2,2]$.</span></p>
<p><span data-covers="setup">The ensemble is fixed by one covariance, $\mathbb E\,H_{ij}H_{kl} = \delta_{il}\delta_{jk}/N$, and the moments of $\rho_N$ are traces, $m_k^{(N)} = \frac1N\operatorname{Tr}H^k$; the normalisation is the one for which $\mathbb E\,m_2^{(N)} = 1$ for every $N$, so the spectrum stays of order one.</span></p>
<p><span data-covers="wick">Wick's theorem writes the expectation of a product of Gaussian entries as a sum over pairings of the factors, and the covariance identifies indices along each pair, so $\mathbb E\,m_k^{(N)}$ becomes a sum over pairings of powers of $N$.</span> <span data-covers="genus">Each pairing glues the $k$-gon of factors into a closed surface, and Euler's formula turns the power of $N$ into $N^{-2g}$ with $g$ the genus: a pairing contributes $1$ when its chords do not cross and the surface is a sphere, and is suppressed otherwise.</span> <span data-covers="catalan">The non-crossing pairings of $2n$ points obey the Catalan recursion, so $\mathbb E\,m_{2n}^{(N)}\to C_n = \frac{1}{n+1}\binom{2n}{n}$, with $1/N^2$ corrections that count the gluings of higher genus.</span></p>
<p><span data-covers="density-p1 density-p2">The semicircle has exactly these moments (substitute $x = 2\cos\theta$), and a density supported in a bounded interval is determined by its moments, so $\mathbb E\,\rho_N\to\rho_{\rm sc}$.</span> <span data-covers="density-p3">A second application of Wick's theorem shows that the variance of each moment is $O(1/N^2)$, so a single large matrix already shows the semicircle, as Figure 1 does at $N = 1000$.</span> <span data-covers="density-p4">The resolvent $G(z)$ packages the same computation into the quadratic equation $G = 1/(z-G)$.</span></p>
<p><span data-covers="disc-p1">Only the second moment of the entries entered, so the law holds for any Wigner matrix, and for the real symmetric ensemble with $1/N$ rather than $1/N^2$ corrections.</span> <span data-covers="disc-p2">The sum over pairings by genus is the simplest instance of the $1/N$ expansion of a matrix integral as a sum over surfaces, the dictionary that JT gravity realises surface by surface.</span> <span data-covers="disc-p3">The semicircle is a statement about the density on the scale of the whole spectrum; it says nothing about level repulsion, which lives at separations of order $1/N$ and needs other tools.</span></p>""",
            status="ai-approved",
        ),
        "children": [
            {
                "id": "intro", "kind": "section", "number": "1", "title": "Introduction", "role": "context",
                "gist": T("Random Hermitian matrices have a universal eigenvalue density, the semicircle; this note proves it by computing moments.", status="author"),
                "brief": T(r"""<p><span data-covers="intro-p1">Wigner's 1955 proposal to model a nuclear Hamiltonian by a random Hermitian matrix led to the observation that the eigenvalue density of such a matrix is universal at large $N$: a semicircle, now met in quantum chaos and in holography as well.</span> <span data-covers="intro-p2">For the GUE normalised so that $\mathbb E|H_{ij}|^2 = 1/N$, the empirical density converges to $\rho_{\rm sc}(x) = \frac{1}{2\pi}\sqrt{4-x^2}$.</span> <span data-covers="intro-p3">The proof here is the moment method: the moments of the spectrum are traces, Wick's theorem turns them into sums over pairings, the pairings that survive at large $N$ are counted by Catalan numbers, and the semicircle is the unique density with those moments.</span></p>""", status="ai-approved"),
                "children": [
                    {"id": "intro-p1", "kind": "paragraph", "role": "context",
                     "gist": T("Wigner's random-matrix model of nuclear spectra, and where the same density appears today.", status="ai-approved"),
                     "body": r"""<p>In 1955 Wigner proposed to model the Hamiltonian of a heavy nucleus by a large random <a data-def="hermitian">Hermitian</a> matrix <a class="cite" href="#ref-wigner55">[1]</a>. The individual eigenvalues of such a matrix are random, but their density is not: for large $N$ it settles on a fixed shape, the <dfn data-def="semicircle">semicircle</dfn>, whatever the details of the distribution of the entries <a class="cite" href="#ref-wigner58">[2]</a>. The same density appears today for random Hamiltonians in quantum chaos, and in holography, where the Hamiltonian of a black hole is modelled by a random matrix and the matrix integral is itself a theory of two-dimensional gravity <a class="cite" href="#ref-sss">[6]</a>.</p>"""},
                    {"id": "intro-p2", "kind": "paragraph", "role": "result",
                     "gist": T("The statement: for the GUE with $\\mathbb E|H_{ij}|^2 = 1/N$, the eigenvalue density converges to the semicircle (1).", status="ai-approved"),
                     "body": r"""<p>Let $H$ be drawn from the <a data-def="gue">Gaussian unitary ensemble</a> of $N\times N$ Hermitian matrices, normalised so that $\mathbb E|H_{ij}|^2 = 1/N$. Then the density of its eigenvalues converges, as $N\to\infty$, to
\[\rho_{\rm sc}(x) = \frac{1}{2\pi}\sqrt{4-x^2}\qquad(|x|\le 2),\tag{1}\label{eq-sc}\]
and to zero outside $[-2,2]$. Figure 1 shows one draw of the spectrum at $N = 1000$.</p>"""},
                    {"id": "fig-semicircle", "kind": "figure", "number": "1", "title": "Figure 1",
                     "body": r"""<figure id="figure-1">""" + FIG1 + r"""<figcaption><b>Figure 1.</b> The histogram of the eigenvalues of one $1000\times 1000$ GUE matrix, scaled by $1/\sqrt N$, against the semicircle <a class="eqref" href="#eq-sc">(1)</a>. (The spectrum was sampled through the tridiagonal model of Dumitriu and Edelman, which has the same joint distribution of eigenvalues.)</figcaption></figure>"""},
                    {"id": "bg-intro", "kind": "background", "title": "Why a random matrix?", "audience": ["physicist", "student"], "fold": True,
                     "body": r"""<p>A heavy nucleus has hundreds of nucleons and no tractable Hamiltonian. Wigner's idea was to give up on the particular matrix and ask instead which properties a Hermitian matrix has <i>typically</i>, when its entries are drawn at random. Questions about one Hamiltonian become questions about an ensemble of them, and the answers that do not depend on the details of the ensemble are the ones one may trust for the real system. The same move is made today for chaotic quantum systems in general, and for black holes, whose Hamiltonian is argued to behave like a random matrix as far as the statistics of its energy levels are concerned.</p>"""},
                    {"id": "intro-p3", "kind": "paragraph", "role": "method",
                     "gist": T("The method: moments are traces, Wick's theorem gives pairings, the surviving pairings are counted by Catalan numbers.", status="ai-approved"),
                     "body": r"""<p>We follow the moment method. The $k$-th moment of the eigenvalue density is $\frac1N\operatorname{Tr}H^k$, a polynomial in the entries whose expectation Wick's theorem turns into a sum over pairings. Counting the pairings that survive at large $N$ gives the Catalan numbers, and the semicircle is the unique density with those moments. <a class="secref" href="#setup">Section 2</a> fixes the setup, <a class="secref" href="#moments">Section 3</a> computes the moments, <a class="secref" href="#density">Section 4</a> identifies the density, and <a class="secref" href="#discussion">Section 5</a> discusses what the argument shows and what it does not. <a class="secref" href="#app-catalan">Appendix A</a> collects facts about Catalan numbers; <a class="secref" href="#app-genus1">Appendix B</a> records the first $1/N^2$ correction.</p>"""},
                ],
            },
            {
                "id": "setup", "kind": "section", "number": "2", "title": "Setup", "role": "background",
                "gist": T("The GUE with entries of variance $1/N$, and the moments of its empirical spectral density.", status="ai-approved"),
                "brief": T(r"""<p><span data-covers="setup-p1">The GUE is the Gaussian measure $\propto\exp(-\frac N2\operatorname{Tr}H^2)$ on Hermitian matrices; equivalently, centred Gaussian entries with covariance $\mathbb E\,H_{ij}H_{kl} = \delta_{il}\delta_{jk}/N$, so that every entry has variance $1/N$.</span> <span data-covers="setup-p2">The empirical spectral density $\rho_N$ is the normalised sum of delta functions at the eigenvalues, and its moments are the traces $m_k^{(N)} = \frac1N\operatorname{Tr}H^k$; with this normalisation $\mathbb E\,m_2^{(N)} = 1$ for every $N$.</span> <span data-covers="setup-p3">The theorem is stated for the expected moments; that a single matrix shows the semicircle is a separate point, settled in Section 4.</span></p>""", status="ai-approved"),
                "children": [
                    {"id": "setup-p1", "kind": "paragraph", "role": "background",
                     "gist": T("Definition of the GUE and its covariance (2).", status="ai-approved"),
                     "body": r"""<p>The <dfn data-def="gue">Gaussian unitary ensemble</dfn> (GUE) is the probability distribution on $N\times N$ <a data-def="hermitian">Hermitian</a> matrices with density proportional to $\exp\!\big(-\tfrac N2\operatorname{Tr}H^2\big)$. Equivalently, the entries are centred Gaussian variables, independent up to the Hermiticity constraint $H_{ji} = \overline{H_{ij}}$, with covariance
\[\mathbb E\,H_{ij}H_{kl} = \frac1N\,\delta_{il}\,\delta_{jk}.\tag{2}\label{eq-cov}\]
In particular $\mathbb E|H_{ij}|^2 = 1/N$ for every pair $i,j$, the diagonal included.</p>"""},
                    {"id": "bg-spectrum", "kind": "background", "title": "Eigenvalues and their density", "audience": ["student"], "fold": True,
                     "body": r"""<p>A <dfn data-def="hermitian">Hermitian matrix</dfn>, one with $H_{ji} = \overline{H_{ij}}$, has $N$ real eigenvalues $\lambda_1\le\dots\le\lambda_N$: the possible energies, if $H$ is a Hamiltonian. Their density is a histogram: for an interval $I$, the fraction of eigenvalues in $I$ is $\int_I\rho_N(x)\,dx$. For one matrix $\rho_N$ is a sum of $N$ spikes; the semicircle law says that as $N$ grows the spikes fill in a smooth curve. The moments $\int x^k\rho_N(x)\,dx$ are the averages of $\lambda^k$ over the eigenvalues, and $\sum_i\lambda_i^k = \operatorname{Tr}H^k$ because the trace does not depend on the basis, and in the eigenbasis $H^k$ is diagonal with entries $\lambda_i^k$.</p>"""},
                    {"id": "setup-p2", "kind": "paragraph", "role": "background",
                     "gist": T("The empirical density, its moments as traces (3), and why the variance $1/N$ keeps the spectrum of order one.", status="ai-approved"),
                     "body": r"""<p>Write $\lambda_1,\dots,\lambda_N$ for the eigenvalues. The <dfn data-def="esd">empirical spectral density</dfn> is $\rho_N(x) = \frac1N\sum_i\delta(x-\lambda_i)$, a random probability measure, and its <dfn data-def="moment">moments</dfn> are traces:
\[m_k^{(N)} \equiv \int x^k\rho_N(x)\,dx = \frac1N\operatorname{Tr}H^k.\tag{3}\label{eq-moments}\]
The normalisation in <a class="eqref" href="#eq-cov">(2)</a> is chosen so that the spectrum stays of order one: $\mathbb E\,m_2^{(N)} = \frac1N\sum_{i,j}\mathbb E|H_{ij}|^2 = 1$ for every $N$.</p>"""},
                    {"id": "setup-p3", "kind": "paragraph", "role": "caveat",
                     "body": r"""<p>Theorem 1 below concerns the expected moments $\mathbb E\,m_k^{(N)}$. Since $\rho_N$ is random, one may ask whether a single large matrix already shows the semicircle; it does, and we return to this in <a class="secref" href="#density-p3">Section 4</a>.</p>"""},
                ],
            },
            {
                "id": "moments", "kind": "section", "number": "3", "title": "The moments", "role": "derivation",
                "gist": T("Wick's theorem writes the $2n$-th moment as a sum over pairings weighted by $N^{-2g}$; the planar ones survive and are counted by Catalan numbers.", status="ai-approved"),
                "brief": T(r"""<p><span data-covers="wick">Wick's theorem turns $\mathbb E\operatorname{Tr}H^k$ into a sum over pairings of the $k$ factors, each pair identifying two indices by the covariance (2), so that $\mathbb E\,m_k^{(N)}$ is $N^{-1-k/2}$ times a sum over pairings of the number of free indices each leaves.</span> <span data-covers="genus">Reading the factors as the edges of a polygon, a pairing is a gluing of the polygon into a closed surface whose vertices are the free indices; Euler's formula gives $\mathbb E\,m_k^{(N)} = \sum_\pi N^{-2g(\pi)}$, and $g = 0$ exactly for the non-crossing pairings.</span> <span data-covers="catalan">The non-crossing pairings of $2n$ points obey the Catalan recursion, whence Theorem 1: $\mathbb E\,m_{2n}^{(N)}\to C_n$.</span></p>""", status="ai-approved"),
                "children": [
                    {
                        "id": "wick", "kind": "section", "number": "3.1", "title": "Wick's theorem", "role": "derivation",
                        "gist": T("Expectations of products of Gaussian variables are sums over pairings; applied to the trace, each pair identifies indices.", status="ai-approved"),
                        "brief": T(r"""<p><span data-covers="wick-p1">For centred jointly Gaussian variables, the expectation of a product is the sum over all pairings of the factors of the product of the pair covariances (4).</span> <span data-covers="wick-p2">In $\mathbb E\operatorname{Tr}H^k$ a pair $\{a,b\}$ contributes $\frac1N\delta_{i_ai_{b+1}}\delta_{i_{a+1}i_b}$, so the moment is a sum over pairings of $N$ to the number of free indices, divided by $N^{1+k/2}$ (5).</span></p>""", status="ai-approved"),
                        "children": [
                            {"id": "wick-p1", "kind": "paragraph", "role": "background",
                             "gist": T("Wick's theorem (4): a sum over pairings of pair covariances.", status="ai-approved"),
                             "body": r"""<p><dfn data-def="wick">Wick's theorem</dfn>. For centred jointly Gaussian variables $X_1,\dots,X_k$,
\[\mathbb E[X_1\cdots X_k] = \sum_{\pi}\ \prod_{\{a,b\}\in\pi}\mathbb E[X_aX_b],\tag{4}\label{eq-wick}\]
where the sum runs over the <dfn data-def="pairing">pairings</dfn> $\pi$ of $\{1,\dots,k\}$, the partitions of the set into $k/2$ two-element blocks, and is empty for odd $k$. There are $(k-1)!! = (k-1)(k-3)\cdots 1$ pairings in all.</p>"""},
                            {"id": "bg-wick", "kind": "background", "title": "Wick's theorem by example", "audience": ["student"], "fold": True,
                             "body": r"""<p>For one centred Gaussian variable $X$ with $\mathbb E X^2 = \sigma^2$, the moments are $\mathbb E X^4 = 3\sigma^4$ and in general $\mathbb E X^{2n} = (2n-1)!!\,\sigma^{2n}$: the number of ways to pair up $2n$ factors, each pair contributing $\sigma^2$. Wick's theorem is the same statement for several variables with a covariance matrix. It follows from the fact that the characteristic function $\mathbb E\,e^{i\sum_a t_aX_a} = e^{-\frac12\sum_{a,b}t_at_b\,\mathbb E[X_aX_b]}$ is the exponential of a quadratic form: expanding it, every term is a product of pair covariances. For four variables, $\mathbb E[X_1X_2X_3X_4] = \mathbb E[X_1X_2]\,\mathbb E[X_3X_4] + \mathbb E[X_1X_3]\,\mathbb E[X_2X_4] + \mathbb E[X_1X_4]\,\mathbb E[X_2X_3]$.</p>"""},
                            {"id": "wick-p2", "kind": "paragraph", "role": "derivation",
                             "gist": T("Applied to the trace: each pair identifies two indices, giving the sum (5) over pairings of free-index counts.", status="ai-approved"),
                             "body": r"""<p>Expanding the trace, $\mathbb E\operatorname{Tr}H^k = \sum_{i_1,\dots,i_k}\mathbb E[H_{i_1i_2}H_{i_2i_3}\cdots H_{i_ki_1}]$, and each expectation is a sum over pairings of the $k$ factors. By <a class="eqref" href="#eq-cov">(2)</a> a pair $\{a,b\}$ contributes $\frac1N\delta_{i_ai_{b+1}}\delta_{i_{a+1}i_b}$: the second index of one factor is identified with the first index of the other, and vice versa (indices are read cyclically, $i_{k+1} = i_1$). Each pairing therefore leaves some number $V(\pi)$ of free index sums, and
\[\mathbb E\,m_k^{(N)} = \frac{1}{N^{1+k/2}}\sum_{\pi} N^{V(\pi)}.\tag{5}\label{eq-free}\]</p>"""},
                        ],
                    },
                    {
                        "id": "genus", "kind": "section", "number": "3.2", "title": "Pairings as surfaces", "role": "derivation",
                        "gist": T("Each pairing glues the $k$-gon into a closed surface; it contributes $N^{-2g}$ with $g$ its genus, so only non-crossing pairings survive.", status="ai-draft"),
                        "brief": T(r"""<p><span data-covers="genus-p1">Draw the $k$ factors as the edges of a polygon; a pairing identifies edges in pairs with opposite orientation, exactly as the covariance identifies indices, and glues the polygon into a closed orientable surface whose vertices are the free indices.</span> <span data-covers="genus-p2">With one face, $k/2$ edges and $V$ vertices, Euler's formula gives $V = k/2 + 1 - 2g$, so each pairing contributes $N^{-2g}$ (6).</span> <span data-covers="genus-p3">The surface is a sphere exactly when the chords of the pairing do not cross (Figure 2); for $k = 4$ this gives $\mathbb E\,m_4^{(N)} = 2 + N^{-2}$.</span></p>""", status="ai-draft"),
                        "children": [
                            {"id": "genus-p1", "kind": "paragraph", "role": "derivation",
                             "gist": T("The polygon picture: a pairing is a gluing of edges; free indices are the vertices of the glued surface.", status="ai-approved"),
                             "body": r"""<p>The count in <a class="eqref" href="#eq-free">(5)</a> has a geometric meaning. Draw the $k$ factors as the $k$ edges of a polygon, oriented cyclically, each edge carrying the two indices of its factor at its two ends. A pair $\{a,b\}$ identifies edge $a$ with edge $b$ with opposite orientations, which is exactly the identification of indices forced by <a class="eqref" href="#eq-cov">(2)</a>. Gluing all $k/2$ pairs of edges turns the polygon into a closed orientable surface, and the index constraints say that all the corners of the polygon that meet at one point of the surface carry the same index. The free indices are therefore the vertices of the glued surface, and $V(\pi)$ is their number.</p>"""},
                            {"id": "bg-genus", "kind": "background", "title": "Euler's formula and the genus", "audience": ["physicist", "student"], "fold": True,
                             "body": r"""<p>A closed orientable surface is a sphere with $g$ handles attached, and $g$ is its genus: $0$ for the sphere, $1$ for the torus. If the surface is cut into $F$ faces by $E$ edges meeting at $V$ vertices, then $V - E + F = 2 - 2g$, whatever the cutting. Below, the glued polygon is cut into one face (the polygon), $E = k/2$ edges (the glued pairs) and $V$ vertices (the points where corners of the polygon meet), so the formula reads $V - k/2 + 1 = 2 - 2g$.</p>"""},
                            {"id": "genus-p2", "kind": "paragraph", "role": "derivation",
                             "gist": T("Euler's formula turns the free-index count into $N^{-2g}$ (6).", status="ai-approved"),
                             "body": r"""<p>The glued surface has one face (the polygon itself), $k/2$ edges and $V$ vertices, so Euler's formula $V - k/2 + 1 = 2 - 2g$ gives $V = k/2 + 1 - 2g$, with $g\ge0$ the <dfn data-def="genus">genus</dfn> of the surface. Substituting in <a class="eqref" href="#eq-free">(5)</a>,
\[\mathbb E\,m_k^{(N)} = \sum_{\pi} N^{-2g(\pi)}.\tag{6}\label{eq-genus}\]
Every pairing contributes at most $1$, and exactly $1$ when the glued surface is a sphere.</p>"""},
                            {"id": "genus-p3", "kind": "paragraph", "role": "derivation",
                             "gist": T("Sphere means non-crossing chords (Figure 2); for $k=4$, $\\mathbb E\\,m_4^{(N)} = 2 + N^{-2}$.", status="ai-approved"),
                             "body": r"""<p>A pairing glues the polygon into a sphere precisely when its chords can be drawn inside the polygon without crossing; such a pairing is called <dfn data-def="noncrossing">non-crossing</dfn>, or planar. A crossing forces a handle (Figure 2). For $k = 4$ there are three pairings, two of them non-crossing, and <a class="eqref" href="#eq-genus">(6)</a> reads $\mathbb E\,m_4^{(N)} = 2 + N^{-2}$, the crossing pairing giving a torus; <a class="secref" href="#app-genus1">Appendix B</a> spells out the index sums.</p>"""},
                            {"id": "fig-pairings", "kind": "figure", "number": "2", "title": "Figure 2",
                             "body": r"""<figure id="figure-2">""" + FIG2 + r"""<figcaption><b>Figure 2.</b> The three pairings of the four factors of $\operatorname{Tr}H^4$, drawn as chords between the four points. The two non-crossing pairings glue the square into a sphere and contribute $1$ each; the crossing pairing glues it into a torus and contributes $N^{-2}$.</figcaption></figure>"""},
                        ],
                    },
                    {
                        "id": "catalan", "kind": "section", "number": "3.3", "title": "Catalan numbers", "role": "result",
                        "gist": T("Non-crossing pairings of $2n$ points are counted by the Catalan numbers; hence the moments converge to $C_n$ (Theorem 1).", status="ai-approved"),
                        "brief": T(r"""<p><span data-covers="thm-moments">Theorem 1: $\mathbb E\,m_{2n}^{(N)}\to C_n = \frac{1}{n+1}\binom{2n}{n}$, and the odd moments vanish.</span> <span data-covers="proof-moments">The chord from point 1 of a non-crossing pairing ends at an even point and separates the rest into two independent blocks, which gives the Catalan recursion (7); Appendix A solves it.</span> <span data-covers="catalan-p3">At finite $N$ the moments are polynomials in $1/N^2$ whose coefficients count the pairings of each genus.</span></p>""", status="ai-approved"),
                        "children": [
                            {"id": "thm-moments", "kind": "theorem", "title": "Theorem 1", "role": "result",
                             "body": r"""<p>For every fixed $k$, $\displaystyle\lim_{N\to\infty}\mathbb E\,m_k^{(N)} = C_{k/2}$ for $k$ even and $0$ for $k$ odd, where
\[C_n = \frac{1}{n+1}\binom{2n}{n} = 1,\ 1,\ 2,\ 5,\ 14,\ 42,\ \dots\]
is the $n$-th <dfn data-def="catalan">Catalan number</dfn>.</p>"""},
                            {"id": "proof-moments", "kind": "proof", "title": "Proof", "fold": True,
                             "gist": T("The first chord of a non-crossing pairing splits the points into two independent non-crossing blocks, giving the Catalan recursion (7).", status="ai-approved"),
                             "body": r"""<p>By <a class="eqref" href="#eq-genus">(6)</a> the limit is the number of genus-zero pairings, that is, of non-crossing pairings of $2n$ points on a circle. Let $c_n$ be that number, with $c_0 = 1$. In a non-crossing pairing the chord from point $1$ ends at some even point $2j$ (an odd endpoint would leave an odd number of points on one side of the chord), and it separates the remaining points into two groups, of $2j-2$ and $2n-2j$ points, that cannot be joined to each other. Hence
\[c_n = \sum_{j=1}^{n} c_{j-1}\,c_{n-j},\tag{7}\label{eq-catrec}\]
which is the recursion of the Catalan numbers; <a class="secref" href="#app-catalan">Appendix A</a> solves it and shows $c_n = C_n$. For odd $k$ there are no pairings at all. $\square$</p>"""},
                            {"id": "catalan-p3", "kind": "paragraph", "role": "result",
                             "body": r"""<p>The exact moments are polynomials in $1/N^2$: $\mathbb E\,m_4^{(N)} = 2 + N^{-2}$ and $\mathbb E\,m_6^{(N)} = 5 + 10N^{-2}$. The coefficient of $N^{-2g}$ counts the pairings of genus $g$; <a class="secref" href="#app-genus1">Appendix B</a> gives the genus-one count in closed form.</p>"""},
                        ],
                    },
                ],
            },
            {
                "id": "density", "kind": "section", "number": "4", "title": "From moments to the density", "role": "derivation",
                "gist": T("The semicircle has moments $C_n$, a compactly supported density is determined by its moments, and the random density concentrates.", status="ai-approved"),
                "brief": T(r"""<p><span data-covers="density-p1">The substitution $x = 2\cos\theta$ shows that the semicircle's even moments are exactly the Catalan numbers (8).</span> <span data-covers="density-p2">A probability measure on a bounded interval is determined by its moments, so convergence of the moments gives weak convergence of the expected density (9).</span> <span data-covers="density-p3">The variance of each moment is $O(1/N^2)$, by Wick's theorem applied to two traces, so the law holds for a single matrix.</span> <span data-covers="density-p4">Equivalently, the resolvent satisfies $G = 1/(z-G)$ (10), whose solution has the semicircle as the discontinuity across its cut.</span></p>""", status="ai-approved"),
                "children": [
                    {"id": "density-p1", "kind": "paragraph", "role": "derivation",
                     "gist": T("The semicircle's moments are the Catalan numbers (8).", status="ai-approved"),
                     "body": r"""<p>The semicircle has exactly the Catalan moments. With $x = 2\cos\theta$,
\[\int_{-2}^{2} x^{2n}\rho_{\rm sc}(x)\,dx = \frac{2^{2n+1}}{\pi}\int_0^{\pi}\cos^{2n}\theta\,\sin^2\theta\,d\theta = \frac{1}{n+1}\binom{2n}{n},\tag{8}\label{eq-scmoments}\]
using $\int_0^\pi\cos^{2m}\theta\,d\theta = \pi\binom{2m}{m}/4^m$ for $m = n$ and $m = n+1$; the odd moments vanish by symmetry.</p>"""},
                    {"id": "density-p2", "kind": "paragraph", "role": "derivation",
                     "gist": T("Moments determine a compactly supported measure, so the expected density converges (9).", status="ai-approved"),
                     "body": r"""<p>A probability measure supported in a bounded interval is determined by its moments: two such measures with the same moments integrate every polynomial, hence (by Weierstrass approximation) every continuous function, to the same value. Convergence of all moments to those of such a measure implies weak convergence to it. Since the Catalan numbers are the moments of $\rho_{\rm sc}$, which is supported in $[-2,2]$,
\[\mathbb E\,\rho_N \longrightarrow \rho_{\rm sc}\qquad(N\to\infty)\tag{9}\label{eq-weak}\]
in the weak sense: $\mathbb E\int f\rho_N\to\int f\rho_{\rm sc}$ for every bounded continuous $f$.</p>"""},
                    {"id": "density-p3", "kind": "paragraph", "role": "result",
                     "gist": T("Concentration: the variance of each moment is $O(1/N^2)$, so one matrix suffices.", status="ai-approved"),
                     "body": r"""<p>The statement holds for a single matrix, not only on average. A second application of Wick's theorem shows $\operatorname{Var}\,m_k^{(N)} = O(N^{-2})$: the connected part of $\mathbb E[\operatorname{Tr}H^k\operatorname{Tr}H^l]$ is a gluing of two polygons into one connected surface, which costs two powers of $N$ relative to the disconnected part. By Chebyshev's inequality each moment of $\rho_N$ then converges in probability, and with it $\rho_N$ itself. Figure 1 shows one draw at $N = 1000$.</p>"""},
                    {"id": "density-p4", "kind": "remark", "title": "Remark", "role": "discussion",
                     "gist": T("The resolvent route: $G = 1/(z-G)$ (10), with the semicircle as the discontinuity across the cut.", status="ai-approved"),
                     "body": r"""<p>The same result follows from the <dfn data-def="resolvent">resolvent</dfn> $G(z) = \int\frac{\rho(x)\,dx}{z-x}$, whose expansion at large $z$ is the generating function of the moments: in the limit, $G(z) = \sum_n C_n z^{-2n-1}$, and the Catalan recursion <a class="eqref" href="#eq-catrec">(7)</a> becomes the quadratic equation
\[G(z) = \frac{1}{z - G(z)},\qquad\text{so}\qquad G(z) = \frac{z-\sqrt{z^2-4}}{2},\tag{10}\label{eq-resolvent}\]
with the branch that behaves as $1/z$ at infinity. The discontinuity across the cut $[-2,2]$ gives back the density, $\rho_{\rm sc}(x) = -\frac1\pi\operatorname{Im}G(x+i0)$. This is the route of the Schwinger–Dyson, or self-consistent, derivation; <a class="secref" href="#app-catalan">Appendix A</a> relates it to the generating function of the Catalan numbers.</p>"""},
                ],
            },
            {
                "id": "discussion", "kind": "section", "number": "5", "title": "Discussion", "role": "discussion",
                "gist": T("The semicircle is universal beyond Gaussian entries; the genus expansion is the matrix-model–surface dictionary; the semicircle says nothing about level repulsion.", status="ai-approved"),
                "brief": T(r"""<p><span data-covers="disc-p1">Only the second moment of the entries was used, so the semicircle holds for any Wigner matrix, and for the real symmetric ensemble with corrections in $1/N$.</span> <span data-covers="disc-p2">The sum over pairings by genus is the simplest form of the correspondence between matrix integrals and sums over surfaces, which JT gravity realises surface by surface.</span> <span data-covers="disc-p3">The semicircle describes the density on the scale of the whole spectrum and is silent about level repulsion at separations of order $1/N$.</span></p>""", status="ai-approved"),
                "children": [
                    {"id": "disc-p1", "kind": "paragraph", "role": "discussion",
                     "gist": T("Universality: any Wigner matrix gives the semicircle; the GOE has $1/N$ corrections.", status="ai-approved"),
                     "body": r"""<p>Nothing in the argument used the Gaussian distribution beyond its second moment, once one knows that higher cumulants are suppressed. For a <dfn data-def="wigner">Wigner matrix</dfn>, with independent entries, $\mathbb E|H_{ij}|^2 = 1/N$ and bounded higher moments, the same pairing terms give the leading contribution and the remaining terms are $O(1/N)$, so the semicircle law holds with the same proof <a class="cite" href="#ref-agz">[5]</a>. For the real symmetric (GOE) ensemble, the sum over pairings includes gluings that produce non-orientable surfaces, and the corrections come in powers of $1/N$ rather than $1/N^2$; the leading term is unchanged.</p>"""},
                    {"id": "disc-p2", "kind": "paragraph", "role": "discussion",
                     "gist": T("The genus expansion (6) is the matrix-model–surface dictionary realised by JT gravity.", status="ai-approved"),
                     "body": r"""<p>Equation <a class="eqref" href="#eq-genus">(6)</a> is the simplest instance of the correspondence between matrix integrals and sums over surfaces <a class="cite" href="#ref-planar">[4]</a>: the $1/N$ expansion of a matrix integral is a topological expansion, each power $N^{-2g}$ collecting the surfaces of genus $g$. In JT gravity the double-scaled matrix integral reproduces the gravitational path integral surface by surface <a class="cite" href="#ref-sss">[6]</a>; the leading density of states there is not a semicircle but $\rho_0(E)\propto\sinh(2\pi\sqrt E)$, the edge of a spectrum shaped by a different potential, and the mechanism of <a class="secref" href="#moments">Section 3</a> is unchanged.</p>"""},
                    {"id": "disc-p3", "kind": "paragraph", "role": "caveat",
                     "gist": T("What the semicircle does not say: nothing about correlations at scale $1/N$.", status="ai-approved"),
                     "body": r"""<p>The semicircle is a statement about the density on the scale of the whole spectrum. It says nothing about the correlations between neighbouring eigenvalues, at separations of order $1/N$, where random matrix theory makes its sharpest and most universal predictions: level repulsion, the sine kernel, the spectral form factor. Those require the joint distribution of the eigenvalues, <a class="eqref" href="#eq-cov">(2)</a> written in terms of the $\lambda_i$, and different tools, orthogonal polynomials or the resolvent at finite distance from the cut <a class="cite" href="#ref-mehta">[7]</a>.</p>"""},
                ],
            },
            {
                "id": "app-catalan", "kind": "appendix", "number": "A", "title": "Catalan numbers", "fold": True,
                "gist": T("Solving the Catalan recursion with a generating function, and its relation to the resolvent.", status="ai-approved"),
                "brief": T(r"""<p><span data-covers="appA-p1">The generating function of the recursion (7) satisfies $C = 1 + tC^2$, so $C(t) = \frac{1-\sqrt{1-4t}}{2t}$ (11).</span> <span data-covers="appA-p2">Expanding the square root gives $c_n = \frac{1}{n+1}\binom{2n}{n}$ (12), with radius of convergence $1/4$, which is why the spectrum ends at $x = 2$.</span> <span data-covers="appA-p3">With $t = 1/z^2$ the same function is the resolvent (10).</span></p>""", status="ai-approved"),
                "children": [
                    {"id": "appA-p1", "kind": "paragraph", "role": "derivation",
                     "body": r"""<p>Let $C(t) = \sum_{n\ge0}c_nt^n$ with $c_n$ as in <a class="eqref" href="#eq-catrec">(7)</a>. Multiplying the recursion by $t^n$ and summing over $n\ge1$ gives
\[C(t) = 1 + t\,C(t)^2,\qquad\text{so}\qquad C(t) = \frac{1-\sqrt{1-4t}}{2t},\tag{11}\label{eq-catgen}\]
the root that is regular at $t = 0$.</p>"""},
                    {"id": "appA-p2", "kind": "paragraph", "role": "derivation",
                     "body": r"""<p>Expanding the square root by the binomial series, $\sqrt{1-4t} = 1 - 2\sum_{n\ge1}\frac1n\binom{2n-2}{n-1}t^n$, and so
\[c_n = \frac{1}{n+1}\binom{2n}{n} = C_n.\tag{12}\label{eq-catalan}\]
The radius of convergence $1/4$ reflects the growth $C_n\sim 4^n/(\sqrt\pi\,n^{3/2})$, which is why the limiting spectrum ends at $x = 2$: the $2n$-th moment of a density supported in $[-R,R]$ grows like $R^{2n}$.</p>"""},
                    {"id": "appA-p3", "kind": "paragraph", "role": "discussion",
                     "body": r"""<p>Setting $t = 1/z^2$ and $G(z) = C(1/z^2)/z$ turns <a class="eqref" href="#eq-catgen">(11)</a> into <a class="eqref" href="#eq-resolvent">(10)</a>: the Catalan generating function and the semicircle resolvent are the same function.</p>"""},
                ],
            },
            {
                "id": "app-genus1", "kind": "appendix", "number": "B", "title": "The genus-one correction", "fold": True,
                "gist": T("The exact GUE moments as polynomials in $1/N^2$, and the count of genus-one gluings.", status="ai-approved"),
                "brief": T(r"""<p><span data-covers="appB-p1">For $k = 4$ the two non-crossing pairings leave three free indices and contribute $1$ each, the crossing one leaves a single index and contributes $N^{-2}$.</span> <span data-covers="appB-p2">In general the coefficient of $N^{-2g}$ counts the gluings of a $2n$-gon of genus $g$; Harer and Zagier's generating function (13) gives $\varepsilon_1(n) = (2n)!/(12\,n!\,(n-2)!)$.</span></p>""", status="ai-approved"),
                "children": [
                    {"id": "appB-p1", "kind": "paragraph", "role": "derivation",
                     "body": r"""<p>For $k = 4$ the three pairings of the factors $H_{i_1i_2}H_{i_2i_3}H_{i_3i_4}H_{i_4i_1}$ are $\{12\}\{34\}$, $\{14\}\{23\}$ and $\{13\}\{24\}$. The pair $\{12\}$ sets $i_1 = i_3$ and the pair $\{34\}$ sets the same, so the first pairing leaves $i_1, i_2, i_4$ free ($V = 3$) and contributes $N^3/N^3 = 1$; so does the second. The crossing pairing $\{13\}\{24\}$ sets $i_1 = i_4$, $i_2 = i_3$ and then $i_1 = i_2$, $i_3 = i_4$: one free index ($V = 1$) and a contribution $N/N^3 = N^{-2}$. Hence $\mathbb E\,m_4^{(N)} = 2 + N^{-2}$.</p>"""},
                    {"id": "appB-p2", "kind": "paragraph", "role": "result",
                     "body": r"""<p>In general $\mathbb E\,m_{2n}^{(N)} = \sum_{g\ge0}\varepsilon_g(n)\,N^{-2g}$, where $\varepsilon_g(n)$ is the number of ways to glue a $2n$-gon into a surface of genus $g$. Harer and Zagier <a class="cite" href="#ref-hz">[3]</a> found the generating function
\[\sum_{g\ge0}\varepsilon_g(n)\,N^{\,n+1-2g} = (2n-1)!!\sum_{k\ge0}2^k\binom{n}{k}\binom{N}{k+1},\tag{13}\label{eq-hz}\]
from which $\varepsilon_0(n) = C_n$ and $\varepsilon_1(n) = \dfrac{(2n)!}{12\,n!\,(n-2)!}$: one torus for $n = 2$, ten for $n = 3$, seventy for $n = 4$.</p>"""},
                ],
            },
            {
                "id": "refs", "kind": "references", "title": "References",
                "body": r"""<ol class="refs">
<li id="ref-wigner55">E. P. Wigner, “Characteristic vectors of bordered matrices with infinite dimensions”, Ann. Math. <b>62</b> (1955) 548.</li>
<li id="ref-wigner58">E. P. Wigner, “On the distribution of the roots of certain symmetric matrices”, Ann. Math. <b>67</b> (1958) 325.</li>
<li id="ref-hz">J. Harer and D. Zagier, “The Euler characteristic of the moduli space of curves”, Invent. Math. <b>85</b> (1986) 457.</li>
<li id="ref-planar">G. ’t Hooft, “A planar diagram theory for strong interactions”, Nucl. Phys. B <b>72</b> (1974) 461; E. Brézin, C. Itzykson, G. Parisi and J.-B. Zuber, “Planar diagrams”, Commun. Math. Phys. <b>59</b> (1978) 35.</li>
<li id="ref-agz">G. W. Anderson, A. Guionnet and O. Zeitouni, <i>An Introduction to Random Matrices</i>, Cambridge University Press (2010).</li>
<li id="ref-sss">P. Saad, S. H. Shenker and D. Stanford, “JT gravity as a matrix integral”, arXiv:1903.11115.</li>
<li id="ref-mehta">M. L. Mehta, <i>Random Matrices</i>, 3rd ed., Elsevier (2004).</li>
</ol>""",
            },
        ],
    },
    # ---- the definitions layer: terms and symbols, each with the sentence that defines it
    "defs": [
        {"id": "gue", "term": "Gaussian unitary ensemble (GUE)", "aliases": ["GUE"],
         "html": r"The distribution on $N\times N$ Hermitian matrices with density $\propto\exp(-\frac N2\operatorname{Tr}H^2)$; equivalently, centred Gaussian entries with $\mathbb E\,H_{ij}H_{kl} = \delta_{il}\delta_{jk}/N$, so that every entry has variance $1/N$.",
         "at": {"node": "setup-p1", "quote": "Gaussian unitary ensemble"}},
        {"id": "semicircle", "term": "semicircle density", "symbol": r"$\rho_{\rm sc}$",
         "html": r"$\rho_{\rm sc}(x) = \frac{1}{2\pi}\sqrt{4-x^2}$ for $|x|\le2$ and $0$ outside: a probability density with variance $1$ whose even moments are the Catalan numbers.",
         "at": {"node": "intro-p2", "quote": "converges, as"}},
        {"id": "esd", "term": "empirical spectral density", "symbol": r"$\rho_N$",
         "html": r"$\rho_N(x) = \frac1N\sum_{i=1}^N\delta(x-\lambda_i)$, the normalised sum of delta functions at the eigenvalues of $H$: a random probability measure.",
         "at": {"node": "setup-p2", "quote": "empirical spectral density"}},
        {"id": "moment", "term": "moment of the spectrum", "symbol": r"$m_k^{(N)}$",
         "html": r"$m_k^{(N)} = \int x^k\rho_N(x)\,dx = \frac1N\operatorname{Tr}H^k$. With $\mathbb E|H_{ij}|^2 = 1/N$ the second moment has expectation $1$ for every $N$.",
         "at": {"node": "setup-p2", "quote": "moments"}},
        {"id": "wick", "term": "Wick's theorem",
         "html": r"For centred jointly Gaussian $X_1,\dots,X_k$: $\mathbb E[X_1\cdots X_k] = \sum_\pi\prod_{\{a,b\}\in\pi}\mathbb E[X_aX_b]$, a sum over all pairings of the factors; zero for odd $k$.",
         "at": {"node": "wick-p1", "quote": "Wick's theorem"}},
        {"id": "pairing", "term": "pairing",
         "html": r"A partition of $\{1,\dots,k\}$ into $k/2$ blocks of two elements. There are $(k-1)!!$ of them.",
         "at": {"node": "wick-p1", "quote": "pairings"}},
        {"id": "genus", "term": "genus of a pairing", "symbol": "$g(\\pi)$",
         "html": r"The genus of the closed surface obtained by gluing the edges of the $k$-gon of factors in the pairs of $\pi$. By Euler's formula the number of free indices is $V = k/2 + 1 - 2g$, so the pairing contributes $N^{-2g}$ to $\mathbb E\,m_k^{(N)}$.",
         "at": {"node": "genus-p2", "quote": "genus"}},
        {"id": "noncrossing", "term": "non-crossing (planar) pairing",
         "html": r"A pairing whose chords, drawn inside a polygon with the $k$ points on its boundary, do not intersect. These are exactly the pairings of genus $0$, and there are $C_{k/2}$ of them.",
         "at": {"node": "genus-p3", "quote": "non-crossing"}},
        {"id": "catalan", "term": "Catalan number", "symbol": "$C_n$",
         "html": r"$C_n = \frac{1}{n+1}\binom{2n}{n} = 1, 1, 2, 5, 14, 42, \dots$; the number of non-crossing pairings of $2n$ points, and the solution of $c_n = \sum_{j=1}^n c_{j-1}c_{n-j}$ with $c_0 = 1$.",
         "at": {"node": "thm-moments", "quote": "Catalan number"}},
        {"id": "resolvent", "term": "resolvent (Stieltjes transform)", "symbol": "$G(z)$",
         "html": r"$G(z) = \int\frac{\rho(x)\,dx}{z-x}$ for $z$ off the support of $\rho$; at large $z$ it is $\sum_k m_k z^{-k-1}$, and $\rho(x) = -\frac1\pi\operatorname{Im}G(x+i0)$ recovers the density.",
         "at": {"node": "density-p4", "quote": "resolvent"}},
        {"id": "hermitian", "term": "Hermitian matrix", "audience": ["student"],
         "html": r"A square matrix equal to its own conjugate transpose, $H_{ji} = \overline{H_{ij}}$. Its eigenvalues are real and its eigenvectors can be chosen orthonormal; a quantum Hamiltonian is Hermitian so that its energies are real.",
         "at": {"node": "bg-spectrum", "quote": "Hermitian matrix"}},
        {"id": "wigner", "term": "Wigner matrix",
         "html": r"A Hermitian matrix with independent entries (up to Hermiticity), $\mathbb E\,H_{ij} = 0$, $\mathbb E|H_{ij}|^2 = 1/N$ and bounded higher moments; the GUE is the Gaussian case.",
         "at": {"node": "disc-p1", "quote": "Wigner matrix"}},
    ],
    # ---- the questions layer: anticipated (and collected) questions, anchored to a part of the paper
    "questions": [
        {"id": "q-universal", "at": {"node": "intro"}, "source": "author", "status": "approved",
         "q": "Is the semicircle special to Gaussian matrices?",
         "a": r"No. The argument only uses the second moment of the entries and the suppression of higher cumulants, so any Wigner matrix (independent entries of variance $1/N$ with bounded higher moments) has the same limiting density. The Gaussian case is where Wick's theorem makes the count exact at every $N$.",
         "answeredBy": ["disc-p1"]},
        {"id": "q-scaling", "at": {"node": "setup"}, "source": "ai", "status": "approved",
         "q": "Why the factor $1/N$ in the variance of the entries?",
         "a": r"It is the only scaling for which the spectrum stays of order one as $N\to\infty$: with it $\mathbb E\,m_2^{(N)} = \frac1N\sum_{ij}\mathbb E|H_{ij}|^2 = 1$ for every $N$. With entries of variance $1$ the eigenvalues would spread over $[-2\sqrt N, 2\sqrt N]$, and (1) would describe $\lambda/\sqrt N$, as in Figure 1.",
         "answeredBy": ["setup-p2"]},
        {"id": "q-real", "at": {"node": "setup"}, "source": "ai", "status": "approved", "audience": "student",
         "q": "Why are the eigenvalues real?",
         "a": r"Because $H$ is Hermitian: if $Hv = \lambda v$ with $v\ne0$, then $\lambda\langle v,v\rangle = \langle v,Hv\rangle = \langle Hv,v\rangle = \bar\lambda\langle v,v\rangle$, so $\lambda = \bar\lambda$. This is also why a Hamiltonian is taken Hermitian: its eigenvalues are energies.",
         "answeredBy": ["bg-spectrum"]},
        {"id": "q-indep", "at": {"node": "wick"}, "source": "ai", "status": "draft",
         "q": "Does Wick's theorem need the entries to be independent?",
         "a": r"No, only that they are jointly Gaussian and centred. The constraint $H_{ji} = \overline{H_{ij}}$ makes the entries dependent, and (2) records exactly that dependence: the covariance $\mathbb E\,H_{ij}H_{kl}$ is non-zero only for $(k,l) = (j,i)$.",
         "answeredBy": ["wick-p1", "setup-p1"]},
        {"id": "q-handle", "at": {"node": "genus"}, "source": "author", "status": "approved",
         "q": "Why does a crossing force a handle?",
         "a": r"Glue a square along the crossing pairing $\{13\}\{24\}$: opposite edges are identified with opposite orientations, which is the word $aba^{-1}b^{-1}$, a torus. In general, if two chords cross, the two gluings they prescribe cannot both be made within a disc, and the identified polygon acquires a handle; the non-crossing case is a sphere by induction on the number of chords (remove an innermost chord, which bounds a disc).",
         "answeredBy": ["genus-p3", "appB-p1"]},
        {"id": "q-ribbon", "at": {"node": "genus"}, "source": "ai", "status": "approved",
         "q": "Is the genus of a pairing the same as the genus of the corresponding Feynman diagram?",
         "a": r"Yes. The usual picture has one vertex (the trace $\operatorname{Tr}H^k$) with $k$ legs and $k/2$ double-line propagators; its faces are the closed index loops. The glued polygon is the dual picture: its vertices are the index loops, its single face is the trace vertex. Both give the same surface and the same Euler characteristic $2-2g$.",
         "answeredBy": ["genus-p1", "genus-p2"]},
        {"id": "q-catalan-not-df", "at": {"node": "catalan"}, "source": "ai", "status": "approved",
         "q": "Why does one get the Catalan numbers rather than $(2n-1)!!$, the number of all pairings?",
         "a": r"$(2n-1)!!$ counts every pairing, and every pairing does contribute to $\mathbb E\,m_{2n}^{(N)}$, but with the weight $N^{-2g}$ of (6). Only the pairings of genus zero, the non-crossing ones, survive as $N\to\infty$, and those are counted by the recursion (7), which is the Catalan recursion. The full count $(2n-1)!!$ is recovered by setting $N = 1$ in (13).",
         "answeredBy": ["proof-moments", "appB-p2"]},
        {"id": "q-determinate", "at": {"node": "density"}, "source": "reader", "status": "approved",
         "q": "Why do the moments determine the density? Is that always true?",
         "a": r"Not always: a measure with heavy tails can share all its moments with a different measure (the log-normal distribution is the classic example). It is true when the support is bounded, because polynomials are then dense in the continuous functions on the support (Weierstrass), and more generally under Carleman's condition on the growth of the moments. The Catalan numbers grow like $4^n$, so the limit measure lives in $[-2,2]$ and the bounded case applies.",
         "answeredBy": ["density-p2"]},
        {"id": "q-single", "at": {"node": "density"}, "source": "ai", "status": "approved",
         "q": "Does a single matrix show the semicircle, or only the average over the ensemble?",
         "a": r"A single matrix does, with high probability at large $N$: the variance of each moment is $O(1/N^2)$, because the connected correlator of two traces is one connected surface made of two polygons, which costs two powers of $N$. Chebyshev's inequality then gives convergence in probability of each moment, hence of $\rho_N$.",
         "answeredBy": ["density-p3"]},
        {"id": "q-jt", "at": {"node": "discussion"}, "source": "author", "status": "approved",
         "q": "Where is the semicircle in JT gravity?",
         "a": r"Nowhere as such: the leading density of states of JT gravity, $\rho_0(E)\propto\sinh(2\pi\sqrt E)$, is the edge of a spectrum shaped by a non-Gaussian potential, taken in a double-scaling limit that zooms on the edge. What carries over is the structure of the computation: the $1/N$ expansion as a sum over surfaces by genus, which in JT gravity becomes the sum over the topologies of the gravitational path integral.",
         "answeredBy": ["disc-p2"]},
        {"id": "q-thooft", "at": {"node": "discussion"}, "source": "ai", "status": "approved", "audience": "physicist",
         "q": "How does this relate to ’t Hooft's large-$N$ expansion of gauge theories?",
         "a": r"It is the same bookkeeping. In a $U(N)$ gauge theory the fields are matrices, propagators are double lines carrying two indices, and every closed index loop gives a factor of $N$; a Feynman diagram of genus $g$ then scales as $N^{2-2g}$ times powers of the ’t Hooft coupling. Here there is no spacetime, a single Gaussian matrix and a single vertex (the trace), so the diagrams are just the gluings of one polygon, but the power $N^{-2g}$ has the same origin.",
         "answeredBy": ["genus-p2", "disc-p2"]},
        {"id": "q-eps1", "at": {"node": "app-genus1"}, "source": "ai", "status": "approved",
         "q": "Where does the formula for $\\varepsilon_1(n)$ come from?",
         "a": r"From expanding the right-hand side of (13) in powers of $N$ and reading off the coefficient of $N^{n-1}$. For $n = 2$: $3\,[N + 4\binom N2 + 4\binom N3] = 2N^3 + N$, so $\varepsilon_0(2) = 2$ and $\varepsilon_1(2) = 1$; for $n = 3$: $15\,[N + 6\binom N2 + 12\binom N3 + 8\binom N4] = 5N^4 + 10N^2$, so $\varepsilon_1(3) = 10$. The closed form $(2n)!/(12\,n!\,(n-2)!)$ reproduces $1, 10, 70, \dots$",
         "answeredBy": ["appB-p2"]},
    ],
}
