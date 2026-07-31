# ADR 0007 — Rodada de aprofundamento: specs 014–027, uma por capítulo

- **Status**: Aceito
- **Data**: 2026-07-31
- **Relacionado**: ADR 0006 (dívida de profundidade registrada no placar); GUIA-EDITORIAL §2

## Contexto

A long run (ADR 0006) priorizou cobertura; o placar de expiração registrou a dívida de
aprofundamento. O Steward determinou: "siga com os aprofundamentos de cada capítulo,
uma spec por capítulo; só pare ao final do capítulo 13", com publicação contínua.

## Decisão

1. **Uma spec por capítulo**: specs 014 (cap. 00) a 027 (cap. 13), cada uma em branch
   própria com merge na `main`; gate humano a posteriori sobre o conjunto (mesmo
   regime do ADR 0006).
2. **Fórmula do aprofundamento** (aplicada uniformemente):
   - **Segundo domínio worked**: a escolha de fornecedor de nuvem — F1 Hiperescala
     (R$ 12.000/mês, 45 ms, SLA 99,95%, suporte 3), F2 Regional (9.000, 20, 99,50, 4),
     F3 Nicho (7.500, 60, 99,00, 5); pesos 0,40/0,20/0,25/0,15 — resolvida com o
     método do capítulo, números gerados pelo motor e reproduzidos em teste novo da
     etapa. O caso é deliberadamente o contraponto do âncora: vencedor robusto (F2)
     em vez de corrida apertada.
   - **Apêndice B — gabarito comentado** das perguntas de Verificação (feedback
     fecha o ciclo do Backward Design; os exercícios de código continuam sem gabarito
     pronto).
   - **Bibliografia**: promover fontes "?" quando verificáveis por registro.
3. Um único caso secundário para todos os capítulos (carga cognitiva — GUIA §1);
   variações por capítulo (F4 dominado, curvas de SLA, personas de grupo) derivam dele.
4. Fontes promovidas na abertura da corrida: Ishizaka & Nemery (2013) ✓ (registro
   Semantic Scholar) e Roy (1996) ✓ (registro Open Library); Triantaphyllou e MACBETH
   permanecem "?" (não indexados nas bases acessíveis) e fora de corpo de capítulo.

## Alternativas avaliadas

- **Segundo domínio diferente por capítulo** — rejeitado: multiplica o custo de
  entender o problema a cada capítulo (contra Carga Cognitiva) e o custo de fixtures.
- **Publicar gabarito das Verificações em arquivo separado** — rejeitado: quebra a
  leitura no Pages; Apêndice B ao fim do capítulo preserva o retrieval practice de quem
  não rola até lá.

## Consequências

- 14 merges; cada capítulo ganha ~2 seções e a etapa ~1 teste de segundo domínio.
- O placar de expiração fecha a linha "capítulos 05–13 aguardam aprofundamento" ao
  final da corrida (edição correspondente do HISTORICO).

## Fontes

- Instrução do Steward em 2026-07-31; GUIA-EDITORIAL §§1–2; ADR 0006.
