# Charlie Architect — Screenshot-led Visual Design Review

## Purpose
Code inspection alone cannot prove a UI looks premium. Use screenshots and live interactions when the agent has browser access, especially when the user has supplied a preferred example.

## Capture protocol
1. Capture the same **type of scene** in each implementation, at the same viewport dimensions and comparable scroll/state. If only different sections are available, note the limitation.
2. Capture desktop (e.g. 1440px wide), mid-size/tablet (~768px), phone (~375px), plus the viewport supplied by the user if known.
3. Capture the hero, the dominant product illustration, the most complex controls, one motion mid-state and the most compressed/mobile section.
4. If animation is relevant, capture beginning, middle and settled frames or use a screen recording. A single static screenshot cannot establish timing or smoothness.
5. Check browser zoom at 100% for real readability; inspect zoom and high text scaling where feasible.

## Visual critique lenses
- **Hierarchy:** Where does the eye go first? Does it go to the intended subject or chrome?
- **Scale:** Is product detail legible at this viewport? Is the main illustration treated as a protagonist?
- **Material:** Does the object exhibit believable depth, contact shadows and appropriate highlights? Do parts look physically separated?
- **Typography:** Are display and body text coherent? Are technical legends appropriately sized?
- **Density:** Is every panel, legend, icon, border or metric necessary?
- **Composition:** Is alignment intentional? Are margins/padding visually balanced rather than mechanically equal?
- **Palette:** Are accent colors meaningful? Is visual noise controlled?
- **Narrative:** Do sections vary in composition and emphasis and progress the concept?
- **Responsive:** Does layout recompose intelligently? Is important material lost or shrunk beyond legibility?
- **Interaction:** Does physical feedback feel responsive without interfering with the core action?
- **Accessibility:** Are zoom, text contrast, keyboard focus, reduced-motion and alternatives functional?

## Report format
| Severity | Visual gap | Evidence | Concrete correction | Verified after change? |
| --- | --- | --- | --- | --- |
| Critical | Product too small for the intended scene | Screenshot at 1440px | Give object an open full-width stage and increase on-screen scale | Pass / Fail / Not tested |
| High | Flat product parts | Screenshot detail | Add case/keycap layers, directional highlights and contact shadows | Pass / Fail / Not tested |
| High | Tiny low-contrast legends | 100% screenshot | Change layout/component scale and contrast, not only font size | Pass / Fail / Not tested |

Sample findings above are examples, not claims about every project.

## Creative Director veto
For an editorial product experience, block signoff if:
- The main object is rendered as a small graphic inside a dense generic panel when it should dominate.
- A technically accurate vector model lacks the material cues visible in the reference.
- The design is legible only when enlarged beyond the intended viewport.
- Layouts repeat the same card-heavy pattern instead of showing a distinct editorial rhythm.
- Color accents dominate the product without a justified brand/function purpose.
- No screenshot review was done despite available browser tools.

When browser tools aren't available, explicitly mark visual outcomes as **NOT VERIFIED** and include a reproducible screenshot-capture checklist.

## Visual correction loop
Inspect → name exact perceptual problem → specify design-system/code modification → implement → capture again → compare. Do not fix a flat or undersized illustration by adding unrelated GSAP timelines or random gradients.
