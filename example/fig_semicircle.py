#!/usr/bin/env python3
"""Figure 1 of the sample paper: one draw of the GUE spectrum at N = 1000 against the semicircle.

Pure Python (no numpy): the GUE eigenvalues are sampled through the Dumitriu-Edelman tridiagonal model
(same joint eigenvalue distribution as the GUE with density exp(-Tr H^2 / 2)), and the histogram counts
come from Sturm sequences, which count the eigenvalues of a symmetric tridiagonal matrix below a given value.
Eigenvalues are scaled by 1/sqrt(N), so the semicircle sits on [-2, 2].

    python3 fig_semicircle.py > figures/semicircle.svg
"""
import math
import random

random.seed(2026)
N = 1000
# tridiagonal model, beta = 2: diagonal ~ N(0,1); off-diagonal b_k = chi_{2(N-k)} / sqrt 2, k = 1..N-1
a = [random.gauss(0, 1) for _ in range(N)]
b = [math.sqrt(2 * random.gammavariate(N - k, 1)) / math.sqrt(2) for k in range(1, N)]


def count_below(lam):
    """Number of eigenvalues below lam (Sturm sequence of the tridiagonal matrix)."""
    cnt = 0
    q = a[0] - lam
    if q < 0:
        cnt += 1
    for i in range(1, N):
        if q == 0:
            q = 1e-300
        q = a[i] - lam - b[i - 1] ** 2 / q
        if q < 0:
            cnt += 1
    return cnt


# histogram of lambda / sqrt(N) in bins of width 0.1 on [-2.4, 2.4]
edges = [round(-2.4 + 0.1 * i, 2) for i in range(49)]
counts = [count_below(e * math.sqrt(N)) for e in edges]
dens = [(counts[i + 1] - counts[i]) / (N * 0.1) for i in range(len(edges) - 1)]

# drawing
W, H = 640, 330
L, R, T, B = 54, 18, 16, 46          # margins
pw, ph = W - L - R, H - T - B
x0, x1 = -2.5, 2.5
ymax = 0.40


def X(x):
    return L + (x - x0) / (x1 - x0) * pw


def Y(y):
    return T + ph - y / ymax * ph


out = []
out.append(f'<svg class="fig fig-semicircle" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="Histogram of the eigenvalues of one 1000 by 1000 GUE matrix, with the semicircle density drawn over it">')
out.append('<g font-family="var(--sans)" font-size="13" fill="currentColor">')
# axes
out.append(f'<line x1="{L}" y1="{Y(0)}" x2="{L + pw}" y2="{Y(0)}" stroke="currentColor" stroke-opacity=".5" stroke-width="1"/>')
out.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{Y(0)}" stroke="currentColor" stroke-opacity=".5" stroke-width="1"/>')
for xt in (-2, -1, 0, 1, 2):
    out.append(f'<line x1="{X(xt):.1f}" y1="{Y(0)}" x2="{X(xt):.1f}" y2="{Y(0) + 5}" stroke="currentColor" stroke-opacity=".5"/>')
    out.append(f'<text x="{X(xt):.1f}" y="{Y(0) + 20}" text-anchor="middle">{xt}</text>')
for yt in (0.1, 0.2, 0.3):
    out.append(f'<line x1="{L - 5}" y1="{Y(yt):.1f}" x2="{L}" y2="{Y(yt):.1f}" stroke="currentColor" stroke-opacity=".5"/>')
    out.append(f'<text x="{L - 9}" y="{Y(yt) + 4.5:.1f}" text-anchor="end">{yt}</text>')
out.append(f'<text x="{L + pw}" y="{Y(0) + 38}" text-anchor="end" font-style="italic">x = λ / √N</text>')
out.append(f'<text x="{L + 8}" y="{T + 12}" font-style="italic">ρ(x)</text>')
# histogram
out.append('<g fill="var(--accent)" fill-opacity=".22" stroke="var(--accent)" stroke-opacity=".55" stroke-width="1">')
for i, d in enumerate(dens):
    xa, xb = edges[i], edges[i + 1]
    if d > 0:
        out.append(f'<rect x="{X(xa):.1f}" y="{Y(d):.1f}" width="{X(xb) - X(xa):.1f}" height="{Y(0) - Y(d):.1f}"/>')
out.append('</g>')
# semicircle
pts = []
steps = 160
for i in range(steps + 1):
    x = -2 + 4 * i / steps
    pts.append(f'{X(x):.1f},{Y(math.sqrt(max(0.0, 4 - x * x)) / (2 * math.pi)):.1f}')
out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linejoin="round"/>')
# legend
lx, ly = L + pw - 190, T + 14
out.append(f'<line x1="{lx}" y1="{ly}" x2="{lx + 26}" y2="{ly}" stroke="var(--accent)" stroke-width="2.6"/>')
out.append(f'<text x="{lx + 34}" y="{ly + 4.5}">semicircle (1)</text>')
out.append(f'<rect x="{lx}" y="{ly + 14}" width="26" height="12" fill="var(--accent)" fill-opacity=".22" stroke="var(--accent)" stroke-opacity=".55"/>')
out.append(f'<text x="{lx + 34}" y="{ly + 24.5}">one GUE draw, N = 1000</text>')
out.append('</g></svg>')
print("\n".join(out))
