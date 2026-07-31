"""ELECTRE I — sobreclassificação com concordância, discordância e veto.

Cap. 09 do livro. Fonte seminal: Roy (1968), RAIRO 2(8) — o nascimento do
outranking. a sobreclassifica b (a S b) quando a coalizão de critérios a favor
é forte (C(a,b) >= c*) E nenhum critério contra protesta alto demais
(D(a,b) <= d*); vetos por critério bloqueiam S incondicionalmente. A saída não
é ranking: é a relação S e o KERNEL (alternativas sem sobreclassificador
estrito — a shortlist defensável).

Motor puro, sem I/O. Discordância normalizada pela amplitude da coluna.
"""

from motor.matriz import MatrizDecisao


class ErroDeLimiares(ValueError):
    """Limiares fora de faixa — a mensagem diz a regra."""


def analisar_electre(
    matriz: MatrizDecisao,
    c_estrela: float = 0.6,
    d_estrela: float = 0.4,
    vetos: list[float | None] | None = None,
) -> dict:
    if matriz.pesos is None:
        raise ValueError("ELECTRE exige pesos (ver cap. 03)")
    if not (0.5 <= c_estrela <= 1.0):
        raise ErroDeLimiares("c* deve estar em [0,5; 1,0]")
    if not (0.0 <= d_estrela <= 1.0):
        raise ErroDeLimiares("d* deve estar em [0; 1]")
    n = len(matriz.criterios)
    vetos = vetos if vetos is not None else [None] * n
    if len(vetos) != n:
        raise ErroDeLimiares(f"{n} critérios, {len(vetos)} vetos")
    m = len(matriz.alternativas)
    colunas = list(zip(*matriz.desempenhos))
    amplitude = [max(c) - min(c) for c in colunas]

    def melhor_igual(a: int, b: int, j: int) -> bool:
        xa, xb = matriz.desempenhos[a][j], matriz.desempenhos[b][j]
        return xa <= xb if matriz.criterios[j].direcao == "custo" else xa >= xb

    def contra(a: int, b: int, j: int) -> float:
        """Vantagem de b sobre a no critério j, em unidades do critério."""
        xa, xb = matriz.desempenhos[a][j], matriz.desempenhos[b][j]
        return (xa - xb) if matriz.criterios[j].direcao == "custo" else (xb - xa)

    def concordancia(a: int, b: int) -> float:
        return sum(matriz.pesos[j] for j in range(n) if melhor_igual(a, b, j))

    def discordancia(a: int, b: int) -> float:
        piores = [
            contra(a, b, j) / amplitude[j]
            for j in range(n)
            if not melhor_igual(a, b, j) and amplitude[j] > 0
        ]
        return max(piores) if piores else 0.0

    def vetado(a: int, b: int) -> bool:
        return any(
            vetos[j] is not None and contra(a, b, j) >= vetos[j] for j in range(n)
        )

    sobre = []
    for a in range(m):
        for b in range(m):
            if a == b:
                continue
            passa = (
                concordancia(a, b) >= c_estrela
                and discordancia(a, b) <= d_estrela
                and not vetado(a, b)
            )
            if passa:
                sobre.append((matriz.alternativas[a], matriz.alternativas[b]))
    estrito = {
        (a, b) for a, b in sobre if (b, a) not in sobre
    }
    kernel = [
        nome for nome in matriz.alternativas
        if not any(b == nome for _, b in estrito)
    ]
    return {
        "concordancia": [
            [round(concordancia(a, b), 4) if a != b else None for b in range(m)]
            for a in range(m)
        ],
        "discordancia": [
            [round(discordancia(a, b), 4) if a != b else None for b in range(m)]
            for a in range(m)
        ],
        "sobreclassifica": sorted(sobre),
        "kernel": kernel,
    }
