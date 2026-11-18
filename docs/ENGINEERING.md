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
