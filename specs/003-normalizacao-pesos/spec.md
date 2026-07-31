# Spec 003 — Normalização e pesos (cap. 03 + etapa 03)

- **Status**: Aprovada (defaults) · **Raia**: Plena · **Data**: 2026-07-30
- **Origem**: sequência didática do SUMARIO (Parte I) — "siga com a rodada 003" do Steward.

## O quê e por quê

Entregar o capítulo 03 (normalização min-max e vetorial; elicitação de pesos por rating
direto, ROC, swing e entropia) com a etapa `03-normalizacao-pesos`, e expor a
elicitação de pesos no produto. São os dois insumos de todo método compensatório — sem
eles o cap. 04 (SAW) não tem o que agregar.

Dor real observada: a soma crua do cap. 01 provou o absurdo de agregar escalas brutas;
os pesos 0,35/0,25/0,25/0,15 usados desde a fundação nunca tiveram origem declarada.

## Requisitos funcionais

- **FR1** — Capítulo 03 no esqueleto v3; tabelas geradas pelo motor (nunca à mão); só
  fontes ✓ no corpo (Edwards & Barron 1994 promovida a ✓ por verificação de registro).
- **FR2** — Etapa 03: `motor/normalizacao.py` (min-max, vetorial) e `motor/pesos.py`
  (rating, ROC, swing, entropia) puros + rotas `POST /api/normalizar` e
  `POST /api/pesos` + página; worked examples do capítulo em teste.
- **FR3** — Produto: `POST /api/pesos` stateless com os mesmos quatro métodos + testes.
- **FR4** — Registro vivo: bibliografia (promoção ✓ com nota de curadoria), SUMARIO
  (03 ✅), nav, HISTORICO (edição 0.3 + snapshot), CHANGELOG, mapa do decisor-zero.

## Fora de escopo (YAGNI)

Agregação SAW no livro (cap. 04); AHP como técnica de pesos (cap. 05); persistir o
vetor de pesos elicitado na decisão salva (entra com a UI de pesos, spec futura).

## Critérios de aceite (DoD)

- [ ] `pytest` verde na etapa 03 e no produto; regressão das etapas 01–02 intacta
- [ ] `mkdocs build --strict` verde com o cap. 03 na nav
- [ ] Nenhuma fonte "?" citada no corpo do cap. 03
- [ ] Gate humano do Steward no merge

## Clarify (resolvido — defaults, 2026-07-30)

- *Quais normalizações?* → só as duas que os métodos das Partes II usam (min-max → SAW;
  vetorial → TOPSIS); soma linear vira exercício do leitor.
- *Entropia sobre qual matriz?* → sobre a min-max normalizada (colunas constantes têm
  diversificação 0), convenção documentada no docstring.
- *Swing com âncora?* → o salto mais importante vale exatamente 100 (validação).
