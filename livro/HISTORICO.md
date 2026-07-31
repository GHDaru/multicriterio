# Histórico — este é um livro vivo

> Princípio IV da constituição (`.specify/memory/constitution.md`): o que este livro
> descreve tem data; toda edição fica registrada aqui, com o modelo de IA usado.

## Como ler as datas do livro

- **Data do evento** — quando algo aconteceu no mundo (ex.: publicação de um paper);
  vive no corpo do texto e não muda.
- **Data de captura** — o "estado da arte capturado em AAAA-MM" no cabeçalho de cada
  capítulo: quando as fontes, bibliotecas e links foram verificados pela última vez.
- **Rodada** — o ciclo spec-kit (`specs/NNN-*`) que produziu ou revisou o conteúdo.

## Tabela de snapshot por capítulo

| Capítulo | Estado da arte capturado em | Etapa testada | Última revisão |
|---|---|---|---|
| 00 Introdução | 2026-07 | ✓ (etapa 00) | 2026-07-30 |
| 01 O problema multicritério | 2026-07 | ✓ (etapa 01) | 2026-07-30 |
| 02 Estruturação e dominância | 2026-07 | ✓ (etapa 02) | 2026-07-30 |
| 03 Normalização e pesos | 2026-07 | ✓ (etapa 03) | 2026-07-30 |
| 04 SAW — o método aditivo | 2026-07 | ✓ (etapa 04) | 2026-07-31 |
| 05 AHP | 2026-07 | ✓ (etapa 05) | 2026-07-31 |
| 06 TOPSIS | 2026-07 | ✓ (etapa 06) | 2026-07-31 |
| 07 MAVT e Even Swaps | 2026-07 | ✓ (etapa 07) | 2026-07-31 |
| 08 PROMETHEE | 2026-07 | ✓ (etapa 08) | 2026-07-31 |
| 09 ELECTRE | 2026-07 | ✓ (etapa 09) | 2026-07-31 |
| 10 VIKOR e BWM | 2026-07 | ✓ (etapa 10) | 2026-07-31 |
| 11 Sensibilidade e rank reversal | 2026-07 | ✓ (etapa 11) | 2026-07-31 |
| 12 Decisão em grupo | 2026-07 | ✓ (etapa 12) | 2026-07-31 |
| 13 Do protótipo ao produto | 2026-07 | ✓ (etapa 13) | 2026-07-31 |

## Edições

### Edições 0.14+ — 2026-07-31 · rodada de aprofundamento (specs 014–027, ADR 0007)

Uma edição por capítulo; fórmula uniforme: segundo domínio (fornecedor de nuvem)
worked com números em teste + Apêndice B (gabarito comentado) + promoções de fonte.

- **0.21 (spec 021, cap. 07)**: curvas B2B (limiar de SLA, orçamento); gabarito;
  etapa 07 `6 passed`.
- **0.20 (spec 020, cap. 06)**: TOPSIS B2B com validação pymcdm; gabarito; etapa 06
  `6 passed`.
- **0.19 (spec 019, cap. 05)**: AHP do CTO no B2B (CR=0,0038); gabarito; etapa 05
  `9 passed`.
- **0.18 (spec 018, cap. 04)**: SAW B2B — vitória robusta (margem 17× maior);
  gabarito; etapa 04 `8 passed`.
- **0.17 (spec 017, cap. 03)**: entropia quase uniforme no B2B como diagnóstico;
  gabarito; etapa 03 `21 passed`.
- **0.16 (spec 016, cap. 02)**: F4 — Revenda dominada por dois candidatos
  (diagnóstico de redundância); gabarito; etapa 02 `9 passed`.
- **0.15 (spec 015, cap. 01)**: modelagem e soma crua do segundo domínio ("elege o
  mais caro de novo"); gabarito; etapa 01 `12 passed, 1 skipped`.
- **0.14 (spec 014, cap. 00)**: segundo domínio apresentado; etapa 00 ganha
  `/api/caso-fornecedor` e testes (`2 passed`).

### Edição 0.13 — 2026-07-31 · Do protótipo ao produto (spec 013) — TRILHA COMPLETA

- Capítulo 13 (porta de persistência, Neon + fallback SQLite, credenciais, /health,
  degraus de infra futuros); etapa `13-persistencia` com a prova de sobrevivência ao
  reinício; `GET /health` no produto. **Os 14 capítulos do SUMARIO estão publicados,
  cada um com etapa executável testada.**
- Varredura final da long run: todas as etapas + produto + build estrito verdes
  (qa-report 013).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.12 — 2026-07-31 · Decisão em grupo (spec 012, long run ADR 0006)

- Capítulo 12 (Borda × Copeland — "A1 vence sem ser o 1º de ninguém"; paradoxo de
  Condorcet; AIJ por média geométrica); etapa `12-grupo`.
- **Verificação**: etapa `6 passed` (qa-report 012).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.11 — 2026-07-31 · Sensibilidade e rank reversal (spec 011, long run ADR 0006)

- Capítulo 11 (varredura de peso — A1 reina só em [0,316; 0,358); ρ=1 entre os 4
  métodos; rank reversal real: A5 de último lugar troca A3/A4 no TOPSIS e o VENCEDOR
  no SAW; protocolo de robustez do livro); etapa `11-sensibilidade`;
  `POST /api/decisoes/{id}/comparar` no produto.
- **Verificação**: etapa `5 passed`; app `21 passed` (qa-report 011).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.10 — 2026-07-31 · VIKOR e BWM (spec 010, long run ADR 0006)

- Capítulo 10 (S/R/Q, condições C1/C2 e o conjunto de compromisso {A1, A4} do caso
  âncora; BWM com 2n−3 comparações e ξ); etapa `10-vikor-bwm` (VIKOR validado contra
  pymcdm; BWM via linprog, forma exata no caso consistente); `vikor` no produto.
- **Verificação**: etapa `6 passed`; app `20 passed` (qa-report 010).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.9 — 2026-07-31 · ELECTRE (spec 009, long run ADR 0006)

- Capítulo 09 (concordância/discordância/veto/kernel; "não ranquear" como resposta
  honesta); etapa `09-electre` com três cenários em teste (relação vazia → shortlist
  {A1, A3} → veto devolvendo A2). Fora do catálogo de ranking do produto por design.
- **Verificação**: etapa `5 passed` (qa-report 009).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.8 — 2026-07-31 · PROMETHEE (spec 008, long run ADR 0006)

- Capítulo 08 (fluxos φ, degrau × V-shape com o salto de A3); etapa `08-promethee`
  validada contra a pymcdm; `promethee2` no catálogo do produto. Incidente didático
  registrado no spec: a primeira versão do teste de propriedade do V-shape estava
  errada — virou lição do capítulo.
- **Verificação**: etapa `5 passed`; app `19 passed` (qa-report 008).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.7 — 2026-07-31 · MAVT e Even Swaps (spec 007, long run ADR 0006)

- Capítulo 07 (funções de valor por partes, independência preferencial, Even Swaps);
  etapa `07-funcoes-de-valor` com as provas "linear ≡ SAW" e "curvas mudam o pódio
  sem tocar nos pesos" (A2: 4º → 2º). MAVT fora do produto até UI de curvas.
- **Verificação**: etapa `5 passed` (qa-report 007).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.6 — 2026-07-31 · TOPSIS (spec 006, long run ADR 0006)

- Capítulo 06 (ideal/anti-ideal, C_i, rank reversal específico apontado); etapa
  `06-topsis` com validação pymcdm a 1e-6; `topsis` no catálogo do produto.
- **Verificação**: etapa `5 passed`; app `18 passed` (qa-report 006).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.5 — 2026-07-31 · AHP (spec 005, long run ADR 0006)

- Capítulo 05 (autovetor, CI/CR, debate Belton & Gear/Dyer; AHP como técnica de pesos
  por decisão do ADR 0006); etapa `05-ahp` com página interativa de julgamentos;
  `/api/pesos` do produto ganha `ahp` (recusa CR > 0,10). Fontes: 6 promovidas a ✓.
- **Verificação**: etapa `8 passed`; app `17 passed` (qa-report 005).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.4 — 2026-07-31 · SAW: o primeiro ranking (spec 004)

- Capítulo 04 (agregação aditiva: fórmula, premissas — independência preferencial,
  escala de intervalo, compensação total — e o processo SMART) no esqueleto v3; o
  worked example central é a virada de ranking: rating direto elege A1, ROC elege A4,
  mesma matriz e mesma ordem de importância.
- Etapa `04-saw`: motor aditivo puro + rota + página com os dois vetores de pesos;
  **validação cruzada com pymcdm** (WSM + min-max) em teste — os escores batem a 1e-6.
- Produto: `POST /api/decisoes/{id}/ranking` aceita sobrescrita de pesos (revalidada);
  teste prova a troca de vencedor sobre a decisão salva.
- Bibliografia: Fishburn (1967) promovida a ✓ (registro DOI; nota: é carta ao editor).
- **Verificação**: etapa 04 `7 passed`; app `16 passed`; `mkdocs build --strict` verde
  (ver `specs/004-saw/qa-report.md`).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana pendente de gate de merge.

### Edição 0.3 — 2026-07-30 · normalização e pesos (spec 003)

- Capítulo 03 (min-max × vetorial; rating direto, ROC, swing e entropia) no esqueleto
  v3, com todas as tabelas geradas pelo motor da etapa; a origem dos pesos
  0,35/0,25/0,25/0,15 usados desde o cap. 01 fica declarada (rating direto).
- Etapa `03-normalizacao-pesos`: `normalizacao.py` + `pesos.py` puros, rotas
  `/api/normalizar` e `/api/pesos`, página comparando as duas normalizações.
- Produto: rota stateless `POST /api/pesos` (rating, ROC, swing, entropia).
- Bibliografia: Edwards & Barron (1994) promovida a ✓ (registro DOI verificado).
- **Verificação**: etapa 03 `20 passed`; app `14 passed`; `mkdocs build --strict` verde
  (ver `specs/003-normalizacao-pesos/qa-report.md`).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana pendente de gate de merge.

### Edição 0.2 — 2026-07-30 · repositório próprio + estruturação e dominância (spec 002)

- O projeto migrou para o repositório próprio **GHDaru/multicriterio** por determinação
  do Steward — extração registrada no ADR 0005 (supera a pendência do ADR 0001); CI e
  workflow do Pages ativos na raiz.
- Capítulo 02 (estruturação: value-focused thinking, checklist da família de critérios,
  dominância/fronteira de Pareto) no esqueleto v3; Keeney (1992) promovido a ✓ na
  bibliografia por verificação direta.
- `decisor-zero` etapa `02-dominancia`: motor de dominância puro + API + página, com o
  worked example (A5 dominado por A1) em teste; `matriz.py` incorporou o gabarito do
  exercício do cap. 01 (peso negativo agora é erro).
- Produto: rota `POST /api/decisoes/{id}/dominancia` com o mesmo motor e teste
  ponta a ponta.
- **Verificação**: etapa 02 `8 passed`; app `10 passed`; `mkdocs build --strict` verde
  (ver `specs/002-estruturacao-dominancia/qa-report.md`).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana pendente de gate de merge.

### Edição 0.1 — 2026-07-30 · fundação do projeto (spec 001)

- Nasce o projeto **Decisor**: constituição própria (v1.0.0, linhagem Engenharia de
  Harness + Maestro), `CLAUDE.md`/`AGENTS.md` para agentes, guia editorial com esqueleto
  v3 e caso âncora, sumário com a sequência didática completa (14 capítulos, Parte I–IV).
- Capítulos 00 e 01 escritos no esqueleto v3; bibliografia inicial com 30+ fontes e
  status de verificação (✓/?) — curadoria registrada em `bibliografia.md`.
- `decisor-zero/` etapas 00 (esqueleto FastAPI) e 01 (matriz de decisão como código),
  com os worked examples dos capítulos reproduzidos em testes.
- `app/` (o produto Decisor): backend FastAPI + motor SAW puro + repositório com
  Postgres (Neon) e fallback SQLite; frontend estático v0. Decisões em ADR 0001–0004.
- **Verificação**: `pytest` verde nas etapas e no app; build do livro verde
  (ver `specs/001-fundacao/qa-report.md`).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana pendente de gate de merge.

## Registro de expiração (o placar das previsões)

| Componente | Existe porque… | Previmos que expira quando… | Estado | Evidência datada |
|---|---|---|---|---|
| Seed no harness_engineering (ADR 0001) | não havia repositório próprio no nascimento | o Steward criar o repositório e o seed ser extraído | 🟢 cumprida | 2026-07-30 — GHDaru/multicriterio criado; ADR 0005 |
| Fallback SQLite no `app/` | a trilha deve rodar a custo zero e offline (Princípio VI) | o cap. 13 tornar o provisionamento Neon parte da trilha | 🟡 em movimento | 2026-07-31 — cap. 13 documenta o provisionamento; fallback permanece pelo custo zero |
| Capítulos 05–13 (long run, ADR 0006) | cobertura completa priorizada sobre profundidade | uma rodada de auditoria/aprofundamento revisar cada um | 🔵 aberta | — |
| Frontend estático v0 | zero build = carga cognitiva mínima nas etapas | a UI do produto exigir estado complexo (comparação multi-método, cap. 11+) → migração conforme ADR 0002 | 🔵 aberta | — |
| Status "?" na bibliografia | editores bloqueiam verificação por robô | cada fonte "?" for promovida a ✓ antes de ser citada em capítulo novo | 🔵 aberta | — |

Legenda: 🔵 aberta · 🟡 em movimento · 🟢 cumprida · 🔴 refutada/não-expira.
Regra de manutenção: revisar este placar a cada edição.
