# QA Report 004 — SAW/WSM e SMART

- **Data**: 2026-07-31 · **Raia**: Plena · **Veredito**: ✅ CONFORME (pendente só o gate humano)

## Checks da DoD ("prove, não declare")

| Check | Comando | Esperado | Resultado |
|---|---|---|---|
| Etapa 04 | `cd decisor-zero/etapas/04-saw && python -m pytest tests/ -q` | 7 passed, sem skip | ✅ `7 passed, 1 warning in 1.34s` (pymcdm instalada — validação cruzada executou) |
| Produto | `cd app/backend && python -m pytest tests/ -q` | 16 passed | ✅ `16 passed, 1 warning in 0.66s` |
| Regressão etapas 01–03 | pytest | inalterado | ✅ `11+1s / 8 / 20` |
| Livro | `mkdocs build --strict` | exit 0 | ✅ `Documentation built in 0.79 seconds` |
| Fontes do corpo do cap. 04 | conferência contra `bibliografia.md` | só ✓ | ✅ Fishburn 1967 ✓ (promovida nesta rodada), Hwang & Yoon ✓, Edwards & Barron ✓, Belton & Stewart ✓ |

Notas:
- A validação cruzada compara nossos escores com `pymcdm.methods.WSM` (min-max) nos
  dois vetores de pesos; concordância a 1e-6 em todos os 8 escores.
- Incidente de rodada: arredondar os pesos ROC a 6 casas no endpoint quebrou Σw=1 e um
  teste falhou (422); corrigido devolvendo os valores sem arredondar — o comentário no
  código registra a lição.

## Cobertura dos requisitos

| FR | Evidência |
|---|---|
| FR1 | `livro/capitulos/04-saw.md` (selo 2026-07, revisão 2026-07-31) |
| FR2 | `decisor-zero/etapas/04-saw/` — testes acima |
| FR3 | `test_validacao_cruzada_com_pymcdm`; `pymcdm>=1.4` em `decisor-zero/requirements.txt` |
| FR4 | `RankingIn` em `decisor/main.py` + 2 testes novos em `tests/test_api.py` |
| FR5 | Bibliografia (✓ + nota), SUMARIO (04 ✅), nav, mapa, HISTORICO 0.4, CHANGELOG |

## Pendência de gate

Merge `--no-ff` na `main` publica. Aprovação indelegável do Steward.
