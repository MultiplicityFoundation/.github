---
slug: proposed-extension
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/aesthetics/Proposed Extension.md
  last_synced: '2026-03-20T17:17:21.819050Z'
---

**A Proposed Extension to the Prime-Indexed Color Mapping Specification for Generative Art and Expressive Rendering**
=====================================================================================================================

### **Introduction: From Scientific Instrument to Creative Engine**

The Prime-Indexed Color Mapping specification, designed with the rigor
and determinism required for scientific visualization, possesses a
powerful and robust framework that is exceptionally well-suited for
adaptation to generative art. Its mathematical foundation, far from
being a creative constraint, offers a predictable and deeply
controllable substrate for artistic expression. The core thesis of this
whitepaper is that with a series of formal extensions, this
specification can be transformed from a scientific instrument into a
comprehensive and versatile engine for creative work.

This document proposes these extensions by first covering the
specification\'s foundational color model and its profound implications
for intuitive control. We will then re-frame the existing V2 parameters
as a suite of orthogonal artistic levers. Building upon this foundation,
this paper will propose major new systems, including a unified framework
for data-driven response shaping, an algorithmic engine for generating
color harmony, an expanded model for advanced layer compositing and
interaction, and a novel approach to re-purposing the system\'s core
constraints as a generative tool.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **1.0 Foundational Principles: The Perceptual Canvas of OKLCH**

The strategic importance of the underlying color space cannot be
overstated. The specification\'s choice of OKLCH is not a minor
implementation detail; it represents a philosophical shift from a
device-centric model of color to a human-centric one. This decision is
the cornerstone upon which all subsequent artistic control is built, as
it ensures that numerical operations directly and predictably correspond
to perceived visual changes.

#### **1.1 Deconstructing Perceptual Uniformity**

The defining characteristic of the OKLCH color space is its **perceptual
uniformity**. This means that a uniform numerical change in a color\'s
coordinates corresponds to a proportionally uniform change in its
perceived appearance to the human eye. This is a stark contrast to
traditional color spaces like RGB and HSL, which are rooted in the
mechanics of display hardware.

In HSL, for instance, a 10-unit change in lightness for a yellow hue
results in a vastly different perceptual shift than the same change for
a blue hue. Similarly, a linear interpolation between two colors in RGB
or HSL often passes through a visually \"muddy\" or desaturated gray
zone---an artifact of the underlying mathematics rather than a
reflection of artistic intent.

OKLCH, derived from models of human color perception, was specifically
designed to correct these deficiencies. The \"so what\" of this choice
is that it transforms color manipulation from numerical guesswork into
an intuitive, predictable dialogue between the artist and the medium.
When an artist intends to make a color \"slightly brighter,\" the
corresponding numerical operation on its Lightness value produces a
result that faithfully matches that perceptual intent.

#### **1.2 The Three Pillars of Expressive Control: Lightness, Chroma, and Hue**

The power of OKLCH is realized through its three intuitive and largely
independent components, which provide orthogonal axes for artistic
manipulation.

-   **Lightness (L):** Representing perceived brightness on a scale from
    > 0 (black) to 1 (white), Lightness in OKLCH is consistent across
    > all hues. A yellow and a blue with the same L value will appear
    > equally bright, a property that is indispensable for creating
    > balanced tonal compositions and is a cornerstone of accessible
    > design.

-   **Chroma (C):** This component defines the \"amount of color\" or
    > vividness, analogous to saturation. It ranges from 0 (a neutral
    > gray) to a maximum value that is bounded by the display\'s gamut.
    > A key feature of OKLCH is that this maximum chroma varies by hue
    > and lightness; for example, a vibrant yellow can be achieved at a
    > higher lightness than a deep blue. This defines the gamut boundary
    > not as a simple box, but as a complex three-dimensional volume
    > representing all physically realizable colors.

-   **Hue (H):** Specified as a 360-degree angle on a color wheel, this
    > cylindrical representation is a profound departure from the
    > Cartesian nature of RGB. By defining hue as a single, continuous
    > dimension, the system provides a powerful latent space for
    > algorithmic creativity. As will be explored later, complex color
    > harmonies can be expressed as simple arithmetic operations on this
    > angle, turning the hue parameter into a programmable axis for
    > generating entire, aesthetically coherent palettes.

#### **1.3 Navigating the Gamut: Robustness and Artistic Intent**

OKLCH is a wide-gamut color space, capable of describing colors far more
vibrant than those representable in standard sRGB. This power presents a
practical challenge: when a requested color is \"out-of-gamut,\" it must
be mapped to the closest available color on the display.

A naive mapping technique like clipping can drastically alter the
perceived hue and lightness, violating artistic intent. OKLCH enables a
vastly superior method: **chroma reduction**. When a color is
out-of-gamut, its Chroma value is progressively reduced while keeping
its Hue and Lightness constant until it falls within the displayable
range. This method is artistically superior because it preserves the two
most crucial perceptual qualities of the color.

This robust gamut handling allows artists to work with ideal theoretical
palettes, confident that the system will preserve their core intent
regarding hue and lightness when translating those ideals to the screen.
With this stable and predictable perceptual canvas established, we can
now analyze the specific parameters that act as the artist\'s primary
controls within this space.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **2.0 Core Artistic Levers: Re-framing V2 Parameters for Expression**

The core parameters of the specification should not be viewed as mere
scientific variables, but as a suite of powerful, largely orthogonal
\"levers\" for artistic control. A nuanced but profound design choice is
the distinct use of normalized energy (\\tilde{E}\_i) to drive Chroma
and normalized intensity (\\bar{I}\_i) to drive Lightness and Opacity.
This decoupling provides a rich expressive space, allowing a feature
with high energy but low intensity to be rendered as a vibrant but
ethereal wisp of color. Conversely, a low-energy, high-intensity feature
can be rendered as a solid, bright, but desaturated object.

#### **2.1 Hue Construction: Balancing Determinism and Variation**

The multi-stage hue construction formula offers a sophisticated balance
between a stable, deterministic foundation and dynamic, data-driven
variation.

-   **Base Anchor (h\_i\^\*):** This is the \"root note\" for a
    > channel\'s color. It is derived deterministically from the
    > channel\'s unique prime number via the formula h\_i\^\* =
    > 2\\theta\_{p\_i}, where \\theta\_{p\_i} is an angle provided by
    > the IMD.SatoTate.Angle interface. This provides a stable,
    > reproducible foundation, analogous to selecting a key signature in
    > a piece of music.

-   **Spread (\\lambda):** This parameter is the primary control for
    > palette diversity. A low value produces a subtle, analogous
    > palette where all hues remain close to their base anchors. A high
    > value creates a chaotic and energetic palette where data can push
    > hues far across the color wheel.

-   **Feature Seed (g\_i):** This is the data-driven component that
    > introduces spatial and temporal variation. By pre-processing the
    > input data used to calculate g\_i, an artist can create dramatic
    > hue shifts that are triggered only at specific data thresholds,
    > highlighting key features with distinct colors.

-   **Offset (\\delta\_i):** While fixed in the base specification for
    > reproducibility, exposing this per-channel offset for artistic
    > control would be a valuable enhancement. It would allow an artist
    > to manually fine-tune the hue of a single channel without
    > affecting global parameters, akin to adjusting the tuning of a
    > single instrument within an orchestra.

#### **2.2 Chroma and Lightness: Shaping Palette Vibrancy and Tonal Range**

These parameters directly control the saturation and dynamic range of
the final image.

-   **Maximum Chroma (C\_{max}):** This acts as the master vibrancy
    > control for the entire image. A low value produces a muted, pastel
    > look, while a high value results in a vivid and intensely
    > saturated visual.

-   **Chroma Response (\\alpha\_C):** This parameter shapes the
    > energy-to-chroma mapping according to the curve q(u) =
    > \\frac{u}{1+u\^{\\alpha\_{C}}}. A high value of \\alpha\_C causes
    > the chroma to ramp up quickly, making even faint, low-energy
    > features \"pop\" with color and revealing subtle details. A low
    > value reserves the highest saturation for only the most energetic
    > features.

-   **Lightness Range (l\_{min}, l\_{max}):** These parameters define
    > the absolute black and white points. Setting l\_{min} \> 0 creates
    > a \"lifted black\" or faded look, simulating atmospheric haze.
    > Setting l\_{max} \< 1 creates \"crushed whites,\" muting
    > highlights for a softer response.

#### **2.3 Opacity and Temporal Dynamics: Controlling Presence and Motion**

These parameters govern how features appear in space and evolve over
time.

-   **Opacity Sensitivity (\\kappa):** This parameter controls the
    > transition from transparency to solidity. A low value creates
    > solid, well-defined shapes even at low intensities. A high value
    > creates wispy, translucent, or \"ghostly\" layers, a key control
    > for achieving ethereal effects.

-   **Hue Drift Speed (\\kappa\_f):** This controls the overall speed of
    > the slow, continuous color cycling. It can produce effects ranging
    > from a meditative, almost imperceptible drift to a rapid,
    > energetic shimmer.

-   **Modulation Amplitudes (\\epsilon\_h, \\epsilon\_C,
    > \\epsilon\_L):** These parameters add subtle, organic life to an
    > otherwise static image by applying a sinusoidal \"wobble\" to hue,
    > chroma, and lightness. Small values can create a gentle flicker or
    > \"breathing\" effect, simulating the look of a living organism.

#### **2.4 Parameter Reference Summary**

The following table synthesizes the core V2 parameters, re-framing their
technical function in terms of their primary artistic impact.

  Parameter                 Symbol         Technical Function                                                   Primary Artistic Effect                                                Suggested Range & Visual Impact Notes
  ------------------------- -------------- -------------------------------------------------------------------- ---------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
  **Spread**                \\lambda       Scales the influence of the feature seed g\_i on hue dispersion.     Controls palette diversity and data-driven color variation.            \[0.0, 2.0\] Low values create harmonious, analogous palettes. High values create chaotic, high-energy palettes.
  **Max Chroma**            C\_{max}       Sets the global maximum chroma value.                                Master control for overall image saturation/vibrancy.                  \[0.0, 0.4\] Defines the range from grayscale/pastel to intensely saturated. Max value is gamut-dependent.
  **Chroma Response**       \\alpha\_C     Controls the steepness of the energy-to-chroma mapping curve.        Adjusts saturation emphasis for low vs. high energy features.          \[0.5, 5.0\] High values make low-energy features \"pop\" with color. Low values reserve saturation for peaks.
  **Min Lightness**         l\_{min}       Sets the minimum lightness value (black point).                      Controls shadow depth and creates \"lifted black\" effects.            \[0.0, 0.5\] A value \> 0 creates a faded, low-contrast look in the shadows.
  **Max Lightness**         l\_{max}       Sets the maximum lightness value (white point).                      Controls highlight brightness and creates \"crushed white\" effects.   \[0.5, 1.0\] A value \< 1 mutes highlights, useful for soft or atmospheric looks.
  **Lightness Slope**       \\alpha\_L     Controls the slope (contrast) of the intensity-to-lightness curve.   Master control for tonal contrast.                                     \[1.0, 10.0\] High values create a harsh, high-contrast image. Low values create a flat, \"milky\" image.
  **Lightness Midpoint**    \\beta\_L      Controls the midpoint (gamma) of the intensity-to-lightness curve.   Master control for overall image brightness.                           \[0.1, 0.9\] Low values brighten the image. High values darken the image.
  **Opacity Sensitivity**   \\kappa        Controls the sensitivity of the intensity-to-opacity mapping.        Adjusts the transparency and \"solidity\" of features.                 \[0.01, 2.0\] Low values create solid, opaque shapes. High values create ethereal, ghostly layers.
  **Hue Drift Speed**       \\kappa\_f     Scales the base frequency for temporal hue modulation.               Controls the speed of color cycling over time.                         \[0.0, 1.0\] Creates effects from a slow, meditative drift to a rapid, energetic shimmer.
  **Hue Modulation Amp.**   \\epsilon\_h   Amplitude of the sinusoidal hue modulation.                          Controls the magnitude of the hue \"wobble\" over time.                \[0.0, 0.1\] Adds a subtle, organic \"breathing\" effect to colors.

These direct controls provide a rich palette of expressive tools.
However, to achieve a higher level of artistic direction, we must move
beyond adjusting individual parameters and begin to shape the
fundamental relationship between data and its visual representation.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **3.0 A Unified Framework for Data-Driven Response**

In compelling artistic works, the relationship between input data and
visual output is rarely linear. The most expressive control an artist
has is the ability to define this mapping, creating non-linear
\"response curves\" that emphasize or transform data to serve an
aesthetic purpose. This concept can be used to define a complete visual
\"look,\" analogous to a Look-Up Table (LUT) in cinematography. This
section proposes generalizing this concept into a unified framework for
comprehensive control over tonality, saturation, and opacity.

#### **3.1 The Sigmoid Function as an Artistic Tool for Tonal Mapping**

The specification\'s use of a logistic (sigmoid) function for lightness
mapping is an ideal foundation. The sigmoid, or \"S-curve,\" is prized
in image processing for its ability to modify contrast smoothly,
avoiding the harsh banding artifacts of simpler functions. Its
characteristic shape provides three distinct regions: a \"toe\" that
rises slowly from black, a steep linear middle section where most
contrast is applied, and a \"shoulder\" where it gracefully approaches
white. The art of tonal mapping lies in manipulating this curve using
two key parameters.

-   **Slope (\\alpha\_L):** This parameter governs the overall
    > **contrast**. A low \\alpha\_L produces a gentle S-curve,
    > resulting in a low-contrast, \"flat\" image that preserves detail
    > in shadows and highlights. A high \\alpha\_L creates a steep
    > curve, resulting in a punchy, high-contrast image that emphasizes
    > mid-tone separation.

-   **Midpoint (\\beta\_L):** This parameter shifts the curve
    > horizontally, controlling the overall **brightness** or gamma. A
    > low \\beta\_L brightens the image by mapping lower input
    > intensities to the mid-tones. A high \\beta\_L darkens the image,
    > reserving brightness for only the most intense features.

#### **3.2 Proposed Generalization: Shaping Chroma and Opacity**

The expressive power of the sigmoid curve is too valuable to be confined
to lightness alone. This document proposes extending this control
framework to the Chroma and Opacity channels, replacing their simpler
response functions with a unified, artist-controllable sigmoid model.

The proposed new formulas would be:

-   **Chroma:** C\_{i} = C\_{max} \\cdot s(\\tilde{E}\_{i};
    > \\alpha\_{C}, \\beta\_{C})

-   **Opacity:** A\_{i} = s(\\bar{I}\_{i}; \\alpha\_{A}, \\beta\_{A})

This generalization unlocks a new level of artistic nuance. For example,
an artist could control \"saturation contrast,\" creating an image where
most features are nearly grayscale but a narrow band of energy values
bursts into full color. Similarly, they could design sophisticated
opacity fade-ins with either sharp, illustrative transitions or long,
gentle fades, providing far more control than the single existing
parameter.

#### **3.3 Response Curve Shape Presets**

The following table serves as a visual dictionary for common looks that
can be achieved by manipulating the sigmoid response parameters for
lightness, providing artists with an intuitive starting point.

  Preset Name            \\alpha\_L Value   \\beta\_L Value   Artistic Description
  ---------------------- ------------------ ----------------- --------------------------------------------------------------------------------------------------------------------------------------------------------
  **Linear (Approx.)**   1.0                0.5               A neutral, low-contrast mapping that preserves maximum detail across the full tonal range. Good for scientific accuracy.
  **High Contrast**      8.0                0.5               Crushes shadow and highlight detail to create a punchy, dramatic image. Emphasizes mid-tone separation.
  **Lifted Blacks**      4.0                0.25              Brightens the overall image by compressing the dark end into a light gray, making shadows appear faded or hazy. Creates a vintage or atmospheric look.
  **Crushed Whites**     4.0                0.75              Darkens the overall image by compressing the bright end into a light gray, muting the highlights. Creates a moody, low-key lighting effect.
  **Hard Threshold**     20.0               0.5               Creates a high-contrast, binary, or posterized look with a sharp transition. Useful for graphic effects and isolating specific data thresholds.

By shaping the response of individual channels, we gain deep control
over their appearance. The next logical step is to ensure that the
*collection* of these channels forms an aesthetically cohesive whole.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **4.0 Proposed Extension: Algorithmic Color Harmony**

A key limitation in the base specification is the lack of a mechanism to
ensure the final collection of generated hues is aesthetically cohesive.
The combination of prime-anchored base hues and data-driven dispersion
can result in a palette that is visually dissonant. This section
proposes a formal system for algorithmic color harmony that leverages
the geometry of the OKLCH color wheel to procedurally generate pleasing
and intentional palettes.

#### **4.1 Defining Classic Harmonies as Mathematical Functions**

The cylindrical nature of the OKLCH hue component, where hue is a
360-degree angle, allows classic color theory rules to be expressed as
simple mathematical functions. These functions take a base hue angle
(h\_{base}) and generate a set of related hues.

-   **Analogous:** Uses colors adjacent on the color wheel.

    -   *Formula:* h\_{\\text{analogous}}(h\_{base}, n) = (h\_{base}
        > \\pm n \\cdot 30\^{\\circ}) \\pmod{360\^{\\circ}}

-   **Complementary:** Uses two colors directly opposite each other.

    -   *Formula:* h\_{\\text{complementary}}(h\_{base}) = (h\_{base} +
        > 180\^{\\circ}) \\pmod{360\^{\\circ}}

-   **Split-Complementary:** Uses a base color and the two colors
    > adjacent to its complement.

    -   *Formulas:* h\_{\\text{split}1}(h\_{base}) = (h\_{base} +
        > 150\^{\\circ}) \\pmod{360\^{\\circ}};
        > h\_{\\text{split}2}(h\_{base}) = (h\_{base} + 210\^{\\circ})
        > \\pmod{360\^{\\circ}}

-   **Triadic:** Uses three colors evenly spaced around the color wheel.

    -   *Formulas:* h\_{\\text{triad}1}(h\_{base}) = (h\_{base} +
        > 120\^{\\circ}) \\pmod{360\^{\\circ}};
        > h\_{\\text{triad}2}(h\_{base}) = (h\_{base} + 240\^{\\circ})
        > \\pmod{360\^{\\circ}}

-   **Tetradic (Rectangular):** Uses four colors arranged into two
    > complementary pairs.

    -   *Formulas:* h\_{\\text{tetrad}1}(h\_{base}) = (h\_{base} +
        > 60\^{\\circ}) \\pmod{360\^{\\circ}};
        > h\_{\\text{tetrad}2}(h\_{base}) = (h\_{base} + 180\^{\\circ})
        > \\pmod{360\^{\\circ}}; h\_{\\text{tetrad}3}(h\_{base}) =
        > (h\_{base} + 240\^{\\circ}) \\pmod{360\^{\\circ}}

#### **4.2 Integration into the Specification Pipeline**

To integrate this system, two new global parameters are proposed:

1.  **HarmonyMode**: An enumerated parameter to select the active
    > harmony rule (e.g., ANALOGOUS, TRIADIC).

2.  **LeadPrimeIndex**: An integer that specifies which prime in the
    > active set will serve as the source for the base hue.

The prime-indexing of the specification provides a unique and powerful
mechanism to anchor these palettes. The deterministic but distinct
nature of the primes can be mapped to specific roles within a color
harmony. An artist could define a rule where the lowest active prime
always provides the \"root\" color, the next prime provides its
complement, and subsequent primes provide accent colors. This fuses the
mathematical rigor of the prime set with the aesthetic structure of
color theory.

The hue construction logic would be modified. For the lead channel, the
hue is calculated as normal. For all other channels, their base hue
anchor (h\_j\^\*) would be overridden by the selected harmony function.
For example, in **Triadic** mode with the first prime as the lead:

-   h\_0\^\* is calculated from its prime, p\_0.

-   h\_1\^\* becomes (h\_0\^\* + 120\^{\\circ}) \\pmod{360\^{\\circ}}.

-   h\_2\^\* becomes (h\_0\^\* + 240\^{\\circ}) \\pmod{360\^{\\circ}}.

-   The pattern repeats for subsequent channels.

This locks the entire prime set into a coherent palette. Furthermore,
HarmonyMode could be a dynamic, data-driven parameter, allowing the
palette itself to become a responsive indicator of the system\'s
state---switching from a calm, analogous harmony to a high-contrast
complementary one when a critical event is detected.

#### **4.3 Color Harmony Reference**

  Harmony Name                 Number of Colors   Hue Angle Formulas (relative to h\_0)                                                                                                                                                  Artistic Character
  ---------------------------- ------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------
  **Analogous**                2+                 h\_{n} = (h\_{0} \\pm n \\cdot 30\^{\\circ}) \\pmod{360\^{\\circ}}                                                                                                                     Serene, comfortable, low-contrast. Often found in nature.
  **Monochromatic**            N/A                h\_{n} = h\_{0} (Vary L and C only)                                                                                                                                                    Subtle, sophisticated, unified. Relies on tonal variation.
  **Complementary**            2                  h\_{1} = (h\_{0} + 180\^{\\circ}) \\pmod{360\^{\\circ}}                                                                                                                                High-contrast, vibrant, energetic. Demands attention.
  **Split-Complementary**      3                  h\_{1} = (h\_{0} + 150\^{\\circ}) \\pmod{360\^{\\circ}} \<br\> h\_{2} = (h\_{0} + 210\^{\\circ}) \\pmod{360\^{\\circ}}                                                                 Strong visual contrast but with less tension than complementary.
  **Triadic**                  3                  h\_{1} = (h\_{0} + 120\^{\\circ}) \\pmod{360\^{\\circ}} \<br\> h\_{2} = (h\_{0} + 240\^{\\circ}) \\pmod{360\^{\\circ}}                                                                 Vibrant and balanced. Can appear playful or dynamic.
  **Tetradic (Rectangular)**   4                  h\_{1} = (h\_{0} + 60\^{\\circ}) \\pmod{360\^{\\circ}} \<br\> h\_{2} = (h\_{0} + 180\^{\\circ}) \\pmod{360\^{\\circ}} \<br\> h\_{3} = (h\_{0} + 240\^{\\circ}) \\pmod{360\^{\\circ}}   Rich, complex, and versatile. Offers the most color variety.

Once we have generated a harmonious set of colors for our layers, the
next step is to define how those layers interact visually when they
overlap.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **5.0 Proposed Extension: Advanced Compositing and Blending**

The default Porter-Duff \"source-over\" compositing method specified is
robust but artistically limited, treating overlapping phenomena as a
simple matter of occlusion. This section proposes a dramatic expansion
of the compositing model to include a full suite of professional-grade
blend modes. This transforms the layer stack from a simple list into a
visual syntax where the interaction between layers can convey meaning
about the interaction between data channels.

#### **5.1 A Catalogue of Expressive Blend Modes**

Blend modes are mathematical functions that define how the colors of
overlapping pixels from a source layer (C\_s) and a backdrop layer
(C\_b) interact. A curated list of essential modes provides a powerful
expressive toolkit. The choice of blend mode allows the artist to
visualize the interaction of data channels in new ways. For example,
using the \"Screen\" mode could visualize a form of constructive
interference, where two overlapping fields combine to create a result
brighter than either input. \"Multiply\" could visualize attenuation or
absorption, where overlapping fields create a darker result. This
provides a powerful new method for artistic and scientific inquiry.

##### **Darken Modes**

These modes produce a darker result, often used for shadows and tinting.

-   **Multiply:** B(C\_b, C\_s) = C\_b \\cdot C\_s. The result is always
    > as dark or darker than the inputs. It is ideal for creating
    > realistic shadow effects.

##### **Lighten Modes**

These modes produce a lighter result, essential for glows and
highlights.

-   **Screen:** B(C\_b, C\_s) = 1 - (1 - C\_b) \\cdot (1 - C\_s). The
    > inverse of Multiply, the result is always as light or lighter. It
    > is the fundamental mode for simulating the additive behavior of
    > light.

##### **Contrast Modes**

These modes darken dark areas and lighten light areas, increasing local
contrast.

-   **Overlay:** A combination of Multiply and Screen that preserves the
    > tonality of the backdrop while blending in the source. It is
    > excellent for adding texture.

-   **Soft Light:** A gentler, more subtle version of Overlay, akin to
    > shining a diffuse spotlight. It is versatile for subtle tinting
    > and atmospheric effects.

##### **Comparative Modes**

These modes create effects based on the differences between layers.

-   **Difference:** B(C\_b, C\_s) = \|C\_b - C\_s\|. This mode subtracts
    > the darker color from the lighter color. It is useful for creating
    > dramatic, psychedelic color effects.

#### **5.2 Enhancing the Compositing Pipeline**

Unlocking the full power of blend modes requires artist control over
layer order, as many modes are non-commutative (A overlay B is not the
same as B overlay A). The default ordering by prime number is arbitrary
from an artistic perspective. This proposal therefore introduces two new
per-channel properties:

1.  **BlendMode\_i**: An enumerated parameter for each channel
    > specifying its blending function (e.g., MULTIPLY, SCREEN).

2.  **CustomOrder\_i**: An integer for each channel defining its
    > position in the rendering stack.

The rendering engine would first sort all active channels by their
CustomOrder\_i value and then composite them sequentially using their
specified BlendMode\_i. This gives the artist full, intentional control
over the visual syntax of layer interaction.

This post-rendering approach treats layers as co-existing phenomena
interacting at the pixel level. An alternative approach is to fuse the
data *before* rendering, implying a more fundamental interaction at the
data level.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **6.0 Proposed Extension: Alternative Aggregation Models**

A crucial distinction exists between post-rendering compositing
(co-existence of phenomena) and pre-rendering aggregation (fusion of
phenomena). The specification\'s default aggregation method uses the
**geometric mean**, which has a distinct visual signature: it produces a
conservative blending that is highly sensitive to low values, tending to
smooth out features. This implies an interaction where the result is a
modulated product of its constituents. To expand the expressive range,
alternative models are needed.

#### **6.1 Alternative Fusion Models and Their Narrative Implications**

The following models are proposed, each carrying a different visual and
narrative weight:

-   **Arithmetic Mean:** Represents simple summation or cumulative
    > effects.

    -   *Formula:* \\bar{E}\_S = \\frac{1}{m} \\sum\_{k=1}\^{m}
        > \\bar{E}\_{i\_k}

    -   *Narrative Implication:* This method produces brighter, more
        > additive results, suitable for visualizing phenomena that are
        > cumulative, like the combined light from multiple sources.

-   **Maximum Value:** Represents a competitive interaction where the
    > strongest signal dominates.

    -   *Formula:* \\bar{E}\_S = \\max(\\bar{E}\_{i\_1}, \...,
        > \\bar{E}\_{i\_m})

    -   *Narrative Implication:* The visual is determined solely by the
        > channel with the highest value at that point. This is useful
        > for winner-take-all systems or where a stronger phenomenon
        > overrides a weaker one.

-   **Minimum Value:** Represents an intersection or a logical AND
    > operation.

    -   *Formula:* \\bar{E}\_S = \\min(\\bar{E}\_{i\_1}, \...,
        > \\bar{E}\_{i\_m})

    -   *Narrative Implication:* The interaction is visible only where
        > *all* contributing channels are present, with its magnitude
        > determined by the weakest channel. This is ideal for
        > visualizing areas of co-occurrence or using one channel as a
        > mask for another.

-   **Weighted Blend:** Provides maximum artistic control by defining
    > the relative importance of each channel.

    -   *Formula:* \\bar{E}\_S = \\sum\_{k=1}\^{m} w\_k
        > \\bar{E}\_{i\_k}, where \\sum w\_k = 1.

    -   *Narrative Implication:* The artist can assign weights to make
        > some layers more visually dominant in the final fusion,
        > allowing for a carefully composed mixture rather than a simple
        > average.

Having explored direct manipulation of data and pixels, we now turn to
the final, most abstract layer of control: re-purposing the very rules
that govern the system\'s output.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **7.0 A Generative Framework: Re-purposing the Certification Pipeline**

This final section proposes a radical re-purposing of the
specification\'s certification and constraint enforcement mechanisms
(IMD interfaces). We re-frame these systems, designed as passive
\"guardrails\" to ensure scientific validity, as active, configurable
parameters for defining and exploring aesthetics. This transforms the
certification pipeline from a quality-control mechanism into a playable
artistic instrument.

#### **7.1 Hue Collision Control as a Harmony Tool**

The minimum hue separation parameter, \\Delta h\_{min}, is designed to
ensure colors are perceptually distinct. Artistically, this is a direct
control over the palette\'s harmonic structure.

-   Setting a **high value** (e.g., 90°) forces the system to find a
    > high-contrast, legible palette where all colors are maximally
    > distinct.

-   Setting a **low value** (e.g., 10°) allows the system to create
    > subtle, analogous harmonies where colors blend gently.

-   The deterministic adjustment process itself can be used as a
    > **generative tool**, where an intentionally colliding palette is
    > procedurally rearranged by the system into a stable state.

#### **7.2 The Certification Pipeline as Aesthetic \"Guardrails\"**

We re-frame the certification pipeline (PQH, PETC, CSL/ACE) as a system
of configurable aesthetic rules that define a desired outcome.

-   To create a **calm, meditative piece**, an artist could set very
    > tight bounds on the temporal continuity checks (PETC), forcing the
    > system to reject any frames with jarring changes.

-   To create a **vibrant, hyper-saturated piece**, an artist could
    > loosen the gamut safety checks (CSL/ACE), effectively telling the
    > system to embrace the visual artifacts of gamut mapping.

#### **7.3 Intentional Rule-Breaking for Experimental Effects**

The most advanced artistic application lies in the intentional violation
of the system\'s rules, treating its \"failure\" modes as creative
opportunities.

-   Disabling the temporal continuity checks (PETC) could create
    > intentional \"glitch\" effects or visual strobes.

-   Intentionally requesting out-of-gamut colors can be a method for
    > exploring the creative artifacts of the gamut mapping algorithm,
    > discovering unexpected and beautiful color relationships as the
    > system attempts to resolve these \"impossible\" requests.

This approach treats the entire constraint system as a playable
instrument. Art emerges from the tension between the artist\'s intent
and the inherent properties of the system as it attempts to resolve the
contradictions within the rules it has been given.

This completes the proposed set of extensions, transforming the
specification from a tool for visualization into a framework for
generation.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **8.0 Conclusion: A New Canvas for Creative Technology**

The Prime-Indexed Color Mapping specification describes a powerful and
rigorous system for scientific visualization. However, embedded within
its deterministic framework is the latent potential for profound
artistic expression. This whitepaper has systematically deconstructed
the specification through the lens of creative control, proposing a
series of expansions to transform a scientific instrument into a
versatile engine for generative art.

The key to this transformation lies in a series of conceptual shifts and
functional expansions:

1.  **Embracing Perceptual Color:** The foundational choice of the OKLCH
    > color space moves the system from a device-centric to a
    > human-centric model, ensuring that all artistic manipulations are
    > intuitive, predictable, and aligned with human perception.

2.  **Re-framing Parameters as Levers:** Each mathematical parameter in
    > the original specification has been re-contextualized as a
    > distinct artistic lever, providing a rich, orthogonal set of
    > controls to shape the final aesthetic.

3.  **Generalizing Response Curves:** The powerful sigmoid curve,
    > originally used only for lightness, is proposed as a unified
    > framework for shaping the data-driven response of chroma and
    > opacity, giving the artist nuanced control over the contrast of
    > every primary visual channel.

4.  **Introducing Algorithmic Harmony:** By leveraging the circular
    > nature of the OKLCH hue angle, a complete system for generating
    > classic color harmonies has been introduced, allowing for the
    > creation of aesthetically cohesive palettes that are
    > algorithmically derived yet artistically directed.

5.  **Expanding Compositing and Interaction:** The simple \"over\"
    > operator has been replaced with a full suite of professional blend
    > modes and alternative data aggregation models, allowing artists to
    > define the visual nature of data interaction beyond simple
    > occlusion.

6.  **Weaponizing Constraints:** The system\'s certification and
    > constraint mechanisms have been re-purposed from passive
    > \"guardrails\" into active, playable instruments, enabling artists
    > to enforce a desired aesthetic or to intentionally explore the
    > creative potential of the system\'s emergent behaviors.

This document demonstrates that a system built on principles of
mathematical rigor is not antithetical to artistic expression; on the
contrary, such a system provides the robust and predictable foundation
necessary for deep and intentional creative exploration. The
Prime-Indexed Color Mapping framework, enhanced with these extensions,
becomes more than a canvas for creating meaning; it becomes a generative
engine for discovering it.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **9.0 References**

1.  CIELAB color space - Wikipedia,
    > https://en.wikipedia.org/wiki/CIELAB\_color\_space

2.  Perceptually uniform color spaces - Programming Design Systems,
    > https://programmingdesignsystems.com/color/perceptually-uniform-color-spaces/

3.  oklch() - CSS-Tricks,
    > https://css-tricks.com/almanac/functions/o/oklch/

4.  Color Everything in CSS - CSS-Tricks,
    > https://css-tricks.com/color-everything-in-css/

5.  RGB, CMYK, HSL... OKLCH? Making Sense of Color Models \| by Nadiya
    > Abrosimova \| Oct, 2025 \| Medium,
    > https://medium.com/\@nadiyq/rgb-cmyk-hsl-oklch-making-sense-of-color-models-88c90b186661

6.  Perceptual uniform color space - Mohan Vadivel,
    > https://mohanvadivel.com/thoughts/perceptual-uniform-color-space

7.  What are OKLCH colors? - Hacker News,
    > https://news.ycombinator.com/item?id=45010876

8.  Oklab color space - Wikipedia,
    > https://en.wikipedia.org/wiki/Oklab\_color\_space

9.  OKLCH in CSS: why we moved from RGB and HSL - Evil Martians,
    > https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl

10. oklch() - CSS \| MDN - Mozilla,
    > https://developer.mozilla.org/en-US/docs/Web/CSS/color\_value/oklch

11. The New CSS Color Format You Didn\'t Know You Needed; OKLCH() - DEV
    > Community,
    > https://dev.to/greenteaisgreat/the-new-css-color-format-you-didnt-know-you-needed-oklch-10hf

12. How to Calculate Complementary, Triadic, and Tetradic Colors from a
    > Hex Code,
    > https://customstickers.com/community/blog/how-to-calculate-complementary-triadic-and-tetradic-colors-from-a-hex-code

13. Is there an equation to easily convert a color to its matching color
    > in another hue?,
    > https://graphicdesign.stackexchange.com/questions/9483/is-there-an-equation-to-easily-convert-a-color-to-its-matching-color-in-another

14. Sigmoid function - Wikipedia,
    > https://en.wikipedia.org/wiki/Sigmoid\_function

15. Adjustable Sigmoid Curve (S-Curve) from (0,0) to \$ (1,1) - Math
    > Stack Exchange,
    > https://math.stackexchange.com/questions/459872/adjustable-sigmoid-curve-s-curve-from-0-0-to-1-1

16. Logistic function - Wikipedia,
    > https://en.wikipedia.org/wiki/Logistic\_function

17. Sicegar: R package for sigmoidal and double-sigmoidal curve
    > fitting - PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC5774301/

18. How do we fit a sigmoid function in Python? - Stack Overflow,
    > https://stackoverflow.com/questions/55102473/how-do-we-fit-a-sigmoid-function-in-python

19. Designing With Color: Complementary, Analogous, Monochromatic &
    > Triadic Color Combinations - Event Leadership Institute,
    > https://pcmainstitute.org/designing-with-color-complementary-analogous-monochromatic-triadic-color-combinations/

20. Computational Color - Rune Madsen,
    > https://printingcode.runemadsen.com/lecture-color/

21. Color Wheel - Color Calculator \| Sessions College,
    > https://www.sessions.edu/color-calculator/

22. Everything You Need To Know About Triadic Colors - The Interaction
    > Design Foundation,
    > https://www.interaction-design.org/literature/article/triadic-color-scheme

23. Compositing and Blending Level 1 - W3C,
    > https://www.w3.org/TR/compositing-1/

24. Compositing and Blending - ColorAide Documentation,
    > https://facelessuser.github.io/coloraide/compositing/
