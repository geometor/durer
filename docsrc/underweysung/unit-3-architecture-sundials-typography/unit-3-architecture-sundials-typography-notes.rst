==========================================================================
Notes — Book III: Algebraic Typography, Pacioli vs. Dürer & Gnomonics
==========================================================================

1. Dürer vs. Luca Pacioli on the Roman Alphabet (1509 vs. 1525)
===============================================================

In *Divina Proportione* (:cite:`pacioli:1509`), :person:`Luca Pacioli <pacioli>` framed Roman
capitals inside a square with a **$1 : 9$** stroke-to-height ratio and constructed round letters
such as **O** using **four distinct circles** (two concentric outer/inner circles or paired ovals).
In Book III of the *Underweysung* (pp. 115–135), :person:`Dürer <durer>` makes three decisive
innovations:

1. **Dual Proportional Canons ($1 : 10$ and $1 : 9$)**: He establishes the primary $10 \times 10$
   square ($w = 1$, thin stroke $t = \frac{1}{3}$) for bold legibility, followed explicitly on
   p. 130 by the slenderer $9 \times 9$ canon (and $1 : 5$ for small handwritten capitals).
2. **Calligraphic Broad-Nib Axis via Shifted Congruent Circles**: In **O** and **Q**
   (:func:`~geometor.durer.typography.construct_durer_roman_letter_O`,
   :func:`~geometor.durer.typography.construct_durer_roman_letter_Q`), shifting a single compass
   radius along the $45^\circ$ diagonal $cb$ ($y = x$) from center $f$ to center $g$ with
   $|fg| = 1$:

   $$f = \left(5 - \frac{\sqrt{2}}{4},\; 5 - \frac{\sqrt{2}}{4}\right), \qquad
   g = \left(5 + \frac{\sqrt{2}}{4},\; 5 + \frac{\sqrt{2}}{4}\right), \qquad
   r = 5 - \frac{\sqrt{2}}{4},$$

   makes $\bigcirc(f, r)$ tangent to the left and bottom edges ($x = 0, y = 0$) and $\bigcirc(g, r)$
   tangent to the right and top edges ($x = 10, y = 10$), while **automatically tilting the maximum
   bowl stress to $45^\circ$ just like a humanist broad-edged pen**! Their lens intersections lie
   at exact nested radical coordinates in $\mathbb{Q}(\sqrt{2}, \sqrt{80\sqrt{2} - 6})$:

   $$P_{1,2} = \left(5 \mp \frac{\sqrt{10\sqrt{2} - \frac{3}{4}}}{2},\;
   5 \pm \frac{\sqrt{10\sqrt{2} - \frac{3}{4}}}{2}\right).$$

3. **Exact Coordinates of Roman Capital A**: In :func:`~geometor.durer.typography.construct_durer_roman_letter_A`,
   placing foot points $i = (1, 0)$ and $k = (9, 0)$ with top midpoint $e = (5, 10)$ inside the leg
   junction yields exact rational coordinates for the triangular counter apex and tangent serif
   centers:

   $$V_{\text{counter}} = \left(\frac{14}{3},\; \frac{200}{21}\right), \qquad
   r_{\text{outer}} = \frac{10}{7}, \qquad r_{\text{inner}} = \frac{1}{2},$$

   with outer fillet circle centers lying over $\mathbb{Q}(\sqrt{449})$ so each arc is simultaneously
   tangent to the $y = 0$ baseline and the oblique leg!

2. Combinatorial Proof of Dürer's *Textura* Counter Inequality
==============================================================

On p. 136, Dürer constructs minuscule **i** (:func:`~geometor.durer.typography.construct_durer_textura_minuscules`)
from three unit squares of width $1$ capped by $45^\circ$-tilted unit squares (*Ort-Fierungen*) of
diagonal $\sqrt{2}$, and immediately remarks that when two stems touch corner-to-corner to form
**n**, *"das felt [wirt] schlemer zwischen den zügen dann ein zug des pustaben preyt ist"* ("the
interior white counter becomes narrower than a stroke is wide").

Why? Because each $45^\circ$-rotated unit square has horizontal span equal to its diagonal
$d = \sqrt{2}$! When two stems meet corner-to-corner at the diamond tips, the center-to-center
**stem pitch** is exactly $p = \sqrt{2}$, so subtracting one stem width ($w = 1$) leaves an exact
interior white counter width of

$$c_{\text{Textura}} = \sqrt{2} - 1 \approx 0.41421356 < 1,$$

giving black-to-white rhythm $1 : (\sqrt{2} - 1) = (\sqrt{2} + 1) : 1$ (the **silver ratio**
$\delta_S = 1 + \sqrt{2}$)! Five pages later (p. 138), Dürer contrasts this dense medieval picket
fence with the modernized *freye Textur* (developed in Nuremberg with :person:`Johann Neudörfer
<neudorfer>` and :person:`Hieronymus Andreae <andreae>`), which widens the counter to equal the full
stroke width $1$.

3. Projective Collineation in the Tower Inscription & Analemma
==============================================================

Both Dürer's Nuremberg gnomonic projection (Figs. 21–23, mapping uniform $15^\circ$ equatorial hour
angles onto tangent lines via $\tan(k \cdot 15^\circ)$ scaled by $\sin 49^\circ$ on the horizontal
plane and $\cos 49^\circ$ on a prime-vertical South wall) and his tower-inscription ray pencil
(p. 114, mapping uniform visual angles $\theta_k$ onto heights $h_k = D\tan\theta_k$) prepare the
reader directly for the central-projection perspective theory of Book IV, and inspired
:person:`D'Arcy Wentworth Thompson's <thompson>` coordinate transformation grids
(:cite:`thompson:1942`).
