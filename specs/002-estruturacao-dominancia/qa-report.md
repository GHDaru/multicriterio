# QA Report 002 — Estruturação e dominância

- **Data**: 2026-07-30 · **Raia**: Plena · **Veredito**: ✅ CONFORME (pendente só o gate humano)

## Checks da DoD ("prove, não declare")

| Check | Comando | Esperado | Resultado |
|---|---|---|---|
| Etapa 02 | `cd decisor-zero/etapas/02-dominancia && python -m pytest tests/ -q` | verde, sem skip | ✅ `8 passed, 1 warning in 0.70s` |
| Produto | `cd app/backend && python -m pytest tests/ -q` | 10 passed | ✅ `10 passed, 1 warning in 1.02s` |
| Regressão etapa 01 | `cd decisor-zero/etapas/01-matriz && python -m pytest tests/ -q` | inalterada | ✅ `11 passed, 1 skipped` |
| Livro | `mkdocs build --strict` | exit 0 | ✅ `Documentation built in 0.94 seconds` |
| Fontes do corpo do cap. 02 | conferência manual contra `bibliografia.md` | só ✓ | ✅ Keeney 1992 ✓ (promovido nesta rodada), Keeney & Raiffa 1976 ✓, Belton & Stewart 2002 ✓, Hwang & Yoon 1981 ✓ |

Notas: o `1 skipped` permanece **apenas na etapa 01** (é o enunciado do exercício do
leitor); na etapa 02 o gabarito virou teste real (`test_peso_negativo_agora_e_erro_de_modelagem`).
Roy (1996) continua "?" e por isso **não** é citado no corpo do cap. 02.

## Cobertura dos requisitos

| FR | Evidência |
|---|---|
| FR1 | `livro/capitulos/02-estruturacao-dominancia.md` (esqueleto v3, selo 2026-07) |
| FR2 | `decisor-zero/etapas/02-dominancia/` — testes acima |
| FR3 | `test_peso_negativo_agora_e_erro_de_modelagem` (pesos somando 1 com negativos) |
| FR4 | `app/backend/decisor/motor/dominancia.py` + `tests/test_dominancia.py` |
| FR5 | SUMARIO (02 ✅), HISTORICO (edição 0.2 + placar 🟢 ADR 0001→0005), CHANGELOG, nav |

## Pendência de gate

Merge `--no-ff` na `main` publica (Pages já ativo por workflow; falta o humano habilitar
Settings → Pages → Source: GitHub Actions na primeira vez). Aprovação indelegável do
Steward.
