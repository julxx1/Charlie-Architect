# Image to premium product experience — reference-image protocol

## Step 0 — Ground the concept in the actual reference image
- Inspect attached image(s) or accessible workspace files, not just their filenames.
- Build a visual evidence sheet: product category, geometry, texture/material, dominant/accent colors, details, lighting, photo angle, context and unknowns. Separate observations from creative hypotheses.
- Identify three unmistakable features that will shape the art direction. Preserve proportions and identity.
- When one image exists, do not claim other angles or unknown specifications are authentic. Crop, mask or composite carefully; label illustrative imagery.

## Creative deliverables — brief, then build
1. One-sentence creative thesis tailored to the product and customer.
2. Specific visual system: palette derived from image, 1–2 fonts with rationale, composition, lighting and shadow rules.
3. Distinctive product-led hero, beyond a centered heading.
4. Narrative sequence of 4–7 meaningful sections and deliberate transitions.
5. Storyboard of 5–8 motion beats; each has element, trigger, effect, timing/easing, technique, user benefit and mobile/reduced-motion fallback.
6. Explain what makes the experience unmistakably about this particular product and not an interchangeable template.

## Motion techniques worth evaluating
- Product silhouette reveal using a clip mask or lighting pass.
- Layered scenes and restrained depth parallax.
- Scroll-linked scale, focus and detail callouts.
- Oversized kinetic typography tied to product geometry.
- Section transitions sharing color or shape.
- Precise cursor/hover feedback on fine pointers.
- Optional 3D only when suitable real assets exist.

## Implementation safeguards
- Design mobile composition intentionally rather than shrinking desktop.
- Make navigation, CTAs, anchors, routes, focus and menus functional.
- No invented checkout, pricing, stock, testimonials, product claims or fake specs; clearly label demo functionality.
- Use licensed/authorized imagery and document provenance.
- Ensure important content is visible without JS and never delayed behind scroll animations.
- Profile complex effects, avoid excess main-thread work, support reduced motion and static fallbacks.

## Acceptance criteria
- The actual supplied product is recognizable.
- Art direction derives from the image, not a generic theme.
- At least one distinctive motion effect is implemented where permitted.
- Motion works in a real browser, not only in a storyboard.
- The experience remains usable on touch, reduced motion and slow network.
- Primary action is genuine and meaningful.
- Run applicable build/tests and browser checks; report what was actually verified.

## Mandatory interaction hypothesis
Identify one or more *product-dependent interactions* before settling the layout. Evaluate the ideas on product relevance, visitor value, implementability, honesty about unverified details, and accessibility. Choose one signature action and make the CTA lead to it. Read `PRODUCT-INTERACTION-STRATEGY.md`.

Storyboards are a design tool, not an instruction to force animations. For each candidate beat document the leader, supporting elements, deliberate stillness, interruption behavior, and touch/keyboard/reduced-motion variants. Build the strongest feasible beats, not necessarily every candidate.

If depicting the object via SVG/CSS, add an explicit illustration/provenance notice. When interactive, do not mark the entire object `aria-hidden` unless a proper functional accessible alternative is provided. Validate the picture-based data model with tests if the UI simulates geometry, parts or inputs.

### Final review
Check actual screenshots/viewport output when available. Compare type, image scale, visual composition, shadows, color and responsive behavior; distinguish real checks from source-only assumptions.
