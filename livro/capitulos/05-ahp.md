# 05 — AHP: pesos por comparações par a par (e o detector de incoerência)

> **Estado da arte capturado em 2026-07** · última revisão 2026-07-31 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Construir** uma matriz de julgamentos par a par na escala 1–9 de Saaty e
   **calcular** o vetor de prioridades pelo autovetor principal.
2. **Avaliar** a coerência dos julgamentos com $\lambda_{max}$, CI e a razão de
   consistência CR — e **explicar** por que CR > 0,10 manda revisar, não calcular.
3. **Analisar** o debate crítico do AHP: rank reversal (Belton & Gear) e a objeção de
   fundamento (Dyer) — e a decisão deste livro de usá-lo como técnica de pesos.

## O problema

O cap. 04 terminou com uma constatação incômoda: o vencedor pertence ao vetor $w$. Mas
pedir "distribua 100 pontos entre 4 critérios" já se mostrou frágil (cap. 03) — pessoas
ancoram, chutam, mudam. O que um decisor *consegue* responder com confiança é uma
pergunta de cada vez: "entre Preço e Área, qual importa mais — e quanto?". O AHP
(*Analytic Hierarchy Process*) transforma um conjunto dessas perguntas simples num
vetor de pesos — e, melhor, **denuncia quando as respostas se contradizem**.

## Fundamentos

Saaty (1977; 1980) propõe: julgue cada par de critérios na escala 1 (igual importância)
a 9 (importância extrema), monte a matriz recíproca $A$ (com $a_{ji} = 1/a_{ij}$) e
extraia as prioridades do **autovetor principal**: $A w = \lambda_{max} w$. Se os
julgamentos fossem perfeitamente coerentes ($a_{ij} = w_i/w_j$ exato), teríamos
$\lambda_{max} = n$; o desvio mede a incoerência:

$$CI = \frac{\lambda_{max} - n}{n - 1}, \qquad CR = \frac{CI}{RI_n}$$

com $RI_n$ tabelado por Saaty a partir de matrizes aleatórias ($RI_4 = 0{,}90$). Regra
prática (Saaty, 1980): **CR ≤ 0,10** — acima disso, os julgamentos se contradizem
demais para produzir pesos confiáveis; a resposta certa é voltar ao decisor, nunca
"usar assim mesmo".

O AHP completo de Saaty também compara as *alternativas* par a par em cada critério e
agrega tudo. É aí que mora a crítica clássica: Belton & Gear (1983) mostraram que
acrescentar uma alternativa irrelevante pode **inverter o ranking** das demais (rank
reversal), e Dyer (1990) questionou o fundamento da agregação — debate respondido por
Saaty no mesmo volume e vivo até hoje. Posição deste livro (ADR 0006): usar o AHP no
que ele tem de mais sólido — **derivar pesos de critérios** — e alimentar com eles os
métodos de ranking cujas premissas já conhecemos (SAW, cap. 04); o rank reversal volta
em detalhe no cap. 11.

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

**Passo 1 — os julgamentos** para os critérios do caso âncora ("Preço importa 2× mais
que Área, 2× mais que Deslocamento, 3× mais que Bairro; Área e Deslocamento empatam e
valem 2× Bairro"):

$$A = \begin{bmatrix} 1 & 2 & 2 & 3 \\ 1/2 & 1 & 1 & 2 \\ 1/2 & 1 & 1 & 2 \\ 1/3 & 1/2 & 1/2 & 1 \end{bmatrix}$$

**Passo 2 — prioridades** (autovetor pelo método das potências):

| Preço | Área | Deslocamento | Bairro |
|---|---|---|---|
| 0,4236 | 0,2270 | 0,2270 | 0,1223 |

(Área e Deslocamento receberam julgamentos idênticos — e o autovetor devolve pesos
idênticos, como deve.)

**Passo 3 — diagnóstico**: $\lambda_{max} = 4{,}0104$ → $CI = 0{,}0035$ →
$CR = 0{,}0038 \le 0{,}10$: julgamentos coerentes, pesos utilizáveis.

**Passo 4 — o contraexemplo.** Julgamentos cíclicos ($a_{12}=3$, $a_{23}=1/5$,
$a_{13}=5$: "1 > 2, 3 ≫ 2, 1 ≫ 3" — mas $3 \times 1/5 = 0{,}6 \neq 5$) produzem
$CR = 0{,}4488$: **reprovado**. É o superpoder do AHP sobre o rating direto — notas
soltas não têm como se contradizer; comparações par a par têm, e o CR flagra.

**Passo 5 — fechando o ciclo**: os pesos AHP no SAW do cap. 04 dão
**A4 (0,5939) > A1 (0,5263) > A2 (0,4838) > A3 (0,4629)** — terceiro vetor defensável,
terceiro pódio diferente. A pergunta "então qual ranking vale?" é exatamente o cap. 11.
*Todos os números são reproduzidos pelos testes da etapa 05.*

## Quando usar (e quando não)

Use o AHP quando os pesos precisam de **processo auditável com defesa contra
incoerência** — comitês, decisões públicas, muitos critérios ($n \le 9$; acima disso a
carga de comparações, $n(n-1)/2$, cansa e a qualidade cai). Evite o AHP completo
(alternativas par a par) quando as alternativas mudam com frequência — é o cenário do
rank reversal (Belton & Gear, 1983); com desempenhos mensuráveis, prefira medir
(matriz de decisão) e usar o AHP só nos pesos. E jamais reporte pesos AHP sem o CR ao
lado — pesos sem diagnóstico são rating direto com cerimônia.

### Leitura executiva

O AHP converte perguntas fáceis ("qual dos dois importa mais?") num vetor de pesos com
**controle de qualidade embutido** — o CR reprova julgamentos que se contradizem, coisa
que nenhuma técnica do cap. 03 faz. **O que levar** hoje: eleve seus pesos de rating
direto a AHP quando a decisão exigir defesa formal; publique sempre CR junto com $w$; e
se o CR passar de 0,10, a reunião certa é sobre julgamentos, não sobre planilha.

## Mão na massa — decisor-zero, etapa 05

Em `decisor-zero/etapas/05-ahp/`, nasce `motor/ahp.py` (validação de reciprocidade,
autovetor por potências, CI/CR) e a rota `POST /api/ahp/prioridades`; a página deixa
editar a metade superior da matriz (a inferior é recíproca automática) e ver pesos + CR
na hora — provoque um ciclo e veja a reprovação. No produto, `/api/pesos` ganhou o
método `ahp`, que **recusa** julgamentos com CR > 0,10. Exercício de completar:
implemente o cálculo de prioridades pela **média geométrica das linhas** (atalho
clássico) e escreva o teste que mede o quanto ela se afasta do autovetor nesta matriz.

## Verificação

1. Por que Área e Deslocamento terminaram com o mesmo peso? O que isso diz sobre o
   autovetor? (Dica: objetivo 1 — linhas idênticas.)
2. $CR = 0{,}25$: o que fazer — normalizar, cortar um critério ou reentrevistar o
   decisor? (Dica: objetivo 2.)
3. Por que este livro evita o AHP completo para ranquear alternativas que mudam toda
   semana? (Dica: objetivo 3 — Belton & Gear.)

---

## Apêndice A — o AHP nas ferramentas

- **pyDecision** traz AHP e fuzzy-AHP com notebooks (método `ahp_method`, incluindo
  CR) — bom para conferir nossos números (<https://github.com/Valdecy/pyDecision>).
- **pymcdm** não traz AHP clássico (foco em métodos que consomem matriz de decisão
  pronta) — coerente com a nossa decisão de tratá-lo como técnica de pesos
  (<https://github.com/kotbaton/pymcdm>).
- O exemplar de Saaty (1980) está acessível no Internet Archive
  (<https://archive.org/details/analytichierarch0000saat>).
