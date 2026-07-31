# QA Report 013 — Persistência + VARREDURA FINAL da long run (ADR 0006)

- 2026-07-31 · Plena · **✅ CONFORME** (gate humano a posteriori sobre toda a corrida)

## Rodada 013

| Check | Resultado |
|---|---|
| Etapa 13 pytest | ✅ `3 passed` (sobrevivência ao reinício; listagem; adaptação da URL Neon) |
| Produto pytest | ✅ `22 passed` (inclui `/health`) |
| mkdocs --strict | ✅ |

## Varredura final (todas as etapas, decisão 5 do ADR 0006)

| Etapa | Resultado |
|---|---|
| 00 (smoke) | ✅ | 
| 01 | ✅ 11 passed, 1 skipped (exercício do leitor) |
| 02 | ✅ 8 · 03 ✅ 20 · 04 ✅ 7 · 05 ✅ 8 · 06 ✅ 5 · 07 ✅ 5 · 08 ✅ 5 · 09 ✅ 5 · 10 ✅ 6 · 11 ✅ 5 · 12 ✅ 6 · 13 ✅ 3 |
| **Total etapas** | **94 passed, 1 skipped** |
| Produto | ✅ 22 passed |
| Livro (`mkdocs build --strict`) | ✅ exit 0, 14 capítulos na nav |
| Segredos | ✅ só placeholders (`usuario:senha`, exemplo de teste) |

## Estado da obra ao fim da long run

14/14 capítulos publicados (Partes I–IV completas), cada um com etapa executável e
worked example em teste; validação cruzada com pymcdm em SAW, TOPSIS, PROMETHEE II e
VIKOR; produto com 4 métodos de ranking, 5 técnicas de pesos, dominância, comparação
multi-método e /health.

## Pendência de gate

Revisão humana a posteriori de toda a corrida (ADR 0006). Dívidas registradas no
placar de expiração: aprofundamento dos caps. 05–13; UI de curvas (mavt); grupo no
produto; migrações/contas/deploy (raia infra).
