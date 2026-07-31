# Changelog

Todas as mudanças notáveis do **Decisor** são registradas aqui. Formato baseado em
[Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/); versionamento semântico.

> Forcing function (herdada do Maestro): toda PR adiciona uma entrada em
> **[Unreleased]** — a CI (`.github/workflows/ci.yml`, job `changelog`) falha se o
> `CHANGELOG.md` não for alterado. Bypass: label `skip-changelog`.

## [Unreleased]

### Added

- **Fundação do projeto (spec 001)**: constituição v1.0.0 (linhagem Engenharia de
  Harness + Maestro), [CLAUDE.md](CLAUDE.md)/[AGENTS.md](AGENTS.md) para agentes,
  spec-kit (`.specify/`), ADRs 0001–0004.
- **Livro**: guia editorial (esqueleto v3 + caso âncora), sumário com a sequência
  didática (14 capítulos), bibliografia com 30+ fontes e status de verificação,
  capítulos [00](livro/capitulos/00-introducao.md) e
  [01](livro/capitulos/01-problema-multicriterio.md), publicação MkDocs Material
  (`mkdocs build --strict` verde).
- **decisor-zero**: etapas `00-esqueleto` e `01-matriz` (motor puro `MatrizDecisao` +
  API + página), 11 testes reproduzindo os números do cap. 01 (+1 exercício do leitor).
- **app (produto v0)**: backend FastAPI + motor SAW puro (com fonte no docstring) +
  persistência Neon/Postgres com fallback SQLite + frontend estático; 8 testes.

- **VIKOR e BWM (spec 010)**: capítulo [10](livro/capitulos/10-vikor-bwm.md), etapa
  `10-vikor-bwm` (compromisso {A1, A4}; BWM via LP) e `vikor` no produto.
- **ELECTRE (spec 009)**: capítulo [09](livro/capitulos/09-electre.md) e etapa
  `09-electre` (relação S, vetos, kernel com página interativa).
- **PROMETHEE (spec 008)**: capítulo [08](livro/capitulos/08-promethee.md), etapa
  `08-promethee` (usual/V-shape, pymcdm) e `promethee2` no produto.
- **MAVT e Even Swaps (spec 007)**: capítulo
  [07](livro/capitulos/07-funcoes-de-valor.md) e etapa `07-funcoes-de-valor`
  (linear ≡ SAW provado; curvas mudam o pódio).
- **TOPSIS (spec 006)**: capítulo [06](livro/capitulos/06-topsis.md), etapa
  `06-topsis` (validação pymcdm) e `topsis` no catálogo do produto.
- **AHP (spec 005)**: capítulo [05](livro/capitulos/05-ahp.md), etapa `05-ahp`
  (autovetor + CR interativos) e método `ahp` em `/api/pesos`; 6 fontes ✓.
- **SAW — o primeiro ranking (spec 004)**: capítulo
  [04](livro/capitulos/04-saw.md) (premissas da forma aditiva + virada de ranking
  rating×ROC), etapa `04-saw` com validação cruzada pymcdm, e sobrescrita de pesos no
  ranking do produto; Fishburn (1967) ✓ na bibliografia.
- **Normalização e pesos (spec 003)**: capítulo
  [03](livro/capitulos/03-normalizacao-pesos.md) (min-max × vetorial; rating, ROC,
  swing, entropia — com vieses declarados), etapa `03-normalizacao-pesos` (motores
  puros + API + página) e rota stateless `POST /api/pesos` no produto; Edwards &
  Barron (1994) ✓ na bibliografia.
- **Estruturação e dominância (spec 002)**: capítulo
  [02](livro/capitulos/02-estruturacao-dominancia.md) (value-focused thinking,
  checklist de critérios, fronteira de Pareto), etapa `02-dominancia` (motor puro +
  API, worked example A5 em teste, gabarito do peso negativo aplicado), rota de
  dominância no produto e Keeney (1992) ✓ na bibliografia.

### Changed

- **Repositório próprio (ADR 0005)**: o seed virou a raiz de `GHDaru/multicriterio`;
  `site_url`/`repo_url` retargetados; CI e Pages ativos.

### Follow-up

- UI de funções de valor no produto para expor o método `mavt` (spec futura).

- Ativar o GitHub Pages no repositório (Settings → Pages → Source: GitHub Actions —
  única etapa manual; ADR 0005).
- Promover fontes "?" da bibliografia a ✓ antes de citá-las em capítulos novos.
- Cap. 05 (AHP — comparações par a par e consistência) — próxima rodada natural.
