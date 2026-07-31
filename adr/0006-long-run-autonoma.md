# ADR 0006 — Long run autônoma: rodadas 005–013 em sequência

- **Status**: Aceito
- **Data**: 2026-07-31
- **Relacionado**: ADR 0003 (sequência didática); specs 005–013

## Contexto

O Steward autorizou executar as rodadas restantes (caps. 05–13) em uma corrida única e
autônoma ("pode rodar agora uma long run e já faça as próximas specs até encerrar,
tomando as decisões e registrando em um ADR"). Cada rodada continua sendo uma spec em
branch própria com merge na `main`; o gate humano passa a ser **a posteriori** (revisão
do conjunto ao final), decisão explícita do Steward ao autorizar a corrida.

## Decisão

1. **Escopo da corrida**: specs 005–013, uma por capítulo restante do SUMARIO
   (05 AHP · 06 TOPSIS · 07 MAVT/Even Swaps · 08 PROMETHEE · 09 ELECTRE ·
   10 VIKOR+BWM · 11 Sensibilidade · 12 Grupo · 13 Produto), cada uma com etapa
   executável, worked example em teste e capítulo no esqueleto v3.
2. **Profundidade calibrada para cobertura**: os capítulos da corrida saem no esqueleto
   v3 completo porém mais enxutos que os caps. 00–04; o aprofundamento fica para
   rodadas futuras de auditoria (é um livro vivo — Princípio IV). O placar de expiração
   registra essa dívida.
3. **Validação cruzada onde existe referência**: TOPSIS, PROMETHEE II e VIKOR são
   validados contra a pymcdm em teste (como o SAW). AHP, ELECTRE I, MAVT, BWM e os
   agregadores de grupo não têm equivalente direto na pymcdm — seus worked examples
   são conferidos por propriedades matemáticas (consistência, simetrias, casos-limite)
   além dos números do capítulo.
4. **Decisões técnicas por método** (defaults da corrida):
   - **AHP (05)**: prioridades pelo autovetor principal via método das potências;
     razão de consistência com RI de Saaty (RI₄ = 0,90); uso no projeto = técnica de
     **pesos** (entra em `/api/pesos`, método `ahp`), não de ranking direto.
   - **TOPSIS (06)**: normalização vetorial + distância euclidiana (formulação clássica
     de Hwang & Yoon).
   - **MAVT (07)**: funções de valor lineares por partes (pontos de quebra declarados);
     caso linear reduz ao SAW — provado em teste.
   - **PROMETHEE II (08)**: funções de preferência usual e linear (V-shape com p);
     fluxo líquido φ.
   - **ELECTRE I (09)**: concordância/discordância com limiares c*, d* e veto;
     saída = relação de sobreclassificação + núcleo (kernel), não ranking.
   - **VIKOR (10)**: S, R, Q com v = 0,5 e checagem das duas condições de aceitação.
     **BWM (10)**: modelo linear resolvido com `scipy.optimize.linprog` (scipy entra
     em `decisor-zero/requirements.txt`); caso consistente conferido em forma fechada.
   - **Sensibilidade (11)**: varredura de peso por critério (reta de estabilidade do
     vencedor) + comparação multi-método com correlação de rankings (Spearman);
     produto ganha `POST /api/decisoes/{id}/comparar`.
   - **Grupo (12)**: Borda e Copeland sobre rankings; média geométrica de julgamentos
     (AIJ) para AHP em grupo.
   - **Produto (13)**: capítulo operacional — Neon (provisionar, `DATABASE_URL`,
     `sslmode=require`), fallback SQLite, deploy com uvicorn; produto ganha `/health`.
5. **Higiene da corrida**: regressão completa (todas as etapas + app + build estrito)
   ao final de cada rodada é substituída por regressão **da rodada** (etapa nova + app
   + build) + **uma varredura completa ao final da corrida**, registrada no qa-report
   da última spec. Motivo: custo; risco baixo porque os motores são aditivos.
6. Métodos de ranking novos entram no catálogo `/api/metodos` do produto na rodada do
   seu capítulo (Princípio II preservado).

## Alternativas avaliadas

- **Um capítulo por sessão com gate humano a cada merge** — rejeitado nesta corrida por
  instrução explícita do Steward; o formato anterior permanece o padrão fora dela.
- **Delegar capítulos a subagentes em paralelo** — rejeitado: o worked example de cada
  método exige conferência numérica acoplada ao motor; paralelizar multiplicaria o
  risco de prosa divergir do código.
- **BWM sem implementação (só conceito)** — rejeitado: violaria o Princípio II;
  o custo do scipy é aceitável na trilha didática.

## Consequências

- 9 merges na `main` em sequência; o Pages publica a cada merge.
- O placar de expiração ganha a linha "capítulos da long run aguardam rodada de
  aprofundamento/auditoria".
- Qualquer decisão imprevista tomada durante a corrida é adicionada ao qa-report da
  rodada correspondente (não a este ADR, que é imutável).

## Fontes

- Instrução do Steward em 2026-07-31; ADR 0003; bibliografia do projeto.
