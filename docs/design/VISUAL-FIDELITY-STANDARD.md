# Charlie Architect — Visual Fidelity & Physical Product Craft

## Why this standard exists

In a user-supplied comparison of two keyboard UI screenshots, the preferred presentation displayed a large, highly legible object with dimensional keycaps, clear separation, controlled shadows and generous product space. The alternative rendered an intricate but much smaller keyboard inside a dense utility panel, with less legible legends and weaker depth. **Both may be functionally sound, but they convey different visual quality.** This standard corrects the tendency to equate an accurate model with an excellent *rendered appearance*.

The user-approved reference is a calibration of design quality, NOT a template to copy or a mandate to make every product look like a keyboard.

## 1 — Product visual hierarchy

- Define the **visual protagonist** of every scene. On product-led editorial sections, let the object command attention rather than become a thumbnail inside card chrome.
- Decide object scale after mapping the available viewport and intended narrative. As a *review heuristic*, ask whether the primary object occupies a substantial share of the usable visual region (often ~60–90% of a dedicated showcase canvas on desktop, when appropriate), without cutting off information or breaking mobile layouts. This is not a universal CSS width requirement.
- Do not default to nested boxes, borders and inset panels for a showcase scene. Use an open stage, well-positioned object, purposeful crop and negative space when it better serves the design.
- Maintain a clean reading order: subject first; title and explanation second; controls third. A diagnostic panel may intentionally invert this hierarchy if diagnostics were requested.
- Inspect at actual display size. A detailed SVG that is technically accurate but unreadably small **fails** visual fidelity.

## 2 — Dimensional material & tactile detail

For physical products represented by SVG/CSS/Canvas, derive visual treatment from the reference:
- **Silhouette:** preserve characteristic proportions, edges, gaps and recognizable structure.
- **Layered construction:** body/case, top surface, raised parts, seams, edges and meaningful internal spacing. A keycap or dial is not merely a flat colored rectangle.
- **Physically plausible light:** consistent directional highlight, inset edge light, ambient occlusion/contact shadow, and cast shadow matching the product's orientation. Avoid randomly assigned glows.
- **Material response:** matte graphite differs from brushed metal, glass, rubber or plastic. Use restrained tonal variation and highlights to communicate it.
- **Depth:** separate the surface from the background with shadows and perspective, without thick cartoon outlines.
- **Microdetail:** legends, tactile marks, kerning and spacing scale with the object's actual display size.
- **State feedback:** an object being pressed or moved must appear to travel in physical space, with altered shadow/lighting appropriate to the motion.
- **Reality check:** when deriving a 3D-like illustration from one low-resolution photo, clearly label unverified details as illustrative.

## 3 — Readability is part of realism

- Prefer a sufficiently large visual treatment over shrinking detailed content to fit dense panels.
- Inspect the smallest meaningful detail at 100% zoom at the actual target viewport. If the text or silhouette is indistinct, enlarge/simplify the visual rather than adding more tiny labels.
- Use high contrast that fits the material and is accessible for essential UI. Decorative component markings may be subtler only if they are not the sole source of information.
- Choose typeface and character sizing suited to the medium; mechanical monospaced caps and editorial typography can coexist with distinct roles.
- Retain the integrity of the layout on responsive breakpoints. Provide scroll or alternate compositions for wide technical illustrations instead of shrinking everything below legibility.

## 4 — Distinguish product stage from utility panel

**Product stage:** generous canvas, large subject, nuanced shadow/lighting, low interface noise, meaningfully progressive storytelling.

**Utility panel:** bounded surface, dense stats, repeated labels and compact controls optimized for frequent tasks.

Use the correct one based on the explicit user brief. A showcase may contain a separate utility chapter, but don't make the diagnostic panel the visual template for every section.

## 5 — Reference-calibrated review

When the user identifies a visual preference, record **observable attributes** before editing:
- subject-to-viewport ratio;
- key/content size and legibility;
- material dimensionality and shadows;
- interface density and nested framing;
- contrast and color discipline;
- type hierarchy and space;
- unique interaction and motion readability.

Compare **equivalent scenes** at equivalent viewport sizes and states when possible. If screenshots depict *different* sections, identify what is transferable and don't claim a fully controlled A/B result.

Build a comparison matrix **Preferred behavior / Current output / Perceptual gap / Concrete code change / Verified?**. Implement changes, recapture screenshots and iterate until critical gaps close.

## 6 — Definition of done for visual work

- [ ] The object has the intended on-screen visual prominence.
- [ ] Distinguishing physical features remain recognizable at actual display size.
- [ ] Material, edge, elevation, shadow and lighting are coherent.
- [ ] Labels and text that matter are legible.
- [ ] The section's framing supports its purpose rather than swallowing the product in panels.
- [ ] The first impression is intentional, with purposeful balance of product, copy and controls.
- [ ] On mobile the object remains comprehensible without unreadable miniaturization.
- [ ] Real browser screenshots have been inspected when runtime access exists.
- [ ] Visual limitations are documented honestly as NOT TESTED when only source is available.

**A code build or set of unit tests can pass while visual fidelity fails.** A premium visual deliverable must pass both.
