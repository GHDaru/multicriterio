# Apêndice D — O método em sala: escolher um carro popular

> **Estado da arte capturado em 2026-08** · última revisão 2026-08-14 · [histórico](HISTORICO.md)
>
> **Exercício conduzido pelo autor com seus alunos**, transcrito aqui na ordem em
> que aconteceu. O método em oito passos é dele; a proveniência de cada passo está
> em aberto e declarada ao final (Princípio VIII). Todos os números são reproduzidos
> pelos testes da etapa 15 do `decisor-zero`.

## O que este apêndice é

Os capítulos 01–13 apresentam métodos consagrados, um a um. Este apêndice faz o
caminho inverso: mostra **um método completo em operação**, do enunciado à
recomendação, com uma turma real decidindo em voz alta. O valor está menos no
resultado (qual carro ganhou) e mais no que a sala descobriu no caminho — três
decisões aparentemente burocráticas que, no fim, decidiram a compra.

A espinha são oito passos:

| # | Passo | A pergunta que responde |
|---|---|---|
| 1 | Definir o problema | O que exatamente está sendo decidido, e por quem? |
| 2 | Levantar alternativas | Quais opções entram na disputa? |
| 3 | Definir os atributos | Sob quais aspectos elas serão comparadas? |
| 4 | Ir a campo | Quais são os números reais de cada uma? |
| 5 | **Criterizar** | Como comparar escalas, faixas e naturezas diferentes? |
| 6 | Ponderar | Quanto vale cada critério em relação aos outros? |
| 7 | Medida resumo | Como consolidar tudo num único número? |
| 8 | Sensibilidade | O resultado se sustenta? O que o faria mudar? |

## Passo 1 — Definir o problema

> Um pai vai dar um carro ao filho que começa a universidade. Como as despesas da
> vida universitária apertam o orçamento, será um **carro popular zero**, escolhido
> pelo **melhor custo-benefício**.

Três coisas já estão embutidas nesse enunciado curto, e vale extraí-las antes de
seguir:

- **"Melhor custo-benefício" ainda não é um critério** — é uma frase. Tornar essa
  frase operacional é o trabalho dos passos 3 a 7. O enunciado é deliberadamente
  vago porque é assim que decisões chegam.
- **Quem decide não é quem usa.** O pai escolhe; o filho dirige. Sempre que um
  atributo depender de gosto ("conforto", "confiança na marca"), a pergunta
  *de quem é a preferência?* volta à mesa — é o território do cap. 12.
- **"Popular" e "zero" são restrições, não critérios.** Filtram quem entra na
  lista; não pontuam ninguém. A distinção é a do cap. 02: restrição elimina,
  critério ordena.

## Passo 2 — Levantar alternativas

A turma fixou uma entrada de linha por fabricante, todas 1.0, ano-modelo 2026:

| # | Alternativa | Versão |
|---|---|---|
| A1 | Renault Kwid | Zen 1.0 |
| A2 | Chevrolet Onix | 1.0 |
| A3 | Peugeot 208 | Style 1.0 |
| A4 | Fiat Mobi | Like 1.0 |

**Contexto de 2026**: o piso do mercado brasileiro estava entre R$ 67 mil e R$ 107
mil, com Mobi, Kwid e Citroën C3 revezando o posto de zero-quilômetro mais barato
do país a golpe de promoção. O "carro popular de R$ 50 mil" já não existia.

Ao travar todas as alternativas em 1.0, a cilindrada deixou de ser critério e virou
filtro: as quatro ficam entre 71 e 82 cv. Um atributo que não discrimina só
adiciona ruído (cap. 02) — e reconhecê-lo cedo poupa uma coluna inútil.

### O achado do passo 2

Rodando o filtro de dominância — que não custa nada e não exige peso algum —
**nenhuma alternativa é dominada**: as quatro estão na fronteira de Pareto. Mas o
Kwid escapa por pouco. Comparado ao Onix, ele perde em cinco dos seis atributos e
vence **só no consumo**, por 0,9 km/l.

E aqui está a lição: se a sala tivesse escolhido **consumo rodoviário** em vez de
urbano (Kwid 15,4 × Onix 16,3), o Onix venceria também nesse atributo, dominaria o
Kwid nos seis e o Kwid **sairia da análise antes de qualquer cálculo**. Uma decisão
de modelagem tomada de passagem no passo 4 determina se uma alternativa existe no
passo 5.

## Passo 3 — Definir os atributos

O passo abre com uma observação do autor: **costuma haver uma dicotomia entre custo
e benefício**. Os seis escolhidos:

| Atributo | Natureza | Direção |
|---|---|---|
| **Preço** | custo | ↓ |
| **Consumo** | benefício (em km/l) | ↑ |
| **Conforto** | benefício | ↑ |
| **Segurança** | benefício | ↑ |
| **Infotenimento** | benefício | ↑ |
| **Confiança** | benefício **de percepção** — nasce qualitativo | ↑ |

A **Confiança** entrou de propósito: o autor queria que a turma lidasse com um
atributo que não vem em unidade nenhuma, para entender que percepção também é
informação decisória e precisa de tratamento explícito — não de exclusão.

Repare que "consumo" só ganha direção depois de escolhida a unidade: em km/l é
benefício, em L/100 km é custo. O mesmo atributo, direção invertida. Direção errada
inverte veredito em silêncio.

## Passo 4 — Ir a campo

A coleta usou uma fonte única de comparação técnica, com os quatro carros lado a
lado. **Fonte única não é preciosismo**: na primeira tentativa de levantar preços em
quatro sites diferentes, dois dos quatro valores estavam errados para as versões
travadas no passo 2 — misturavam preço promocional com preço de tabela, e datas
diferentes. Preço é o dado mais perecível do exercício.

Para os três atributos sem coluna própria na fonte (Conforto, Segurança,
Infotenimento), a turma criou uma régua de contagem sobre a legenda de cores do
comparativo: **item verde vale 1 ponto, amarelo vale 0,5**.

A matriz que saiu de campo:

| Alternativa | Preço ↓ | Consumo ↑ | Conforto ↑ | Segurança ↑ | Infoten. ↑ | Confiança ↑ |
|---|---|---|---|---|---|---|
| Kwid Zen | R$ 82.790 | 14,4 | 10 | 18 | 4 | Baixa |
| Onix 1.0 | R$ 81.837 | 13,5 | 18 | 20 | 11 | **Alta** |
| 208 Style | **R$ 106.990** | 13,6 | 18 | **21** | 9 | Baixa |
| Mobi Like | **R$ 66.934** | **14,5** | 7,5 | 16,5 | 5 | Média |

Consumo: urbano, gasolina, em km/l.

Um problema encontrado e **não resolvido** merece registro, porque é o tipo de
coisa que se esconde numa planilha: os dados de segurança do Latin NCAP vinham em
**pontos** para três carros e em **percentual** para o 208 — protocolos de épocas
diferentes. Postos na mesma coluna sem tratamento, seriam grandezas distintas
somadas. A régua de contagem de itens contornou o problema, mas ao custo de medir
*quantidade de equipamento*, não *desempenho em ensaio de colisão*.

## Passo 5 — Criterização

> **A pergunta**: como comparar atributos com escalas, faixas de valores e
> naturezas diferentes — alguns deles qualitativos?

Este é o passo que dá nome ao método, e a palavra é precisa. **Atributo** é a
propriedade medida (preço em reais, consumo em km/l). **Critério** é o atributo já
com direção de preferência e escala de valor. Criterizar é a transformação de um no
outro; não é "normalizar números".

Duas operações:

1. **Declarar a direção** de preferência de cada atributo;
2. **Levar do domínio original ao domínio normalizado** $[0,1] \times C$, com
   **C = 10** — uma nota de 0 a 10.

O C não muda ranking algum (multiplicar tudo por constante positiva preserva
qualquer ordenação), mas muda quem entende a tabela: "8,6" é lido sem tradução por
qualquer aluno brasileiro; "0,86" pede explicação. É escolha de comunicação.

### Forma 1 — tabela de-para (para o qualitativo)

| Rótulo | Nota |
|---|---|
| Alta | 10 |
| Média | 7 |
| Baixa | 4 |

Duas afirmações estão embutidas aí, e nenhuma é neutra. O **espaçamento uniforme**
(de 3 em 3) diz que a distância de "Alta" a "Média" vale o mesmo que de "Média" a
"Baixa". E o **piso em 4**, não em 0, diz que o pior rótulo ainda leva 40% da
régua — ou seja, a tabela já decidiu que Confiança pode punir no máximo 6 pontos,
antes de qualquer discussão de peso. Guarde essa escolha: ela reaparece no passo 8
decidindo o exercício.

### Forma 2 — interpolação

O recurso de quadro é um "I" maiúsculo ligando as duas escalas:

```
      Vmax ──────────── Cmax        (melhor valor  →  10)
        │                 │
       vi  ────────────  ci         (o que tenho  →  o que quero)
        │                 │
      Vmin ──────────── Cmin        (pior valor   →   0)
```

A proporção que o desenho torna evidente:

$$\frac{v_i - V_{min}}{V_{max} - V_{min}} = \frac{c_i - C_{min}}{C_{max} - C_{min}}
\qquad\Longrightarrow\qquad
c_i = C_{min} + (v_i - V_{min})\cdot\frac{C_{max} - C_{min}}{V_{max} - V_{min}}$$

A dedução em sala usa uma conversão que ninguém contesta — Celsius para Fahrenheit,
com as âncoras da água (0 ↔ 32, 100 ↔ 212), que devolve $c_i = 32 + 1{,}8\,v_i$.
Só depois a mesma fórmula vai para o Conforto (0 ↔ 0, 20 ↔ 10), onde se reduz a
$c_i = v_i/2$.

**A direção de preferência entra pelas âncoras, não por uma regra à parte**: num
critério de custo, basta amarrar o melhor valor ao 10. O Preço foi ancorado em
R$ 60.000 ↔ 10 e R$ 110.000 ↔ 0.

### Forma 3 — fórmula do máximo

Caso particular da interpolação com o piso no zero real ($V_{min} = 0$,
$C_{min} = 0$):

$$c_i = \frac{10\,v_i}{V_{max}}$$

Aplicada a Conforto (teto 20) e Segurança (teto 21).

### A decisão mais fina do passo

Ancorar Segurança em **21 ↔ 10 e 0 ↔ 0** — em vez de esticar o pior da amostra até
zero — muda muito mais do que parece:

| | Segurança na régua min-max | Segurança pela escala real |
|---|---|---|
| Kwid | 3,33 | **8,57** |
| Onix | 7,78 | **9,52** |
| 208 | 10,00 | 10,00 |
| **Mobi** | **0,00** | **7,86** |

Os dados brutos são idênticos. Na régua min-max, o Mobi "não tem segurança"; pela
escala real, ele tem 16,5 dos 21 itens — quase 80% do que o melhor tem. A primeira
leitura é falsa, e ainda faz a nota de todos depender de quem entrou na comparação:
se um quinto carro pior aparecesse, o Mobi deixaria de ser zero e a tabela inteira
se moveria. É a porta de entrada do rank reversal (cap. 11). **Âncora externa
imuniza contra isso; âncora observada, não.**

### A regra do piso levantado

Consumo e Infotenimento receberam piso 5 em vez de 0. O motivo é a faixa: o consumo
dos quatro varia de 13,5 a 14,5 km/l — 1 km/l separa o melhor do pior. Mandar essa
diferença para a régua inteira transformaria 7% de diferença real em 100% de
diferença de nota.

Daí a regra que o exercício produziu, e que vale enunciar:

> **Ancore no zero real quando ele existir e a faixa for larga; levante o piso
> quando a diferença entre o melhor e o pior for pequena demais para justificar a
> régua inteira.** Comprimir demais faz o critério virar enfeite; exagerar faz uma
> diferença irrelevante gritar como se fosse total.

### O resultado do passo 5

| Critério | De | Para | Tipo de âncora |
|---|---|---|---|
| Preço ↓ | 60.000 / 110.000 | 10 / 0 | externa |
| Consumo ↑ | 13,5 / 14,5 | 5 / 10 | observada, piso levantado |
| Conforto ↑ | 0 / 20 | 0 / 10 | escala real |
| Segurança ↑ | 0 / 21 | 0 / 10 | escala real |
| Infotenimento ↑ | 4 / 11 | 5 / 10 | observada, piso levantado |
| Confiança ↑ | Baixa / Média / Alta | 4 / 7 / 10 | de-para |

| | Preço | Consumo | Conforto | Segurança | Infoten. | Confiança |
|---|---|---|---|---|---|---|
| **Kwid Zen** | 5,44 | 9,50 | 5,00 | 8,57 | 5,00 | 4,00 |
| **Onix 1.0** | 5,63 | 5,00 | 9,00 | 9,52 | **10,00** | **10,00** |
| **208 Style** | **0,60** | 5,50 | 9,00 | **10,00** | 8,57 | 4,00 |
| **Mobi Like** | **8,61** | **10,00** | 3,75 | 7,86 | 5,71 | 7,00 |

## Passo 6 — Ponderar

A construção parte de um **grafo de dominância** entre critérios: monta-se a matriz
binária em que $a_{ij} = 1$ quando o critério $i$ é pelo menos tão importante quanto
o $j$ — **incluindo a diagonal**. A autodominância não é detalhe: sem ela, o último
critério somaria zero e um critério que o decisor conscientemente incluiu sairia do
modelo com peso nulo, o que é pior do que não tê-lo posto.

Com a ordem declarada, a soma das linhas dá $n, n-1, \dots, 1$ — e daí a
simplicidade prática que o método entrega: **atribua $n$ ao mais importante e 1 ao
menos importante**. O total é $n(n+1)/2$; aqui, 21.

| Critério | Pontos | Peso |
|---|---|---|
| Preço | 6 | 0,2857 |
| Segurança | 5 | 0,2381 |
| Consumo | 4 | 0,1905 |
| Confiança | 3 | 0,1429 |
| Conforto | 2 | 0,0952 |
| Infotenimento | 1 | 0,0476 |

### Peso declarado não é influência

Multiplicando cada peso pela **amplitude real** da sua coluna criterizada, aparece
o que cada critério de fato consegue mexer no resultado:

| Critério | Peso | Amplitude | Influência real |
|---|---|---|---|
| Preço | 0,286 | 8,01 | **42,8%** |
| Consumo | 0,190 | 5,00 | 17,8% |
| Confiança | 0,143 | 6,00 | **16,0%** |
| **Segurança** | **0,238** | **2,14** | **9,5%** |
| Conforto | 0,095 | 5,25 | 9,4% |
| Infotenimento | 0,048 | 5,00 | 4,5% |

**A Segurança foi declarada o segundo critério mais importante e pesa como o
quarto** — menos que a Confiança, colocada em quarto, e empatada com o Conforto,
colocado em quinto. O motivo é aritmético: os quatro carros tiram entre 7,86 e
10,00 em segurança, e peso alto sobre coluna achatada não move resultado.

A pergunta honesta que isso levanta em sala não é "erramos o peso?", e sim: **a
compressão é fiel ou é artefato?** Se os quatro populares realmente têm pacotes de
segurança parecidos, a baixa influência está correta e o modelo está sendo sincero.
Se a contagem de itens é uma régua grosseira demais para captar o que importa,
então o conserto é no passo 4 — medir melhor — e não no peso.

## Passo 7 — Medida resumo

Multiplicar peso por nota e somar. A soma ponderada e a média ponderada dão a mesma
ordem (dividir por $\sum w$ é constante positiva); a média é preferível por
comunicação, pois devolve o resultado na mesma régua 0–10 dos critérios.

| # | Alternativa | Soma ponderada | Média ponderada |
|---|---|---|---|
| 1 | **Fiat Mobi Like 1.0** | 165,18 | **7,87** |
| 2 | Chevrolet Onix 1.0 | 159,42 | 7,59 |
| 3 | Renault Kwid Zen 1.0 | 140,51 | 6,69 |
| 4 | Peugeot 208 Style 1.0 | 114,18 | 5,44 |

De onde veio a nota de cada um (contribuição de cada critério):

| | Preço | Segurança | Consumo | Confiança | Conforto | Infoten. |
|---|---|---|---|---|---|---|
| Kwid | 1,56 | 2,04 | 1,81 | 0,57 | 0,48 | 0,24 |
| Onix | 1,61 | 2,27 | 0,95 | **1,43** | **0,86** | **0,48** |
| 208 | 0,17 | **2,38** | 1,05 | 0,57 | 0,86 | 0,41 |
| Mobi | **2,46** | 1,87 | **1,91** | 1,00 | 0,36 | 0,27 |

**O Mobi vence perdendo em quatro dos seis critérios.** Ele ganha só em preço e
consumo — mas são justamente os dois com maior amplitude efetiva, e isso basta. O
Onix vence em quatro e fica em segundo.

O 208 é o caso mais didático da tabela: tira a **melhor nota de segurança do
exercício** (2,38 de contribuição, o maior valor isolado da matriz) e termina em
último, porque os R$ 106.990 lhe custam quase todo o critério de maior peso —
0,17 de 2,86 possíveis.

## Passo 8 — Sensibilidade

A margem do primeiro sobre o segundo é **0,275 ponto: 2,7% da régua**. Apertado o
bastante para justificar os três instrumentos a seguir.

### (a) A pergunta de negociação

Em vez de "o resultado é robusto?", pergunte "**de quanto seria o desconto que
vira o jogo?**":

| Alternativa | Distância | Desconto necessário | Preço-alvo |
|---|---|---|---|
| **Onix** | 0,275 | **−R$ 4.804** | R$ 77.033 |
| Kwid | 1,175 | −R$ 20.558 | R$ 62.232 |
| 208 | 2,428 | −R$ 42.496 | R$ 64.494 |

Um desconto de R$ 4.804 no Onix — 5,9% do preço — empata a disputa. Isso é
negociação de sábado de manhã, não hipótese de laboratório. Já o 208 precisaria
custar **menos que o Mobi de tabela** apenas para empatar. É a diferença entre
"está perto" e "está fora": um se resolve conversando; o outro, não.

### (b) Faixa de estabilidade do peso

| Peso do Preço | Vencedor |
|---|---|
| 0 → 0,213 | Onix |
| **0,214 → 1,000** | **Mobi** |

O peso declarado foi 0,286 e a fronteira está em 0,214. O Mobi reina com folga
razoável, mas se o preço perdesse cerca de um quarto da importância atribuída, o
Onix assumiria — na régua original, bastaria o preço cair de 6 para ~4,3 pontos na
contagem de dominância.

### (c) O teste que fecha o exercício

Lembra do piso 4 na tabela de-para da Confiança? Se ela fosse **10 / 5 / 0** em vez
de 10 / 7 / 4:

| # | Alternativa | Nota |
|---|---|---|
| 1 | **Onix 1.0** | 7,591 |
| 2 | Mobi Like | 7,580 |

**O vencedor troca — por 0,011 ponto.** E note o que *não* mudou: o Onix continua
"Alta", o Mobi continua "Média", os pesos são os mesmos, os carros são os mesmos.
Mudou apenas onde se pôs o piso de uma tabela que converte três rótulos
qualitativos em número.

## O que o exercício ensina

As três coisas que mais mexeram no resultado final não foram dados dos carros —
foram **escolhas de modelagem**:

1. **A âncora da Segurança** (passo 5): min-max observado × escala real muda a nota
   do Mobi de 0,00 para 7,86.
2. **O piso da Confiança** (passo 5): 10/7/4 × 10/5/0 troca o vencedor.
3. **A distribuição dos pesos** (passo 6): a fronteira em 0,214 está a um quarto de
   distância do peso declarado.

Nenhuma dessas três aparece na tabela final. Todas aparecem no relatório de quem
segue o método até o passo 8 — e é por isso que o passo 8 não é opcional.

Há ainda uma lição de ordem prática: **o passo 5 é uma decisão de peso disfarçada**.
Um critério cuja nota varia de 5 a 10 tem metade da influência de um que varia de 0
a 10, ainda que ambos recebam o mesmo peso no passo 6. Quem comprime a escala e
depois atribui peso alto está puxando com uma mão e soltando com a outra —
exatamente o que aconteceu com a Segurança neste exercício.

## De onde isto veio

O Princípio VIII da constituição vale também para os métodos do próprio autor:
nenhum cai do céu. **Esta seção está deliberadamente incompleta** — o autor
registrou que depois indicará de onde adaptou cada passo, e nada aqui deve ser
tomado como atribuição feita por ele.

O que este livro pode dizer por conta própria, como leitura editorial (📖) e não
como afirmação histórica:

| Elemento do método | Parentesco reconhecível no próprio livro | Selo |
|---|---|---|
| Passos 1–3 (problema → alternativas → atributos) | A estruturação do cap. 02: objetivos-fim, família de critérios, restrição × critério | 📖 |
| Passo 5, interpolação | Transformação linear entre escalas; é a min-max do cap. 03 com âncoras declaradas em vez de observadas | 📖 |
| Passo 5, tabela de-para | Função de valor declarada por pontos, do cap. 07 | 📖 |
| Passo 6, grafo de dominância | Chega à família de **pesos ordinais** do cap. 03 (mesma pergunta que o ROC responde de outro jeito: o ROC concentra 0,408 no primeiro critério, esta construção 0,286) | 📖 |
| Passo 7 | A soma ponderada do cap. 04 | 📖 |
| Passo 8 | Varredura de peso e faixa de estabilidade do cap. 11 | 📖 |

A contribuição que **não** encontramos pronta nos capítulos, e que o exercício
produziu: a regra do **piso levantado** (§ "A regra do piso levantado") e o
diagnóstico de **influência efetiva** como peso × amplitude, que expõe a distância
entre importância declarada e importância exercida.

Fechar esta seção com fontes é trabalho de uma rodada futura, conduzida com o
autor.

---

## Mão na massa — decisor-zero, etapa 15

Em `decisor-zero/etapas/15-criterizacao/` vive `motor/criterizacao.py`, com as
funções puras do método: `interpolar`, `pela_escala_maxima`, `por_tabela`,
`pesos_por_dominancia`, `ranquear`, `influencia_efetiva`, `desconto_para_empatar` e
`varredura_de_peso`. Os 20 testes reproduzem **todos** os números deste apêndice,
inclusive as três descobertas do passo 8.

Exercício de completar: implemente o **passo 4 como validação** — uma função que
recebe a matriz bruta e recusa colunas cujas unidades não foram declaradas (o erro
do NCAP em pontos × percentual). Escreva o teste que o exercício desta aula teria
reprovado.

## Verificação

1. O Mobi vence perdendo em quatro dos seis critérios. Isso é um defeito do método
   ou uma propriedade da soma ponderada? (Dica: cap. 04 — compensação.)
2. Por que ancorar a Segurança em 21 (escala real) em vez de 16,5 (pior da amostra)
   protege o exercício contra o rank reversal do cap. 11?
3. A Segurança foi declarada o 2º critério mais importante e influenciou como o 4º.
   Aponte os dois lugares onde isso poderia ser corrigido — e diga qual dos dois
   você escolheria.

## Apêndice — gabarito comentado

1. É **propriedade**, não defeito: a soma ponderada é compensatória por
   construção, e vantagem grande num critério de peso alto compensa desvantagens
   pequenas espalhadas. O que o método deve fazer — e faz, no passo 7 — é
   **mostrar a decomposição**, para que a compensação seja visível em vez de
   silenciosa. Se compensar fosse inaceitável (ex.: segurança mínima inegociável),
   o instrumento correto seria outro: veto, no ELECTRE do cap. 09.
2. Porque a âncora externa não depende do conjunto de alternativas. Com 21 fixo, a
   nota do Mobi (16,5/21 = 7,86) é a mesma esteja ele sozinho ou entre dez
   concorrentes. Com âncora no pior observado, entrar ou sair um carro remede todo
   mundo — que é exatamente o mecanismo do rank reversal.
3. **No passo 5**, trocando a régua (medir desempenho de ensaio NCAP em vez de
   contar itens, o que provavelmente abriria a faixa); ou **no passo 6**, subindo o
   peso para compensar a compressão. A primeira é preferível: aumentar peso para
   compensar escala achatada mascara o problema — o critério continua sem
   discriminar, e o peso passa a mentir sobre o que está sendo medido. Peso deve
   dizer importância; amplitude deve dizer o que os dados mostram.
