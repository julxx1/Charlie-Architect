#!/usr/bin/env python3
"""Validate instruction pack structure; does not test a web app."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    "CLAUDE.md", "README.md", "docs/DESIGN-SYSTEM.md",
    "docs/IMAGE-TO-EXPERIENCE.md", "docs/MOTION-SYSTEM.md",
    "docs/ENGINEERING.md", "docs/QUALITY-GATES.md",
    ".claude/skills/premium-design/SKILL.md",
    ".claude/skills/motion-system/SKILL.md",
    ".claude/skills/fullstack-build/SKILL.md",
    ".claude/skills/quality-audit/SKILL.md",
    "prompts/START-PROJECT.md", "prompts/IMAGE-REFERENCE-TEST.md",
    "prompts/REVIEW-PROJECT.md",
]
missing = [p for p in required if not (root / p).is_file()]
for path in required:
    print(("MISSING" if path in missing else "OK     ") + " " + path)
if missing:
    raise SystemExit(1)
print("Instruction pack structure: PASS")
