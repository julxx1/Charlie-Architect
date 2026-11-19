# Premium art direction & UI standards

## Visual strategy
- Define audience, brand attributes, primary user action, tone, references and meaningful differentiation.
- Write a one-sentence creative direction before composing the interface.
- Reject common AI templates: random gradients, endless glassmorphism, identical cards, filler copy, arbitrary icons and generic hero.
- Establish editorial rhythm, hierarchy, deliberate asymmetry, effective negative space, grid and depth.
- Choose thoughtful typography with readable line lengths, clear scale and consistent spacing.
- Use a restrained, accessible semantic palette, backgrounds, accents, feedback and focus colors.
- Use owned/licensed assets with optimized dimensions, truthful claims and descriptive alt text.

## Visual fidelity before implementation — Charlie v4
For a physical or visually distinctive product, read `VISUAL-FIDELITY-STANDARD.md` and prepare a visual scale/material plan. The product's on-screen size, part thickness, spacing, relief, directional lighting, coherent shadows and label readability must survive rendering at actual viewport size. Avoid reducing an excellent illustration to illegible miniature detail inside unnecessary panel borders. Distinguish a generous editorial product stage from a dense diagnostic control surface. The intended experience mode decides which dominates.

Read `SCREENSHOT-DESIGN-REVIEW.md` for user-preference calibration and actual rendered QA. Preserve design-system consistency without forcing every section into the same card-and-grid composition.

## Design tokens and components
Define typography, spacing, radii, elevation, palette, breakpoints, motion durations and easings. Build reusable accessible buttons, inputs, cards, navigation and required stateful components. Customize primitives instead of shipping their defaults.

## Screens to inspect
- First viewport and critical journey.
- Empty, loading, success, validation and error states.
- Mobile around 375px, tablet around 768px, desktop around 1440px and intermediate widths.
- Keyboard navigation, focus visibility and screen-reader semantics.

Never use animation to hide weak layout or incomplete functionality. Be inspired by references without cloning copyrighted work.

## Charlie v2 — visual and behavioral craft
- Invent a product-specific visual metaphor and useful primary interaction before creating repeated sections or generic interface cards. Read `PRODUCT-INTERACTION-STRATEGY.md`.
- Make object material, physical construction, proportions, reflections, matte finish and geometric characteristics influence the actual visual system when supported by evidence.
- Review small details just as closely as hero composition: press and hover, focus and active states, meaningful empty/error states, origin-aware floating surfaces and immediate repeated controls.
- Prefer a consistent brand/type hierarchy and believable lighting over decorative gradients, indiscriminate glass effects and repeated fade-up animations.
- A decorative object can be visually elaborate; an operable object must have semantic controls, accessible alternatives and understandable instructions.
- Review with `DESIGN-ENGINEERING-CRAFT.md` before signoff. If artistic direction is ambiguous, experiment with genuinely different concepts using `PROTOTYPE-AND-LEARNING.md`.
