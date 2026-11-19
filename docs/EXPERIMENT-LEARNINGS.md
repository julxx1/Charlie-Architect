# Charlie Architect — Generalized insights from a product-image experiment

This public note is intentionally anonymized: the compared websites are held in private repositories. It does not copy their source code or publish private links.

## What the source comparison showed
- Both websites used TypeScript and Vite with CSS and native browser animation rather than loading GSAP or Three.js. A distinctive result is possible without animation dependencies.
- One version foregrounded a physical interaction aligned with the product, a substantial three-pose scroll story, a restrained palette, fast key feedback and carefully shaped lighting/typography. The user preferred this result.
- The other version retained valuable engineering patterns: automated geometric key-layout tests, a physical keyboard tester with an activation state, mouse-event diagnostics and clear OS/browser limitations.
- Visual polish and automated test coverage are separate quality dimensions. The preferred version did not include the baseline's automated key-layout tests.
- The photograph was a limited-resolution reference. Both sites described their generated keyboards as illustrations and avoided inventing many product specifications.
- The source alone cannot prove which improvement was caused by the third-party skill, and cannot establish live FPS, Lighthouse or real-device smoothness.

## What Charlie takes forward
1. The signature user action should come from the product itself.
2. Tiny interaction details deserve an explicit craft review.
3. Choreograph key interactions and editorial movement differently.
4. Select animation tools by necessity rather than prestige.
5. Do not make an operable illustration inaccessible.
6. Add model/geometry/state tests for custom interactive simulations.
7. Maintain a release report based on actual executed checks.
8. Preserve project-specific user corrections separately from global rules.

### Attribution
This synthesis was also informed by design-engineering ideas published in Emil Kowalski's open-source collection: https://github.com/emilkowalski/skills (MIT license). Charlie Architect is a separate, vendor-neutral system.
