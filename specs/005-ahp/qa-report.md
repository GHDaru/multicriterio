# QA Report 005 — AHP

- **Data**: 2026-07-31 · **Raia**: Plena · **Veredito**: ✅ CONFORME (gate a posteriori, ADR 0006)

| Check | Resultado |
|---|---|
| Etapa 05 pytest | ✅ `8 passed` (worked example, contraexemplo cíclico CR=0,4488, caso CR=0, recíproco inválido, SAW+AHP) |
| Produto pytest | ✅ `17 passed` (inclui `ahp` consistente e recusa de CR alto) |
| mkdocs --strict | ✅ `Documentation built in 0.50 seconds` |
| Fontes do corpo | ✅ Saaty 1977 ✓, Saaty 1980 ✓, Belton & Gear ✓, Dyer ✓ (promovidas nesta corrida) |

Regressão completa das etapas anteriores: adiada para a varredura final da long run
(decisão 5 do ADR 0006).
