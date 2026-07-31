# ADR 0008 — Capítulo de contribuição original (AEO) e artigo vivo

- **Status**: Aceito
- **Data**: 2026-07-31
- **Relacionado**: spec 028; cap. 14; Apêndice C

## Contexto

O Steward propôs um método próprio: ranqueamento multicritério com informação
puramente ordinal via simulação de funções de importância (valores e pesos sorteados
de U(0,1), ordenados conforme as preferências, normalizados, agregados; tally de
posições em muitas rodadas), com dois complementos — modo sem ordem de pesos (força
intrínseca) e leitura inversa de "crenças". Pediu: busca bibliográfica, formalização
com axiomas/teoremas, algoritmo, simulações, capítulo + artigo completo em apêndice,
em iterações.

## Decisão

1. **Nome provisório**: Agregação Estocástica Ordinal (AEO) — sujeito a renomeação
   pelo autor.
2. **Posicionamento honesto**: a busca identificou a família SMAA como parente direto
   (SMAA 1998; SMAA-2 2001 — rank acceptability e central weights; SMAA-O 2003 —
   critérios ordinais; survey Tervonen & Figueira 2008; mais Butler/Jia/Dyer 1997 e
   Barron & Barrett 1996), todas verificadas ✓. O capítulo e o artigo declaram a
   concepção independente E o parentesco, e delimitam as diferenças: prior de
   imputação (uniformes ordenadas normalizadas pela soma), protocolo de decisão
   próprio, uso duplo com/sem ordem de pesos.
3. **Protocolo de decisão** (resposta à pergunta aberta do autor sobre "como decidir
   com as contagens"): (i) publicar a matriz de aceitabilidade completa; (ii) ordem
   final por posto esperado (≡ Borda média — provado) com desempate lexicográfico;
   (iii) selo de robustez via vencedor de Condorcet estocástico (reportar
   divergências); (iv) empate técnico quando duelo ∈ [0,45; 0,55].
4. **Formato**: cap. 14 (via didática, esqueleto v3, marcado como contribuição
   original) + Apêndice C (artigo completo, vivo, versionado por iteração); motor
   `simular_aeo` na etapa 14 com semente reprodutível; todos os números do texto são
   fixtures de teste.
5. **Agenda de iterações** registrada no artigo (§8): priors alternativos, empates e
   ordens parciais, correlação entre critérios, elicitação híbrida, validação
   empírica das crenças, exposição no produto.

## Alternativas avaliadas

- **Apresentar como método inédito sem posicionamento** — rejeitado: violaria o
  Princípio I e a honestidade acadêmica; a força da contribuição está no protocolo e
  nas leituras, não em ignorar a SMAA.
- **Decidir só por "mais 1ºs"** (proposta original) — rejeitado como regra única: os
  próprios experimentos do livro produziram um caso em que ela diverge do posto
  esperado; virou o item (iii)/(iv) do protocolo.

## Consequências

- SUMARIO ganha a Parte V (contribuição original); nav publica cap. 14 e Apêndice C.
- Iterações futuras do artigo são specs próprias (029+), cada uma bump de versão do
  Apêndice C.

## Fontes

- As seis referências SMAA/simulação verificadas (bibliografia, seção "Contribuição
  original"); instrução do Steward em 2026-07-31.
