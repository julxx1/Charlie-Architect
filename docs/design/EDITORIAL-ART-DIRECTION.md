# Charlie Architect — Editorial art direction, visual rhythm and motion personality

## The real differentiator

An attractive site is not the same as a memorable product experience. Premium visual work requires a *connected direction*: typography, object, light, scale, composition, language and animation feel like parts of one idea.

## Visual presence and tactile realism — Charlie v4

The user-preferred product presentation in a screenshot comparison featured a large object, readable legends, sculpted individual parts, meaningful spacing and deep but restrained material shadows. The less successful presentation placed a smaller, flatter and harder-to-read product model inside a dense UI panel. Use this as a *quality lesson*, never as a reusable keyboard layout.

For editorial showcases, allocate a generous visual stage to the object. Deliberately design physical layers (case, caps, edges), material-specific highlights, key shadows and contact shadow. Check actual display scale. A detailed miniature is not automatically premium; a technically accurate model can fail as visual design.

Apply `docs/design/VISUAL-FIDELITY-STANDARD.md` and `docs/quality/SCREENSHOT-DESIGN-REVIEW.md`. A code review without comparable screenshots cannot verify the perceived result.

## First-screen art direction

- Make the real product (or explicitly illustrative reconstruction) visually dominant when the brief is product-led.
- Choose a composition with intentional weight, occlusion, cropping and negative space, not an interchangeable column of copy plus a centered image.
- Connect headline language to the product's **actual behavior**; short active verbs may be more memorable than a generic benefit sentence.
- Use a deliberate relationship between title and object: direction, edge alignment, perspective, scale or visual tension.
- Avoid excessive decorative badges, colored dots, utility readouts and extra UI when they weaken the visual premise.
- Above-the-fold interactivity should be discoverable and satisfying, not merely a hidden event listener or data label.

## Material, depth and studio lighting

- Study the reference material: matte or reflective, hard or soft, dense or light, industrial or organic.
- Build geometry and lighting from those observations. Realistic pressure/depth may require layers, keycap shadows, physical edges, texture or a restrained light sweep.
- A physically modeled object can make a minimal stack feel expensive. Do not mistake more dependencies for more realism.
- If creating an SVG/CSS interpretation, preserve the recognizable silhouette and disclose unverified views/specs.

## Signature motions vs supporting effects

A site should have a **motion personality**:
- A product can reveal itself through meaningful sub-parts rather than one whole-object fade or slide when the sub-parts matter.
- Pointer-reactive motion can lend liveliness to a suitable visual hero, but should settle smoothly, stay subtle, and disable on coarse pointer/reduced motion.
- Scroll-linked transformations should have narratively distinct poses, carefully chosen holds and transitions, and a clear visual end state.
- Separate **storytelling motion** (rare, expressive) from **daily control motion** (fast, almost invisible).
- Don't assign a fixed number of effects; compose a coherent sequence and remove anything that steals attention from the key moment.

## Page-wide visual rhythm

- Sketch all major section compositions before writing them. Check for repetition in layout, background, type scale and visual weight.
- Use intentional tonal shifts (including possible light-to-dark transitions) to mark narrative phases, not a constant repeated gradient.
- Let each section have one primary subject and varied density: full-bleed object, typographic interlude, interactive detail, visual evidence, meaningful action.
- Editorial composition and reliable real controls can coexist without transforming the entire page into dashboard panels.
- The end-to-end experience should feel art-directed, not simply component-driven.

## Taste calibration from real user preferences

If a user identifies one implementation as distinctly better:
1. Treat the preference as a **calibration signal**, not universal evidence that every feature of that implementation is superior.
2. Extract transferable design reasons: visual contrast, narrative richness, tactile feedback, typography hierarchy, object scale, animation sequencing, exploratory affordances.
3. Identify engineering qualities of the alternative worth preserving, including modularity, tests, and security.
4. Design a *third solution* that carries the strengths of both; do not copy the preferred site's composition, text, or interactions onto unrelated products.
5. Evaluate the output against a side-by-side screenshot review when browsers are available; do not claim visual superiority from source code alone.

## Evidence-driven visual QA

Capture if possible:
- First viewport (desktop and mobile)
- Every major narrative transition/section
- Mid-scroll poses
- Functional interaction before/during/after
- Reduced motion and keyboard focus
- At least one narrow-width layout with long text

Record comparison as **Preferred quality / Current output / Gap / Concrete implementation fix / Actual verification**.

### Design-director final veto

Fail visual QA if the site is accurate but reads as a utility when the user asked for an editorial showcase; its hero is interchangeable; lighting and composition have no identifiable art direction; its story does not progress; or its only memorable motion is an introductory fade. Explain the gap precisely and revise it, not by layering arbitrary effects.
