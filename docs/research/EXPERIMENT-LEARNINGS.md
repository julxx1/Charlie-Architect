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

## Follow-up evaluation: user preference clarified
A later source-code comparison verified that the user's new favorite repository had exactly the same Git tree as the previously preferred product-showcase version. The latest Charlie-generated alternative used modular model/render/pose code, a comprehensive physical keyboard/mouse tester and automated Vitest suites. **The user's stronger preference was for the editorial, tactile product showcase, not the diagnostics-first concept.**

The important regression was **experience-type selection**, not inadequate animation libraries. The latest implementation had a modern hero and a pose-based scroll section, but much of its design weight and copy was dedicated to a technical test suite. It reduced separate product-exploration chapters and playful direct interaction. The preferred version used key-by-key entrance choreography, a long-form spatial study, a lively spring pointer response, discrete product chapters and a real typing challenge. These are source-backed design differences, not measured browser or FPS claims.

The technically newer site still contributed valuable aspects: independently testable geometry, coverage model, pose windows, and explicit diagnostics. Retain those methods. Its global key capture with broad `preventDefault()` when armed should be reviewed for focused-field/shortcut safety; claims to detect specific hardware failures should be softened because browser input can only observe received events.

**Generalizable decision:** distinguish the requested emotional experience (editorial product storytelling) from a repeatable tool (diagnostics) *before* coding. A beautiful, correct utility is still the wrong deliverable when the brief requests a cinematic product website. See `docs/strategy/EXPERIENCE-MODE-SELECTION.md` and `docs/design/EDITORIAL-ART-DIRECTION.md`. This lesson is about creative fidelity, not cloning the private source.
