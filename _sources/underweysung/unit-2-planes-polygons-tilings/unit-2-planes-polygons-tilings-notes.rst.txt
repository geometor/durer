==========================================================================
Notes — Book II: Algebraic Audit of Dürer's Pentagon, Heptagon & $\pi$
==========================================================================

1. Exact Radical Audit of Dürer's Rusty-Compass Pentagon (Fig. 16)
==================================================================

Why did :person:`Dürer <durer>` present *two* pentagon constructions back-to-back on pages 058–059
(Figs. 15 and 16)? While Figure 15 gives :person:`Ptolemy's <ptolemy>` exact golden-ratio chord
over $\mathbb{Q}(\phi)$, Figure 16 requires **never changing the compass opening** (*auß
vnuerruckten zirckel*)—a classic medieval stonemasons' and Islamic workshop protocol going back to
:person:`Abū al-Wafāʾ <abu-l-wafa>` (:cite:`abulwafa:craftsmen`) and :person:`Matthäus Roriczer
<roritzer>` (:cite:`roritzer:1487`), which :person:`Hermann Staigmüller <durer>` (:cite:`staigmuller:1891`)
and :person:`Émile Lemoine <lemoine>` (:cite:`lemoine:1902`) celebrated as a milestone of
constructive simplicity.

In :func:`~geometor.durer.polygons.construct_durer_vs_euclid_pentagon`, let the given base be
$A = (0, 0)$ and $B = (1, 0)$ with fixed unit aperture $R = 1$:

- The vesica intersections are $C = \left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$ and
  $D = \left(\frac{1}{2}, -\frac{\sqrt{3}}{2}\right)$.
- The third unit circle centered at $D$ meets $\bigcirc(A, 1)$ at
  $E = \left(\frac{1}{2} - \frac{\sqrt{3}}{2},\, -\frac{\sqrt{3}}{2} + \frac{1}{2}\right)$ and
  meets the vertical axis $CD$ at $G = \left(\frac{1}{2},\, 1 - \frac{\sqrt{3}}{2}\right)$.
- Ray $EG$ has slope $m = \frac{1}{\sqrt{3}}(2 - \sqrt{3})$? Let us read off $\Delta x =
  \frac{\sqrt{3}}{2}$ and $\Delta y = \frac{1}{2}$, so ray $EG$ makes an exact **$30^\circ$ angle**
  with the horizontal! Intersecting ray $EG$ with $\bigcirc(B, 1)$ yields the closed-form nested
  quadratic coordinates of vertex $H_{\text{Dürer}}$:

$$H_{\text{Dürer}} = \left(\frac{5}{8} + \frac{\sqrt{3}\,\sqrt{6\sqrt{3} - 4}}{8},\;
-\frac{\sqrt{3}}{2} + \frac{7}{8} + \frac{\sqrt{6\sqrt{3} - 4}}{8}\right),$$

and by bilateral reflection $I_{\text{Dürer}} = (1 - x_H, y_H)$. Stepping unit circles from
$I_{\text{Dürer}}$ and $H_{\text{Dürer}}$ closes at apex $K_{\text{Dürer}} = \left(\frac{1}{2},
y_K\right)$.

Symbolic verification in ``geometor.durer`` proves:

1. **100% Exact Equilateral Side Quadrances**: Every edge $AB, BH_{\text{Dürer}}, H_{\text{Dürer}}K_{\text{Dürer}},
   K_{\text{Dürer}}I_{\text{Dürer}}, I_{\text{Dürer}}A$ has exact quadrance $Q = 1$.
2. **Non-Equiangularity (+21.97 Arcminutes)**: Whereas Euclid's $\mathbb{Q}(\phi)$ pentagon has all
   five interior angles equal to $108^\circ$ (interior line spread $s = \frac{5 + \sqrt{5}}{8}$),
   Dürer's pentagon has interior angles:

   - At base vertices $A, B$: **$108.36612^\circ$** ($+0.36612^\circ = +21.97'$ too wide),
   - At shoulder vertices $I_{\text{Dürer}}, H_{\text{Dürer}}$: **$107.03899^\circ$** ($-57.66'$),
   - At apex $K_{\text{Dürer}}$: **$109.18978^\circ$** ($+1^\circ 11.39'$).

Within twenty-five years of Dürer's book, :person:`Lodovico Ferrari <ferrari>` and
:person:`Gerolamo Cardano <cardano>` proved that **even the exact $\mathbb{Q}(\phi)$ pentagon can
be constructed with straightedge and a single fixed compass opening**, albeit requiring many more
circles than Dürer's ultra-fast five-circle workshop layout.

2. Eisenstein Irreducibility & Residual of the Workshop Heptagon (Figs. 11 & 15)
================================================================================

For a regular heptagon inscribed in the unit circle $R = 1$, setting $\theta = \frac{2\pi}{7}$ gives
chord quadrance $q = 4\sin^2\frac{\pi}{7} = 2 - 2\cos\frac{2\pi}{7}$. Since $2\cos\theta$ satisfies
$t^3 + t^2 - 2t - 1 = 0$, substituting $t = 2 - q$ yields the minimal polynomial of the regular
heptagon's side quadrance (:func:`~geometor.durer.polygons.construct_durer_heptagon_workshop`):

$$P_7(q) = q^3 - 7q^2 + 14q - 7 = 0.$$

By **Eisenstein's criterion** at the prime $p = 7$ ($7 \mid -7, 14, -7$ and $7^2 \nmid -7$),
$P_7(q)$ is **irreducible over $\mathbb{Q}$** of degree $3 \neq 2^k$. By the **Gauss–Wantzel
theorem** (:person:`Gauss <gauss>` :cite:`gauss:1801`; :person:`Wantzel <wantzel>`
:cite:`wantzel:1837`), no unmarked ruler-and-compass construction can ever construct $q_{\text{exact}}
\approx 0.753020396$, vindicating Dürer's explicit *Mechanice* label! Evaluating $P_7$ at Dürer's
half-equilateral quadrance $Q_{\text{Dürer}} = \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{3}{4}$
gives the extraordinarily tiny exact rational residual:

$$P_7\!\left(\frac{3}{4}\right) = \frac{27}{64} - \frac{63}{16} + \frac{21}{2} - 7 = -\frac{1}{64},$$

corresponding to a relative chord error of **$-0.2008\%$** (less than $0.2\text{ mm}$ on a
$100\text{ mm}$ radius circle!). Similarly, Dürer's hendecagon rule $s_{11} = \frac{9}{16}R =
0.5625\,R$ misses $2\sin\frac{\pi}{11} \approx 0.563465\,R$ by just **$-0.1713\%$**.

Philological Note on the 1525 Errata (SLUB N1525 p. 182)
---------------------------------------------------------
In the 1525 first printing of p. 058 (Fig. 15), the typesetter omitted the clause bisecting ``a.c.``
at ``e`` before drawing segment ``e.d.``, and the woodblock cutter omitted line ``d.e.`` inside the
first circle. Dürer caught this himself on the final Errata leaf (p. 182): *"Im .E. am vierten plat
in der fünftzeheten figur im ersten cirkel soll .d.e. mit einer lini zusamen gezogen werden."*

3. Dürer's Circle Quadrature & $\pi_{\text{Dürer}} = \frac{25}{8}$ (Fig. 34)
============================================================================

For a square of side $a$ and area $a^2$, the diagonal (*ortstrich*) has length $a\sqrt{2}$. Taking
$d = \frac{8}{10}\,a\sqrt{2} = \frac{4\sqrt{2}}{5}a$ gives radius $r = \frac{2\sqrt{2}}{5}a =
\sqrt{\frac{8}{25}}\,a$. Equating $\pi_{\text{Dürer}}\,r^2 = a^2$ yields

$$\pi_{\text{Dürer}} = \frac{25}{8} = 3.125,$$

the classical Roman-Vitruvian value ($3\frac{1}{8}$, relative error $-0.528\%$), which Dürer
rightly refuses to pass off as *demonstrative*—anticipating Lindemann's 1882 proof of the
transcendence of $\pi$ (:cite:`klein:1895`).
