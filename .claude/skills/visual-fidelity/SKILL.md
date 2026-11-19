---
name: visual-fidelity
description: Review and improve actual perceived visual quality of product websites, especially object scale, material realism, 3D depth, contact shadows, keycap/component detail, legibility, typography, density and visual hierarchy. Use when the UI looks flatter or smaller than a preferred reference, or when a code-correct page lacks premium polish.
---

# Charlie Architect — Visual Fidelity

1. Read `AGENTS.md`, `docs/design/VISUAL-FIDELITY-STANDARD.md` and `docs/quality/SCREENSHOT-DESIGN-REVIEW.md`.
2. Inspect the real product image, the current implementation and any user-preferred screenshot. Do not assume two screenshots show equivalent sections.
3. List the three highest-impact visible differences. Describe each in perceptual terms and connect it to a code/design change.
4. Inspect primary subject scale and framing, material layers, key/part geometry, shadows, legibility, contrast and editorial hierarchy. A correct SVG with illegible details is not visually correct.
5. Edit the implementation and keep the real functionality, responsive layouts, reduced motion, focus and keyboard/touch access intact.
6. Capture comparable rendered views if browser access exists; iterate until major differences are addressed.
7. Report PASS/FAIL/NOT VERIFIED separately for browser aesthetics and code/build checks. Never invent screenshots, FPS or scores.
