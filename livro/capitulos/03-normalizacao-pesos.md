# 03 — Normalização e pesos: os dois insumos de toda agregação

> **Estado da arte capturado em 2026-07** · última revisão 2026-07-30 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Calcular** as duas normalizações centrais do livro — min-max e vetorial — e
   **explicar** o que cada uma preserva, o que destrói e qual resolve a direção.
2. **Avaliar** por que a escolha de normalização é decisão de modelagem (pode trocar o
   ranking final), e não um default de biblioteca.
3. **Elicitar** pesos por quatro caminhos — rating direto, ROC, swing e entropia — e
   **comparar** o que cada um realmente mede.
4. **Distinguir** importância declarada (preferência do decisor) de poder de
   discriminação (propriedade dos dados) — a confusão mais comum em pesos.

## O problema

A etapa 02 deixou quatro alternativas na fronteira de Pareto, em conflito puro. Para
compará-las, o cap. 01 já mostrou o beco: somar colunas em R$, m², minutos e notas 1–5
produz "o preço com ruído". Antes de qualquer método compensatório, duas perguntas
precisam de resposta explícita: **como tornar as colunas comensuráveis?** (normalização)
e **de onde vem o vetor $w$?** (elicitação de pesos). As duas parecem detalhe técnico;
as duas mudam resultado.

## Fundamentos

**Normalização.** Hwang & Yoon (1981) já sistematizavam as transformações que levam
cada coluna a uma escala comum; Krishnan (2022), revisando quatro décadas de prática,
mostra que a literatura conhece dezenas de variantes e que **a troca de normalização
pode inverter rankings** — a escolha, portanto, é parte declarável do modelo. As duas
que este livro usa:

- **min-max**: $r_{ij} = \dfrac{x_{ij} - \min_j}{\max_j - \min_j}$ (benefício) e
  $r_{ij} = \dfrac{\max_j - x_{ij}}{\max_j - \min_j}$ (custo). Leva tudo a $[0,1]$,
  **resolve a direção** (1 = melhor da coluna) e é sensível aos extremos: entra uma
  alternativa nova com preço recorde, todos os $r$ da coluna mudam — guarde isso para o
  rank reversal (cap. 11).
- **vetorial**: $r_{ij} = \dfrac{x_{ij}}{\sqrt{\sum_i x_{ij}^2}}$. Preserva proporções,
  dá norma 1 à coluna e **não resolve a direção** — o método que a consome (TOPSIS,
  cap. 06) trata benefício/custo depois. Somar colunas vetoriais "de benefício" com
  "de custo" sem esse cuidado é erro clássico.

**Pesos.** Edwards & Barron (1994), no par SMARTS/SMARTER, dão as duas técnicas de
elicitação que o livro adota como padrão: **swing** (parta do pior cenário em tudo e
pergunte "qual salto pior→melhor você mais quer? esse vale 100" — o único procedimento
aqui que olha as **amplitudes reais** do problema) e **ROC** (se o decisor só consegue
ordenar critérios, use o centroide dos pesos compatíveis com essa ordem:
$w_k = \frac{1}{n}\sum_{i=k}^{n} \frac{1}{i}$). Belton & Stewart (2002) alertam para o
que o rating direto ignora: peso sem referência às amplitudes é número solto — "preço
importa muito" significa outra coisa se os preços variam 5% ou 50%. E o **método da
entropia** (Hwang & Yoon, 1981) não pergunta nada a ninguém: mede quanta informação
cada coluna carrega ($d_j = 1 - e_j$, com $e_j$ a entropia de Shannon normalizada) —
pesos "objetivos" que capturam discriminação, não importância.

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

**Passo 1 — min-max no caso âncora** (repare: 1,0000 é sempre o melhor da coluna,
inclusive nos custos):

| | Preço | Área | Deslocamento | Bairro |
|---|---|---|---|---|
| A1 — Centro | 0,3889 | 0,2333 | **1,0000** | 0,6667 |
| A2 — Jardim | 0,7778 | 0,5000 | 0,0000 | 0,3333 |
| A3 — Parque | 0,0000 | **1,0000** | 0,5000 | **1,0000** |
| A4 — Estação | **1,0000** | 0,0000 | 0,7500 | 0,0000 |

**Passo 2 — vetorial no mesmo problema** (norma 1 por coluna; note o Preço: a mais
**cara**, A3, fica com o maior valor — a direção não foi resolvida):

| | Preço | Área | Deslocamento | Bairro |
|---|---|---|---|---|
| A1 — Centro | 0,5256 | 0,4499 | 0,3015 | 0,5443 |
| A2 — Jardim | 0,4439 | 0,5079 | 0,7035 | 0,4082 |
| A3 — Parque | **0,6074** | 0,6168 | 0,5025 | 0,6804 |
| A4 — Estação | 0,3972 | 0,3991 | 0,4020 | 0,2722 |

**Passo 3 — quatro caminhos para $w$, mesmo decisor, números diferentes:**

| Técnica | O que se pergunta | Resposta dada | Pesos resultantes (Preço, Área, Desl., Bairro) |
|---|---|---|---|
| Rating direto | "distribua 100 pontos" | 35 / 25 / 25 / 15 | 0,3500 · 0,2500 · 0,2500 · 0,1500 |
| ROC | "só ordene" | Preço ≻ Área ≻ Desl. ≻ Bairro | 0,5208 · 0,2708 · 0,1458 · 0,0625 |
| Swing | "qual salto pior→melhor vale mais?" | 100 / 60 / 70 / 40 | 0,3704 · 0,2222 · 0,2593 · 0,1481 |
| Entropia | ninguém — só os dados | — | 0,2365 · 0,2948 · 0,2178 · 0,2509 |

Três leituras: (1) o rating 35/25/25/15 é a origem dos pesos que o livro usa desde o
cap. 01 — agora você sabe de onde vieram; (2) o ROC **exagera** o primeiro do ranking
(0,5208 para o Preço) — é o preço de só ordenar; (3) a entropia elegeu a **Área** como
critério de maior peso, contrariando todos os métodos subjetivos — porque mede outra
coisa (a Área é a coluna que mais discrimina as quatro alternativas, não a que o
decisor mais valoriza). *Todas as tabelas deste capítulo são reproduzidas pelos testes
da etapa 03 (`test_normalizacao.py`, `test_pesos.py`).*

## Quando usar (e quando não)

Min-max quando o método precisa de direção resolvida e escala comum (SAW, cap. 04);
vetorial quando o método pede proporções preservadas (TOPSIS, cap. 06) — e nunca misture
as duas na mesma agregação. No vetor $w$: swing é o padrão-ouro prático (considera
amplitudes), ROC é o fallback honesto quando só há ranking, rating direto serve para
rascunho — e entropia **não substitui preferência**: use-a como diagnóstico ("estou
dando peso alto a um critério que não separa ninguém?") ou em problemas sem decisor
identificável. Regra do livro: pesos entram no modelo **com o método que os produziu
declarado** — "w = (0,35; 0,25; 0,25; 0,15), rating direto" é auditável; "w veio de uma
reunião" não é.

### Leitura executiva

Normalização e pesos são as duas alavancas silenciosas de qualquer ranking
compensatório: a primeira decide o que "1" significa em cada coluna, a segunda decide
quanto cada coluna fala. Nenhuma é neutra — min-max reage a extremos, ROC exagera o
topo, entropia mede discriminação e não importância. **O que levar** hoje: declare a
normalização e a técnica de pesos como parte do modelo (não como default), e quando os
pesos vierem de gente, prefira swing — é o único procedimento simples que obriga o
decisor a olhar as amplitudes reais antes de opinar.

## Mão na massa — decisor-zero, etapa 03

Em `decisor-zero/etapas/03-normalizacao-pesos/`, nascem `motor/normalizacao.py`
(min-max e vetorial) e `motor/pesos.py` (rating, ROC, swing, entropia), com as rotas
`POST /api/normalizar` e `POST /api/pesos` — e a página deixa você alternar entre as
duas normalizações e ver o aviso sobre direção. Exercício de completar: implemente a
normalização **linear pela soma** ($r_{ij} = x_{ij} / \sum_i x_{ij}$, com inversão
prévia nos custos), adicione-a ao dicionário `NORMALIZACOES` e escreva o teste que
verifica que cada coluna soma 1 — sem quebrar os existentes.

## Segundo domínio — normalização e entropia na decisão B2B

O caso do fornecedor expõe a incomensurabilidade em grau extremo: R$ 12.000 convivem
com 99,95% e notas 1–5 na mesma matriz. O min-max resolve — e a entropia conta uma
história diferente da do apartamento: os pesos "dos dados" saem quase equalizados
(Custo 0,2295 · Latência 0,2764 · SLA 0,2450 · Suporte 0,2491), porque as três
alternativas se espalham de forma parecida em todas as colunas. Lição: entropia quase
uniforme significa "nenhuma coluna é redundante nem decisiva sozinha" — a
responsabilidade volta inteira para os pesos subjetivos. *Teste
`test_segundo_dominio_entropia_quase_uniforme` da etapa 03.*

## Verificação

1. Na tabela vetorial do passo 2, por que seria um erro somar as colunas ponderadas
   diretamente para ranquear? (Dica: objetivo 1 — quem resolve a direção?)
2. O decisor diz "preço é o dobro da área". Rating direto e swing podem dar vetores
   diferentes para essa mesma frase? Por quê? (Dica: objetivo 3 — amplitudes.)
3. A entropia deu peso máximo à Área; o decisor jura que Preço importa mais. Quem está
   "certo"? (Dica: objetivo 4 — são perguntas diferentes.)

---

## Apêndice A — normalização e pesos nas ferramentas

- **pymcdm** traz dezenas de normalizações em `pymcdm.normalizations` e técnicas de
  pesos em `pymcdm.weights` (incluindo entropia) — o catálogo mais completo para
  comparar com os nossos resultados (<https://github.com/kotbaton/pymcdm>).
- **scikit-criteria** trata normalização como transformador de pipeline
  (`skcriteria.preprocessing.scalers`), reforçando a tese do capítulo: é passo
  declarado do modelo, não efeito colateral do método
  (<https://scikit-criteria.quatrope.org/>).
- **pyDecision** documenta por notebook qual normalização cada método assume — leitura
  útil antes de comparar resultados entre bibliotecas
  (<https://github.com/Valdecy/pyDecision>).
- O survey aberto de Krishnan (2022) na *Frontiers in Big Data* cataloga os critérios
  publicados para escolher normalização
  (<https://pmc.ncbi.nlm.nih.gov/articles/PMC9433668/>).

## Apêndice B — gabarito comentado da Verificação

1. Porque a normalização vetorial **não resolve a direção**: nas colunas de custo, o
   maior valor cru continua com o maior $r$. Somar colunas ponderadas sem tratar a
   direção premiaria o mais caro e o mais distante — o método que consome vetorial
   (TOPSIS) trata a direção depois, na escolha do ideal.
2. Podem. "Preço é o dobro da área" no rating direto vira $w_1 = 2w_2$ sem contexto;
   no swing a pergunta é sobre o salto pior→melhor **daquele problema** — se a faixa
   de preços for estreita, o salto de preço vale pouco e o swing devolve razão menor
   que 2. O swing amarra o peso às amplitudes; o rating não.
3. Nenhum dos dois está "errado" — medem coisas diferentes. A entropia responde "quais
   colunas separam as alternativas deste conjunto"; o decisor responde "o que importa
   para mim". Use a entropia como diagnóstico (ex.: peso alto em coluna que não
   discrimina é peso desperdiçado) e o decisor como fonte da preferência.
