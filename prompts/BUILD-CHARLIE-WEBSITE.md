# Charlie Architect — Build the Official Website

## 0. Assignment

You are Charlie Architect, working through the AI coding environment the user has chosen (Claude Code for this run). Read `AGENTS.md` in full and follow the relevant `docs/` guidance, especially:

- `docs/EXPERIENCE-MODE-SELECTION.md`
- `docs/EDITORIAL-ART-DIRECTION.md`
- `docs/VISUAL-FIDELITY-STANDARD.md`
- `docs/SCREENSHOT-DESIGN-REVIEW.md`
- `docs/DESIGN-SYSTEM.md`
- `docs/MOTION-SYSTEM.md`
- `docs/DESIGN-ENGINEERING-CRAFT.md`
- `docs/MOTION-CRAFT-CHECKLIST.md`
- `docs/ENGINEERING.md`
- `docs/QUALITY-GATES.md`

**Build Charlie Architect's own official website**, not a website about generic AI services and not a mockup. Work in a standalone `website/` directory inside this repository. Preserve `AGENTS.md`, `docs/`, the other `prompts/`, and existing adapters/skills. Do not publish, deploy, create external repositories, overwrite config, or commit without the user's direction.

The target is a distinctive, high-craft, professional web presence with meaningful motion and working interactions. The price of a project, awards and measured performance are not design claims; never assert them without independent evidence.

## 1. What Charlie Architect actually is

Charlie Architect is a **vendor-neutral creative engineering instruction system**: a reusable repository containing a canonical agent protocol, design/motion/engineering/QA standards, and tool-specific adapters for Claude Code, Cursor, GitHub Copilot and Gemini CLI; AGENTS.md is also useful to other compatible coding assistants.

It guides a capable AI through six professional lenses:
1. Creative Director
2. Senior UX/UI & Product Designer
3. Motion Graphics Specialist / Creative Developer
4. Software Architect
5. Senior Full-Stack Engineer
6. QA, Accessibility & Performance Lead

**Do not portray Charlie as a standalone trained AI model, a running multi-agent service, an autonomous cloud product, a paid SaaS, or a verified team of humans.** The six roles are review lenses and workflows applied by the selected AI. The site should explain this clearly and confidently.

Primary audience: creative developers, independent makers, teams and technical founders who want more distinctive, usable, functional, well-crafted web products from their coding AI.

Primary conversion: **Visit the real GitHub repository / copy installation instructions / begin with a prompt**. Verified canonical URL: `https://github.com/julxx1/Charlie-Architect`.

Secondary conversion: inspect principles, example workflows, docs and supported tool setups. Avoid dead CTAs or fake signup/login/waitlist.

## 2. Core creative concept

Working concept: **“An idea needs architecture.”**

Visual metaphor: a living, precision-built **creative instrument / drawing table** that turns raw intent into a structured interactive interface. Combine the restraint of an editorial design studio with the exactness of engineering diagrams. Charlie's public-facing site should itself be proof of its design standards.

- Beautiful contemporary typography with a clear, ownable typographic wordmark treatment for CHARLIE / ARCHITECT.
- Restrained material palette: off-white / warm technical grey / carbon-black with **one** controlled signal accent, chosen for hierarchy and interaction (not blanket bright gradients).
- Fine drafting lines, measured grid, precise annotations, and carefully placed typographic labels may support the concept, but **never drown it in blueprint clichés, generic glowing orbs, meaningless AI particle swarms, bento/card walls or glassmorphism**.
- A strong asymmetric hero composition with an unmistakable interactive visual. Do not use a generic centered headline + gradient + three cards layout.
- High-quality negative space, variation in page density, large editorial type, deliberate transitions between light and dark scenes, and physically believable details.

Treat the concept above as an art-direction brief, not a rigid layout template. If a demonstrably more distinctive direction emerges from the product, adapt it while retaining the goal.

## 3. Signature interactive centerpiece — The Workbench

Create a **genuine interactive client-side demonstrator** of Charlie's creative decision-making process. It should look like a carefully designed instrument, not a dull control panel.

Consider a central sketch-to-interface transformation:
- A visitor can select among **Editorial Showcase**, **Interactive Demo**, and **Utility**.
- The visualization **really recomposes** to match each selection (different typographic scales, layout density, motion personality and information hierarchy), rather than simply changing an accent color.
- Include a short, specific explanation of the design decision for each mode, with accessible button/tab controls and immediate functional response.
- Make each mode visually compelling and clearly different, while retaining a common design language.
- The visualization is an **interactive illustration of Charlie's standards**, not a live AI generation engine. Label it transparently, e.g. “Interactive methodology demo — no AI call”.
- Do not require accounts, keys, server inference, or external services to make this work.

If a better signature interaction is possible with the available tooling, build it and explain why it communicates Charlie's actual value more effectively. The experience must be meaningful without animation.

## 4. Information architecture (adapt intelligently, do not force filler)

**Hero — The proposition.** Make a striking first viewport with the logo/wordmark, a short sharp idea, precise support copy, primary GitHub CTA and a visual composition visitors can engage with.

**Workbench — See the decision system.** The interactive concept above: distinct experience modes, genuinely changing layouts and rationale.

**Six disciplines, one coherent system.** Explain the six professional lenses as an integrated methodology. Avoid six identical generic icon cards. Use an intentional typographic or diagrammatic composition with readable descriptions. Do not suggest separate running AI agents.

**The process — From brief to release.** Show what really happens: understand → art-direct → choreograph → build → inspect → audit. An orchestrated scroll sequence is appropriate if accessible, performance-conscious and genuinely informative.

**Motion & craft.** Show a small number of working interaction details or animation principles, such as tactile feedback and visual transition timing. Demonstrate how motion reinforces an action, not “animation everywhere”.

**Getting started.** Include the verified repository link and an actually working copy button for the clone command:
`git clone https://github.com/julxx1/Charlie-Architect.git`
Explain that the user opens the project in a compatible AI coding environment and asks it to read `AGENTS.md`. Include links to `prompts/UNIVERSAL-START.md`, `prompts/IMAGE-REFERENCE-TEST.md`, and adapter docs. Clearly state that the files do not magically install themselves across every assistant and that tool capabilities differ.

**Footer.** Repository link, MIT license / open source if supported by the repository, clean navigation and brief factual positioning.

Do **not** invent testimonials, usage statistics, client logos, award badges, product launches, pricing or public examples. Do not embed content or screenshots from private projects in a public website without explicit authorization.

## 5. Motion art direction

Design a motion score with **one or two meaningful signature moments**, plus restrained fast supporting interactions:
- Editorial type reveals using line masks where useful.
- Architectural layers, lines or geometry that transform into an interface, if this helps explain the Workbench.
- Scroll-driven changes with clear narrative stages and purposeful stillness; no scroll hijacking.
- Precise press, focus, mode-switch and copy-button feedback.
- Section transitions with controlled tonal contrast and motion rhythm.
- If building pointer-reactive visuals, use them only for fine pointers and avoid annoying persistent movement.

Prefer CSS and browser APIs for simple effects. Add GSAP/Motion only when it materially simplifies multi-stage choreography. WebGL is optional and should not be used as a prestige dependency.

All functional controls respond immediately. Respect `prefers-reduced-motion`, keyboard, touch, no-JS visibility where appropriate and lower-performance devices. Animation must never obscure the CTA or block reading.

## 6. Implementation standards

- Use a suitable modern stack; choose based on required functionality. A lightweight Vite + TypeScript setup is entirely acceptable; React is only necessary if complexity warrants it.
- Self-contained `website/` with a clear README and scripts for development, testing and production build.
- Responsive architecture designed for phone, tablet and desktop rather than just scaling down desktop.
- Real accessible navigation, focus states, interactions and action feedback.
- Good typography, semantic HTML, SEO and social metadata, optimized assets and fonts, graceful empty/error behavior where relevant.
- Avoid external image dependencies if not necessary. Use authored SVG/CSS visuals for the architectural metaphor, documenting what is illustrative.
- No invented backend, fabricated AI computation, fake buttons or hidden network dependencies.
- Add meaningful tests for interaction-state logic if appropriate, and run typecheck/build. Include a smoke-test checklist.

## 7. Creative and technical QA — mandatory

Before shipping, inspect **actual rendered output** when browser capabilities exist. Use `docs/SCREENSHOT-DESIGN-REVIEW.md`:
- Desktop first viewport and all major section compositions.
- Mobile first viewport, navigation, Workbench controls and layout.
- Workbench mode transitions and reduced-motion.
- Real primary CTA, clipboard copy behavior, keyboard navigation and visible focus.
- Main interactive illustration at **actual rendered scale**: clear proportions, material depth, shadows if relevant, readable detail, no tiny graphics buried in chrome.
- Three highest-impact visual gaps: name them, implement the corrections, recapture and review.
- Run relevant automated checks, distinguish PASS / FAIL / NOT TESTED. No invented Lighthouse, accessibility compliance, FPS or screenshots.

## 8. Deliverables

1. Functional `website/` source and project README.
2. Art-direction thesis, page outline and why the signature interaction is appropriate.
3. Working responsive design with implemented motion and controls.
4. Instructions for local `dev`, build, test and preview.
5. Precise report: created/changed files, implemented effects, tests actually run, browser review actually performed, unresolved issues.

**Execution instruction:** Do not stop after presenting the plan. Build the page, run all checks available in your environment and correct the most meaningful defects. Do not modify the existing Charlie Architect instruction system unless strictly necessary for integration, and explain any such proposed change first.
