"""TOPSIS — proximidade relativa ao ideal (Hwang & Yoon, 1981). Cap. 06.

Formulação clássica: normalização vetorial, ponderação, ideal/anti-ideal por
direção, distâncias euclidianas, C_i = D-/(D+ + D-). Motor puro; cópia da
etapa 06 do decisor-zero (etapas são congeladas).
"""

from math import dist, sqrt

from decisor.motor.tipos import Problema


def _normalizar_vetorial(problema: Problema) -> list[list[float]]:
    colunas = list(zip(*problema.desempenhos))
    normas = [sqrt(sum(x * x for x in c)) for c in colunas]
    return [
        [0.0 if normas[j] == 0 else x / normas[j] for j, x in enumerate(linha)]
        for linha in problema.desempenhos
    ]


def ranquear_topsis(problema: Problema) -> list[dict]:
    if problema.pesos is None:
        raise ValueError("TOPSIS exige pesos (ver cap. 03 do livro)")
    ponderada = [
        [w * r for w, r in zip(problema.pesos, linha)]
        for linha in _normalizar_vetorial(problema)
    ]
    colunas = list(zip(*ponderada))
    ideal, anti = [], []
    for j, criterio in enumerate(problema.criterios):
        if criterio.direcao == "custo":
            ideal.append(min(colunas[j])); anti.append(max(colunas[j]))
        else:
            ideal.append(max(colunas[j])); anti.append(min(colunas[j]))
    resultado = []
    for nome, v in zip(problema.alternativas, ponderada):
        d_mais, d_menos = dist(v, ideal), dist(v, anti)
        c = d_menos / (d_mais + d_menos) if d_mais + d_menos else 0.0
        resultado.append({"alternativa": nome, "escore": round(c, 6)})
    resultado.sort(key=lambda l: l["escore"], reverse=True)
    for pos, linha in enumerate(resultado, start=1):
        linha["posicao"] = pos
    return resultado
