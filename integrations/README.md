# AI integrations and portability

Charlie Architect's canonical guidelines live in `AGENTS.md`, with detailed shared manuals in `docs/`.

| Environment | Adapter | How to use |
| --- | --- | --- |
| Generic coding AI / other agents | `AGENTS.md` + `prompts/UNIVERSAL-START.md` | Explicitly ask the agent to read the files; where files aren't supported, paste their content |
| OpenAI Codex-compatible project agents | `AGENTS.md` | Place in the project root and confirm the chosen agent recognizes it |
| Claude Code | `CLAUDE.md` + optional `.claude/skills/` | Open Claude in the project and confirm it loaded `AGENTS.md` |
| Cursor | `.cursor/rules/charlie-architect.mdc` | Copy into the project and enable project rules |
| GitHub Copilot repository instructions | `.github/copilot-instructions.md` | Use in supported Copilot coding workflows |
| Gemini CLI | `GEMINI.md` | Run from project and check that the context file is recognized |

Not every model/product automatically reads these files. Supported config formats can change. Explicit file loading and test prompts are the portable fallback.

These adapters do not grant the model access to unavailable tools, browser, image inputs, shell commands, or external accounts. They are instructions, not plugins or model weights.
