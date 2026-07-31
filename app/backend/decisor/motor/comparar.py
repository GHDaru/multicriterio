"""Comparação multi-método + correlação de Spearman (cap. 11). Motor puro."""

from decisor.motor.promethee import ranquear_promethee2
from decisor.motor.saw import ranquear_saw
from decisor.motor.tipos import Problema
from decisor.motor.topsis import ranquear_topsis
from decisor.motor.vikor import ranquear_vikor

METODOS_COMPARAVEIS = {
    "saw": ranquear_saw,
    "topsis": ranquear_topsis,
    "promethee2": ranquear_promethee2,
    "vikor": ranquear_vikor,
}


def spearman(ordem_a: list[str], ordem_b: list[str]) -> float:
    m = len(ordem_a)
    posicao_b = {nome: i for i, nome in enumerate(ordem_b)}
    d2 = sum((i - posicao_b[nome]) ** 2 for i, nome in enumerate(ordem_a))
    return 1 - 6 * d2 / (m * (m * m - 1))


def comparar_metodos(problema: Problema) -> dict:
    ordens = {
        nome: [l["alternativa"] for l in metodo(problema)]
        for nome, metodo in METODOS_COMPARAVEIS.items()
    }
    nomes = list(ordens)
    correlacao = {
        a: {b: round(spearman(ordens[a], ordens[b]), 4) for b in nomes}
        for a in nomes
    }
    pares = [
        correlacao[a][b] for i, a in enumerate(nomes) for b in nomes[i + 1:]
    ]
    return {
        "rankings": ordens,
        "spearman": correlacao,
        "concordancia_media": round(sum(pares) / len(pares), 4),
    }
