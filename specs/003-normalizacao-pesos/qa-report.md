# QA Report 003 — Normalização e pesos

- **Data**: 2026-07-30 · **Raia**: Plena · **Veredito**: ✅ CONFORME (pendente só o gate humano)

## Checks da DoD ("prove, não declare")

| Check | Comando | Esperado | Resultado |
|---|---|---|---|
| Etapa 03 | `cd decisor-zero/etapas/03-normalizacao-pesos && python -m pytest tests/ -q` | 20 passed | ✅ `20 passed, 1 warning in 0.37s` |
| Produto | `cd app/backend && python -m pytest tests/ -q` | 14 passed | ✅ `14 passed, 1 warning in 0.64s` |
| Regressão etapa 01 | pytest | inalterada | ✅ `11 passed, 1 skipped` |
| Regressão etapa 02 | pytest | inalterada | ✅ `8 passed` |
| Livro | `mkdocs build --strict` | exit 0 | ✅ `Documentation built in 0.67 seconds` |
| Fontes do corpo do cap. 03 | conferência contra `bibliografia.md` | só ✓ | ✅ Hwang & Yoon ✓, Krishnan 2022 ✓, Edwards & Barron 1994 ✓ (promovida nesta rodada), Belton & Stewart ✓ |

Nota metodológica: todas as tabelas numéricas do cap. 03 foram geradas executando o
motor da etapa **antes** da escrita da prosa (fluxo do GUIA-EDITORIAL §5), e são
reproduzidas por `test_normalizacao.py` e `test_pesos.py`.

## Cobertura dos requisitos

| FR | Evidência |
|---|---|
| FR1 | `livro/capitulos/03-normalizacao-pesos.md`; promoção ✓ registrada na nota de curadoria |
| FR2 | `decisor-zero/etapas/03-normalizacao-pesos/` — 20 testes acima |
| FR3 | `app/backend/decisor/motor/pesos.py` + `tests/test_pesos.py` (4 testes) |
| FR4 | SUMARIO (03 ✅), nav, HISTORICO (edição 0.3 + snapshot), CHANGELOG, mapa do decisor-zero |

## Pendência de gate

Merge `--no-ff` na `main` publica (Pages já habilitado pelo Steward). Aprovação
indelegável do Steward.
