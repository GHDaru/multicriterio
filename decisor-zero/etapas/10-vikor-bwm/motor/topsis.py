"""TOPSIS — proximidade relativa à solução ideal (Hwang & Yoon, 1981).

Cap. 06 do livro. Formulação clássica: normalização vetorial (cap. 03),
ponderação, solução ideal A+ (melhor de cada coluna, respeitando direção) e
anti-ideal A-, distâncias euclidianas e coeficiente C_i = D-/(D+ + D-).
Motor puro, sem I/O.
"""

from math import dist

from motor.matriz import MatrizDecisao
from motor.normalizacao import normalizar_vetorial


def ranquear_topsis(matriz: MatrizDecisao) -> list[dict]:
    """Ranking por proximidade relativa (C_i em [0,1], 1 = colada no ideal)."""
    if matriz.pesos is None:
        raise ValueError("TOPSIS exige pesos (ver cap. 03)")
    n = len(matriz.criterios)
    ponderada = [
        [w * r for w, r in zip(matriz.pesos, linha)]
        for linha in normalizar_vetorial(matriz)
    ]
    colunas = list(zip(*ponderada))
    ideal, anti_ideal = [], []
    for j in range(n):
        if matriz.criterios[j].direcao == "custo":
            ideal.append(min(colunas[j]))
            anti_ideal.append(max(colunas[j]))
        else:
            ideal.append(max(colunas[j]))
            anti_ideal.append(min(colunas[j]))
    resultado = []
    for nome, v in zip(matriz.alternativas, ponderada):
        d_mais, d_menos = dist(v, ideal), dist(v, anti_ideal)
        proximidade = d_menos / (d_mais + d_menos) if d_mais + d_menos else 0.0
        resultado.append({"alternativa": nome, "escore": round(proximidade, 6)})
    resultado.sort(key=lambda linha: linha["escore"], reverse=True)
    for pos, linha in enumerate(resultado, start=1):
        linha["posicao"] = pos
    return resultado
