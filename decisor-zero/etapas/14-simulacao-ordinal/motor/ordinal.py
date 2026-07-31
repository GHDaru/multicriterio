"""AEO — Agregação Estocástica Ordinal (contribuição original deste livro).

Cap. 14 e Apêndice C (artigo completo). Ideia (do autor): quando só há
informação ORDINAL — o ranking das alternativas em cada critério e, opcional-
mente, a ordem de importância dos critérios — simule "infinitas funções de
importância" compatíveis com essa ordem: a cada rodada, sorteie valores U(0,1),
ordene-os conforme os rankings (maior valor para o mais preferido), normalize
colunas e pesos para somar 1, agregue por soma ponderada e anote o ranking.
A matriz alternativa × posição (aceitabilidade) resume o torneio.

Parentesco (ver artigo, §2): família SMAA — Lahdelma, Hokkanen & Salminen
(1998); SMAA-2 (Lahdelma & Salminen, 2001: aceitabilidade por posição, vetor
de pesos central); SMAA-O (Lahdelma, Miettinen & Salminen, 2003: critérios
ordinais). Difere no prior de imputação cardinal (uniformes ordenadas
normalizadas pela soma) e no protocolo de decisão recomendado (posto esperado
+ checagem de Condorcet estocástico + desempate lexicográfico).

Motor puro; aleatoriedade só via random.Random(semente) — reprodutível.
"""

import random


class ErroDeOrdinal(ValueError):
    """Entrada ordinal inválida — a mensagem diz a regra."""


def _validar(alternativas, rankings_criterios, ordem_pesos):
    universo = sorted(alternativas)
    if len(set(alternativas)) != len(alternativas):
        raise ErroDeOrdinal("alternativas repetidas")
    if len(alternativas) < 2:
        raise ErroDeOrdinal("são necessárias ao menos 2 alternativas")
    if not rankings_criterios:
        raise ErroDeOrdinal("é necessário ao menos 1 critério")
    for j, ranking in enumerate(rankings_criterios):
        if sorted(ranking) != universo:
            raise ErroDeOrdinal(
                f"ranking do critério {j} não é permutação das alternativas"
            )
    n = len(rankings_criterios)
    if ordem_pesos is not None and sorted(ordem_pesos) != list(range(n)):
        raise ErroDeOrdinal("ordem_pesos deve ser permutação de 0..n-1")


def simular_aeo(
    alternativas: list[str],
    rankings_criterios: list[list[str]],
    ordem_pesos: list[int] | None = None,
    n_simulacoes: int = 10_000,
    semente: int | None = None,
) -> dict:
    """Roda o torneio estocástico e devolve o dossiê completo.

    Retorna: aceitabilidade (fração de vezes em cada posição, por alternativa),
    posto_esperado, ordem_final (por posto esperado; desempate lexicográfico na
    aceitabilidade), prob_par_a_par, vencedor_condorcet (ou None) e
    pesos_centrais (média dos vetores de peso nas rodadas em que a alternativa
    venceu — as "crenças" que a elegem).
    """
    _validar(alternativas, rankings_criterios, ordem_pesos)
    rng = random.Random(semente)
    m, n = len(alternativas), len(rankings_criterios)
    indice = {nome: i for i, nome in enumerate(alternativas)}

    posicoes = [[0] * m for _ in range(m)]        # [alt][posição]
    vitorias = [[0] * m for _ in range(m)]        # [a][b]: score_a > score_b
    soma_pesos_vencedor = [[0.0] * n for _ in range(m)]
    vitorias_totais = [0] * m

    for _ in range(n_simulacoes):
        # valores ordinais → cardinais: uniformes ordenadas, coluna soma 1
        valores = [[0.0] * n for _ in range(m)]
        for j, ranking in enumerate(rankings_criterios):
            sorteio = sorted((rng.random() for _ in range(m)), reverse=True)
            total = sum(sorteio)
            for posicao, nome in enumerate(ranking):
                valores[indice[nome]][j] = sorteio[posicao] / total
        # pesos: uniformes; com ordem declarada, o maior vai ao mais importante
        brutos = [rng.random() for _ in range(n)]
        if ordem_pesos is not None:
            ordenados = sorted(brutos, reverse=True)
            pesos = [0.0] * n
            for posicao, criterio in enumerate(ordem_pesos):
                pesos[criterio] = ordenados[posicao]
        else:
            pesos = brutos
        total_w = sum(pesos)
        pesos = [w / total_w for w in pesos]
        # agrega e ranqueia (empate tem probabilidade zero)
        escores = [
            sum(w * v for w, v in zip(pesos, valores[i])) for i in range(m)
        ]
        ordem = sorted(range(m), key=escores.__getitem__, reverse=True)
        for posicao, i in enumerate(ordem):
            posicoes[i][posicao] += 1
        for a in range(m):
            for b in range(m):
                if a != b and escores[a] > escores[b]:
                    vitorias[a][b] += 1
        campeao = ordem[0]
        vitorias_totais[campeao] += 1
        for j in range(n):
            soma_pesos_vencedor[campeao][j] += pesos[j]

    aceitabilidade = {
        nome: [round(c / n_simulacoes, 4) for c in posicoes[i]]
        for nome, i in indice.items()
    }
    posto_esperado = {
        nome: round(
            sum((p + 1) * c for p, c in enumerate(posicoes[i])) / n_simulacoes, 4
        )
        for nome, i in indice.items()
    }
    # ordem final: posto esperado; desempate lexicográfico (mais 1ºs, 2ºs, …)
    ordem_final = sorted(
        alternativas,
        key=lambda nome: (posto_esperado[nome],
                          [-x for x in aceitabilidade[nome]]),
    )
    prob = {
        a: {
            b: round(vitorias[indice[a]][indice[b]] / n_simulacoes, 4)
            for b in alternativas if b != a
        }
        for a in alternativas
    }
    condorcet = next(
        (a for a in alternativas
         if all(prob[a][b] > 0.5 for b in alternativas if b != a)),
        None,
    )
    pesos_centrais = {}
    for nome, i in indice.items():
        if vitorias_totais[i] == 0:
            pesos_centrais[nome] = None
        else:
            media = [s / vitorias_totais[i] for s in soma_pesos_vencedor[i]]
            total = sum(media)
            pesos_centrais[nome] = [round(x / total, 4) for x in media]
    return {
        "n_simulacoes": n_simulacoes,
        "aceitabilidade": aceitabilidade,
        "posto_esperado": posto_esperado,
        "ordem_final": ordem_final,
        "prob_par_a_par": prob,
        "vencedor_condorcet": condorcet,
        "pesos_centrais": pesos_centrais,
    }
