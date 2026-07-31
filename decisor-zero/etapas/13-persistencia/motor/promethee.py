"""PROMETHEE I/II — sobreclassificação por fluxos (Brans & Vincke, 1985).

Cap. 08 do livro. Para cada par (a, b) e critério j, a diferença de desempenho
(ajustada pela direção) passa por uma FUNÇÃO DE PREFERÊNCIA P_j; o índice
π(a,b) = Σ w_j·P_j agrega. Fluxos: φ+ (quanto a supera os demais), φ− (quanto
é superada), φ = φ+ − φ− (PROMETHEE II, ordem total). Funções implementadas
(ADR 0006): "usual" (degrau) e "vshape" (linear até o limiar p).

Motor puro, sem I/O.
"""

from motor.matriz import MatrizDecisao


class ErroDePreferencia(ValueError):
    """Configuração de preferência inválida — a mensagem diz a regra."""


def _p_usual(d: float, _p: float | None) -> float:
    return 1.0 if d > 0 else 0.0


def _p_vshape(d: float, p: float | None) -> float:
    if p is None or p <= 0:
        raise ErroDePreferencia("vshape exige limiar p > 0")
    if d <= 0:
        return 0.0
    return min(d / p, 1.0)


FUNCOES = {"usual": _p_usual, "vshape": _p_vshape}


def fluxos_promethee(
    matriz: MatrizDecisao,
    funcao: str = "usual",
    limiares: list[float] | None = None,
) -> list[dict]:
    """PROMETHEE II: φ+, φ− e φ por alternativa, ordenado por φ decrescente."""
    if matriz.pesos is None:
        raise ValueError("PROMETHEE exige pesos (ver cap. 03)")
    if funcao not in FUNCOES:
        raise ErroDePreferencia(f"função {funcao!r} desconhecida (use {sorted(FUNCOES)})")
    n = len(matriz.criterios)
    p_por_criterio = limiares if limiares is not None else [None] * n
    if len(p_por_criterio) != n:
        raise ErroDePreferencia(f"{n} critérios, {len(p_por_criterio)} limiares")
    m = len(matriz.alternativas)
    pref = FUNCOES[funcao]

    def pi(a: int, b: int) -> float:
        total = 0.0
        for j in range(n):
            xa, xb = matriz.desempenhos[a][j], matriz.desempenhos[b][j]
            d = xa - xb if matriz.criterios[j].direcao == "beneficio" else xb - xa
            total += matriz.pesos[j] * pref(d, p_por_criterio[j])
        return total

    resultado = []
    for a in range(m):
        positivo = sum(pi(a, b) for b in range(m) if b != a) / (m - 1)
        negativo = sum(pi(b, a) for b in range(m) if b != a) / (m - 1)
        resultado.append({
            "alternativa": matriz.alternativas[a],
            "fluxo_positivo": round(positivo, 6),
            "fluxo_negativo": round(negativo, 6),
            "escore": round(positivo - negativo, 6),  # φ líquido
        })
    resultado.sort(key=lambda l: l["escore"], reverse=True)
    for pos, linha in enumerate(resultado, start=1):
        linha["posicao"] = pos
    return resultado
