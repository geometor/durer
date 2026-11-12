======================================================
Cross-Corpus Concordance (*Underweysung* ↔ GEOMETOR)
======================================================

The table below links the thirteen canonical mathematical loci across Books I–IV of Albrecht
Dürer's *Underweysung der Messung* (1525) to their algebraic fields in ``geometor.durer`` and
sister editions across the GEOMETOR Digital Scriptorium.

.. list-table::
   :header-rows: 1
   :widths: 11 16 22 18 16 17

   * - ID
     - 1525 Locus
     - Vernacular / 1532 Latin
     - Topic & Epistemic Mode
     - Algebraic Field
     - Sister Repos
   * - ``UDM-I-01``
     - Book I, pp. 007–009, Figs. 1–4
     - *Punct, Schlangenlini, Barlini* / *Linea serpentina, Parallela*
     - Elementary Lines & Parallels (*axiomatic*)
     - $\mathbb{Q}$
     - ``euclid``, ``elements``, ``hilbert``, ``proclus``
   * - ``UDM-I-02``
     - Book I, pp. 011–024, Figs. 7–24
     - *Schneckenlini, Schrauffenlini* / *Cochlis, Helix*
     - 12-Sector Spirals, Ionic Volutes & Spatial Helices (*kinematic*)
     - $\mathbb{Q}(\sqrt{3})$ at $30^\circ$ stations
     - ``thompson``, ``phyllotaxis``, ``divine``
   * - ``UDM-I-03``
     - Book I, pp. 031–033, Figs. 31–33
     - *Muschellini* / *Linea conchois*
     - Conchoid of Nicomedes & Slotted Trammel (*neusis*)
     - Quartic locus $r = b + a\sec\theta$
     - ``pappus``, ``klein``
   * - ``UDM-I-04``
     - Book I, pp. 034–039, Figs. 34–37
     - *Eierlini, Brennspiegellini, Gabellini* / *Ellipsis, Parabola, Hyperbola*
     - Two-View Descriptive Geometry of Conics (*demonstrative*)
     - $\mathbb{Q}(\sqrt{2}, \sqrt{5}, \sqrt{13})$
     - ``pappus``, ``model``
   * - ``UDM-II-01``
     - Book II, pp. 054–056, Figs. 3–8, 22–28
     - *Ebne Pflasterung* / *Planorum coaptatio*
     - Regular, Star & Pentagonal Parquetries (*combinatorial*)
     - $\mathbb{Q}, \mathbb{Q}(\sqrt{2}), \mathbb{Q}(\sqrt{3}), \mathbb{Q}(\phi)$
     - ``divine``, ``pacioli``
   * - ``UDM-II-02``
     - Book II, pp. 058–059, Figs. 15–16
     - *Fünffeck demonstrative vs. unverruckt* / *Pentagonum*
     - Euclid $\mathbb{Q}(\phi)$ Pentagon vs. Rusty-Compass Pentagon
     - $\mathbb{Q}(\phi)$ vs. $\mathbb{Q}(\sqrt{3}, \sqrt{6\sqrt{3}-4})$
     - ``euclid``, ``elements``, ``pacioli``, ``lemoine``, ``divine``
   * - ``UDM-II-03``
     - Book II, pp. 057–061, Figs. 11, 15, 18, 19
     - *Sibeneck, Neuneck, Eylffeck, Dreytzeheneck*
     - Workshop 7-, 9-, 11-, 13-gons (*mechanice*)
     - $\mathbb{Q}(\sqrt{3})$ vs. Eisenstein $P_7(q)$
     - ``klein``, ``lemoine``, ``elements``
   * - ``UDM-II-04``
     - Book II, pp. 069–075, Figs. 29–36
     - *Vergleichung der Ebnen & Quadratura Circuli*
     - Area Transformations & $\frac{8}{10}$-Diagonal Circle Quadrature
     - $\mathbb{Q}(\sqrt{2})$ vs. $\pi_{\text{Dürer}} = \frac{25}{8}$
     - ``euclid``, ``elements``, ``klein``
   * - ``UDM-III-01``
     - Book III, pp. 077–114, Figs. 1–27
     - *Seulen, Horalogia & Thurnschrift*
     - Columns, Nuremberg $49^\circ$ Sundials & Optical Scaling
     - Projective & Gnomonic Pencils
     - ``pappus``, ``thompson``
   * - ``UDM-III-02``
     - Book III, pp. 115–141
     - *Lateinisch ABC & Textur*
     - Roman *Antiqua* ($10 \times 10$ Square) & Modular *Textura*
     - $\mathbb{Q}(\sqrt{2}, \sqrt{449})$
     - ``pacioli``, ``thompson``
   * - ``UDM-IV-01``
     - Book IV, pp. 142–158, Figs. 29–43
     - *Aufgeschnittene Corpora*
     - First Printed Planar Nets (5 Platonic + 7 Archimedean)
     - $\mathbb{Q}, \mathbb{Q}(\sqrt{3}), \mathbb{Q}(\sqrt{5}, \sin 36^\circ)$
     - ``pacioli``, ``euclid``, ``elements``, ``plato``, ``divine``
   * - ``UDM-IV-02``
     - Book IV, pp. 159–164, Figs. 44–51
     - *Duplicatio Cubi & Büchsenkugeln*
     - Delian Cube Doubling (Sporus, Plato, Hero) & Ballistics
     - $\mathbb{Q}(\sqrt[3]{2})$
     - ``plato``, ``pappus``, ``klein``, ``euclid``
   * - ``UDM-IV-03``
     - Book IV, pp. 165–181, Figs. 52–63
     - *Perspectiva (Durchsehung)*
     - Cube Sciagraphy & Homogeneous Glass-Frame Projection
     - $\mathbb{P}^3(\mathbb{Q}) \to \mathbb{P}^2(\mathbb{Q})$, $\operatorname{CR} = -1$
     - ``pappus``, ``model``
