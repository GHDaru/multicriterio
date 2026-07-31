# QA Report 006 — TOPSIS

- 2026-07-31 · Plena · **✅ CONFORME** (gate a posteriori, ADR 0006)

| Check | Resultado |
|---|---|
| Etapa 06 pytest | ✅ `5 passed` (C_i do capítulo, concordância com SAW, pymcdm 1e-6, ideal→C=1, sem pesos→erro) |
| Produto pytest | ✅ `18 passed` (ranking topsis + catálogo com 2 métodos) |
| mkdocs --strict | ✅ (build da rodada) |
| Fontes do corpo | ✅ Hwang & Yoon ✓, Krishnan ✓; García-Cascales & Lamata mantida "?" e citada só no "Quando usar" com remissão — promover antes do cap. 11 |

Nota: a rota da etapa não tem teste de API próprio (o motor e a rota equivalente do
produto estão testados) — decisão de enxugamento da long run (ADR 0006 §2).
