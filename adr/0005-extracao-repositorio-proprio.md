# ADR 0005 — Extração concluída: o projeto vive em GHDaru/multicriterio

- **Status**: Aceito
- **Data**: 2026-07-30
- **Relacionado**: ADR 0001 (nascimento como seed); supera a pendência registrada lá

## Contexto

O ADR 0001 registrou o nascimento do projeto como seed autocontido (`decisor/`) na
branch de sessão do `harness_engineering`, com extração futura condicionada à criação
de um repositório próprio — ação externa que exigia o humano. O Steward criou
`GHDaru/multicriterio` e determinou que todo o desenvolvimento passa a ser commitado lá.

## Decisão

1. O conteúdo integral do seed vira a **raiz** de `GHDaru/multicriterio`; a partir da
   fundação, o desenvolvimento segue o fluxo da constituição (branch `NNN-nome` por
   rodada, merge na `main` publica).
2. Referências retargetadas: `site_url` → `https://ghdaru.github.io/multicriterio/`,
   `repo_url` → `https://github.com/GHDaru/multicriterio`. Os workflows de
   `.github/workflows/` (CI e Pages) ficam ativos automaticamente por estarem na raiz.
3. O diretório `decisor/` na branch de sessão do harness_engineering torna-se histórico
   morto: não recebe mais commits e a branch pode ser descartada sem merge.
4. Etapa manual única restante (humano): **Settings → Pages → Source: GitHub Actions**
   no repositório novo, para o deploy do livro passar a publicar.

## Alternativas avaliadas

- **Manter o desenvolvimento no seed e sincronizar por subtree** — rejeitado: duas
  fontes de verdade, contra o Princípio VI do Maestro (artefato duplicado).

## Consequências

- O placar de expiração do `livro/HISTORICO.md` marca a previsão do ADR 0001 como
  cumprida (🟢) na edição 0.2.
- A partir daqui, `main` do multicriterio é a linha publicável; CI (testes + build
  estrito + gate de CHANGELOG) vale para toda PR.

## Fontes

- ADR 0001 deste repositório; instrução do Steward em 2026-07-30.
