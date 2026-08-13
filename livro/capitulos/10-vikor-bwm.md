# 10 — VIKOR e BWM: compromisso honesto, pesos com menos perguntas

> **Estado da arte capturado em 2026-07** · última revisão 2026-08-13 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Calcular** o VIKOR completo — S, R, Q — e **aplicar** as duas condições de
   aceitação que podem transformar o "vencedor" num conjunto de compromisso.
2. **Explicar** o dial $v$ (maioria × pior arrependimento) e o que o VIKOR mede que o
   TOPSIS não mede.
3. **Elicitar** pesos pelo BWM com apenas $2n-3$ comparações e **interpretar** o índice
   de consistência $\xi$.

## O problema

Duas frustrações acumuladas. Primeira: todo ranking até aqui **elege alguém** — mesmo
quando a vantagem do 1º sobre o 2º é ridícula (no cap. 04, 0,007!). Um método honesto
deveria saber dizer "é empate técnico". Segunda: o AHP pede $n(n-1)/2$ comparações — 6
para 4 critérios, 36 para 9; decisores cansam, e julgamento cansado é julgamento ruim.

## De onde isto veio

Dois métodos, dois apertos — com quarenta anos e um contraste instrutivo entre eles.

**O aperto (VIKOR).** **Serafim Opricovic** assina pela Faculdade de Engenharia Civil
de Belgrado — e o aperto dele era de engenharia de recursos, não de escritório. A
medida que está no coração do VIKOR (a distância $L_p$ de que S e R são os casos
$p=1$ e $p=\infty$) aparece pela primeira vez em 1980, num trabalho com Lucien
Duckstein sobre **otimização multiobjetivo no desenvolvimento de bacias
hidrográficas**: água, o problema clássico em que nenhum critério pode ser sacrificado
até o fim e ninguém aceita um vencedor por margem mínima. Uma correção que vale
registrar: a versão corrente atribui a origem do VIKOR ao planejamento de
**reconstrução pós-terremoto**; o que a literatura documenta é o pós-terremoto como
**aplicação** madura do método (Opricovic & Tzeng, 2002), duas décadas depois da
semente hidrológica. A história boa não é a que se repete — é a que a bibliografia
sustenta.

**O aperto (BWM).** Quarenta anos depois, o problema é de fadiga: **Jafar Rezaei**
(TU Delft, logística — afiliação corrente) via decisores desistirem no meio das
$n(n-1)/2$ comparações do AHP; julgamento cansado é julgamento incoerente, e o CR
só detecta o estrago depois.

**O que se fazia antes.** Para o compromisso: TOPSIS — perto do ideal, mas sem
protocolo para dizer "empate técnico" (C1/C2 não existem lá). Para pesos: AHP
completo, com todas as comparações e a inconsistência corrigida a posteriori.

**A virada.** No VIKOR: medir **dois arrependimentos** (a maioria, S, e o crítico mais
sacrificado, R) e — a parte realmente nova — um **protocolo de aceitação** que
transforma vantagem insuficiente em conjunto de compromisso declarado. No BWM: só
comparar todos contra **os dois extremos** (melhor e pior) — $2n-3$ julgamentos, e a
consistência sai alta *por construção*, não por sorte.

**A ideia reaproveitável.** Do VIKOR: **um ranking precisa de condições de
proclamação** — sem margem mínima e estabilidade, o resultado honesto é um conjunto,
não um campeão. Do BWM: **pontos de referência extremos baratearam a elicitação** —
âncoras nos dois polos extraem mais informação por pergunta do que pares arbitrários
(o mesmo princípio dos dois polos do TOPSIS, aplicado a perguntas em vez de
distâncias).

**O nome.** VIKOR é acrônimo sérvio — *VIšekriterijumsko KOmpromisno Rangiranje*,
"ordenação de compromisso multicritério" (atribuição corrente). BWM é literal:
*Best-Worst Method*. Repare que a palavra do meio é a tese do método: **compromisso**,
no sentido de acordo por concessões mútuas, não de meio-termo preguiçoso.

| Afirmação | Selo |
|---|---|
| Afiliação Faculdade de Engenharia Civil de Belgrado; a medida $L_p$ do VIKOR introduzida em Duckstein & Opricovic (1980), sobre bacias hidrográficas; linhagem da solução de compromisso em Yu (1973) e do ótimo em Pareto (1896) | ✓ Opricovic & Tzeng (2007), *EJOR* 178(2) — lido |
| Pós-terremoto como **aplicação** documentada (Opricovic & Tzeng, 2002, *Computer-Aided Civil and Infrastructure Engineering*) | ✓ referência do artigo lido |
| Pós-terremoto como **origem** do método (fim dos anos 1970) | ⏳ atribuição corrente que a leitura não sustenta — a semente documentada é hidrológica; a monografia de Belgrado (em sérvio) segue ❌ não alcançada |
| Opricovic & Tzeng (2004), o comparativo que internacionalizou o VIKOR | ✓ᵐ (DOI na bibliografia; conteúdo não lido) |
| Rezaei (2015), *Omega*; afiliação TU Delft | ✓ᵐ o paper (bibliografia); ⏳ a afiliação e a motivação narrada |
| Expansão servo-croata do acrônimo | ⏳ corrente |

## Fundamentos

**VIKOR** (Opricovic & Tzeng, 2004) mede cada alternativa por dois arrependimentos:
$S_i$ (soma ponderada das distâncias ao melhor de cada critério — a "vontade da
maioria") e $R_i$ (o **pior** arrependimento individual — o critério mais sacrificado).
O índice $Q_i$ mistura os dois com o dial $v$ (aqui 0,5, ADR 0006) e ordena por $Q$
**crescente**. O diferencial não é a fórmula — é o protocolo de aceitação: o líder só é
proclamado sozinho se (C1) sua vantagem for **aceitável** ($Q_{(2)} - Q_{(1)} \ge DQ =
\frac{1}{m-1}$) e (C2) ele for **estável** (líder também em S ou R). Falhou C1 ou C2?
A resposta é um **conjunto de compromisso**.

**BWM** (*Best-Worst Method*, Rezaei, 2015) ataca a fadiga do AHP: escolha o critério
**mais** importante (best) e o **menos** (worst); compare só o best com todos
($a_{Bj}$) e todos com o worst ($a_{jW}$) — $2n-3$ julgamentos. Os pesos saem de uma
otimização (no modelo linear: minimizar o maior desvio $\xi$ das razões declaradas,
resolvido aqui por programação linear — ADR 0006), e $\xi^*$ é o índice de
consistência: 0 = julgamentos perfeitamente coerentes.

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

**VIKOR no caso âncora** (pesos 0,35/0,25/0,25/0,15, $v = 0{,}5$):

| Alternativa | S | R | Q ↓ |
|---|---|---|---|
| **A1 — Centro** | 0,4556 | 0,2139 | **0,0000** |
| A4 — Estação | 0,4625 | 0,2500 | 0,1684 |
| A3 — Parque | 0,4750 | 0,3500 | 0,6000 |
| A2 — Jardim | 0,5528 | 0,2500 | 0,6327 |

A1 lidera em S **e** em R (estável ✓). Mas $Q_{(2)} - Q_{(1)} = 0{,}1684 < DQ =
0{,}3333$: **vantagem não aceitável** — C1 falha. Veredito do VIKOR: **conjunto de
compromisso {A1, A4}**. É a formalização do que os caps. 04–06 insinuavam: entre A1 e
A4, a diferença não sustenta um decreto. *Números e condições validados contra a
pymcdm (Q a 10⁻⁶) nos testes da etapa 10.*

**BWM nos critérios do caso âncora** (best = Preço, worst = Bairro; $a_B = (1,2,2,4)$,
$a_W = (4,2,2,1)$): os julgamentos são perfeitamente consistentes ($a_{Bj} \cdot
a_{jW} = a_{BW} = 4$ para todo $j$), e o modelo devolve $\xi = 0$ com pesos exatos
$(4/9,\ 2/9,\ 2/9,\ 1/9) = (0{,}4444;\ 0{,}2222;\ 0{,}2222;\ 0{,}1111)$ — com **5
comparações** contra 6 do AHP (e a economia cresce com $n$). Julgamentos incoerentes
produzem $\xi > 0$ — o análogo do CR do cap. 05, também testado.

## Quando usar (e quando não)

VIKOR quando o custo político de proclamar um vencedor por margem mínima é alto —
comitês, rankings públicos: o conjunto de compromisso é blindagem metodológica. (Entre
TOPSIS e VIKOR: o TOPSIS agrega as duas distâncias numa razão; o VIKOR mantém S e R
separados e ainda pergunta "a vantagem basta?" — Opricovic & Tzeng, 2004.) BWM quando
há muitos critérios ou pouco tempo de decisor — mas lembre: ele elicita *pesos*; a
independência preferencial da agregação continua sendo premissa de quem consome esses
pesos (cap. 07).

### Leitura executiva

O VIKOR institucionaliza o empate técnico ($DQ$) e o BWM corta o custo da elicitação
de quadrático para linear, ambos com diagnóstico embutido (condições C1/C2; $\xi$).
**O que levar** hoje: reporte rankings com a pergunta do VIKOR em mente — "a vantagem
do 1º é aceitável?" — e, com mais de 6 critérios, troque o AHP pelo BWM na elicitação:
menos perguntas, mesma auditabilidade.

## Mão na massa — decisor-zero, etapa 10

Em `decisor-zero/etapas/10-vikor-bwm/`, nascem `motor/vikor.py` (S/R/Q + condições +
conjunto de compromisso) e `motor/bwm.py` (modelo linear via `scipy.optimize.linprog`
— scipy entrou nos requirements da trilha); rotas `POST /api/matriz/vikor` e
`POST /api/pesos/bwm`. O produto ganhou `vikor` no catálogo (escore = Q, menor é
melhor). Exercício de completar: varra $v \in \{0; 0{,}25; 0{,}5; 0{,}75; 1\}$ e
escreva o teste que mostra em qual $v$ o conjunto de compromisso muda.

## Segundo domínio — VIKOR na decisão B2B (o compromisso que surpreende)

Fornecedores: **Q = F2 0,0000 < F3 0,3957 < F1 1,0000**, com F2 líder estável em S e
R. E aqui vem a lição fina do protocolo: com $m = 3$, o limiar de vantagem sobe para
$DQ = \frac{1}{m-1} = 0{,}5$ — e $Q(F3) - Q(F2) = 0{,}3957 < 0{,}5$. Mesmo uma vitória
que todos os outros métodos chamam de robusta **não passa no C1 do VIKOR com poucas
alternativas**: conjunto de compromisso {F2, F3}. Moral: o DQ embute o tamanho do
conjunto — com poucas alternativas, o VIKOR exige vantagens enormes para proclamar
vencedor único. Reporte o conjunto e o porquê. *Teste
`test_segundo_dominio_dq_alto_com_poucas_alternativas` da etapa 10.*

## Verificação

1. Por que A1 tem $Q = 0$ exato? (Dica: objetivo 1 — normalizações de S e R.)
2. O que muda no VIKOR com $v = 1$ (só maioria) e $v = 0$ (só pior arrependimento)?
   Qual perfil de decisor cada extremo representa? (Dica: objetivo 2.)
3. No BWM do capítulo, mostre por que $a_{Bj} \cdot a_{jW} = a_{BW}$ implica $\xi = 0$.
   (Dica: objetivo 3 — substitua $w_B/w_j$ e $w_j/w_W$.)

---

## Apêndice A — VIKOR e BWM nas ferramentas

- **pymcdm**: `VIKOR(v=...)` — validação cruzada desta etapa
  (<https://github.com/kotbaton/pymcdm>).
- **pyDecision** traz BWM (modelos de Rezaei 2015/2016) e VIKOR/fuzzy-VIKOR com
  notebooks (<https://github.com/Valdecy/pyDecision>).
- O solver do site oficial do BWM (Excel) está em <https://bestworstmethod.com/> —
  vendor acadêmico; útil para conferência manual.

## Apêndice B — gabarito comentado da Verificação

1. Porque A1 minimiza S **e** R simultaneamente: nas duas normalizações
   $(S-S^*)/(S^--S^*)$ e $(R-R^*)/(R^--R^*)$ ela é o ponto de referência (numerador
   zero) — e qualquer combinação convexa de zeros é zero. Q = 0 não significa
   "perfeita"; significa "melhor do conjunto nos dois eixos".
2. $v = 1$: só a soma dos arrependimentos conta — perfil utilitarista, aceita
   sacrificar um critério se a média compensa. $v = 0$: só o pior arrependimento —
   perfil maximin/cauteloso, protege o critério mais sacrificado. O 0,5 padrão declara
   empate entre as duas éticas; mudá-lo é decisão de política, não de cálculo.
3. Consistência plena significa $a_{Bj} = w_B/w_j$ e $a_{jW} = w_j/w_W$ exatos.
   Então $a_{Bj} \cdot a_{jW} = (w_B/w_j)(w_j/w_W) = w_B/w_W = a_{BW}$ para todo $j$ —
   e existe um vetor $w$ que zera todos os desvios: $\xi^* = 0$. Qualquer quebra
   dessa cadeia força $\xi > 0$.
