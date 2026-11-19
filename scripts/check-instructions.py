#!/usr/bin/env python3
"""Validate Charlie Architect's cross-agent instruction pack; does not test a web app."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    "AGENTS.md", "README.md", "CLAUDE.md", "GEMINI.md",
    "docs/README.md", "prompts/README.md",
    "docs/design/DESIGN-ENGINEERING-CRAFT.md", "docs/strategy/PRODUCT-INTERACTION-STRATEGY.md",
    "docs/motion/MOTION-CRAFT-CHECKLIST.md", "docs/strategy/PROTOTYPE-AND-LEARNING.md",
    "docs/research/EXPERIMENT-LEARNINGS.md",
    "docs/design/VISUAL-FIDELITY-STANDARD.md", "docs/quality/SCREENSHOT-DESIGN-REVIEW.md",
    "prompts/VISUAL-CALIBRATION-REVIEW.md",
    ".claude/skills/visual-fidelity/SKILL.md",
    "docs/strategy/EXPERIENCE-MODE-SELECTION.md",
    "docs/design/EDITORIAL-ART-DIRECTION.md",
    ".cursor/rules/charlie-architect.mdc", ".github/copilot-instructions.md",
    "integrations/README.md", "prompts/UNIVERSAL-START.md",
    "docs/design/DESIGN-SYSTEM.md", "docs/design/IMAGE-TO-EXPERIENCE.md",
    "docs/motion/MOTION-SYSTEM.md", "docs/engineering/ENGINEERING.md", "docs/quality/QUALITY-GATES.md",
    ".claude/skills/premium-design/SKILL.md",
    ".claude/skills/motion-system/SKILL.md",
    ".claude/skills/fullstack-build/SKILL.md",
    ".claude/skills/quality-audit/SKILL.md",
    "prompts/IMAGE-REFERENCE-TEST.md",
    "prompts/REVIEW-PROJECT.md",
]
missing = [p for p in required if not (root / p).is_file()]
for path in required:
    print(("MISSING" if path in missing else "OK     ") + " " + path)

# Validate Markdown navigation and explicitly referenced root-relative docs.
# External links and anchors are intentionally excluded.
import re
from urllib.parse import unquote

sources = [
    root / "README.md", root / "AGENTS.md", root / "CLAUDE.md",
    root / "GEMINI.md", root / "integrations/README.md",
    root / ".github/copilot-instructions.md",
    *sorted((root / "docs").rglob("*.md")),
    *sorted((root / "prompts").rglob("*.md")),
    *sorted((root / ".claude/skills").rglob("*.md")),
]
broken_links = []
for source in sources:
    if not source.is_file():
        continue
    body = source.read_text(encoding="utf-8")
    for link in re.findall(r"\]\(([^)]+)\)", body):
        if link.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        target = unquote(link.split("#", 1)[0])
        if target and not (source.parent / target).exists():
            broken_links.append((source.relative_to(root), link))
    for ref in re.findall(r"(?<![\w/])docs/[A-Za-z0-9_/-]+\.md", body):
        if not (root / ref).is_file():
            broken_links.append((source.relative_to(root), ref))

for source, target in broken_links:
    print(f"BROKEN  {source}: {target}")

if missing or broken_links:
    raise SystemExit(1)
print("Charlie Architect structure and documentation links: PASS")
