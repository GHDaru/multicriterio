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

## Edições

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
| Fallback SQLite no `app/` | a trilha deve rodar a custo zero e offline (Princípio VI) | o cap. 13 tornar o provisionamento Neon parte da trilha | 🔵 aberta | — |
| Frontend estático v0 | zero build = carga cognitiva mínima nas etapas | a UI do produto exigir estado complexo (comparação multi-método, cap. 11+) → migração conforme ADR 0002 | 🔵 aberta | — |
| Status "?" na bibliografia | editores bloqueiam verificação por robô | cada fonte "?" for promovida a ✓ antes de ser citada em capítulo novo | 🔵 aberta | — |

Legenda: 🔵 aberta · 🟡 em movimento · 🟢 cumprida · 🔴 refutada/não-expira.
Regra de manutenção: revisar este placar a cada edição.
