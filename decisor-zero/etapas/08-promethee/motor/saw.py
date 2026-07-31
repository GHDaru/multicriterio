"""SAW (Simple Additive Weighting) — o método aditivo clássico.

Cap. 04 do livro. Agregação aditiva: escore_i = Σ_j w_j · r_ij, sobre a matriz
min-max normalizada (direção resolvida, cap. 03). Fontes: Fishburn (1967),
Operations Research 15(3) — a formalização da utilidade aditiva — e Hwang &
Yoon (1981), que o catalogam como o método de referência do MADM; o processo
de elicitação que o acompanha (SMART/SMARTS) é de Edwards & Barron (1994).
Ver livro/bibliografia.md.

Motor puro: consome MatrizDecisao COM pesos, não faz I/O.
"""

from motor.matriz import MatrizDecisao
from motor.normalizacao import normalizar_minmax


def ranquear_saw(matriz: MatrizDecisao) -> list[dict]:
    """Ranking SAW em ordem decrescente de escore.

    Exige pesos na matriz (Σw=1, w>=0 — validados pela MatrizDecisao); a
    normalização é sempre a min-max, que já entrega 1 = melhor da coluna.
    """
    if matriz.pesos is None:
        raise ValueError("SAW exige pesos (ver cap. 03: rating, ROC, swing…)")
    normalizada = normalizar_minmax(matriz)
    escores = {
        nome: sum(w * r for w, r in zip(matriz.pesos, linha))
        for nome, linha in zip(matriz.alternativas, normalizada)
    }
    ordenado = sorted(escores.items(), key=lambda par: par[1], reverse=True)
    return [
        {"posicao": pos, "alternativa": nome, "escore": round(escore, 6)}
        for pos, (nome, escore) in enumerate(ordenado, start=1)
    ]
