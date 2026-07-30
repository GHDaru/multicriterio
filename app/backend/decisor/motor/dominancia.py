"""Dominância de Pareto — análise sem pesos nem agregação (cap. 02 do livro).

a domina b se a é ao menos tão boa em todos os critérios (respeitando a
direção) e estritamente melhor em pelo menos um (Hwang & Yoon 1981, cap. 2;
Belton & Stewart 2002). Motor puro, sem I/O.
"""

from decisor.motor.tipos import Problema


def _melhor_ou_igual(x: float, y: float, direcao: str) -> bool:
    return x <= y if direcao == "custo" else x >= y


def _estritamente_melhor(x: float, y: float, direcao: str) -> bool:
    return x < y if direcao == "custo" else x > y


def domina(problema: Problema, i: int, k: int) -> bool:
    linha_i, linha_k = problema.desempenhos[i], problema.desempenhos[k]
    direcoes = [c.direcao for c in problema.criterios]
    return all(
        _melhor_ou_igual(x, y, d) for x, y, d in zip(linha_i, linha_k, direcoes)
    ) and any(
        _estritamente_melhor(x, y, d) for x, y, d in zip(linha_i, linha_k, direcoes)
    )


def analise_dominancia(problema: Problema) -> dict:
    """{"dominadas": {nome: [dominadoras]}, "fronteira_pareto": [nomes]}."""
    m = len(problema.alternativas)
    dominadas: dict[str, list[str]] = {}
    for k in range(m):
        dominadoras = [
            problema.alternativas[i]
            for i in range(m)
            if i != k and domina(problema, i, k)
        ]
        if dominadoras:
            dominadas[problema.alternativas[k]] = dominadoras
    fronteira = [nome for nome in problema.alternativas if nome not in dominadas]
    return {"dominadas": dominadas, "fronteira_pareto": fronteira}
