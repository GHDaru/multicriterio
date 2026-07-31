"""Decisão em grupo — agregação de rankings e de julgamentos. Cap. 12.

Dois caminhos clássicos (Belton & Stewart 2002; Greco et al. 2016):
- agregar RANKINGS individuais: contagem de Borda (posições viram pontos) e
  Copeland (torneio de maiorias par a par — vitórias menos derrotas);
- agregar JULGAMENTOS AHP: média geométrica elemento a elemento (preserva a
  reciprocidade), depois autovetor (etapa 05).

Motor puro, sem I/O.
"""

from motor.ahp import prioridades_ahp


class ErroDeGrupo(ValueError):
    """Entrada inválida — a mensagem diz a regra."""


def _validar_rankings(rankings: list[list[str]]) -> list[str]:
    if len(rankings) < 2:
        raise ErroDeGrupo("são necessários ao menos 2 rankings")
    universo = sorted(rankings[0])
    for i, r in enumerate(rankings):
        if sorted(r) != universo:
            raise ErroDeGrupo(f"ranking {i} não é permutação das mesmas alternativas")
    return universo


def borda(rankings: list[list[str]]) -> list[dict]:
    """1º lugar vale m−1 pontos, último vale 0; soma entre os votantes."""
    universo = _validar_rankings(rankings)
    m = len(universo)
    pontos = {nome: 0 for nome in universo}
    for ranking in rankings:
        for posicao, nome in enumerate(ranking):
            pontos[nome] += m - 1 - posicao
    linhas = [{"alternativa": n, "escore": p} for n, p in pontos.items()]
    linhas.sort(key=lambda l: (-l["escore"], l["alternativa"]))
    for pos, linha in enumerate(linhas, start=1):
        linha["posicao"] = pos
    return linhas


def copeland(rankings: list[list[str]]) -> list[dict]:
    """Torneio de maiorias: escore = vitórias − derrotas nos duelos par a par."""
    universo = _validar_rankings(rankings)
    posicoes = [{nome: r.index(nome) for nome in universo} for r in rankings]

    def duelo(a: str, b: str) -> int:
        votos_a = sum(1 for p in posicoes if p[a] < p[b])
        votos_b = len(posicoes) - votos_a
        return (votos_a > votos_b) - (votos_b > votos_a)  # 1, -1 ou 0

    escores = {a: sum(duelo(a, b) for b in universo if b != a) for a in universo}
    linhas = [{"alternativa": n, "escore": e} for n, e in escores.items()]
    linhas.sort(key=lambda l: (-l["escore"], l["alternativa"]))
    for pos, linha in enumerate(linhas, start=1):
        linha["posicao"] = pos
    return linhas


def agregar_julgamentos(matrizes: list[list[list[float]]]) -> dict:
    """Média geométrica elemento a elemento (AIJ) + prioridades AHP do grupo."""
    if len(matrizes) < 2:
        raise ErroDeGrupo("são necessárias ao menos 2 matrizes de julgamento")
    n = len(matrizes[0])
    if any(len(m) != n or any(len(l) != n for l in m) for m in matrizes):
        raise ErroDeGrupo("todas as matrizes devem ser n×n iguais")
    k = len(matrizes)
    agregada = [
        [
            (lambda prod: prod ** (1 / k))(
                __import__("math").prod(m[i][j] for m in matrizes)
            )
            for j in range(n)
        ]
        for i in range(n)
    ]
    return {"julgamentos_agregados": agregada, **prioridades_ahp(agregada)}
