# 04 — SAW: o método aditivo (e o primeiro ranking do livro)

> **Estado da arte capturado em 2026-07** · última revisão 2026-07-31 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Calcular** um ranking SAW completo à mão: normalização min-max, multiplicação
   pelos pesos, soma, ordenação.
2. **Explicar** as premissas que a agregação aditiva assume caladas — independência
   preferencial, escala de intervalo nos $r_{ij}$, compensação total entre critérios.
3. **Demonstrar** que, num problema equilibrado, o vencedor pertence ao vetor de pesos:
   o mesmo SAW elege A1 com um vetor defensável e A4 com outro.
4. **Situar** o SAW dentro do processo SMART/SMARTS — o método é a última linha de um
   procedimento de estruturação e elicitação, não um atalho para pulá-lo.

## O problema

Três capítulos de preparação — matriz validada, dominadas eliminadas, colunas
normalizadas, pesos com origem declarada — e ainda nenhuma resposta para a pergunta
original: **qual apartamento?** Falta o passo que junta tudo. O mais simples, mais
usado e mais antigo dos agregadores é uma soma ponderada; a pergunta honesta do
capítulo não é "como calcular" (é uma linha), e sim **o que essa linha assume** e
**quanto do resultado já estava decidido antes dela**.

## Fundamentos

**A forma aditiva.** SAW (*Simple Additive Weighting*, também WSM — *Weighted Sum
Model*) ordena as alternativas pelo escore

$$V(a_i) = \sum_{j=1}^{n} w_j \cdot r_{ij}$$

com $r_{ij}$ vindo da normalização min-max (direção resolvida, cap. 03) e $w$ somando
1 (cap. 03). Hwang & Yoon (1981) o catalogam como o método de referência do MADM — "o
mais conhecido e o mais amplamente usado". A licença matemática para somar valor entre
critérios vem de Fishburn (1967), que formalizou as condições da utilidade aditiva —
curiosidade de curadoria: o texto saiu na *Operations Research* como carta ao editor,
e virou a referência canônica de meio século de somas ponderadas.

**O que a soma assume.** Três premissas, todas violáveis na prática (Belton & Stewart,
2002): **independência preferencial** — o valor de 1 ponto de Bairro não pode depender
da Área (se "bairro ótimo só importa em apartamento grande", a forma aditiva está
errada — cap. 07 trata disso); **escala de intervalo** — o passo 0,4 → 0,5 vale o
mesmo que 0,8 → 0,9 em cada critério normalizado; **compensação total** — qualquer
déficit em um critério é compensável por sobra em outro: o SAW aceita trocar bairro
péssimo por preço baixo sem limite. Quando compensar é inaceitável ("segurança não se
negocia"), a resposta não é ajustar pesos — é trocar de família de método (outranking,
caps. 08–09).

**O processo em volta da soma.** Edwards & Barron (1994) empacotam o passo a passo
completo — estruturar critérios, medir, elicitar pesos por swing (ou ROC, no SMARTER),
somar — no processo SMART/SMARTS. A lição da sigla: a soma é o passo *final e trivial*
de um processo cujo trabalho duro é tudo o que os caps. 01–03 fizeram.

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

**Passo 1 — os insumos** (todos do cap. 03): a matriz min-max normalizada e os pesos
do rating direto $w = (0{,}35;\ 0{,}25;\ 0{,}25;\ 0{,}15)$.

**Passo 2 — multiplicar e somar** (mostrando A1 por extenso):

$$V(A1) = 0{,}35 \cdot 0{,}3889 + 0{,}25 \cdot 0{,}2333 + 0{,}25 \cdot 1{,}0 + 0{,}15 \cdot 0{,}6667 = 0{,}5444$$

**Passo 3 — o ranking:**

| # | Alternativa | Escore SAW |
|---|---|---|
| 1 | **A1 — Centro** | **0,5444** |
| 2 | A4 — Estação | 0,5375 |
| 3 | A3 — Parque | 0,5250 |
| 4 | A2 — Jardim | 0,4472 |

A1 vence — por 0,007. Três alternativas dentro de 0,02: a corrida é apertada, e
corrida apertada é aviso de sensibilidade.

**Passo 4 — o teste da sensibilidade.** Troque só o vetor de pesos pelo ROC do cap. 03
(mesma ordem declarada de importância — Preço ≻ Área ≻ Deslocamento ≻ Bairro):

| # | Alternativa | Escore SAW (pesos ROC) |
|---|---|---|
| 1 | **A4 — Estação** | **0,6302** |
| 2 | A2 — Jardim | 0,5613 |
| 3 | A1 — Centro | 0,4532 |
| 4 | A3 — Parque | 0,4063 |

O vencedor trocou (A1 → A4) e o vice também (A4 → A2) — com a **mesma matriz, o mesmo
método e a mesma ordem de importância dos critérios**. O ROC concentra 0,52 no Preço, e
A4 é a mais barata. Nenhum dos dois rankings está "errado": eles respondem a vetores
$w$ diferentes, ambos defensáveis. *Os dois rankings são reproduzidos pelos testes da
etapa 04 — e validados contra a biblioteca pymcdm (WSM + min-max), que produz
exatamente os mesmos escores.*

## Quando usar (e quando não)

O SAW é o padrão sensato quando as premissas valem: critérios preferencialmente
independentes, compensação aceitável, decisor disposto a declarar pesos. É transparente
(o escore decompõe critério a critério — dá para *explicar* por que A1 venceu),
auditável e barato. Não use quando compensar é inaceitável (outranking, caps. 08–09),
quando há interação forte entre critérios (MAUT, cap. 07) ou quando ninguém consegue
declarar pesos com um mínimo de convicção — nesse caso o problema é de elicitação, e
métodos como o AHP (cap. 05) existem exatamente para extrair pesos de comparações mais
simples. E lembre o cap. 03: o resultado herda as escolhas de normalização e de
técnica de pesos — o passo 4 acima é a prova.

### Leitura executiva

O SAW junta os caps. 01–03 numa linha: $V_i = \sum_j w_j r_{ij}$. A matemática é
trivial de propósito — todo o conteúdo da decisão já entrou antes, na estruturação, na
normalização e nos pesos. Num problema equilibrado, o algoritmo não escolhe o vencedor;
o vetor $w$ escolhe. **O que levar** hoje: apresente rankings aditivos sempre com o
vetor de pesos ao lado e com pelo menos um vetor alternativo defensável — se o vencedor
não sobrevive à troca, a conversa certa é sobre pesos, não sobre alternativas.

## Mão na massa — decisor-zero, etapa 04

Em `decisor-zero/etapas/04-saw/`, nasce `motor/saw.py` (uma função: normaliza,
multiplica, soma, ordena) e a rota `POST /api/matriz/saw`; a página tem dois botões —
rating direto e ROC — para você ver a virada de ranking ao vivo. Os testes incluem a
**validação cruzada com a pymcdm** (nossos escores contra o `WSM` deles, nos dois
vetores de pesos). Exercício de completar: implemente o WPM (*Weighted Product Model*,
$V_i = \prod_j r_{ij}^{\,w_j}$, sobre desempenhos crus com direção tratada por
inversão), exponha-o em `/api/matriz/wpm` e escreva o teste que mostra se o vencedor
do caso âncora muda em relação ao SAW.

## Verificação

1. Refaça $V(A2)$ à mão com os pesos do rating direto e confira com a tabela do passo
   3. (Dica: objetivo 1 — os $r_{2j}$ estão no cap. 03.)
2. "Bairro ótimo só me importa se o apartamento for grande." Qual premissa do SAW essa
   frase viola, e qual capítulo trata o caso? (Dica: objetivo 2.)
3. No passo 4, a ordem de importância dos critérios foi a mesma do rating direto — e o
   vencedor mudou. O que exatamente mudou entre os dois vetores? (Dica: objetivo 3 —
   ordem ≠ magnitude.)

---

## Apêndice A — o método aditivo nas ferramentas

- **pymcdm** implementa o SAW como `WSM(normalization_function=...)` — a normalização é
  parâmetro explícito, exatamente a tese do cap. 03; nossa etapa 04 valida os escores
  contra ela em teste (<https://github.com/kotbaton/pymcdm>).
- **scikit-criteria** o expõe como `WeightedSumModel`, dentro de um pipeline em que
  scaler e inversão de direção são passos declarados
  (<https://scikit-criteria.quatrope.org/>).
- **pyDecision** traz SAW/WSM com notebook de exemplo
  (<https://github.com/Valdecy/pyDecision>).
- Em planilhas, o SAW é a fórmula `=SOMARPRODUTO(pesos; linha_normalizada)` — força e
  fraqueza: qualquer um monta, e qualquer um pula os caps. 01–03 sem perceber.
