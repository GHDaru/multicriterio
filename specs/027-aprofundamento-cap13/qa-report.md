# QA 027 — cap. 13 + VARREDURA FINAL da corrida de aprofundamento (ADR 0007)

- 2026-07-31 · Plena · **✅ CONFORME** (gate humano a posteriori sobre a corrida)

## Varredura final (todas as etapas + produto + livro)

| Etapa | Testes |
|---|---|
| 00 `2` · 01 `12+1s` · 02 `9` · 03 `21` · 04 `8` · 05 `9` · 06 `6` · 07 `6` · 08 `6` · 09 `6` · 10 `7` · 11 `7` · 12 `7` · 13 `4` | **110 passed, 1 skipped** |
| Produto | ✅ `22 passed` |
| Livro | ✅ `mkdocs build --strict` exit 0 |

## Balanço da corrida (specs 014–027)

- 14 capítulos aprofundados com a fórmula do ADR 0007: segundo domínio (fornecedor de
  nuvem) worked com números do motor em teste + Apêndice B (gabarito comentado).
- +16 testes novos nas etapas (94 → 110); fio narrativo novo: decisão frágil
  (apartamento) × decisão robusta (fornecedor), quantificado no cap. 11.
- Fontes promovidas: Ishizaka & Nemery ✓, Roy 1996 ✓ (abertura da corrida).
- Placar: linha "caps. 05–13 aguardam aprofundamento" fechada 🟢.

## Pendência de gate

Revisão humana a posteriori do conjunto (ADR 0007). Dívidas remanescentes: UI de
curvas (mavt), grupo no produto, raia infra (migrações/contas/deploy),
Triantaphyllou "?".
