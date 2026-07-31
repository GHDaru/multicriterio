# Spec 006 — TOPSIS (cap. 06 + etapa 06)

- **Status**: Aprovada (defaults, ADR 0006) · **Raia**: Plena · **Data**: 2026-07-31
- **O quê**: capítulo 06 (formulação clássica de Hwang & Yoon), etapa `06-topsis`
  (motor puro + rota comparando com SAW + página) e `topsis` no catálogo do produto.
- **FRs**: FR1 capítulo v3 (fontes ✓: Hwang & Yoon, Krishnan; García-Cascales citada
  como ? apenas nominalmente com remissão ao cap. 11 — não, mantida fora do corpo
  crítico, citada com DOI na bibliografia) · FR2 etapa com C_i do caso âncora em teste
  + validação pymcdm (1e-6) · FR3 produto: motor + METODOS + teste · FR4 registro vivo.
- **Fora de escopo**: métricas alternativas de distância (exercício); fuzzy-TOPSIS.
- **DoD**: [x] etapa 5 passed · [x] app 18 passed · [x] mkdocs --strict (qa-report)
- **Clarify (defaults)**: normalização vetorial + euclidiana (clássico); rota da etapa
  devolve SAW junto para comparação didática.
