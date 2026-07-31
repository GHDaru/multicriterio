# Plan 004 — SAW/WSM e SMART

- **Spec**: [spec.md](spec.md) · **Raia**: Plena · **Data**: 2026-07-31

## Constitution Check (constituição v1.0.0)

| Princípio | Conformidade |
|---|---|
| I. Evidência | ✅ Worked examples (rating e ROC) em teste; validação cruzada com pymcdm; Fishburn verificada por registro DOI antes de citar |
| II. Método ↔ implementação ↔ fonte | ✅ A dívida da fundação (SAW no produto sem capítulo) é quitada; docstrings citam Fishburn/Hwang & Yoon/Edwards & Barron |
| III. Pedagogia | ✅ Esqueleto v3; caso âncora; a virada de ranking é o worked example central; WPM fica como part-task practice |
| IV. Livro vivo | ✅ Edição 0.4; nota de curadoria sobre a natureza da fonte (carta ao editor) |
| V. Segurança | ✅ Nenhuma credencial tocada |
| VI. Neutralidade | ✅ Premissas e limites da forma aditiva declarados; aponta outranking/MAUT quando elas caem |
| VII. Spec-driven | ✅ Branch `004-saw`; merge --no-ff na main publica |

**Sem violações.**

## Como

1. Etapa herda os motores da 03 e adiciona só `saw.py` (o diff é a lição: uma linha).
2. Números do capítulo gerados pelo motor e conferidos contra pymcdm ANTES da prosa.
3. Produto: sobrescrita de pesos no corpo do ranking (revalidação via `Problema`).

## Verificação (DoD)

| Check | Comando | Esperado |
|---|---|---|
| Etapa 04 | `cd decisor-zero/etapas/04-saw && python -m pytest tests/ -q` | 7 passed (nenhum skip: pymcdm instalada) |
| Produto | `cd app/backend && python -m pytest tests/ -q` | 16 passed |
| Regressão | pytest etapas 01–03 | inalterado |
| Livro | `mkdocs build --strict` | exit 0 |
| Fontes do corpo | conferência contra `bibliografia.md` | só ✓ |
