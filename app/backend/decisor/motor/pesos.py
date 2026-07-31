"""Elicitação de pesos — rating direto, ROC, swing e entropia (cap. 03).

Fontes: Edwards & Barron (1994) para swing/ROC (SMARTS/SMARTER); Hwang & Yoon
(1981) para o método da entropia; ver livro/bibliografia.md. Motor puro.
"""

from math import log

from decisor.motor.saw import normalizar_minmax
from decisor.motor.tipos import Problema


class ErroDePesos(ValueError):
    """Entrada inválida para elicitação de pesos — a mensagem diz a regra."""


def _normalizar_pela_soma(valores: list[float], contexto: str) -> list[float]:
    if any(v < 0 for v in valores):
        raise ErroDePesos(f"{contexto}: valores não podem ser negativos")
    total = sum(valores)
    if total <= 0:
        raise ErroDePesos(f"{contexto}: a soma deve ser positiva")
    return [v / total for v in valores]


def pesos_rating_direto(pontos: list[float]) -> list[float]:
    return _normalizar_pela_soma(pontos, "rating direto")


def pesos_swing(saltos: list[float]) -> list[float]:
    if not saltos or max(saltos) != 100:
        raise ErroDePesos("swing: o salto mais importante deve valer exatamente 100")
    return _normalizar_pela_soma(saltos, "swing")


def pesos_roc(ranking: list[int]) -> list[float]:
    n = len(ranking)
    if sorted(ranking) != list(range(n)):
        raise ErroDePesos(
            "ROC: o ranking deve ser uma permutação de 0..n-1 (ordem estrita)"
        )
    peso_da_posicao = [sum(1 / i for i in range(k, n + 1)) / n for k in range(1, n + 1)]
    pesos = [0.0] * n
    for posicao, criterio in enumerate(ranking):
        pesos[criterio] = peso_da_posicao[posicao]
    return pesos


def pesos_entropia(problema: Problema) -> list[float]:
    m = len(problema.alternativas)
    if m < 2:
        raise ErroDePesos("entropia: são necessárias ao menos 2 alternativas")
    colunas = list(zip(*normalizar_minmax(problema)))
    diversificacao = []
    for coluna in colunas:
        total = sum(coluna)
        if total == 0:
            diversificacao.append(0.0)
            continue
        p = [x / total for x in coluna]
        entropia = -sum(pi * log(pi) for pi in p if pi > 0) / log(m)
        diversificacao.append(1 - entropia)
    if sum(diversificacao) == 0:
        raise ErroDePesos("entropia: nenhum critério discrimina as alternativas")
    return _normalizar_pela_soma(diversificacao, "entropia")
