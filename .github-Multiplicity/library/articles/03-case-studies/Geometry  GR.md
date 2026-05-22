---
slug: geometry-gr
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Geometry  GR.md
  last_synced: '2026-03-20T17:17:21.795870Z'
---

**A New Geometry for Einstein's Theory of Relativity**
======================================================

*A team of mathematicians based in Vienna is developing tools to extend
the scope of general relativity.*

8

![](media/image1.png){width="6.5in" height="3.6666666666666665in"}

Harol Bustos for *Quanta Magazine*

![](media/image8.jpg){width="6.5in" height="6.763888888888889in"}

By

Steve Nadis

*Contributing Writer*

*July 16, 2025*

**View PDF/Print Mode**

black holes

general relativity

geometry

gravity

mathematical physics

mathematics

partial differential equations

space-time

[All topics](https://www.quantamagazine.org/topics)

![Introducing Fundamentals, a new newsletter from Quanta
Magazine.](media/image7.gif){width="3.3333333333333335in"
height="5.736111111111111in"}

(opens a new tab)

In October 2015, a young mathematician named Clemens Sämann

(opens a new tab)

was flying home to Austria from a conference in Turin, Italy, when he
had a chance encounter. He found himself seated beside Michael Kunzinger

(opens a new tab)

, another conference attendee. Kunzinger was a math professor at the
University of Vienna, where Sämann had just started his postdoctoral
research. They soon got to talking, landing on a subject Sämann had
started thinking about in graduate school --- whether there was a
mathematical way to get around the limitations of Albert Einstein's
general theory of relativity.

Einstein's theory defines gravity as the curvature of space-time caused
by the presence of matter and energy. Since its formulation in 1915, it
has held up remarkably well. Consisting of 10 interconnected
differential equations, the theory describes how objects fall, how light
bends, and how planets, stars and galaxies move. It tells us that the
universe is expanding, and it predicted the existence of both black
holes and gravitational waves a century before they were definitively
observed.

But in spite of these successes, Einstein's theory also has
shortcomings. Its equations can only describe how matter curves
space-time when the geometry of that space-time is smooth --- with no
sharp corners or cusps, no regions where it suddenly becomes jagged.
Picture space-time as a flat rubber sheet, and matter as a bowling ball
placed on that sheet, causing it to bend. If space-time is smooth, then
this bending will be gradual.

But physicists know that's not always true. A black hole, for instance,
warps space-time more violently, causing the sheet to bend sharply
until, at the black hole's center (a so-called singularity), the
curvature "blows up," becoming infinite. Some physicists even posit that
space-time doesn't become non-smooth only at isolated singularities, but
at every point. On the smallest scales, space-time might be "discrete,"
or pixelated --- broken up into tiny, disconnected bits in the same way
that a fluid, while appearing to be a single uniform entity, is actually
made up of distinct atoms and molecules.

In these situations, general relativity hits an impasse. Whenever
space-time isn't sufficiently smooth, Einstein's equations stop working.
They can no longer tell us how matter curves space-time, or how curved
space-time influences matter.

That's because the equations rely on a technique from calculus [called
differentiation](https://www.quantamagazine.org/the-jagged-monstrous-function-that-broke-calculus-20250123/)
that measures how quickly functions change, and differentiation is no
longer possible in settings that are far from smooth. And so, on their
flight back to Austria, Kunzinger and Sämann wondered whether they could
devise alternative methods --- ones that would still work in the
inhospitable environments where the usual tools of calculus broke down.

Share this article

(opens a new tab)

Newsletter

*Get Quanta Magazine delivered to your inbox*

[**Subscribe
now**](https://www.quantamagazine.org/a-new-geometry-for-einsteins-theory-of-relativity-20250716/#newsletter)

Recent newsletters

(opens a new tab)

![Man in orange T-shirt standing outside in front of a red geometric
sculpture.](media/image1.png){width="6.5in"
height="4.388888888888889in"}

Clemens Sämann has helped prove important singularity theorems in
space-times that "could have corners, edges and folds."

Der Knopfdrücker

The pair wouldn't start working on the problem in earnest for another
year. But since then, they've made significant advances toward their
goal. They've found new ways to estimate curvature and other geometric
properties without relying on smoothness and differentiation. In
collaboration with other researchers, they've used their methods to
rederive (and sometimes strengthen) core theorems about the universe
without depending on Einstein's equations, putting those theorems on
even firmer mathematical footing.

And they're now part of an ambitious new program

(opens a new tab)

--- launched last year under the direction of Roland Steinbauer

(opens a new tab)

, another University of Vienna mathematician --- that aims to provide "a
new geometry for Einstein's theory of relativity and beyond."

"Standard general relativity talks about geometric objects, namely
space-times, but only if they behave nicely enough," Steinbauer said.
"With this new framework, we can go beyond that. We can handle very edgy
objects, very badly behaved objects."

**A Path Via Triangulation**
----------------------------

When Kunzinger and Sämann started working together in 2016, their first
goal was to revisit one of the most basic concepts to appear in
Einstein's equations: curvature.

Curvature is a measure of how much space-time bends at a given point.
There are many ways to describe it mathematically. Typically, computing
these different types of curvature requires calculus. But Kunzinger and
Sämann wanted to find a way to estimate the curvature of space-time
without requiring assumptions of smoothness. In particular, they wanted
to do so for the kind of curvature central to Einstein's equations ---
what's known as Ricci curvature --- so that they could then use their
methods to prove important statements about black holes and other
phenomena.

But Ricci curvature is complicated, and Kunzinger and Sämann weren't
ready to tackle it --- yet. They first turned to a more straightforward
notion of curvature, called sectional curvature, which tells you how
different two-dimensional slices of space-time curve at a point. If they
could compute this curvature in non-smooth settings, it would still
allow them to take on more restricted versions of the statements they
wanted to prove.

They had an idea for where to start. When it comes to ordinary
mathematical spaces --- rather than the confounding space-time of
general relativity --- mathematicians have had an alternative way to
describe sectional curvature for decades. The method allows them to put
bounds on the curvature of a shape using simple triangles.

Say you have a two-dimensional surface that resembles a sphere. To
estimate its curvature, first draw three points on the surface and
connect them with the shortest (and therefore straightest) possible
paths. This gives you a triangle. Then draw another triangle with the
same side lengths on a flat plane. You already know the plane's
curvature --- it's zero --- so this new triangle will give you a helpful
reference.

Now compare the two triangles. You'll find that the triangle on the
spherelike surface has larger angles than the triangle on the plane, and
that a line segment drawn between the midpoints of two of its sides is
longer. This tells you that the curvature of your surface is greater
than zero.

![](media/image1.png){width="0.6944444444444444in"
height="0.6944444444444444in"}

Mark Belan/*Quanta Magazine*

Similarly, you can compare the original triangle to one drawn on a
highly curved surface (such as a sphere with a small radius, whose
curvature can be calculated easily) in order to get an upper bound. If
you continue tweaking your comparison surfaces, you can home in on a
more accurate range of curvatures for your surface of interest.

By comparing triangles in this way, mathematicians get around the need
to compute curvature using calculus --- and their method doesn't require
the surfaces they study to be smooth.

> ![Man in a dark blue shirt standing in front of a gray
> wall.](media/image1.png){width="6.5in" height="7.875in"}
>
> Michael Kunzinger wants to extend Einstein's general theory of
> relativity to less smooth --- and perhaps more realistic --- settings.
>
> Joseph Krpelan

Kunzinger and Sämann wanted to adapt this method to work for space-time,
too. But carrying out triangle comparisons in the context of general
relativity is more complicated, because space-time has some strange,
counterintuitive features. Distances, for instance, are no longer
absolute. They contract or expand depending on the observer's speed.
Moreover, computations that involve the time dimension are different
from those involving just the space dimensions. (Moving in the time
direction subtracts from distance calculations, rather than adding to
them.)

So Kunzinger and Sämann chose to measure distance in terms of "time
separation" --- the time it takes to travel from one point to another,
according to a clock moving along that path. (They assumed that it's
never possible to travel faster than the speed of light.)

When they then drew each side of their triangle, they chose the path
that would yield the maximum time separation. That is, each edge formed
the longest possible path (in terms of time), not the shortest. That's
because this path, like its counterpart on a conventional mathematical
surface, is still as straight as possible. A time-based definition of
distance defies our usual instincts. A more circuitous path through
space-time actually takes less time than a straighter one. "Here,
detours are shorter," Kunzinger said. "That is the crux of the new
setup."

Using this notion of distance, he and Sämann drew triangles in a given
model of space-time and compared them to ones drawn in a reference model
where they already knew the curvature. They then showed that their
method can provide good curvature estimates: They could use it to
demonstrate, for instance, that in the interior of a black hole, the
sectional curvature becomes infinite.

And it would work in any non-smooth setting they might choose, Sämann
said, so long as they could define distance in terms of time in the same
way. "Your space-time could have corners, edges and folds, and it
doesn't matter," he said. "This approach doesn't care about
non-smoothness."

Now they wanted to do something with their approach.

**A Singular Preoccupation**
----------------------------

In 1965, the physicist Roger Penrose proved a theorem for which he later
received a Nobel Prize. Using geometric arguments, he proved that, under
certain conditions (such as the presence of a "trapped surface" caused
by a collapsing star's gravitational pull), a singularity will
inevitably form --- a point where the curvature becomes so intense, and
gravity so strong, that even light rays moving away from it cannot
escape. In other words, the singularities at the centers of black holes
weren't just mathematical abstractions; they could actually form in the
universe.

The following year, Stephen Hawking translated Penrose's idea into a
cosmological setting, showing that if you again assume certain
conditions, there must have been a singularity at some time in the past.
Hawking's theorem, according to Steinbauer, "is generally thought of as
mathematical evidence for the occurrence of a Big Bang."

But both Penrose's and Hawking's proofs required them to assume that
space-time was smooth --- a limitation that Hawking himself acknowledged
in a 1973 book he wrote with the physicist George Ellis.

![](media/image1.png){width="6.5in" height="7.388888888888889in"}

A team of mathematicians led by Roland Steinbauer (upper right) is
developing new geometric techniques to answer questions about our
universe. Raquel Perales (upper left) and Chiara Rigoni are two of the
team's principal investigators.

Joseph Krpelan; Martin Piskernig

Kunzinger and Sämann wanted to use their new way of estimating curvature
to determine whether these singularity theorems would still be valid if
they no longer assumed space-time is smooth. Would singularities persist
even in rougher, more realistic-looking spaces? It's important to find
out if the smoothness condition can be waived, Sämann said, because
doing so would bring the theorems closer to physical reality. After all,
he added, "we believe non-smoothness is an inescapable part of the
natural world."

In 2019, together with Stephanie Alexander of the University of Illinois
(who died in 2023) and Melanie Graf

(opens a new tab)

, now at the University of Hamburg, the mathematicians proved a special
case of Hawking's singularity theorem.

(opens a new tab)

For simpler models of space-time --- which were not smooth, but had a
special structure --- they showed that if you traced the paths of
particles or light rays backward in time, then those paths would have to
be finite.

In other words, a singularity would inevitably arise at some point in
the past.

"It's a proof of concept that with our approach, we can prove
singularity theorems that had been in more restricted, smooth domains,"
Sämann said. Their triangle comparison method wasn't just for show; it
could help tell them something useful about the universe, about the
presence of singularities in various kinds of space-times.

But the technique could only give them estimates of sectional curvature.
And sectional curvature provides more detailed information about the
curvature of space-time than Penrose's and Hawking's theorems had
needed. By basing their argument on sectional curvature, Kunzinger,
Sämann and their colleagues proved their result under a more limited set
of conditions than they would have preferred to. To re-prove the
singularity theorem in its full generality --- as Hawking and Penrose
had done --- the mathematicians would instead need to base their
arguments on less detailed information about curvature. They'd need to
use Ricci curvature, not sectional curvature.

To achieve that, they needed some new players to join the effort.

**A Napoleonic Notion**
-----------------------

In 2018, while Kunzinger and Sämann were developing their techniques for
sectional curvature, Robert McCann

(opens a new tab)

of the University of Toronto decided to approach the problem using tools
from an entirely different area of math. In particular, he hoped to make
use of a method called optimal transport.

> ![An engraving of a man](media/image1.png){width="6.5in"
> height="6.916666666666667in"}
>
> In the late 18th century, Gaspard Monge found a way to efficiently
> transport soil to build fortifications for Napoleon's army.
> Mathematicians have continued to develop his "optimal transport"
> technique to solve other optimization problems.
>
> Henri-Joseph Hesse via Wikimedia Commons

The idea dates back to the late 18th century, when Napoleon tasked the
French geometer Gaspard Monge with transporting large quantities of soil
to construct fortifications. Monge used his mathematical skills to
figure out the most cost-efficient way to divvy the materials up and
send them to their destinations.

More than two centuries later, McCann found a way to use Monge's
technique to estimate Ricci curvature. Whereas sectional curvature tells
you precisely how two-dimensional slices of a space bend in different
directions, Ricci curvature gives a more average sense of that bending.
It essentially measures how the volume of an object will change as it
moves through regions of space-time with varying curvature. And optimal
transport, McCann realized, could give you information about these
changes in volume.

To get a sense of how this works, let's consider a simpler example. Say
you have a pile of sand at the Earth's North Pole, and you want to
transport it to the South Pole. You can use optimal transport techniques
to study how grains of sand will move between the two poles, and how
their volume will change along the way. As they travel over the surface
of the Earth, following the most direct possible paths toward the
equator, they spread out, encompassing a bigger volume, before
contracting again. The way their volume changes reflects the curvature
of the Earth.

McCann used the connection between optimal transport and curvature to
develop a method for estimating the Ricci curvature of space-time

(opens a new tab)

without calculus. But the approach only worked when space-time was
smooth.

Then, a few months later, two mathematicians --- Andrea Mondino

(opens a new tab)

of the University of Oxford and Stefan Suhr

(opens a new tab)

of Ruhr University Bochum in Germany --- figured out how to adapt
optimal transport techniques (using insights from Kunzinger and Sämann's
research) to work in non-smooth settings

(opens a new tab)

. In 2020, Mondino and Fabio Cavalletti

(opens a new tab)

of the University of Milan showed that Hawking's singularity theorem
still held up in those settings

(opens a new tab)

. In fact, they were able to get it to work for more general models of
space-time than Kunzinger and Sämann had. And their method for
estimating Ricci curvature allowed them to prove the theorem without
making the same limiting assumptions that Kunzinger and Sämann had to.

The proof not only showcases the power of their method, but also
provides an even firmer mathematical basis for the idea of a Big Bang
singularity.

"It shows that the singularity theorems are even more fundamental" than
mathematicians and physicists had ever been able to show, according to
Eric Ling

(opens a new tab)

of the University of Copenhagen, who was not involved in the research.
Hawking's and Penrose's singularities don't require a smooth space-time.
Even in a rougher environment --- one with corners or edges or other
strange geometric features --- they'll inevitably arise.

"Major results in general relativity actually extend to a much weaker
setting where a smooth underlying space-time is not necessary," said
Eric Woolgar

(opens a new tab)

, a mathematician at the University of Alberta. "The ideas involved are
quite remarkable."

**A New Calculus**
------------------

The ideas are still coming. Last year, McCann, Sämann and six colleagues
started to develop ways to extend techniques from calculus

(opens a new tab)

to non-smooth settings. "We can't do full-on calculus yet," Sämann said,
but "this should expand the toolbox a lot." Mathematicians are already
using those techniques

(opens a new tab)

to prove other singularity theorems

(opens a new tab)

and related statements.

**Related:**
------------

-   [Singularities in Space-Time Prove Hard to
    > Kill](https://www.quantamagazine.org/singularities-in-space-time-prove-hard-to-kill-20250527/)

    > [Mathematicians Prove Hawking Wrong About the Most Extreme Black
    > Holes](https://www.quantamagazine.org/mathematicians-prove-hawking-wrong-about-extremal-black-holes-20240821/)

    > [A Traveler Who Finds Stability in the Natural
    > World](https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/)

And last month, Cavalletti and Mondino, along with Davide Manini

(opens a new tab)

of the International School for Advanced Studies in Italy, became the
first mathematicians to re-prove Penrose's singularity theorem

(opens a new tab)

about black holes in non-smooth space-times.

Financial support has come too. Last year, Steinbauer, Kunzinger, Sämann
and their colleagues received a grant of 7 million euros from the
Austrian Science Fund to continue their work. They've been recruiting
more researchers to the team, who are now working on several projects
--- all aimed at developing novel mathematics to expand the reach of
general relativity.

Steinbauer is excited by the possibility that this program might one day
help establish a mathematical foundation for a theory of quantum
gravity: a long-sought way to unify the laws of general relativity with
those of the submicroscopic world of quantum physics. "There are many
approaches to quantum gravity which predict that, on a fundamental
level, space-time is discrete," he said. "You have isolated points in
space rather than a space-time continuum. And our framework can still
speak about curvature in these discrete situations." And if it can speak
about curvature, then perhaps it can speak about gravity.

Sämann can't wait to see what this collective enterprise will turn up
next. "People are still arriving," he said. "This project is really just
starting."

*Correction: July 16, 2025\
An earlier version of this article misstated when Napoleon tasked
Gaspard Monge with finding an efficient way to transport materials for
fortifications. He did so in the 1790s, not 1781.*
