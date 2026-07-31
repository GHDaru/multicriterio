# Spec 004 — SAW/WSM e SMART (cap. 04 + etapa 04)

- **Status**: Aprovada (defaults) · **Raia**: Plena · **Data**: 2026-07-31
- **Origem**: sequência didática do SUMARIO (Parte II) — "proxima rodada" do Steward.

## O quê e por quê

Entregar o capítulo 04 (agregação aditiva: fórmula, premissas, sensibilidade a pesos,
processo SMART) com a etapa `04-saw`, pagando a dívida da fundação: o motor SAW existe
no produto desde a spec 001 e ainda não tinha capítulo (Princípio II exigia esta rodada).

Dor real observada: rankings aditivos circulam como se fossem "objetivos"; o worked
example prova que, em corrida apertada, o vencedor pertence ao vetor de pesos.

## Requisitos funcionais

- **FR1** — Capítulo 04 no esqueleto v3; só fontes ✓ no corpo (Fishburn 1967 promovida
  a ✓ por verificação de registro DOI).
- **FR2** — Etapa `04-saw`: motor aditivo puro + rota `POST /api/matriz/saw` + página
  com os dois vetores de pesos; worked examples (rating e ROC) em teste.
- **FR3** — Validação cruzada: escores da etapa batem com `pymcdm.methods.WSM`
  (min-max) em teste automatizado; pymcdm entra em `decisor-zero/requirements.txt`.
- **FR4** — Produto: `POST /api/decisoes/{id}/ranking` aceita sobrescrita de pesos no
  corpo (revalidada), com teste da virada de vencedor.
- **FR5** — Registro vivo: bibliografia (✓ + nota "Letter to the Editor"), SUMARIO
  (04 ✅), nav, mapa do decisor-zero, HISTORICO (edição 0.4), CHANGELOG.

## Fora de escopo (YAGNI)

WPM (vira exercício do leitor); AHP (cap. 05); análise de sensibilidade sistemática
(cap. 11); UI de comparação de vetores no produto.

## Critérios de aceite (DoD)

- [ ] `pytest` verde na etapa 04 (incl. validação pymcdm) e no produto; regressão 01–03
- [ ] `mkdocs build --strict` verde com o cap. 04 na nav
- [ ] Nenhuma fonte "?" citada no corpo do cap. 04
- [ ] Gate humano do Steward no merge

## Clarify (resolvido — defaults, 2026-07-31)

- *Normalização do SAW?* → min-max fixa (é a que resolve direção; cap. 03).
- *pymcdm como dependência?* → sim, só no decisor-zero (validação cruzada é evidência
  do Princípio I; o produto continua sem numpy).
- *Pesos ROC no endpoint do caso âncora?* → sem arredondamento (arredondar quebra Σw=1).
