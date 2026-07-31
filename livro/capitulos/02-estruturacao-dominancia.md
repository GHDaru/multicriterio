# 02 — Estruturação: de valores a critérios (e o veredito da dominância)

> **Estado da arte capturado em 2026-07** · última revisão 2026-07-30 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Derivar** critérios mensuráveis a partir de objetivos — distinguindo objetivos-fim
   de objetivos-meio com o teste "por que isso importa?" (value-focused thinking).
2. **Avaliar** uma família de critérios contra as cinco propriedades clássicas:
   completa, operacional, decomponível, não-redundante e mínima.
3. **Definir** dominância de Pareto e **calcular** a fronteira de Pareto de uma matriz
   de decisão — o único veredito que não exige pesos nem agregação.
4. **Explicar** por que a dominância quase nunca decide sozinha — e por que isso é bom.

## O problema

No capítulo 01, os quatro critérios do caso âncora caíram do céu. Decisões reais não
começam com critérios: começam com desconforto ("preciso morar melhor") e com uma lista
de opções. Dois erros nascem exatamente aqui. O primeiro é **medir o que é fácil em vez
do que importa** — "número de quartos" é fácil de contar, mas o que você quer mesmo é
espaço utilizável. O segundo é **contar a mesma coisa duas vezes** — "preço" e "preço
por m²" parecem dois critérios, mas carregam a mesma informação, e qualquer método
posterior dará a esse fator peso em dobro sem que ninguém perceba.

E há um terceiro desperdício, mais silencioso: gastar energia comparando alternativas
que nenhuma preferência racional escolheria. Um quinto candidato entrou na nossa busca —
**A5 (Colina): R$ 470.000, 60 m², 18 min, bairro 3**. Precisamos de algum método
sofisticado para descartá-lo?

## Fundamentos

**Pense em valores antes de alternativas.** Keeney (1992) inverte a ordem usual: em vez
de perguntar "qual opção escolho?" (*alternative-focused thinking*), pergunte primeiro
"o que eu quero de verdade?" (*value-focused thinking*). O instrumento é o teste **"por
que isso importa?"**: aplicado a "quero um apartamento perto do metrô", a resposta
("para gastar menos tempo") revela que "proximidade do metrô" é um **objetivo-meio** —
o critério certo é *tempo de deslocamento*, que captura também home office, carro,
trânsito. Objetivo-fim vira critério; objetivo-meio vira, no máximo, dado.

**Uma família de critérios tem requisitos.** Keeney & Raiffa (1976) enumeram as
propriedades que usamos como checklist neste livro: **completa** (nada que importa ficou
de fora), **operacional** (dá para medir cada alternativa a custo razoável),
**decomponível** (dá para julgar um critério sem depender dos outros — premissa que os
métodos aditivos vão exigir no cap. 04), **não-redundante** (nenhuma informação contada
duas vezes) e **mínima** (o menor conjunto que satisfaz as anteriores). Belton & Stewart
(2002) acrescentam o alerta prático: critério que não discrimina as alternativas em
disputa só adiciona ruído — corte-o.

**Dominância: o veredito grátis.** Com a família de critérios fechada, uma conclusão
independe de qualquer pesagem: a alternativa $a$ **domina** $b$ se $a$ é pelo menos tão
boa quanto $b$ em todos os critérios (respeitada a direção de cada um) e estritamente
melhor em pelo menos um. Formalmente, para critérios de benefício:

$$a \succ b \iff \forall j:\; x_{aj} \ge x_{bj} \;\;\text{e}\;\; \exists j:\; x_{aj} > x_{bj}$$

(com desigualdades invertidas nos critérios de custo). Alternativas dominadas podem ser
descartadas antes de qualquer método; as que sobram formam a **fronteira de Pareto** —
o conjunto onde todo ganho custa uma perda (Hwang & Yoon, 1981).

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

**Passo 1 — o teste do "por que importa?"** na nossa lista original de desejos:

| Desejo declarado | Por que importa? | Vira |
|---|---|---|
| "Perto do metrô" | gastar menos tempo | critério *Deslocamento (min)* ↓ |
| "Bairro seguro e com comércio" | qualidade de vida no entorno | critério *Bairro (1–5)* ↑ |
| "Caber no orçamento" | fim em si | critério *Preço (R$)* ↓ |
| "Espaço para escritório" | fim em si | critério *Área (m²)* ↑ |
| "Preço por m² justo" | é Preço ÷ Área — informação já contada | **cortado** (redundante) |

A família resultante passa no checklist: completa, operacional, decomponível,
não-redundante, mínima — são os quatro critérios do cap. 01, agora com justificativa.

**Passo 2 — a matriz com o candidato A5.**

| Alternativa | Preço (R$) ↓ | Área (m²) ↑ | Deslocamento (min) ↓ | Bairro (1–5) ↑ |
|---|---|---|---|---|
| A1 — Centro | 450.000 | 62 | 15 | 4 |
| A2 — Jardim | 380.000 | 70 | 35 | 3 |
| A3 — Parque | 520.000 | 85 | 25 | 5 |
| A4 — Estação | 340.000 | 55 | 20 | 2 |
| **A5 — Colina** | **470.000** | **60** | **18** | **3** |

**Passo 3 — comparação par a par com A1.** A1 é mais barata (450.000 < 470.000), maior
(62 > 60), mais perto (15 < 18) e em bairro melhor (4 > 3). Quatro de quatro: **A1
domina A5** — não existe pesagem, por mais excêntrica que seja, que faça A5 vencer A1.
Nenhum outro par se domina (confira A2 × A5: A2 ganha em preço e área, mas perde em
deslocamento — conflito, não dominância).

**Passo 4 — o veredito.** Dominadas: {A5, por A1}. Fronteira de Pareto: {A1, A2, A3,
A4} — exatamente o caso âncora do cap. 01, cuja afirmação "nenhuma domina outra" agora
está provada. *Este resultado é reproduzido pelos testes
`test_a5_e_dominada_por_a1_e_somente_por_a1` e
`test_caso_ancora_original_nao_tem_dominadas` da etapa 02.*

## Quando usar (e quando não)

A dominância é o primeiro filtro de qualquer análise — barata, incontestável e sem
parâmetros. Mas quase nunca decide sozinha: em problemas reais bem estruturados, a
fronteira de Pareto contém várias alternativas (se a família de critérios é
não-redundante e as opções sobreviveram a uma pré-seleção, conflito é a regra). E isso
é bom: dominada eliminada é energia poupada para o conflito de verdade. Dois cuidados:
o veredito depende da **direção** declarada de cada critério (uma direção errada
inverte conclusões silenciosamente — por isso a etapa 02 testa isso); e eliminar
dominadas **antes** de escolher método evita que alternativas irrelevantes influenciem
o resultado — semente do debate de rank reversal que reencontraremos nos caps. 05 e 11.

### Leitura executiva

Estruturar é metade da decisão: o teste "por que isso importa?" transforma desejos em
critérios-fim mensuráveis, o checklist das cinco propriedades blinda a família contra
redundância, e a dominância descarta de graça o que nenhuma preferência salvaria. **O
que levar** hoje: antes de discutir pesos com qualquer stakeholder, passe o filtro de
dominância — cada alternativa eliminada aí é uma discussão de pesos que você não vai
precisar ter.

## Mão na massa — decisor-zero, etapa 02

Em `decisor-zero/etapas/02-dominancia/`, dois diffs em relação à etapa 01 — e o diff é
a lição: (1) `motor/matriz.py` ganhou a correção do exercício do cap. 01 (peso negativo
agora é `ErroDeModelagem`; o teste que o prova usa pesos que somam 1 e escapavam da
checagem antiga); (2) nasce `motor/dominancia.py`, com `domina()` e
`analise_dominancia()` devolvendo dominadas e fronteira de Pareto — e a página mostra
A5 riscado da tabela. Exercício de completar: `analise_dominancia` compara todos os
pares duas vezes ($O(m^2 n)$ com constante dobrada) — corte as comparações redundantes
sem quebrar nenhum teste existente.

## Segundo domínio — dominância na decisão B2B

No caso do fornecedor, um quarto candidato aparece: **F4 — Revenda** (R$ 12.500/mês,
50 ms, SLA 99,00%, suporte 3) — um revendedor que empacota a Hiperescala com margem.
O filtro de dominância o elimina com um requinte que o A5 não tinha: F4 é dominado
por **dois** candidatos ao mesmo tempo — F1 (mais barato, mais rápido, SLA maior,
suporte igual) e F2 (melhor em tudo). Fronteira de Pareto: {F1, F2, F3}. Dominadores
múltiplos são um sinal diagnóstico útil: a alternativa não está apenas mal posicionada
— ela é redundante no conjunto. *Teste `test_segundo_dominio_f4_dominada_por_dois` da
etapa 02.*

## Verificação

1. "Nota no Google Maps do quarteirão" e "Bairro (1–5)" podem coexistir na família de
   critérios do caso âncora? Contra qual propriedade isso esbarra? (Dica: objetivo 2 —
   não-redundância.)
2. Se trocarmos a direção do critério Preço para "benefício" por engano, quem passa a
   dominar quem entre A1 e A5? (Dica: objetivo 3 — refaça o passo 3.)
3. Uma fronteira de Pareto com uma única alternativa dispensaria todos os próximos
   capítulos. Por que isso quase nunca acontece em decisões reais bem estruturadas?
   (Dica: objetivo 4.)

---

## Apêndice A — estruturação e dominância nas ferramentas

- **scikit-criteria** implementa o filtro deste capítulo em
  `skcriteria.preprocessing.filters` (incluindo remoção de dominadas) e expõe
  `DecisionMatrix.dominance` com exatamente a nossa semântica de direção MIN/MAX
  (<https://scikit-criteria.quatrope.org/>).
- **pymcdm** assume que a matriz já chega estruturada — a etapa de estruturação fica
  fora das bibliotecas, o que reforça a lição do capítulo: software calcula, mas a
  família de critérios é responsabilidade do decisor
  (<https://github.com/kotbaton/pymcdm>).
- Na otimização multiobjetivo (alternativas contínuas, fora do nosso escopo — cap. 01),
  a fronteira de Pareto é o próprio objeto de estudo; o leitor que quiser essa ponte
  encontra o panorama em Greco, Ehrgott & Figueira (2016).

## Apêndice B — gabarito comentado da Verificação

1. Não deveriam coexistir: a nota do Google Maps e a escala 1–5 de Bairro medem
   substancialmente o **mesmo objetivo-fim** (qualidade do entorno) — redundância, peso
   contado duas vezes. Escolha o atributo mais operacional e descarte o outro.
2. Com a direção do Preço invertida por engano, "mais caro = melhor": A5 (470 mil)
   passaria a vencer A1 (450 mil) no critério Preço — e como A1 só vencia A5 em tudo,
   a dominância desapareceria (nenhum dos dois dominaria o outro). Direção errada
   inverte vereditos em silêncio; por isso a etapa 02 a testa.
3. Porque uma família de critérios bem construída (não-redundante, discriminante) e
   uma pré-seleção razoável de alternativas produzem, por construção, opções com
   perfis conflitantes — se uma alternativa dominasse todas, a decisão nem chegaria à
   mesa. Fronteira grande é sintoma de problema bem posto.
