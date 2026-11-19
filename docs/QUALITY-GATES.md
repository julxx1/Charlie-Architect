# Release checklist — evidence over claims

## Design
- [ ] Distinctive, coherent and product-specific art direction
- [ ] Consistent typography, spacing, semantics and visual states
- [ ] Intentional mobile/tablet/desktop layouts
- [ ] No false claims, fake logos, placeholder experience or generic filler

## Motion
- [ ] Animation serves user comprehension, feedback or storytelling
- [ ] No focus theft, scroll hijack, blocked content or major motion jank
- [ ] Reduced-motion and touch alternatives work
- [ ] Animation contexts cleaned up, 3D fallback if relevant

## Functionality and trust
- [ ] Real primary journey works or demos are plainly labeled
- [ ] Interactive controls have valid actions, feedback and error handling
- [ ] Authentication and authorization tested where applicable
- [ ] Input, secret and data protection reviewed

## Accessibility and performance
- [ ] Keyboard, focus, labels and semantics checked
- [ ] Target WCAG 2.2 AA; don't claim conformance without evidence
- [ ] Inspect loading, layout shift, responsive behavior and runtime errors
- [ ] Measure representative device performance when tools available

## Delivery
- [ ] Actual install/build/typecheck/lint/test results noted
- [ ] Setup/deployment documented
- [ ] Remaining issues and mitigation identified

Report PASS / FAIL / NOT TESTED with evidence, not fabricated scores or screenshots.

## Charlie v2 — evidence-based craft review
- [ ] A concrete, product-dependent signature interaction is present, or a simpler informational site has been justified
- [ ] Hero, supporting narrative and CTA are grounded in the actual product's geometry, usage and buyer goals
- [ ] Custom illustration is correctly labeled and cannot be confused with verified product photography
- [ ] Interactive illustrations are accessible and do not hide operable elements behind `aria-hidden`
- [ ] Keyboard, touch, mouse and reduced-motion paths work for essential features
- [ ] Motion is appropriate to interaction frequency and each effect has an explicit purpose
- [ ] Entrance/exit sequencing does not create waits; repeated actions can interrupt animations cleanly
- [ ] Animations avoid unnecessary layout work, redundant effects and always-on rAF
- [ ] Non-trivial geometry, input mappings, scoring and state changes have automated tests where feasible
- [ ] Stress cases cover realistic long, missing, localized, empty and interrupted inputs
- [ ] Report distinguishes code inspection, build/test output, visual browser review and real-device performance
- [ ] Any unsupported measurements are labeled NOT TESTED, never converted to fabricated numeric scores

Consult `DESIGN-ENGINEERING-CRAFT.md` and `MOTION-CRAFT-CHECKLIST.md` before approving a release.

## Charlie v3 — intended experience and creative acceptance
- [ ] Experience type is explicitly identified from the user's actual goal before work (editorial / commerce / demo / utility / portfolio)
- [ ] Image-led premium briefs did not silently turn into diagnostics, dashboard cards or utilitarian specifications
- [ ] Product is visually dominant and its materials, lighting, geometry and content drive a bespoke art direction
- [ ] Hero communicates a memorable product idea and meaningful interaction, not generic marketing copy or a last-event status badge alone
- [ ] At least a few distinct meaningful chapters advance the narrative; layout, contrast, type or pace vary for a reason
- [ ] Intro, scroll and interaction motion have different jobs; signature movement is not limited to a single rigid whole-object fade
- [ ] The chosen primary action matches the user's goal and is not merely the easiest feature to implement
- [ ] Aesthetic/editorial quality is reviewed separately from code completeness and automated tests
- [ ] User-declared preferred reference is used as an explicit taste-calibration benchmark without copying product-specific layouts
- [ ] Desktop, mobile and key interactive states are visually inspected when runtime tools exist; otherwise mark NOT TESTED
Read `docs/EXPERIENCE-MODE-SELECTION.md` and `docs/EDITORIAL-ART-DIRECTION.md` before creative signoff.
