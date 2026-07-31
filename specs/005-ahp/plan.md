# Plan 005 — AHP

- **Spec**: [spec.md](spec.md) · **Raia**: Plena · **Data**: 2026-07-31

## Constitution Check

| Princípio | Conformidade |
|---|---|
| I | ✅ Worked example + contraexemplo em teste; 4 fontes promovidas a ✓ por registro antes de citar |
| II | ✅ `ahp.py` cita Saaty 1977/1980 no docstring; produto só expõe com capítulo pronto |
| III | ✅ Esqueleto v3; página interativa é a learning task; média geométrica é o exercício |
| IV | ✅ Edição 0.5 no HISTORICO |
| V | ✅ Sem credenciais |
| VI | ✅ Debate crítico (rank reversal, Dyer) no corpo com fontes; posição do livro declarada e justificada em ADR |
| VII | ✅ Branch 005-ahp; gate humano a posteriori conforme ADR 0006 |

**Sem violações.**

## Verificação (DoD)

| Check | Esperado | Obtido |
|---|---|---|
| etapa 05 pytest | verde | 8 passed |
| app pytest | verde | 17 passed |
| mkdocs --strict | exit 0 | ok (ver qa-report) |
