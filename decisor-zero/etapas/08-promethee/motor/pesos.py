"""Pesos — de onde vem o vetor w que todo método compensatório consome.

Cap. 03 do livro. Quatro técnicas, das mais subjetivas às mais "objetivas":

- rating direto: o decisor distribui pontos; normaliza-se pela soma. Simples e
  frágil (âncora no primeiro número dito) — Belton & Stewart (2002).
- ROC (Rank Order Centroid): o decisor só ORDENA os critérios; os pesos são o
  centroide do simplex compatível com essa ordem (Edwards & Barron, 1994 —
  SMARTER). w_k = (1/n) Σ_{i=k..n} 1/i para a posição k do ranking.
- swing: parte do pior cenário e pergunta "qual salto pior→melhor você mais
  quer?"; o salto mais valioso vale 100 e ancora os demais (Edwards & Barron,
  1994). Único aqui que olha as AMPLITUDES reais do problema.
- entropia: pesos extraídos dos DADOS — critério que discrimina mais as
  alternativas pesa mais (método da entropia em Hwang & Yoon, 1981). Não
  consulta preferência nenhuma: é medida de informação, não de importância.

Motor puro, sem I/O.
"""

from math import log

from motor.matriz import MatrizDecisao
from motor.normalizacao import normalizar_minmax


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
    """Pontos livres (ex.: 35, 25, 25, 15) → pesos que somam 1."""
    return _normalizar_pela_soma(pontos, "rating direto")


def pesos_swing(saltos: list[float]) -> list[float]:
    """Valores de swing (o salto mais importante = 100) → pesos que somam 1."""
    if not saltos or max(saltos) != 100:
        raise ErroDePesos("swing: o salto mais importante deve valer exatamente 100")
    return _normalizar_pela_soma(saltos, "swing")


def pesos_roc(ranking: list[int]) -> list[float]:
    """ROC a partir de um ranking de índices de critério (do mais ao menos importante).

    Ex.: ranking [0, 1, 2, 3] com n=4 → pesos por critério na ordem ORIGINAL
    das colunas, não na ordem do ranking.
    """
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


def pesos_entropia(matriz: MatrizDecisao) -> list[float]:
    """Pesos pela entropia de Shannon sobre a matriz normalizada (min-max).

    e_j = -Σ_i p_ij·ln(p_ij) / ln(m); d_j = 1 - e_j (grau de diversificação);
    w_j = d_j / Σ d_j. Critério que não discrimina (coluna constante) → d_j = 0.
    """
    m = len(matriz.alternativas)
    if m < 2:
        raise ErroDePesos("entropia: são necessárias ao menos 2 alternativas")
    colunas = list(zip(*normalizar_minmax(matriz)))
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
