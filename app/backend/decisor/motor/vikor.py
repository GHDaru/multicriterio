"""VIKOR (Opricovic & Tzeng, 2004) — cap. 10. v = 0,5. Escore = Q (menor é
melhor); inclui condições de aceitação e conjunto de compromisso. Motor puro;
cópia adaptada da etapa 10."""

from decisor.motor.tipos import Problema


def ranquear_vikor(problema: Problema) -> list[dict]:
    if problema.pesos is None:
        raise ValueError("VIKOR exige pesos (ver cap. 03 do livro)")
    m = len(problema.alternativas)
    colunas = list(zip(*problema.desempenhos))
    melhor, pior = [], []
    for c, criterio in zip(colunas, problema.criterios):
        if criterio.direcao == "custo":
            melhor.append(min(c)); pior.append(max(c))
        else:
            melhor.append(max(c)); pior.append(min(c))
    S, R = [], []
    for linha in problema.desempenhos:
        termos = [
            w * abs(f_m - x) / abs(f_m - f_p) if f_m != f_p else 0.0
            for w, f_m, f_p, x in zip(problema.pesos, melhor, pior, linha)
        ]
        S.append(sum(termos)); R.append(max(termos))
    s_min, s_max, r_min, r_max = min(S), max(S), min(R), max(R)
    linhas = []
    for i, nome in enumerate(problema.alternativas):
        parte_s = (S[i] - s_min) / (s_max - s_min) if s_max != s_min else 0.0
        parte_r = (R[i] - r_min) / (r_max - r_min) if r_max != r_min else 0.0
        linhas.append({"alternativa": nome, "escore": round(0.5 * parte_s + 0.5 * parte_r, 6)})
    linhas.sort(key=lambda l: l["escore"])  # Q: menor é melhor
    for pos, linha in enumerate(linhas, start=1):
        linha["posicao"] = pos
    return linhas
