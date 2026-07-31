"""PROMETHEE II (Brans & Vincke, 1985) — cap. 08. Função "usual" (default do
produto; V-shape na etapa 08). Motor puro; cópia adaptada da etapa 08."""

from decisor.motor.tipos import Problema


def ranquear_promethee2(problema: Problema) -> list[dict]:
    if problema.pesos is None:
        raise ValueError("PROMETHEE exige pesos (ver cap. 03 do livro)")
    m, n = len(problema.alternativas), len(problema.criterios)

    def pi(a: int, b: int) -> float:
        total = 0.0
        for j in range(n):
            xa, xb = problema.desempenhos[a][j], problema.desempenhos[b][j]
            d = xa - xb if problema.criterios[j].direcao == "beneficio" else xb - xa
            total += problema.pesos[j] * (1.0 if d > 0 else 0.0)
        return total

    resultado = []
    for a in range(m):
        positivo = sum(pi(a, b) for b in range(m) if b != a) / (m - 1)
        negativo = sum(pi(b, a) for b in range(m) if b != a) / (m - 1)
        resultado.append({
            "alternativa": problema.alternativas[a],
            "escore": round(positivo - negativo, 6),
        })
    resultado.sort(key=lambda l: l["escore"], reverse=True)
    for pos, linha in enumerate(resultado, start=1):
        linha["posicao"] = pos
    return resultado
