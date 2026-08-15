"""Motor do método de criterização em 8 passos (Apêndice D).

Método conduzido em sala pelo autor do livro; o apêndice conta o exercício
completo (a escolha de um carro popular). Aqui vive só a matemática, pura e
sem I/O, como manda a constituição ("Restrições" §2).

Vocabulário do método — a distinção que dá nome ao passo 5:
    ATRIBUTO  = a propriedade medida (preço em R$, consumo em km/l)
    CRITÉRIO  = o atributo já com direção de preferência e escala de valor

Fontes da formulação: interpolação linear entre duas âncoras (a mesma conta de
Celsius→Fahrenheit); pesos por soma das linhas de um grafo de dominância com
autodominância — família dos pesos ordinais discutida no cap. 03 (ver Apêndice
D, "De onde isto veio").
"""

from collections.abc import Sequence


class ErroDeCriterizacao(ValueError):
    """Insumo incoerente com o método (âncoras iguais, rótulo sem de-para…)."""


# --------------------------------------------------------------------------
# Passo 5 — criterização
# --------------------------------------------------------------------------

def interpolar(vi: float, v_min: float, v_max: float,
               c_min: float = 0.0, c_max: float = 10.0) -> float:
    """Leva ``vi`` do domínio original [v_min, v_max] para [c_min, c_max].

    É o "I maiúsculo" do quadro: âncora de cima (v_max ↔ c_max), âncora de
    baixo (v_min ↔ c_min) e a proporção entre elas.

        (vi - v_min) / (v_max - v_min) = (ci - c_min) / (c_max - c_min)

    Direção de preferência entra pelas âncoras, não por uma flag: num critério
    de custo basta inverter c (melhor valor ↔ 10). Ex.: preço com
    ``interpolar(v, 60_000, 110_000, 10, 0)``.
    """
    if v_max == v_min:
        raise ErroDeCriterizacao(
            "âncoras iguais (v_min == v_max): a escala não tem amplitude"
        )
    return c_min + (vi - v_min) * (c_max - c_min) / (v_max - v_min)


def pela_escala_maxima(vi: float, v_max: float, c_max: float = 10.0) -> float:
    """Caso particular da interpolação com o piso no zero real (0 ↔ 0).

        ci = c_max * vi / v_max

    Usar quando o zero do atributo existe de verdade (nenhum item de segurança
    é zero item, não "o pior da amostra"). Preserva a proporção do mundo e
    torna a nota independente de quem está na disputa — logo, imune ao rank
    reversal do cap. 11.
    """
    return interpolar(vi, 0.0, v_max, 0.0, c_max)


def por_tabela(rotulo: str, de_para: dict[str, float]) -> float:
    """Converte atributo qualitativo por tabela de-para ({'Alta': 10, ...}).

    A tabela é uma função de valor declarada por pontos (cap. 07): ela fixa a
    ordem, o espaçamento entre os rótulos E o piso — e o piso decide quanto o
    critério pode punir. Piso 4 em vez de 0 já limita o critério a 60% da
    régua antes de qualquer discussão de peso.
    """
    if rotulo not in de_para:
        raise ErroDeCriterizacao(f"rótulo sem de-para: {rotulo!r}")
    return float(de_para[rotulo])


# --------------------------------------------------------------------------
# Passo 6 — pesos por grafo de dominância
# --------------------------------------------------------------------------

def pesos_por_dominancia(ordem: Sequence[str]) -> dict[str, float]:
    """Pesos a partir da ordem de importância, via grafo de dominância.

    Monta a matriz binária a[i][j] = 1 se o critério i é pelo menos tão
    importante quanto j — **incluindo a diagonal** (autodominância). A soma de
    cada linha é a pontuação; normaliza-se pelo total.

    A autodominância não é detalhe: sem ela o último critério somaria zero, e
    um critério que o decisor conscientemente incluiu sairia do modelo com
    peso nulo. Com ela, a ordem de n critérios rende n, n-1, …, 1 — e o total
    é n(n+1)/2.

    ``ordem`` vai do mais para o menos importante.
    """
    n = len(ordem)
    if n == 0:
        raise ErroDeCriterizacao("ordem vazia")
    if len(set(ordem)) != n:
        raise ErroDeCriterizacao("critério repetido na ordem")
    linhas = [sum(1 for j in range(n) if i <= j) for i in range(n)]
    total = sum(linhas)
    return {c: linha / total for c, linha in zip(ordem, linhas)}


# --------------------------------------------------------------------------
# Passo 7 — medida resumo
# --------------------------------------------------------------------------

def ranquear(criterizada: dict[str, list[float]], pesos: dict[str, float],
             alternativas: Sequence[str]) -> list[tuple[str, float]]:
    """Média ponderada das notas criterizadas, do maior para o menor.

    Soma ponderada e média ponderada dão a MESMA ordem (a divisão por Σw é
    constante positiva); a média é preferida por comunicação — devolve o
    resultado na mesma régua 0–10 dos critérios.
    """
    faltando = set(pesos) - set(criterizada)
    if faltando:
        raise ErroDeCriterizacao(f"critérios sem coluna: {sorted(faltando)}")
    soma_pesos = sum(pesos.values())
    if soma_pesos <= 0:
        raise ErroDeCriterizacao("soma dos pesos deve ser positiva")
    notas = [
        (alt, sum(pesos[c] * criterizada[c][i] for c in pesos) / soma_pesos)
        for i, alt in enumerate(alternativas)
    ]
    return sorted(notas, key=lambda par: -par[1])


# --------------------------------------------------------------------------
# Passo 8 — sensibilidade
# --------------------------------------------------------------------------

def influencia_efetiva(criterizada: dict[str, list[float]],
                       pesos: dict[str, float]) -> dict[str, float]:
    """Peso × amplitude da coluna, normalizado — o que cada critério MEXE.

    Peso declarado não é influência: um critério cuja coluna varia de 7,9 a
    10,0 não decide nada, por maior que seja seu peso. Diagnóstico barato
    para detectar critério achatado (a lição de amplitude do cap. 03).
    """
    bruta = {
        c: pesos[c] * (max(criterizada[c]) - min(criterizada[c])) for c in pesos
    }
    total = sum(bruta.values())
    if total == 0:
        raise ErroDeCriterizacao("nenhum critério discrimina as alternativas")
    return {c: v / total for c, v in bruta.items()}


def desconto_para_empatar(nota_lider: float, nota_rival: float,
                          peso_preco: float, soma_pesos: float,
                          reais_por_ponto: float) -> float:
    """Quanto o preço do rival precisa cair para empatar com o líder.

    Torna a sensibilidade uma pergunta de negociação: em vez de "o resultado é
    robusto?", pergunta-se "de quanto é o desconto que vira o jogo?".
    ``reais_por_ponto`` é a inclinação da régua de preço — com âncoras
    60.000/110.000 em 10/0, cada ponto de nota vale R$ 5.000.
    """
    gap = nota_lider - nota_rival
    if gap <= 0:
        return 0.0
    return (gap * soma_pesos / peso_preco) * reais_por_ponto


def varredura_de_peso(criterizada: dict[str, list[float]],
                      pesos: dict[str, float], alvo: str,
                      alternativas: Sequence[str],
                      passos: int = 1000) -> list[tuple[float, str]]:
    """Varre o peso de ``alvo`` de 0 a 1 renormalizando os demais.

    Devolve as fronteiras: [(peso a partir do qual, vencedor), ...]. A largura
    da faixa do vencedor atual é a margem de segurança do resultado (cap. 11).
    """
    outros = [c for c in pesos if c != alvo]
    soma_outros = sum(pesos[c] for c in outros)
    if soma_outros <= 0:
        raise ErroDeCriterizacao("é preciso mais de um critério para varrer")
    trocas: list[tuple[float, str]] = []
    anterior = None
    for k in range(passos + 1):
        w = k / passos
        p = {alvo: w}
        p.update({c: (1 - w) * pesos[c] / soma_outros for c in outros})
        vencedor = ranquear(criterizada, p, alternativas)[0][0]
        if vencedor != anterior:
            trocas.append((w, vencedor))
            anterior = vencedor
    return trocas
