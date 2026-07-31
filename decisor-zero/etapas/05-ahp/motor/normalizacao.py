"""Normalização — tornar comensurável o que veio em unidades diferentes.

Cap. 03 do livro. Duas famílias implementadas:

- min-max ("linear max-min" na taxonomia de Krishnan, 2022): r fica em [0, 1]
  e a DIREÇÃO é resolvida aqui (1 = sempre o melhor desempenho do critério).
  É a normalização que o SAW usa no cap. 04.
- vetorial (divisão pela norma euclidiana da coluna; Hwang & Yoon, 1981): a
  direção NÃO é resolvida aqui — métodos que a usam (TOPSIS, cap. 06) tratam
  benefício/custo na etapa da distância. Preserva proporções.

A escolha de normalização não é detalhe: pode trocar o ranking final
(Krishnan, 2022) — por isso ela é decisão declarada do modelo, não default
escondido. Motor puro, sem I/O.
"""

from math import sqrt

from motor.matriz import MatrizDecisao


def normalizar_minmax(matriz: MatrizDecisao) -> list[list[float]]:
    """r_ij em [0, 1], com 1 = melhor (inverte critérios de custo).

    Critério em que todas as alternativas empatam não discrimina: r = 0.
    """
    colunas = list(zip(*matriz.desempenhos))
    normalizada: list[list[float]] = [[] for _ in matriz.alternativas]
    for j, coluna in enumerate(colunas):
        menor, maior = min(coluna), max(coluna)
        amplitude = maior - menor
        for i, x in enumerate(coluna):
            if amplitude == 0:
                r = 0.0
            elif matriz.criterios[j].direcao == "beneficio":
                r = (x - menor) / amplitude
            else:
                r = (maior - x) / amplitude
            normalizada[i].append(r)
    return normalizada


def normalizar_vetorial(matriz: MatrizDecisao) -> list[list[float]]:
    """r_ij = x_ij / ||coluna_j|| (norma euclidiana). Não resolve direção."""
    colunas = list(zip(*matriz.desempenhos))
    normalizada: list[list[float]] = [[] for _ in matriz.alternativas]
    for coluna in colunas:
        norma = sqrt(sum(x * x for x in coluna))
        for i, x in enumerate(coluna):
            normalizada[i].append(0.0 if norma == 0 else x / norma)
    return normalizada
