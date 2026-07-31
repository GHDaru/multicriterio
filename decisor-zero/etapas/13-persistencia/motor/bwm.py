"""BWM — Best-Worst Method (Rezaei, 2015). Cap. 10.

O decisor escolhe o critério MAIS importante (best) e o MENOS (worst) e faz só
2n−3 comparações: best-para-todos (a_Bj) e todos-para-worst (a_jW). Os pesos
saem do modelo LINEAR (Rezaei, 2016): min ξ sujeito a |w_B − a_Bj·w_j| ≤ ξ,
|w_j − a_jW·w_W| ≤ ξ, Σw = 1, w ≥ 0 — resolvido com scipy.optimize.linprog
(ADR 0006). ξ* é o índice de consistência (0 = perfeitamente consistente).

Motor puro (usa scipy), sem I/O.
"""

from scipy.optimize import linprog


class ErroDeBWM(ValueError):
    """Entrada inválida para o BWM — a mensagem diz a regra."""


def pesos_bwm(best: int, worst: int, best_para_todos: list[float],
              todos_para_worst: list[float]) -> dict:
    n = len(best_para_todos)
    if len(todos_para_worst) != n:
        raise ErroDeBWM("os dois vetores devem ter o mesmo tamanho")
    if best == worst:
        raise ErroDeBWM("best e worst devem ser critérios diferentes")
    if not (0 <= best < n and 0 <= worst < n):
        raise ErroDeBWM("índices de best/worst fora da faixa")
    if best_para_todos[best] != 1 or todos_para_worst[worst] != 1:
        raise ErroDeBWM("a_BB e a_WW devem valer 1")
    if any(a < 1 or a > 9 for a in best_para_todos + todos_para_worst):
        raise ErroDeBWM("comparações devem estar na escala 1–9")

    # Variáveis: w_0..w_{n-1}, ξ. Minimizar ξ.
    a_ub, b_ub = [], []
    for j in range(n):
        if j != best:
            linha = [0.0] * (n + 1); linha[best] = 1; linha[j] = -best_para_todos[j]
            linha[n] = -1; a_ub.append(linha); b_ub.append(0.0)
            linha = [0.0] * (n + 1); linha[best] = -1; linha[j] = best_para_todos[j]
            linha[n] = -1; a_ub.append(linha); b_ub.append(0.0)
        if j != worst:
            linha = [0.0] * (n + 1); linha[j] = 1; linha[worst] = -todos_para_worst[j]
            linha[n] = -1; a_ub.append(linha); b_ub.append(0.0)
            linha = [0.0] * (n + 1); linha[j] = -1; linha[worst] = todos_para_worst[j]
            linha[n] = -1; a_ub.append(linha); b_ub.append(0.0)
    resultado = linprog(
        c=[0.0] * n + [1.0], A_ub=a_ub, b_ub=b_ub,
        A_eq=[[1.0] * n + [0.0]], b_eq=[1.0], bounds=[(0, None)] * (n + 1),
    )
    if not resultado.success:
        raise ErroDeBWM(f"otimização falhou: {resultado.message}")
    return {
        "pesos": [round(float(x), 6) for x in resultado.x[:n]],
        "xi": round(float(resultado.x[n]), 6),  # 0 = consistente
    }
