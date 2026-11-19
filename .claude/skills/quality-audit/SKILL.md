---
name: quality-audit
description: Inspect product against premium design, interaction, accessibility, security and production-readiness quality gates.
---

# Quality Audit

1. Read docs/QUALITY-GATES.md and inspect code and feature scope.
2. Run real supported checks (test, lint, typecheck, build, browser review).
3. Review mobile, keyboard, reduced motion, security, performance and main user journey.
4. Fix high-impact defects without regressions.
5. Give PASS / FAIL / NOT TESTED table with evidence. Never invent Lighthouse scores or test runs.
6. Prioritize remaining issues by severity and effort.

7. Start with the **experience-mode match**: did the user ask for editorial storytelling, commercial conversion, a demonstration or utility? Read `docs/EXPERIENCE-MODE-SELECTION.md`.
8. For editorial sites inspect product prominence, non-repetitive chapters, clear visual contrast progression, credible materials, bespoke typography and motion personality using `docs/EDITORIAL-ART-DIRECTION.md`.
9. Preserve technical test coverage but reject the mistaken substitution of diagnostics for a requested cinematic showcase. Separate qualitative visual judgement from measured tests.
