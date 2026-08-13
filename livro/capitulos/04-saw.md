# 04 — SAW: o método aditivo (e o primeiro ranking do livro)

> **Estado da arte capturado em 2026-07** · última revisão 2026-08-13 · [histórico](../HISTORICO.md)

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

## De onde isto veio

**O aperto.** A soma ponderada entra na literatura gerencial por uma **briga** — e o
motivo da briga é o que ensina. Em outubro de 1953, **C. West Churchman e Russell
Ackoff**, do Case Institute of Technology, submetem uma resposta a um trabalho recente
que propunha medir valor a partir de "estados-armadilha" (*trapped states*): situações
de onde o sistema não sai mais, sendo ganhar ou perder uma guerra o exemplo. A objeção
deles é curta e demolidora: definir valor último em termos de *vencer* é pôr o carro
diante dos bois. O contraexemplo que usam é doméstico — um enxadrista pode querer
**perder** a partida para um adversário a quem quer bem. Vitória precisa ser definida
em função do que se valoriza, e não o contrário.

**O que se fazia antes.** Ou o valor amarrado a um desfecho binário (a crítica acima),
ou — na prática das empresas — **cifrão em tudo**. O manual que os dois assinam três
anos depois com Arnoff (*Introduction to Operations Research*, 1957, capítulo
"Weighting Objectives", também lido) abre justamente contra esse hábito e contra o
apelido dado aos objetivos que resistem à conversão: chamá-los de "intangíveis" é
confundir *intocável pelo dinheiro* com *impossível de medir*. Segurança, boa vontade,
o custo de uma lesão: medem-se por outro método.

**A virada.** Separar a decisão em **duas medidas independentes** — a eficiência de um
curso de ação para produzir cada desfecho, e a importância de cada desfecho — e
escolher o que maximiza a eficiência total ponderada. É o $\sum_j w_j r_{ij}$ deste
capítulo, com os pesos elicitados das escolhas declaradas de quem decide, aplicável a
qualquer número de objetivos e de decisores. E, no mesmo artigo, a honestidade que a
literatura posterior costuma esquecer: as três hipóteses estão enunciadas (A-1 a A-3),
e a de aditividade vem **acompanhada dos casos em que falha** — se um desfecho implica
o outro, ou se os dois são mutuamente exclusivos (ganhar exatamente 10 mil e ganhar
exatamente 20 mil ao ano), somar valores não significa nada. A axiomatização completa
viria em 1967 com Fishburn — publicada, detalhe saboroso, como **carta ao editor** da
*Operations Research*; mas as condições de validade nasceram junto com o método, não
depois dele.

Do manual de 1957 vem a segunda virada, prática: nota solta precisa de **contraprova**.
O "método das comparações sucessivas" atribui valores tentativos e os testa contra
combinações ("você prefere $O_1$, ou $O_2$+$O_3$+$O_4$ juntos?"), ajustando até a
coerência e normalizando pela soma — vinte anos antes do CR do cap. 05, a mesma ideia
de julgamento redundante como detector de contradição.

**A ideia reaproveitável.** Duas. (1) **Defina valor antes de definir vitória.** Quando
alguém propõe medir sucesso por um desfecho ("bater a meta", "vencer o concorrente",
"passar no teste"), a pergunta que desarma é a do enxadrista: e se o desfecho não for
o que se valoriza? (2) **Publique a hipótese junto com o caso em que ela falha.** A
aditividade nasceu com sua própria bula; foi a literatura de repetição que perdeu a
bula pelo caminho.

**O nome.** SAW (*Simple Additive Weighting*) e WSM (*Weighted Sum Model*) são rótulos
posteriores e descritivos: o artigo de 1954 não batiza nada, só chama o que propõe de
uma medida **aproximada** de valor — a modéstia está no título.

| Afirmação | Selo |
|---|---|
| Churchman & Ackoff (1954), Case Institute of Technology, recebido em 20/10/1953; a réplica aos "trapped states"; o enxadrista que quer perder; as duas medidas (eficiência × importância); hipóteses A-1 a A-3 com os casos de falha da aditividade | ✓ artigo lido (*JORSA* 2(2), 172–187; DOI 10.1287/opre.2.2.172) |
| Comentários convidados de Nicholas M. Smith Jr. no mesmo fascículo (p. 181) | ✓ nota de rodapé do artigo lido |
| Método das comparações sucessivas, caso executivo trabalhado e a crítica aos "intangíveis" | ✓ capítulo "Weighting Objectives" lido em Churchman, Ackoff & Arnoff (1957) — exemplar aberto no Internet Archive |
| Fishburn (1967) axiomatiza a utilidade aditiva, publicado como carta ao editor | ✓ᵐ (DOI e formato verificados na bibliografia; conteúdo não lido) |

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
métodos como o AHP (cap. 05) existem para extrair pesos de comparações mais
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

## Segundo domínio — SAW na decisão B2B (o outro desfecho)

Fornecedores, pesos 0,40/0,20/0,25/0,15: **F2 — Regional 0,6732 > F3 — Nicho 0,5500 >
F1 — Hiperescala 0,3250**. Compare os desfechos: no apartamento, o 1º e o 2º se
separam por 0,007; aqui, por **0,12** — dezessete vezes mais. F2 não vence por ajuste
fino de pesos; vence porque é boa em quase tudo. É a diferença entre vitória frágil e
vitória robusta, que o cap. 11 vai medir com instrumento (varredura de pesos).
*Teste `test_segundo_dominio_f2_vence_com_folga` da etapa 04.*

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
  parâmetro explícito, a tese do cap. 03 em código; nossa etapa 04 valida os escores
  contra ela em teste (<https://github.com/kotbaton/pymcdm>).
- **scikit-criteria** o expõe como `WeightedSumModel`, dentro de um pipeline em que
  scaler e inversão de direção são passos declarados
  (<https://scikit-criteria.quatrope.org/>).
- **pyDecision** traz SAW/WSM com notebook de exemplo
  (<https://github.com/Valdecy/pyDecision>).
- Em planilhas, o SAW é a fórmula `=SOMARPRODUTO(pesos; linha_normalizada)` — força e
  fraqueza: qualquer um monta, e qualquer um pula os caps. 01–03 sem perceber.

## Apêndice B — gabarito comentado da Verificação

1. $V(A2) = 0{,}35 \cdot 0{,}7778 + 0{,}25 \cdot 0{,}5 + 0{,}25 \cdot 0 + 0{,}15
   \cdot 0{,}3333 = 0{,}2722 + 0{,}125 + 0 + 0{,}05 = 0{,}4472$ — último lugar: o
   deslocamento de 35 min (r = 0) custou caro.
2. Viola a **independência preferencial**: o valor de um ponto de Bairro passa a
   depender do nível de Área. A forma aditiva perde a licença; o instrumento certo é
   o cap. 07 (funções multilineares/MAUT) ou repensar os critérios.
3. Mudou a **magnitude relativa** dos pesos, não a ordem: o ROC concentra 0,5208 no
   1º do ranking (contra 0,35 do rating). Com metade do peso total num critério em
   que A4 é imbatível (a mais barata), o pódio virou — ordem igual, números
   diferentes, vencedor diferente.
