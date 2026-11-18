---
name: motion-system
description: Design and implement cinematic, usable web motion including scroll storytelling, GSAP, typography reveals and microinteractions where appropriate.
---

# Motion System

For a product reference image, produce a concrete 5–8 beat motion storyboard tied to the page. Implement feasible signature sequences and report which beats actually shipped.

1. Read docs/MOTION-SYSTEM.md and inspect current UI and dependencies.
2. Define three motion adjectives and an inventory: what moves, why, trigger, duration, easing, fallback.
3. Choose CSS for simple motion, Motion for React for layout/state, GSAP ScrollTrigger for coordinated scroll, WebGL only when justified.
4. Implement entry, hover, feedback and narrative transitions without hiding content when JS fails.
5. Add reduced-motion, touch, keyboard and low-performance fallbacks.
6. Clean up listeners and animation contexts; inspect layout thrash, scroll problems and obscured content.
7. Document what was built and actually verified.
