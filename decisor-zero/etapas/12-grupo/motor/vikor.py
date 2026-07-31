"""VIKOR — a solução de compromisso (Opricovic & Tzeng, 2004). Cap. 10.

S_i (soma ponderada dos arrependimentos), R_i (o pior arrependimento) e
Q_i = v·(S−S*)/(S⁻−S*) + (1−v)·(R−R*)/(R⁻−R*), com v = 0,5 (ADR 0006).
Ranking por Q CRESCENTE. O VIKOR ainda checa duas condições e pode devolver um
CONJUNTO de compromisso em vez de vencedor único: C1 (vantagem aceitável:
Q(2º)−Q(1º) >= 1/(m−1)) e C2 (estabilidade: o 1º em Q também lidera S ou R).

Motor puro, sem I/O.
"""

from motor.matriz import MatrizDecisao


def analisar_vikor(matriz: MatrizDecisao, v: float = 0.5) -> dict:
    if matriz.pesos is None:
        raise ValueError("VIKOR exige pesos (ver cap. 03)")
    if not 0.0 <= v <= 1.0:
        raise ValueError("v deve estar em [0, 1]")
    m = len(matriz.alternativas)
    colunas = list(zip(*matriz.desempenhos))
    melhor, pior = [], []
    for c, criterio in zip(colunas, matriz.criterios):
        if criterio.direcao == "custo":
            melhor.append(min(c)); pior.append(max(c))
        else:
            melhor.append(max(c)); pior.append(min(c))
    S, R = [], []
    for linha in matriz.desempenhos:
        termos = [
            w * abs(f_m - x) / abs(f_m - f_p) if f_m != f_p else 0.0
            for w, f_m, f_p, x in zip(matriz.pesos, melhor, pior, linha)
        ]
        S.append(sum(termos)); R.append(max(termos))
    s_min, s_max, r_min, r_max = min(S), max(S), min(R), max(R)

    def q(i: int) -> float:
        parte_s = (S[i] - s_min) / (s_max - s_min) if s_max != s_min else 0.0
        parte_r = (R[i] - r_min) / (r_max - r_min) if r_max != r_min else 0.0
        return v * parte_s + (1 - v) * parte_r

    linhas = [
        {"alternativa": nome, "S": round(S[i], 6), "R": round(R[i], 6),
         "escore": round(q(i), 6)}  # escore = Q; MENOR é melhor
        for i, nome in enumerate(matriz.alternativas)
    ]
    linhas.sort(key=lambda l: l["escore"])
    for pos, linha in enumerate(linhas, start=1):
        linha["posicao"] = pos
    dq = 1.0 / (m - 1)
    vantagem_aceitavel = (linhas[1]["escore"] - linhas[0]["escore"]) >= dq
    lider = linhas[0]["alternativa"]
    estavel = (
        min(range(m), key=S.__getitem__) == matriz.alternativas.index(lider)
        or min(range(m), key=R.__getitem__) == matriz.alternativas.index(lider)
    )
    if vantagem_aceitavel and estavel:
        compromisso = [lider]
    else:
        compromisso = [
            l["alternativa"] for l in linhas
            if l["escore"] - linhas[0]["escore"] < dq
        ]
    return {
        "ranking": linhas,
        "dq": round(dq, 6),
        "vantagem_aceitavel": vantagem_aceitavel,
        "estavel": estavel,
        "conjunto_compromisso": compromisso,
    }
