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
