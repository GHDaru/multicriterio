# QA Report 007 — MAVT e Even Swaps

- 2026-07-31 · Plena · **✅ CONFORME** (gate a posteriori, ADR 0006)

| Check | Resultado |
|---|---|
| Etapa 07 pytest | ✅ `5 passed` (linear≡SAW a 1e-6; pódio curvo A1>A2>A4>A3; interpolação/bordas; monotonia; função faltante) |
| mkdocs --strict | ✅ (build da rodada) |
| Fontes do corpo | ✅ Keeney & Raiffa ✓, Hammond/Keeney/Raiffa HBR ✓, Belton & Stewart ✓; MACBETH segue "?" e aparece só no Apêndice A com URL institucional |

Decisão da rodada: produto não ganha `mavt` (exige UI de curvas — follow-up).
