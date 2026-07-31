"""AHP — prioridades a partir de comparações par a par (Saaty).

Cap. 05 do livro. Fontes: Saaty (1977), J. Math. Psychology 15(3) — autovetor
principal, escala 1–9 e razão de consistência — e Saaty (1980), o livro.
Decisão do projeto (ADR 0006): o AHP entra como técnica de PESOS; autovetor
pelo método das potências (Python puro, sem numpy); RI de Saaty.

Motor puro, sem I/O. Cópia do decisor-zero etapa 05 (etapas são congeladas).
"""

RI_SAATY = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32,
            8: 1.41, 9: 1.45, 10: 1.49}
LIMITE_CR = 0.10  # Saaty (1980): acima disso, revisar os julgamentos


class ErroDeJulgamentos(ValueError):
    """A matriz de comparações viola a definição — a mensagem diz a regra."""


def _validar(julgamentos: list[list[float]]) -> int:
    n = len(julgamentos)
    if n < 2:
        raise ErroDeJulgamentos("são necessários ao menos 2 itens comparados")
    for i, linha in enumerate(julgamentos):
        if len(linha) != n:
            raise ErroDeJulgamentos(f"linha {i} tem {len(linha)} colunas para n={n}")
        if abs(linha[i] - 1.0) > 1e-9:
            raise ErroDeJulgamentos(f"diagonal deve ser 1 (posição {i},{i})")
        for j, valor in enumerate(linha):
            if valor <= 0:
                raise ErroDeJulgamentos(f"julgamento ({i},{j}) deve ser positivo")
            if abs(valor * julgamentos[j][i] - 1.0) > 1e-6:
                raise ErroDeJulgamentos(
                    f"recíproco violado: a[{i}][{j}]·a[{j}][{i}] ≠ 1"
                )
    return n


def prioridades_ahp(julgamentos: list[list[float]], iteracoes: int = 200) -> dict:
    """Vetor de prioridades + diagnóstico de consistência.

    Retorna {"pesos", "lambda_max", "ci", "cr", "consistente"}; cr é None para
    n=1..2 (sempre consistentes por construção).
    """
    n = _validar(julgamentos)
    w = [1.0 / n] * n
    for _ in range(iteracoes):
        aw = [sum(julgamentos[i][j] * w[j] for j in range(n)) for i in range(n)]
        total = sum(aw)
        w = [x / total for x in aw]
    aw = [sum(julgamentos[i][j] * w[j] for j in range(n)) for i in range(n)]
    lambda_max = sum(aw[i] / w[i] for i in range(n)) / n
    ci = (lambda_max - n) / (n - 1) if n > 1 else 0.0
    ri = RI_SAATY.get(n)
    if ri is None:
        raise ErroDeJulgamentos(f"RI de Saaty tabelado só até n={max(RI_SAATY)}")
    cr = None if ri == 0 else ci / ri
    return {
        "pesos": w,
        "lambda_max": lambda_max,
        "ci": ci,
        "cr": cr,
        "consistente": True if cr is None else cr <= LIMITE_CR,
    }
