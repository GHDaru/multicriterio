# Spec 010 — VIKOR e BWM (cap. 10 + etapa 10)

- **Status**: Aprovada (defaults, ADR 0006) · **Raia**: Plena · **Data**: 2026-07-31
- **O quê**: capítulo 10 (S/R/Q, condições de aceitação, conjunto de compromisso; BWM
  com modelo linear), etapa `10-vikor-bwm`, `vikor` no catálogo do produto.
- **FRs**: FR1 capítulo v3 (fontes ✓ Opricovic & Tzeng, Rezaei) · FR2 VIKOR do caso
  âncora em teste + pymcdm 1e-6 + conjunto de compromisso {A1, A4} · FR3 BWM: caso
  consistente em forma exata (ξ=0) e inconsistente (ξ>0) em teste; scipy nos
  requirements da trilha · FR4 produto vikor + teste · FR5 registro vivo.
- **Decisões da rodada**: BWM só na trilha (produto sem scipy — /api/pesos inalterado);
  escore do vikor no produto = Q com ordenação crescente, documentado no catálogo.
- **DoD**: [x] etapa 6 passed · [x] app 20 passed · [x] mkdocs --strict.
