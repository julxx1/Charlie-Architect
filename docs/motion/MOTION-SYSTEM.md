# Creative motion and interaction system

## Purpose
Motion supports hierarchy, orientation, feedback and narrative. Define a consistent vocabulary across all sections and views.

## Techniques (select, do not blindly stack)
- GSAP ScrollTrigger or scroll-driven timelines for product storytelling.
- Kinetic typography: word/line reveals, precise stagger, clipping and readable fallback.
- Restrained depth/parallax, not motion-sickness effects.
- Shared-element or View Transitions when useful.
- Magnetic buttons and cursor interactions only on fine pointers, with touch/keyboard alternatives.
- Spring-style microinteractions and tactile feedback.
- Rive/Lottie where relevant, with no essential information animation-dependent.
- Three.js/WebGL/shaders only when real visual value warrants the performance budget and a fallback exists.

## Technical constraints
- Prefer transforms and opacity; avoid forced synchronous reflow.
- In React scope effects and clean up GSAP contexts, observers and listeners.
- Respect prefers-reduced-motion, no-JS visibility and keyboard control.
- CSS for simple states; Motion for React for state/layout; GSAP for timelines; WebGL only for real scenes.
- Lenis is optional; preserve native anchor/navigation/focus behavior, never scroll hijack.
- Keep critical headings and CTA visible promptly.
- Scale back heavy effects on mobile, battery-constrained and coarse-pointer devices; measure actual performance.

## Indicative timings, adaptable
- Button feedback: 120–180ms
- UI changes: 180–320ms
- Section reveals: 450–750ms
- Route transitions: around 250–550ms
- Elegant easing example: cubic-bezier(.22, 1, .36, 1)
- Stagger: usually no more than 80ms per item.

## Review
Check narrow screens, touch, keyboard, browser back, route navigation, reduced motion and slow hardware. Never let transitions obscure vital content or trap user input.

## Charlie v2 — motion judgment
The first decision is **whether anything should move**. A high-frequency keyboard action is not a marketing reveal. Use expressive motion primarily for rare narrative moments, and keep working controls immediately responsive.

- Match tactile response to the physical metaphor: press feels fast, release settles smoothly; real movement originates where the user interacted.
- Avoid doubling the entrance animation on both parent and children. Coordinate related effects as one gesture with overlap rather than a queue.
- Prefer CSS transitions/keyframes, WAAPI and scoped rAF when sufficient; libraries are tools, not evidence of quality.
- Ensure gestures can reverse mid-motion. Limit hover-only tracking to fine pointers.
- Avoid `transition: all`, heavy layout effects per scroll frame, and unnecessary global animation loops.
- Treat `clip-path`, blur and complex shadows as potential paint costs; benchmark rather than assume GPU acceleration.
- Provide comprehensible static/discrete reduced-motion variants; critical content cannot remain hidden.
- Use `MOTION-CRAFT-CHECKLIST.md` to specify the effect's purpose, timing, leader, support, interruption, fallbacks and actual test evidence.
