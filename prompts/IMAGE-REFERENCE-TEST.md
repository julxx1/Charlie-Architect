# Charlie Architect — universal product image test

Voy a proporcionarte una imagen de un producto. Construye una experiencia web completa, original y de calidad premium usando la imagen como base de dirección artística. No quiero una landing genérica ni una maqueta de botones falsos.

Lee AGENTS.md, docs/IMAGE-TO-EXPERIENCE.md, docs/DESIGN-SYSTEM.md, docs/MOTION-SYSTEM.md, docs/ENGINEERING.md y docs/QUALITY-GATES.md. Aplica los estándares equivalentes de diseño, motion, desarrollo y auditoría según las capacidades de tu entorno. En Claude Code puedes usar los skills especializados si están disponibles.

**Imagen adjunta o ruta:** [ADJUNTAR IMAGEN O RUTA]
**Producto (opcional):** [NOMBRE]
**Acción principal:** [EXPLORAR / COTIZAR / RESERVAR / COMPRAR MEDIANTE INTEGRACIÓN REAL / OTRA]

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
Read `docs/PRODUCT-INTERACTION-STRATEGY.md`, `docs/DESIGN-ENGINEERING-CRAFT.md`, and `docs/MOTION-CRAFT-CHECKLIST.md` before choosing the visual concept.

Design one **product-specific signature interaction** rather than copying another project's demo. Build an excellent functioning primary action with a clear link from the hero. Coordinate expressive narrative motion with immediate, physically convincing feedback on everyday controls. Explain what each animation accomplishes and what should stay still.

For illustrated products, label illustrative details and implement accessible keyboard and touch equivalents. Add model/geometry/input tests where there is custom behavior. After implementation, audit source code and any live viewport available, distinguishing what was actually verified from anything not tested.
