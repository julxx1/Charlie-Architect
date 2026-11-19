# Charlie Architect

**AI-agnostic creative engineering system** that turns a capable coding assistant into a coordinated professional digital product team: Creative Director, Senior UX/UI Designer, Motion Graphics Specialist, Software Architect, Full-Stack Engineer and QA/Accessibility Lead.

Charlie Architect is a reusable **set of instructions, professional standards and specialized workflows**, not a separate AI model, deployable app or automatic guarantee of a particular price or award.

## Compatible workflows

- **Any code-capable AI:** read `AGENTS.md` and start with `prompts/UNIVERSAL-START.md`
- **Claude Code:** `CLAUDE.md` and optional `.claude/skills/`
- **Cursor:** `.cursor/rules/charlie-architect.mdc`
- **GitHub Copilot:** `.github/copilot-instructions.md`
- **Gemini CLI:** `GEMINI.md`
- **Other tools:** copy `AGENTS.md` and relevant `docs/` into their custom-instruction/context mechanism

See `integrations/README.md` for precise setup and limitations. Instruction auto-loading depends on the tool and its version.

## Charlie v4 — perceived visual quality

An additional comparison of user-provided screenshots exposed a gap that purely technical QA missed: an intricate, tested product model can still look flat, undersized and visually weak when it is squeezed into a utility panel. The preferred design had generous product prominence, sculpted components, deep material shadows, legible details and clearer editorial hierarchy.

Charlie now requires **visual fidelity inspection**, not just architecture and motion quality:
- `docs/VISUAL-FIDELITY-STANDARD.md` — subject scale, realistic materials, readable details and composition
- `docs/SCREENSHOT-DESIGN-REVIEW.md` — screenshot-led comparative QA, correction loop and mobile checks
- `prompts/VISUAL-CALIBRATION-REVIEW.md` — universal prompt for improving perceived quality
- `.claude/skills/visual-fidelity/SKILL.md` — optional Claude Code adapter

**Important:** Source correctness and visual quality are separate release gates. Browser checks are required when accessible; otherwise report the visual check as NOT VERIFIED.

## Getting started

1. Clone this repository or copy the instruction files into your project root.
2. Open the project using your chosen AI coding tool.
3. Confirm that the assistant can read `AGENTS.md`. If it can't, paste it or attach it.
4. Use `prompts/UNIVERSAL-START.md` (or `prompts/IMAGE-REFERENCE-TEST.md` with a product image).
5. Ask for the creative concept, implementation, motion system and evidence-based audit.

## Six integrated professional lenses

| Role | Responsibility |
| --- | --- |
| Creative Director | Unique visual concept and art direction |
| UX/UI Product Designer | User journeys, responsive design and interface system |
| Motion Graphics Specialist | Cinematic motion, microinteractions and storytelling |
| Software Architect | Architecture, integrations, scalability and security |
| Senior Full-Stack Engineer | Functional product implementation |
| QA/Accessibility Lead | Real tests, accessibility and performance validation |

## Repository structure

- `AGENTS.md` — canonical **vendor-neutral** protocol
- `CLAUDE.md`, `GEMINI.md`, `.cursor/`, `.github/` — adapters
- `.claude/skills/` — Claude-specific optional skills
- `docs/` — common design, image-to-experience, motion, engineering and QA standards
- `prompts/` — universal start, product-image and QA prompts
- `integrations/README.md` — installation guidance for different AI tools
- `scripts/check-instructions.py` — basic presence validation

## Trust and limitations

Charlie Architect doesn't install animation libraries by itself. AI assistants need tool access to edit files, run tests or inspect reference images. The quality bar is an aspiration, not a guaranteed USD 10,000 valuation or a verified Awwwards award. Respect image licenses, security policies and reduced-motion accessibility. Never invent test results.

MIT license.

## Charlie v2 — design engineering craft

The original Charlie instructions focused on appearance, architecture and large-scale cinematic effects. Charlie v2 adds **interaction-level craft**: product-specific signature actions, refined tactile response, choreography that respects user attention, and explicit decisions about when *not* to animate.

New guidance:
- `docs/PRODUCT-INTERACTION-STRATEGY.md` — design from actual product behavior
- `docs/DESIGN-ENGINEERING-CRAFT.md` — detailed interaction and motion decision gates
- `docs/MOTION-CRAFT-CHECKLIST.md` — precise specifications and performance diagnostics
- `docs/PROTOTYPE-AND-LEARNING.md` — concept variants, design decisions and confirmed user preferences
- `docs/EXPERIMENT-LEARNINGS.md` — anonymized lessons from a reference-image comparison

This release was also informed by the independent [Emil Kowalski design engineering skills](https://github.com/emilkowalski/skills), which remain separate and are **not** embedded wholesale into Charlie. No third-party skill is required to run Charlie v2.

## Charlie v3 — creative fidelity after a controlled preference comparison

A follow-up comparison exposed a key failure: Charlie could interpret a request for a high-end editorial product website as a technically sound diagnostics tool. Both are useful, but they solve different problems.

**Charlie v3 chooses experience mode before designing.** A product image with a brief for a memorable non-generic web experience defaults to an editorial showcase, not an unsolicited tester or dashboard. It requires a stronger visual arc, memorable product prominence, original choreography, and post-build creative review **without sacrificing engineering reliability**.

- `docs/EXPERIENCE-MODE-SELECTION.md`: classify editorial / commerce / demo / utility / portfolio first.
- `docs/EDITORIAL-ART-DIRECTION.md`: creative direction, visual contrast, product narrative and motion character.

The comparison involved private user projects. The public repository contains **generalized design principles**, not private project links or third-party source code.
