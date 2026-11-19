# Charlie Architect — Design Engineering Craft Standard

## Definition of craft
High-end work is more than beautiful CSS. It is a coherent combination of a distinctive product idea, precise interaction feedback, editorial layout, believable materials, functional behavior, accessibility and rigorous review.

## Eight gates before animating an interaction
1. **Relevance:** What product quality or user goal does this express?
2. **Frequency:** Is it a rare first-visit scene or a control repeated dozens of times?
3. **Purpose:** Does movement give feedback, indicate a new state, preserve spatial orientation, explain a feature or advance a story?
4. **Attention:** Does the animation delay the primary action, conceal information or create pointless waiting?
5. **Physics:** Does the visual response match the object or gesture? Does it originate in the right place?
6. **Efficiency:** Is CSS sufficient? Is JavaScript, a motion library or 3D really justified?
7. **Alternatives:** Is it usable with keyboard, touch, reduced motion and limited hardware?
8. **Proof:** Can it be verified in an actual browser, not just described in a spec?

If these gates do not justify movement, change state instantly. An animation quota is never a quality metric.

## Fine interaction details
- Functional key/button presses respond immediately; release may settle more gently. Do not sacrifice perceived responsiveness for showmanship.
- Prefer explicit transition properties; avoid `transition: all`.
- Contextual UI should enter from the position that explains its origin. Anchored popovers align to the trigger; dialogs remain centered.
- Avoid starting a UI reveal from zero scale. Use a modest offset/opacity only if entrance motion helps.
- Rapid toggles, swipes and reversals must be interruptible. Fixed keyframes are rarely right for frequently changed states.
- Skip or minimize animations on keyboard shortcuts, repetitive navigation and high-frequency actions.
- Limit hover-only treatment to devices with `hover: hover` and `pointer: fine`.
- Treat focus, disabled, empty, loading, error, live and success states as part of visual design.
- Prefer restrained light, real shadows, useful negative space and coherent typography over decorative card patterns.

## Choreography
For a multi-element event, identify the **lead**, **supporting** elements and items that remain **still**. Animate the container OR its children unless a meaningful causal story requires both. Parallel changes often feel faster and more connected than queues of delayed elements. Interaction must be available immediately, not after the motion completes.

## Review format
Record an issue as **Current behavior | Better behavior | User benefit | Verification**. Examine not only what to add but what to remove.

## Source acknowledgement
Charlie Architect uses original, summarized craft guidance inspired in part by public design-engineering lessons from Emil Kowalski. See https://github.com/emilkowalski/skills (MIT). His original skills are not bundled here.
