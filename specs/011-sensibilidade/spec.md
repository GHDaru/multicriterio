# Spec 011 — Sensibilidade, robustez e rank reversal (cap. 11 + etapa 11)

- **Status**: Aprovada (defaults, ADR 0006) · **Raia**: Plena · **Data**: 2026-07-31
- **O quê**: capítulo 11 (varredura de peso, concordância entre métodos, ensaio de
  rank reversal, protocolo de robustez), etapa `11-sensibilidade`, e
  `POST /api/decisoes/{id}/comparar` no produto.
- **FRs**: FR1 capítulo v3 (fontes ✓: Belton & Stewart, Wątróbski, Nguyen,
  García-Cascales & Lamata — promovida nesta rodada, Belton & Gear) · FR2 faixas
  [0; 0,316; 0,358] e ρ=1 entre os 4 métodos em teste · FR3 rank reversal real no
  TOPSIS (A4↔A3) e no SAW (vencedor troca) com A5 de último lugar, em teste ·
  FR4 produto comparar + teste · FR5 registro vivo.
- **Incidente registrado**: a hipótese inicial "SAW sobrevive ao A5" caiu no teste —
  o vencedor troca; o achado (mais forte) foi incorporado ao capítulo. Também: a
  função `teste_rank_reversal` colidia com a coleta do pytest → renomeada
  `ensaio_rank_reversal`.
- **DoD**: [x] etapa 5 passed · [x] app 21 passed · [x] mkdocs --strict.
