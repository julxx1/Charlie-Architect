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
