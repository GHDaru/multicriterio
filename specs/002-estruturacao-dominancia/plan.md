# Plan 002 — Estruturação e dominância

- **Spec**: [spec.md](spec.md) · **Raia**: Plena · **Data**: 2026-07-30

## Constitution Check (constituição v1.0.0)

| Princípio | Conformidade |
|---|---|
| I. Evidência | ✅ Worked example do cap. 02 (A5 dominado) é teste; Keeney 1992 verificado por acesso direto (archive.org) antes de citar |
| II. Método ↔ implementação ↔ fonte | ✅ `dominancia.py` cita a definição e a fonte no docstring; capítulo só publica o que a etapa testa |
| III. Pedagogia | ✅ Esqueleto v3; caso âncora estendido com A5 (worked example antes do exercício); o gabarito do exercício do cap. 01 entra como diff-lição |
| IV. Livro vivo | ✅ Edição 0.2 no HISTORICO; previsão do ADR 0001 marcada 🟢 no placar |
| V. Segurança | ✅ Nenhuma credencial tocada nesta rodada |
| VI. Neutralidade | ✅ O capítulo diz explicitamente o que a dominância NÃO decide (alternativas em conflito) |
| VII. Spec-driven | ✅ Branch `002-estruturacao-dominancia`; merge --no-ff na main publica |

**Sem violações.**

## Como

1. Etapa 02 = etapa 01 + (a) correção do peso negativo em `matriz.py`, (b)
   `motor/dominancia.py` puro (`domina`, `analise_dominancia` → dominadas com seus
   dominadores + fronteira de Pareto), (c) endpoint `/api/matriz/dominancia`, (d) página
   com o candidato A5.
2. Capítulo 02: value-focused thinking (Keeney 1992) → propriedades de uma boa família
   de critérios (Keeney & Raiffa) → dominância/Pareto com o worked example A5.
3. Produto: mesmo motor puro copiado para `app/backend/decisor/motor/dominancia.py` +
   rota + teste (etapas são congeladas; o produto tem a sua cópia — padrão do projeto).
4. Registro vivo (SUMARIO, HISTORICO, CHANGELOG, nav).

## Verificação (DoD)

| Check | Comando | Esperado |
|---|---|---|
| Etapa 02 | `cd decisor-zero/etapas/02-dominancia && python -m pytest tests/ -q` | tudo verde, sem skip (o exercício virou teste real) |
| Produto | `cd app/backend && python -m pytest tests/ -q` | 10 passed |
| Livro | `mkdocs build --strict` | exit 0 |
| Fontes do corpo | citações do cap. 02 conferidas contra `bibliografia.md` | só ✓ |
