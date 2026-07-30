"""Dominância de Pareto — o único veredito que não exige pesos nem agregação.

Definição (cap. 02; formulação usual em MADM, ver Hwang & Yoon 1981, cap. 2, e
Belton & Stewart 2002): a alternativa a domina b se a é pelo menos tão boa
quanto b em TODOS os critérios (respeitando a direção de cada um) e
estritamente melhor em PELO MENOS UM. Alternativas idênticas não se dominam.
A fronteira de Pareto é o conjunto das não-dominadas — só nelas vale a pena
gastar método.

Motor puro: consome MatrizDecisao, não faz I/O.
"""

from motor.matriz import MatrizDecisao


def _melhor_ou_igual(x: float, y: float, direcao: str) -> bool:
    return x <= y if direcao == "custo" else x >= y


def _estritamente_melhor(x: float, y: float, direcao: str) -> bool:
    return x < y if direcao == "custo" else x > y


def domina(matriz: MatrizDecisao, i: int, k: int) -> bool:
    """A alternativa de índice i domina a de índice k?"""
    linha_i, linha_k = matriz.desempenhos[i], matriz.desempenhos[k]
    direcoes = [c.direcao for c in matriz.criterios]
    ao_menos_tao_boa = all(
        _melhor_ou_igual(x, y, d) for x, y, d in zip(linha_i, linha_k, direcoes)
    )
    melhor_em_algum = any(
        _estritamente_melhor(x, y, d) for x, y, d in zip(linha_i, linha_k, direcoes)
    )
    return ao_menos_tao_boa and melhor_em_algum


def analise_dominancia(matriz: MatrizDecisao) -> dict:
    """Quem domina quem, e o que sobra (a fronteira de Pareto).

    Retorna:
        {"dominadas": {nome_dominada: [nomes das dominadoras]},
         "fronteira_pareto": [nomes das não-dominadas, na ordem original]}
    """
    m = len(matriz.alternativas)
    dominadas: dict[str, list[str]] = {}
    for k in range(m):
        dominadoras = [
            matriz.alternativas[i] for i in range(m) if i != k and domina(matriz, i, k)
        ]
        if dominadoras:
            dominadas[matriz.alternativas[k]] = dominadoras
    fronteira = [nome for nome in matriz.alternativas if nome not in dominadas]
    return {"dominadas": dominadas, "fronteira_pareto": fronteira}
