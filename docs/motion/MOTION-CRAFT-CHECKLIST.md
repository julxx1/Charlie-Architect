# Charlie Architect — Motion Craft and Performance Checklist

## Mandatory spec for each significant effect
| Field | Requirement |
| --- | --- |
| Context | Component, scene and user journey |
| Purpose | Feedback / orientation / explanation / narrative |
| Trigger | On load, tap, click, scroll, pointer, focus, route; approximate frequency |
| Choreography | Lead, followers, parallel changes, deliberate stillness |
| Recipe | Properties, direction, origin, easing, duration, spring if useful |
| Interruptibility | How repeat/reverse/escape/cancel behaves |
| Fallback | Mobile, coarse pointer, keyboard, reduced-motion and no-JS behavior |
| Evidence | Actual runtime/device tested or explicitly NOT TESTED |

## Implementation decision tree
- Use CSS transitions for simple reversible states and precise press feedback.
- CSS keyframes work for predetermined once-only sequences; consider WAAPI for programmatic control.
- For continuous pointer/scroll effects use scoped requestAnimationFrame, passive events, a scheduled-frame guard and visibility gating. Stop loops when settled or offscreen.
- Use GSAP/Motion only when complex timelines, state relationships or gestures justify them. Use WebGL/Three.js only when content and assets justify real 3D.
- Prefer transform/opacity; clipping, filters and shadow effects can cost paint and must be benchmarked. Beware layout-bound `width`, `height`, `top` and `margin` effects.
- Avoid `transition: all` and indiscriminate `will-change`. Consider the cost of updating inherited CSS variables over large trees.
- Use existing duration/easing tokens and a motion vocabulary suited to the product. Fast tactile press is different from an editorial reveal.

## Review conditions
- The hero still delivers value when all motion is disabled.
- All controls are operable as soon as visible; stagger is not a blocking queue.
- Keyboard shortcuts and high-frequency actions are fast.
- A gesture can reverse without jumping or replaying a fixed keyframe sequence.
- Scroll animations do not hijack the viewport.
- Hover-only effects never block touch users.
- `prefers-reduced-motion` avoids excessive travel, and static/discrete alternatives are understandable.
- Runtime is responsive on mid-range devices; otherwise mark performance NOT TESTED.
- Test the scene in a browser; a successful build alone does not prove the effect looks smooth.

## Red flags
Continuous global rAF; hundreds of elements staggered; hidden content whose observer never fires; `aria-hidden` around working controls; uncancelled timers; page-size jumps; slow keyboard feedback; mouse-only core tasks; no mobile fallback.
