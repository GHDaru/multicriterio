"""MAVT — funções de valor por critério (Keeney & Raiffa, 1976). Cap. 07.

Cada critério ganha uma função de valor v_j: desempenho físico → valor [0,1],
declarada por pontos de quebra (interpolação linear por partes, monótona).
V(a_i) = Σ_j w_j · v_j(x_ij). Caso especial: funções lineares ancoradas em
min/max reproduzem exatamente o SAW min-max do cap. 04 (provado em teste).

Motor puro, sem I/O.
"""

from motor.matriz import MatrizDecisao


class ErroDeFuncaoValor(ValueError):
    """Função de valor mal declarada — a mensagem diz a regra."""


def _validar(pontos: list[tuple[float, float]], nome: str) -> list[tuple[float, float]]:
    if len(pontos) < 2:
        raise ErroDeFuncaoValor(f"{nome}: são necessários ao menos 2 pontos")
    pontos = sorted((float(x), float(v)) for x, v in pontos)
    valores = [v for _, v in pontos]
    crescente = all(b >= a for a, b in zip(valores, valores[1:]))
    decrescente = all(b <= a for a, b in zip(valores, valores[1:]))
    if not (crescente or decrescente):
        raise ErroDeFuncaoValor(f"{nome}: a função de valor deve ser monótona")
    if min(valores) < 0 or max(valores) > 1:
        raise ErroDeFuncaoValor(f"{nome}: valores devem estar em [0, 1]")
    return pontos


def valor(pontos: list[tuple[float, float]], x: float) -> float:
    """Interpolação linear por partes; constante fora do intervalo declarado."""
    if x <= pontos[0][0]:
        return pontos[0][1]
    if x >= pontos[-1][0]:
        return pontos[-1][1]
    for (x0, v0), (x1, v1) in zip(pontos, pontos[1:]):
        if x0 <= x <= x1:
            return v0 + (v1 - v0) * (x - x0) / (x1 - x0)
    raise AssertionError("inalcançável")


def ranquear_mavt(
    matriz: MatrizDecisao, funcoes: dict[str, list[tuple[float, float]]]
) -> list[dict]:
    """Ranking por valor multiatributo aditivo (exige pesos e uma função por critério)."""
    if matriz.pesos is None:
        raise ValueError("MAVT exige pesos (ver cap. 03)")
    validadas = {}
    for criterio in matriz.criterios:
        if criterio.nome not in funcoes:
            raise ErroDeFuncaoValor(f"falta função de valor para {criterio.nome!r}")
        validadas[criterio.nome] = _validar(funcoes[criterio.nome], criterio.nome)
    resultado = []
    for nome, linha in zip(matriz.alternativas, matriz.desempenhos):
        parcelas = [
            w * valor(validadas[c.nome], x)
            for w, c, x in zip(matriz.pesos, matriz.criterios, linha)
        ]
        resultado.append({"alternativa": nome, "escore": round(sum(parcelas), 6)})
    resultado.sort(key=lambda l: l["escore"], reverse=True)
    for pos, linha in enumerate(resultado, start=1):
        linha["posicao"] = pos
    return resultado
