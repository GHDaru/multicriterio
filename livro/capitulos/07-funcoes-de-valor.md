# 07 — MAVT e Even Swaps: o valor não é linear

> **Estado da arte capturado em 2026-07** · última revisão 2026-08-10 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Construir** funções de valor por critério (pontos de quebra, monotonia) e
   **calcular** o valor multiatributo aditivo $V(a_i) = \sum_j w_j\, v_j(x_{ij})$.
2. **Demonstrar** que o SAW do cap. 04 é o caso particular de funções de valor
   lineares — e que curvá-las muda o pódio sem tocar nos pesos.
3. **Aplicar** o método dos Even Swaps para eliminar critérios e alternativas por
   trocas explícitas, sem calcular peso nenhum.
4. **Explicar** a premissa que sustenta a forma aditiva (independência preferencial) e
   o que fazer quando ela cai.

## O problema

Todos os métodos até aqui assumem, em silêncio, que valor cresce **linearmente** com o
desempenho: economizar R$ 60 mil vale o mesmo partindo de R$ 520 mil ou de R$ 400 mil.
Decisores reais não funcionam assim — abaixo do orçamento, cada real economizado vale
pouco; acima, dói progressivamente. E a área: de 55 m² para 70 m² muda a vida; de 70
para 85, menos. Ignorar a **forma** da preferência distorce o ranking tanto quanto
errar os pesos.

## De onde isto veio

**O aperto.** A pré-história favorita do campo é uma carta: a literatura conta que
**Benjamin Franklin**, em 1772, respondendo ao amigo Joseph Priestley (que agonizava
sobre aceitar ou não um emprego), descreveu sua "álgebra moral ou prudencial" — prós e
contras em colunas, riscando pares que se equivalem até a decisão ficar visível.
(Buscamos a carta na fonte primária aberta nesta rodada; o acesso falhou do nosso
ambiente, então **não citamos o texto** — só a atribuição, que segue na fila de
verificação.) Dois séculos depois, o aperto moderno: a análise de decisão do pós-guerra
tinha teoria da utilidade rigorosa para **uma** dimensão — e as decisões públicas dos
anos 1960–70 (usinas, aeroportos, orçamentos) chegavam com dez.

**O que se fazia antes.** Ou uma dimensão de cada vez (e a soma implícita do SAW, com
linearidade assumida em silêncio), ou nada de formal — comitê e retórica.

**A virada.** Keeney & Raiffa estenderam a arquitetura axiomática de von
Neumann–Morgenstern para $n$ atributos: enunciar **as condições** (independência
preferencial) sob as quais a forma aditiva com funções de valor $v_j$ existe — e
transformar a elicitação dessas curvas num procedimento. Vinte anos depois, os mesmos
autores (com Hammond) destilaram tudo de volta ao espírito da carta de Franklin: os
**Even Swaps** são a álgebra prudencial com disciplina de engenheiro — trocas
explícitas, um critério eliminado por vez.

**A ideia reaproveitável.** Duas pontas do mesmo fio. Da teoria: antes de usar uma
forma matemática cômoda, **pergunte que premissa comportamental ela exige** — e teste a
premissa, não a fórmula. Da prática: para reduzir um problema grande, **elimine
dimensões por trocas explícitas** — cada troca é pequena, auditável e reversível, e a
sequência inteira substitui o cálculo de pesos.

**O nome.** MAVT/MAUT são siglas descritivas (valor sem incerteza, utilidade com);
*Even Swaps* — "trocas equilibradas" — nomeia o gesto central do método.

| Afirmação | Selo |
|---|---|
| Franklin → Priestley (1772), "moral or prudential algebra" | ⏳ atribuição corrente; primária aberta existe, inacessível deste ambiente — item nº 1 da fila; sem citação verbatim até lá |
| Keeney & Raiffa (1976) como fundação axiomática multiatributo | ✓ᵐ (registro na bibliografia; conteúdo não lido) |
| Hammond, Keeney & Raiffa (1998), Even Swaps na HBR | ✓ᵐ (URL na bibliografia) |
| Contexto "decisões públicas dos anos 1960–70" | ⏳ narrativa corrente da história da análise de decisão |

## Fundamentos

**MAVT** (*Multi-Attribute Value Theory*, Keeney & Raiffa, 1976) é a fundação
axiomática dos métodos aditivos: sob **independência preferencial mútua** (a troca que
você aceita entre dois critérios não depende do nível dos demais), existe uma função de
valor aditiva $V = \sum_j w_j v_j(x_j)$, onde cada $v_j$ leva o desempenho físico a
valor em $[0,1]$ — e os pesos são **taxas de troca entre extremos** dos $v_j$
(exatamente o que o swing do cap. 03 elicita). Este livro declara os $v_j$ por pontos
de quebra com interpolação linear por partes (ADR 0006). Sob incerteza, a mesma
arquitetura com loterias vira MAUT — fora do nosso núcleo (ver MIT OCW IDS.333).

**Even Swaps** (Hammond, Keeney & Raiffa, 1998) é o irmão sem álgebra: iguale duas
alternativas em um critério por meio de uma troca explícita ("aceito 5 min a mais de
deslocamento por R$ 15 mil a menos?"), e o critério igualado **deixa de importar** para
aquele par — repita até sobrar uma escolha óbvia. É MAVT operado por perguntas, uma de
cada vez, e o melhor detector prático de independência violada: se a troca "depende"
de outro critério, a premissa caiu (Belton & Stewart, 2002 — e aí a forma aditiva não
vale; modele a interação ou troque de família de método).

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

**Passo 1 — declarar as curvas** (pesos inalterados: 0,35/0,25/0,25/0,15):

- Preço: $(340\text{k}, 1{,}0) \to (400\text{k}, 0{,}8) \to (520\text{k}, 0{,}0)$ —
  até 400 mil, perder valor devagar; acima, despencar.
- Área: $(55, 0) \to (70, 0{,}8) \to (85, 1{,}0)$ — saturação após 70 m².
- Deslocamento e Bairro: lineares (como antes).

**Passo 2 — avaliar e somar:**

| Alternativa | $v(\text{Preço})$ | $v(\text{Área})$ | $V$ | (era, no SAW linear) |
|---|---|---|---|---|
| **A1 — Centro** | 0,4667 | 0,3733 | **0,6067** | 0,5444 (1º) |
| A2 — Jardim | 0,8667 | 0,8000 | 0,5533 | 0,4472 (4º!) |
| A4 — Estação | 1,0000 | 0,0000 | 0,5375 | 0,5375 (2º) |
| A3 — Parque | 0,0000 | 1,0000 | 0,5250 | 0,5250 (3º) |

**A2 saltou de último para 2º** — seus R$ 380 mil caem na região onde preço vale muito
(0,8667 contra 0,7778 lineares) e seus 70 m² capturam quase toda a saturação da área.
Nenhum peso mudou. *Ambos os fatos — "linear ≡ SAW" e este pódio — são testes da etapa
07.*

**Passo 3 — Even Swaps no mesmo problema** (amostra): A1 vs A4 diferem em tudo; iguale
o Deslocamento — "quanto de preço A4 precisaria ceder para valer os 5 min a mais?". Se
o decisor responde "R$ 20 mil", A4 vira (360k, 55, 15, 2) e o Deslocamento sai da
comparação. Três trocas depois, sobra uma dominância — e a escolha se decide sem
nenhum vetor $w$.

## Quando usar (e quando não)

Funções de valor valem o esforço quando os desempenhos cobrem faixas largas (dinheiro,
tempo, risco) ou quando há limiares reais (orçamento, mínimo habitável) — e são o
antídoto para a crítica "seu modelo acha que tudo é linear". Even Swaps brilha com
poucas alternativas e um decisor disposto a responder trocas honestas; cansa com muitas.
Se a independência preferencial cai ("bairro só importa em apartamento grande"), a
forma aditiva — SAW, TOPSIS, MAVT — perde a licença: as saídas clássicas são funções
multilineares (Keeney & Raiffa, 1976) ou métodos de outranking (caps. 08–09), que não
somam nada.

### Leitura executiva

MAVT revela o que o SAW escondia: toda soma ponderada carrega funções de valor — o SAW
apenas as assume lineares sem avisar. Declarar as curvas é elicitar a *forma* da
preferência, e a forma muda pódio. **O que levar** hoje: para critérios com limiar
(orçamento!), desenhe a curva com o decisor antes de discutir pesos; e use uma rodada
de Even Swaps como teste de fumaça — se as trocas fluem, a forma aditiva se sustenta.

## Mão na massa — decisor-zero, etapa 07

Em `decisor-zero/etapas/07-funcoes-de-valor/`, nasce `motor/valor.py` (validação de
monotonia, interpolação por partes, `ranquear_mavt`) e a rota `POST /api/matriz/mavt`;
a página alterna funções lineares × curvas e mostra o salto de A2. Decisão da rodada:
o MAVT ainda **não** entra no catálogo do produto — exige UI de edição de curvas
(spec futura registrada no CHANGELOG). Exercício de completar: implemente a checagem
de "troca consistente" dos Even Swaps (dada uma troca declarada, aplicar à matriz e
verificar que o critério igualado sai da comparação) com teste.

## Segundo domínio — curvas de valor na decisão B2B

No fornecedor, as curvas são quase autoexplicativas: SLA tem **limiar de contrato**
($(99{,}0,\ 0) \to (99{,}5,\ 0{,}7) \to (99{,}95,\ 1{,}0)$ — atingir 99,5% captura
70% do valor, o resto é refinamento) e Custo tem orçamento ($(7.500,\ 1) \to
(9.500,\ 0{,}75) \to (12.000,\ 0)$ — acima de R$ 9.500 a dor acelera). Resultado com
os mesmos pesos: **F2 0,775 > F3 0,550 > F1 0,325** — o pódio do SAW se mantém, mas a
folga de F2 cresce (0,775 contra 0,673 no linear), porque seus 99,5% de SLA caem
exatamente no joelho da curva. Curvas não mudaram o vencedor aqui; mudaram o
**tamanho da vitória** — informação que importa para negociar contrato. *Teste
`test_segundo_dominio_curva_de_sla` da etapa 07.*

## Verificação

1. Por que MAVT linear ancorado em min/max dá exatamente o SAW? (Dica: objetivo 2 —
   compare $v_j$ linear com a fórmula min-max.)
2. Que pergunta você faria ao decisor para descobrir o ponto de quebra da curva de
   preço? (Dica: objetivo 1 — onde "começa a doer".)
3. Nos Even Swaps, por que o critério igualado pode ser ignorado dali em diante — e
   que premissa isso usa em silêncio? (Dica: objetivos 3–4.)

---

## Apêndice A — funções de valor nas ferramentas

- **MACBETH** (Bana e Costa & Vansnick, 1994; software M-MACBETH) constrói funções de
  valor cardinais a partir de julgamentos qualitativos — a alternativa mais rigorosa à
  nossa declaração direta de pontos (<https://m-macbeth.com/>).
- **1000minds** implementa elicitação por trocas (PAPRIKA), parente dos Even Swaps
  (<https://www.1000minds.com/>) — vendor; leitura complementar.
- **scikit-criteria** aceita transformações por critério no pipeline, onde as curvas
  deste capítulo se encaixariam (<https://scikit-criteria.quatrope.org/>).

## Apêndice B — gabarito comentado da Verificação

1. Com $v_j$ linear ancorada em (pior, 0) e (melhor, 1), a interpolação devolve
   exatamente $(x - \min)/(\max - \min)$ nos benefícios e o espelho nos custos — a
   fórmula min-max do cap. 03. Somar com os mesmos pesos ⇒ o mesmo escore do SAW,
   termo a termo.
2. "A partir de que preço a compra começa a doer de verdade?" (e depois: "onde ela se
   torna proibitiva?"). As respostas ancoram o ponto de quebra e a inclinação de cada
   trecho — elicitação de forma, não de peso.
3. Depois da troca, as duas alternativas empatam naquele critério; qualquer forma
   aditiva atribui a ele a mesma parcela nas duas — ele não discrimina mais o par. A
   premissa silenciosa: a troca declarada não depende dos níveis dos demais critérios
   (independência preferencial — se depender, a simplificação não vale).
