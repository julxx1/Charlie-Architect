# Charlie Architect — universal product image test

Voy a proporcionarte una imagen de un producto. Construye una experiencia web completa, original y de calidad premium usando la imagen como base de dirección artística. No quiero una landing genérica ni una maqueta de botones falsos.

Lee AGENTS.md, docs/design/IMAGE-TO-EXPERIENCE.md, docs/design/DESIGN-SYSTEM.md, docs/motion/MOTION-SYSTEM.md, docs/engineering/ENGINEERING.md y docs/quality/QUALITY-GATES.md. Aplica los estándares equivalentes de diseño, motion, desarrollo y auditoría según las capacidades de tu entorno. En Claude Code puedes usar los skills especializados si están disponibles.

**Imagen adjunta o ruta:** [ADJUNTAR IMAGEN O RUTA]
**Producto (opcional):** [NOMBRE]
**Acción principal:** [EXPLORAR / COTIZAR / RESERVAR / COMPRAR MEDIANTE INTEGRACIÓN REAL / OTRA]

## Charlie v4 — visual benchmark required
Before coding, read `docs/design/VISUAL-FIDELITY-STANDARD.md` and `docs/quality/SCREENSHOT-DESIGN-REVIEW.md`. Treat the *actual rendered appearance* of the product as a release criterion. Make the object large enough to be admired, with visibly dimensional construction, material-specific directional highlights, depth and contact shadows where justified. Technical accuracy is insufficient if details become tiny, flat or unreadable.

Build an editorial product canvas when the brief asks for a cinematic showcase; do not shrink the object into a generic diagnostics panel. Contrast, typography, crop, spacing and composition must support the product.

After coding, compare screenshots at desktop and mobile, inspect material depth and fine-print legibility, identify and correct the top three visual gaps. If you cannot run a browser, state that visual quality was NOT VERIFIED. Keep the functionality and tests. For an explicit visual comparison request, use `prompts/VISUAL-CALIBRATION-REVIEW.md`.

## Protocolo obligatorio
1. Mira la imagen de verdad. Extrae forma, material, color, iluminación y detalles. Separa lo visible de especulaciones. Si no puedes abrirla, pídela; no finjas analizarla.
2. Explica brevemente una dirección creativa específica: concepto, fuentes, paleta, composición, estructura narrativa y un hero memorable.
3. Diseña 5–8 beats de motion graphics con disparador, técnica, duración y alternativa mobile/reduced-motion.
4. Implementa el proyecto funcional inmediatamente después del plan. No te quedes en concepto, wireframe o pseudocódigo.
5. Selecciona tecnologías con criterio: GSAP/ScrollTrigger para coreografías, Motion para estados, CSS para lo simple, Three.js/WebGL solo si los assets justifican su uso. No incluyas librerías inactivas.
6. Evita gradientes cliché, glassmorphism arbitrario, hero genérico centrado, tres tarjetas repetidas, textos vacíos y fade-ins idénticos.
7. Revisa y corrige escritorio, móvil, teclado, touch, rendimiento y reduced-motion. Usa navegador/capturas si están disponibles.
8. Ejecuta tests/build/lint disponibles y reporta PASS / FAIL / NOT TESTED con pruebas. No asegures 60 FPS o WCAG AA sin medirlo.

**Objetivo:** experiencia distintiva de estudio creativo profesional. USD 10.000 es una aspiración de calidad, nunca una valoración garantizada.

**Entrega:** sitio operativo, breve racional artístico, animaciones realmente implementadas, comandos de ejecución, checks reales y limitaciones conocidas. Procede con supuestos sensatos cuando falten datos no esenciales.

## Charlie v2 — specialist craft review
Read `docs/strategy/PRODUCT-INTERACTION-STRATEGY.md`, `docs/design/DESIGN-ENGINEERING-CRAFT.md`, and `docs/motion/MOTION-CRAFT-CHECKLIST.md` before choosing the visual concept.

Design one **product-specific signature interaction** rather than copying another project's demo. Build an excellent functioning primary action with a clear link from the hero. Coordinate expressive narrative motion with immediate, physically convincing feedback on everyday controls. Explain what each animation accomplishes and what should stay still.

For illustrated products, label illustrative details and implement accessible keyboard and touch equivalents. Add model/geometry/input tests where there is custom behavior. After implementation, audit source code and any live viewport available, distinguishing what was actually verified from anything not tested.

## Charlie v3 — preserve editorial intent
For a product photo + premium high-motion web brief, select **editorial product experience** by default, unless the user explicitly asks for commerce, testing or a repeatable utility. Read `docs/strategy/EXPERIENCE-MODE-SELECTION.md` and `docs/design/EDITORIAL-ART-DIRECTION.md` before design.

Make the actual product the visual protagonist. Use purposeful chapter-to-chapter contrast, memorable typography and lighting, a product-relevant signature interaction, and distinct storytelling moments. Do not replace an experiential landing page with hardware diagnostics or a dashboard merely because those features are easy to test.

Before coding, show a compact creative thesis, story arc and first-viewport composition. Reject a generic or utility-first solution at the Creative Director review. After building, verify that the delivered experience is editorially compelling as well as functional, with screenshots/browsers where available. Keep test coverage, safety and accessible behavior from technically stronger alternatives.
