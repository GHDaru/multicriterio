# Spec 002 — Estruturação de critérios e dominância (cap. 02 + etapa 02)

- **Status**: Aprovada (defaults) · **Raia**: Plena · **Data**: 2026-07-30
- **Origem**: sequência didática do SUMARIO (Parte I) — "Continuemos" do Steward; inclui
  a migração operacional para o repositório próprio (ADR 0005), determinada pelo Steward.

## O quê e por quê

Entregar o capítulo 02 do livro (estruturação: de valores a critérios; dominância e
fronteira de Pareto) com sua etapa executável `02-dominancia`, e expor a análise de
dominância no produto. É o último degrau antes de qualquer método: o que dá para
concluir **sem** pesos e **sem** agregação.

Dor real observada: decisores incluem critérios redundantes (peso contado duas vezes) e
gastam energia comparando alternativas que nenhuma preferência racional escolheria
(dominadas). O cap. 01 deixou a dor plantada: o validador da matriz ainda aceitava peso
negativo (exercício do leitor) — esta rodada aplica o gabarito, e o diff é a lição.

## Requisitos funcionais

- **FR1** — Capítulo 02 no esqueleto v3, citando apenas fontes ✓ no corpo (Keeney 1992
  promovido a ✓; Keeney & Raiffa 1976 ✓; Belton & Stewart 2002 ✓).
- **FR2** — Etapa `02-dominancia` autocontida: motor de dominância puro + API + página;
  o worked example do capítulo (candidato A5 dominado por A1) reproduzido em teste.
- **FR3** — A etapa 02 incorpora a correção do peso negativo (gabarito do exercício do
  cap. 01) com teste que a prova.
- **FR4** — Produto: `POST /api/decisoes/{id}/dominancia` com o mesmo motor puro e teste.
- **FR5** — Registro vivo: SUMARIO (cap. 02 ✅), HISTORICO (edição 0.2 + snapshot +
  placar: previsão do ADR 0001 cumprida 🟢), CHANGELOG, nav do mkdocs.

## Fora de escopo (YAGNI)

Normalização e pesos (cap. 03); elicitação de objetivos com UI no produto; ELECTRE-like
outranking (não confundir dominância com sobreclassificação — cap. 09).

## Critérios de aceite (DoD)

- [ ] `pytest` verde em `decisor-zero/etapas/02-dominancia` (worked example do cap. 02)
- [ ] `pytest` verde em `app/backend` (incluindo o teste novo de dominância)
- [ ] `mkdocs build --strict` verde com o cap. 02 na nav
- [ ] Nenhuma fonte "?" citada no corpo do cap. 02
- [ ] Gate humano: revisão do Steward no merge

## Clarify (resolvido — defaults, 2026-07-30)

- *Dominância fraca ou estrita?* → padrão do livro: A domina B se A é ≥ em todos os
  critérios e > em pelo menos um (dominância de Pareto usual em MCDA); empate total não
  domina.
- *A etapa 02 repete a API da 01?* → sim (etapas são autocontidas); o diff entre 01 e 02
  é a lição: correção do peso + módulo de dominância + endpoint novo.
