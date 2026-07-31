# 10 — VIKOR e BWM: compromisso honesto, pesos com menos perguntas

> **Estado da arte capturado em 2026-07** · última revisão 2026-07-31 · [histórico](../HISTORICO.md)

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
