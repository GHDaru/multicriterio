# Plan 003 — Normalização e pesos

- **Spec**: [spec.md](spec.md) · **Raia**: Plena · **Data**: 2026-07-30

## Constitution Check (constituição v1.0.0)

| Princípio | Conformidade |
|---|---|
| I. Evidência | ✅ Tabelas do capítulo geradas pelo motor antes da prosa; Edwards & Barron (1994) verificada por registro (Semantic Scholar/DOI) antes de citar |
| II. Método ↔ implementação ↔ fonte | ✅ Cada função de `pesos.py`/`normalizacao.py` cita a fonte no docstring; capítulo publica só o que a etapa testa |
| III. Pedagogia | ✅ Esqueleto v3; caso âncora; worked example antes do exercício (soma linear fica para o leitor) |
| IV. Livro vivo | ✅ Edição 0.3 no HISTORICO; nota de curadoria datada na bibliografia |
| V. Segurança | ✅ Nenhuma credencial tocada |
| VI. Neutralidade | ✅ O capítulo declara vieses de cada técnica (ROC exagera o topo; entropia mede discriminação, não importância; min-max sensível a extremos) |
| VII. Spec-driven | ✅ Branch `003-normalizacao-pesos`; merge --no-ff na main publica |

**Sem violações.**

## Como

1. Motor primeiro, números depois, prosa por último: `normalizacao.py` + `pesos.py`
   na etapa; rodar o motor para gerar as tabelas; escrever o capítulo com elas.
2. Etapa herda `matriz.py` da etapa 02 (com a correção do peso negativo).
3. Produto ganha `motor/pesos.py` + rota stateless `POST /api/pesos` (entropia recebe o
   problema no corpo; não exige decisão salva).
4. Registro vivo no mesmo PR.

## Verificação (DoD)

| Check | Comando | Esperado |
|---|---|---|
| Etapa 03 | `cd decisor-zero/etapas/03-normalizacao-pesos && python -m pytest tests/ -q` | 20 passed |
| Produto | `cd app/backend && python -m pytest tests/ -q` | 14 passed |
| Regressão | pytest nas etapas 01 e 02 | inalterado |
| Livro | `mkdocs build --strict` | exit 0 |
| Fontes do corpo | conferência contra `bibliografia.md` | só ✓ |
