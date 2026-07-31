# 06 — TOPSIS: perto do ideal, longe do pior

> **Estado da arte capturado em 2026-07** · última revisão 2026-07-31 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Calcular** um ranking TOPSIS completo: normalização vetorial, ponderação,
   soluções ideal e anti-ideal, distâncias e coeficiente de proximidade.
2. **Explicar** a intuição geométrica que o distingue do SAW — e por que ele exige a
   normalização vetorial (cap. 03), não a min-max.
3. **Avaliar** quando a concordância entre TOPSIS e SAW é esperada e por que ela não é
   garantida (ponte para o cap. 11).

## O problema

O SAW soma virtudes: cada critério contribui na proporção do peso. Mas há outra
intuição legítima de "melhor": **a alternativa que mais se aproxima do apartamento
ideal — e mais se afasta do pior cenário**. São réguas diferentes: uma alternativa
equilibrada pode somar bem e ainda assim estar longe do ideal em algum eixo. O TOPSIS
(*Technique for Order Preference by Similarity to Ideal Solution*) formaliza a régua
geométrica.

## Fundamentos

Hwang & Yoon (1981) definem o procedimento em cinco passos sobre a matriz $X$ e os
pesos $w$: (1) normalização **vetorial** $r_{ij} = x_{ij}/\sqrt{\sum_i x_{ij}^2}$ —
preserva proporções, e a direção fica para o passo 3; (2) ponderação $v_{ij} = w_j
r_{ij}$; (3) solução **ideal** $A^+$ (melhor $v$ de cada coluna, respeitando a
direção) e **anti-ideal** $A^-$; (4) distâncias euclidianas $D_i^+ = \lVert v_i - A^+
\rVert$ e $D_i^-$; (5) **coeficiente de proximidade**

$$C_i = \frac{D_i^-}{D_i^+ + D_i^-} \in [0,1]$$

— 1 significa colado no ideal, 0 colado no pior. Krishnan (2022) lembra que trocar a
normalização (ou a métrica de distância) muda resultados: as escolhas acima são a
formulação clássica, e são **declaradas** no modelo (é também com elas que a pymcdm
valida nossos números).

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

Caso âncora com os pesos do rating direto (0,35/0,25/0,25/0,15). A matriz vetorial é a
do cap. 03 (passo 2 daquele capítulo); após ponderar e extrair $A^+$/$A^-$:

| Alternativa | $D^+$ menor que $D^-$? | $C_i$ |
|---|---|---|
| **A1 — Centro** | sim | **0,6359** |
| A4 — Estação | sim | 0,5514 |
| A3 — Parque | levemente | 0,5189 |
| A2 — Jardim | não | 0,3707 |

Ranking: **A1 > A4 > A3 > A2** — o mesmo pódio do SAW com estes pesos (cap. 04, passo
3). Concordância aqui é propriedade *deste problema* (a corrida era apertada mas as
duas réguas apontaram igual), não lei: métodos legítimos podem divergir, e o cap. 11
mede exatamente isso. *Os quatro $C_i$ e a concordância com a pymcdm (a 10⁻⁶) são
testes da etapa 06.*

## Quando usar (e quando não)

TOPSIS brilha quando a narrativa "quão perto do ideal?" comunica melhor que "soma
ponderada" — painéis executivos, benchmarking — e quando se quer sensibilidade a
*todas* as dimensões simultaneamente (a distância euclidiana pune desvios grandes mais
que proporcionalmente). Cuidados: como o ideal/anti-ideal dependem do **conjunto de
alternativas**, entrada ou saída de candidatos move as âncoras — o rank reversal
específico do TOPSIS (García-Cascales & Lamata, 2012, discutido no cap. 11); e a
compensação continua total, como no SAW.

### Leitura executiva

TOPSIS é o SAW trocado de régua: em vez de somar virtudes, mede distância a dois faróis
— o ideal e o pior. Mesmos insumos (matriz, direções, pesos), outra geometria, e neste
problema, o mesmo vencedor. **O que levar** hoje: quando dois métodos com premissas
diferentes concordam, a decisão ganha robustez de graça — rode os dois e reporte a
concordância (ou a divergência) como parte do resultado.

## Mão na massa — decisor-zero, etapa 06

Em `decisor-zero/etapas/06-topsis/`, nasce `motor/topsis.py`; a rota
`POST /api/matriz/topsis` devolve o ranking TOPSIS **e** o SAW lado a lado, e a página
os compara. O produto ganhou `topsis` no catálogo `/api/metodos`. Exercício de
completar: troque a distância euclidiana pela de Manhattan ($\sum |v - a|$) e escreva o
teste que verifica se o pódio do caso âncora muda.

## Verificação

1. Por que o TOPSIS usa a normalização vetorial e não a min-max? O que quebraria?
   (Dica: objetivo 2 — quem resolve a direção, e onde.)
2. A4 é a mais barata e ficou em 2º. Que papel o anti-ideal teve nisso? (Dica:
   objetivo 1 — $D^-$.)
3. Se um 5º apartamento caríssimo entrar na disputa, os $C_i$ dos outros quatro mudam
   mesmo sem nenhum deles mudar. Por quê? (Dica: objetivo 3 — âncoras dependem do
   conjunto.)

---

## Apêndice A — o TOPSIS nas ferramentas

- **pymcdm**: `TOPSIS(normalization_function=...)` — nossa etapa valida contra
  `vector_normalization` em teste (<https://github.com/kotbaton/pymcdm>).
- **scikit-criteria**: `TOPSIS` com métrica configurável
  (<https://scikit-criteria.quatrope.org/>).
- **pyDecision**: `topsis_method` com notebook
  (<https://github.com/Valdecy/pyDecision>).
