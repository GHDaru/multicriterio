"""Sensibilidade, robustez e rank reversal. Cap. 11.

Três instrumentos: (1) varredura de peso — em que faixa do peso de um critério
o vencedor se mantém (os demais pesos são renormalizados proporcionalmente);
(2) comparação multi-método com correlação de Spearman entre rankings;
(3) teste de rank reversal — o efeito de acrescentar uma alternativa sobre a
ordem relativa das originais (Belton & Gear 1983; García-Cascales & Lamata
2012). Motor puro, sem I/O.
"""

from collections.abc import Callable

from motor.matriz import Criterio, MatrizDecisao
from motor.promethee import fluxos_promethee
from motor.saw import ranquear_saw
from motor.topsis import ranquear_topsis
from motor.vikor import analisar_vikor


def _ordem(linhas: list[dict]) -> list[str]:
    return [l["alternativa"] for l in linhas]


METODOS: dict[str, Callable[[MatrizDecisao], list[str]]] = {
    "saw": lambda m: _ordem(ranquear_saw(m)),
    "topsis": lambda m: _ordem(ranquear_topsis(m)),
    "promethee2": lambda m: _ordem(fluxos_promethee(m)),
    "vikor": lambda m: _ordem(analisar_vikor(m)["ranking"]),
}


def _com_pesos(matriz: MatrizDecisao, pesos: list[float]) -> MatrizDecisao:
    return MatrizDecisao(
        alternativas=matriz.alternativas, criterios=matriz.criterios,
        desempenhos=matriz.desempenhos, pesos=pesos,
    )


def varredura_peso(
    matriz: MatrizDecisao, indice: int, metodo: str = "saw", passos: int = 1000
) -> list[dict]:
    """Faixas do peso do critério `indice` em que cada vencedor reina.

    Os demais pesos mantêm as proporções originais entre si.
    """
    ranquear = METODOS[metodo]
    resto = [w for j, w in enumerate(matriz.pesos) if j != indice]
    soma_resto = sum(resto)
    faixas: list[dict] = []
    for i in range(passos + 1):
        w_alvo = i / passos
        fator = (1 - w_alvo) / soma_resto if soma_resto else 0.0
        pesos = []
        k = 0
        for j in range(len(matriz.pesos)):
            if j == indice:
                pesos.append(w_alvo)
            else:
                pesos.append(resto[k] * fator); k += 1
        vencedor = ranquear(_com_pesos(matriz, pesos))[0]
        if not faixas or faixas[-1]["vencedor"] != vencedor:
            faixas.append({"a_partir_de": round(w_alvo, 4), "vencedor": vencedor})
    return faixas


def spearman(ordem_a: list[str], ordem_b: list[str]) -> float:
    """Correlação de Spearman entre dois rankings das mesmas alternativas."""
    m = len(ordem_a)
    posicao_b = {nome: i for i, nome in enumerate(ordem_b)}
    d2 = sum((i - posicao_b[nome]) ** 2 for i, nome in enumerate(ordem_a))
    return 1 - 6 * d2 / (m * (m * m - 1))


def comparar_metodos(matriz: MatrizDecisao) -> dict:
    """Rankings pelos 4 métodos + matriz de correlação de Spearman."""
    ordens = {nome: metodo(matriz) for nome, metodo in METODOS.items()}
    nomes = list(ordens)
    correlacao = {
        a: {b: round(spearman(ordens[a], ordens[b]), 4) for b in nomes}
        for a in nomes
    }
    return {"rankings": ordens, "spearman": correlacao}


def ensaio_rank_reversal(
    matriz: MatrizDecisao, nome_novo: str, desempenhos_novo: list[float],
    metodo: str = "topsis",
) -> dict:
    """Acrescenta uma alternativa e compara a ordem relativa das originais."""
    ranquear = METODOS[metodo]
    ordem_antes = ranquear(matriz)
    ampliada = MatrizDecisao(
        alternativas=matriz.alternativas + [nome_novo],
        criterios=matriz.criterios,
        desempenhos=matriz.desempenhos + [desempenhos_novo],
        pesos=matriz.pesos,
    )
    ordem_depois_completa = ranquear(ampliada)
    ordem_depois = [n for n in ordem_depois_completa if n != nome_novo]
    return {
        "antes": ordem_antes,
        "depois_completa": ordem_depois_completa,
        "ordem_relativa_depois": ordem_depois,
        "houve_reversao": ordem_depois != ordem_antes,
    }
