# Engineering architecture & implementation

## Select stack deliberately
For interactive React products: Next.js + TypeScript + Tailwind CSS + truly customized components may be suitable. Use shadcn/ui only as an accessible primitive base. Choose Motion or GSAP based on motion needs. Use PostgreSQL + Prisma/Drizzle for appropriate persistent data, and established authentication where required. Other stacks are valid.

## Real functionality
Implement the primary flow end-to-end. Never claim mocked persistence is real. Clearly identify demos, stubs and external dependencies. Define data sources, validation, errors, transaction boundaries, roles and permissions.

## Security
- Store secrets in environment variables, never the client bundle or git.
- Server-side validation and authorization on each protected read and write.
- Safe queries, CSRF/XSS/CSP/session practices appropriate to the architecture.
- Rate-limit public endpoints and protect expensive operations.
- Collect only necessary user data and review dependency provenance and licenses.

## Performance
Set measurable per-project performance budgets and benchmark on representative devices. Optimize LCP images/fonts, lazy-load below-fold media, reduce unnecessary hydration/JavaScript, prevent CLS and inspect INP. Never invent Lighthouse results.

## Operations
Run typechecking, lint, and relevant unit/integration/E2E tests. Include safe env examples, setup, deployment and monitoring guidance. Avoid premature abstraction or complexity.

## Interactive simulations and native input
For CSS/SVG/Canvas product representations, model geometry and parts in coherent data structures rather than scattered DOM constants. Add tests for unique identifiers, bounds, accidental overlap, input mappings, scoring and state changes when relevant.

Listen to keyboard and mouse input only when the user expects it, not as covert global collection. Avoid logging sensitive text or accidentally hijacking browser shortcuts. Handle blur, cleanup and disabled states. Clearly explain what localStorage stores and what never leaves the device.

Build tools, UI frameworks and animation packages must be selected by real complexity and performance needs. The high-quality example with native CSS and rAF is evidence that a web project doesn't automatically need React, GSAP or WebGL.

A passing TypeScript build is not a substitute for testing the real browser, accessibility, physical touch and motion performance.
