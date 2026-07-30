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

- **Estruturação e dominância (spec 002)**: capítulo
  [02](livro/capitulos/02-estruturacao-dominancia.md) (value-focused thinking,
  checklist de critérios, fronteira de Pareto), etapa `02-dominancia` (motor puro +
  API, worked example A5 em teste, gabarito do peso negativo aplicado), rota de
  dominância no produto e Keeney (1992) ✓ na bibliografia.

### Changed

- **Repositório próprio (ADR 0005)**: o seed virou a raiz de `GHDaru/multicriterio`;
  `site_url`/`repo_url` retargetados; CI e Pages ativos.

### Follow-up

- Ativar o GitHub Pages no repositório (Settings → Pages → Source: GitHub Actions —
  única etapa manual; ADR 0005).
- Promover fontes "?" da bibliografia a ✓ antes de citá-las em capítulos novos.
- Cap. 03 (normalização e pesos) — próxima rodada natural.
