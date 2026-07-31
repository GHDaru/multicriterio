# Spec 013 — Do protótipo ao produto (cap. 13 + etapa 13)

- **Status**: Aprovada (defaults, ADR 0006) · **Raia**: Plena (a parte de infra real —
  provisionar Neon — é ação do leitor/Steward, documentada; nenhum deploy foi feito
  pela sessão) · **Data**: 2026-07-31
- **O quê**: capítulo 13 (porta de persistência, Neon + fallback, credenciais,
  operação), etapa `13-persistencia` (RepositorioDecisoes + mini-app + /health),
  `GET /health` no produto. Fecha a trilha de 14 capítulos.
- **FRs**: FR1 capítulo v3 · FR2 etapa com prova de sobrevivência a "reinício" em
  teste (SQLite temporário; testes nunca tocam banco real) · FR3 produto /health +
  teste · FR4 registro vivo + varredura final da long run.
- **DoD**: [x] etapa 3 passed · [x] app 22 passed · [x] varredura completa (qa-report).
