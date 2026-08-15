"""Testes da etapa 15 — todos os números do Apêndice D são fixture (Princípio I).

Se um número do apêndice mudar sem que este arquivo mude junto, a CI reprova.
Caso do apêndice: a escolha de um carro popular zero (exercício de sala, 2026).
"""

import pytest

from motor.criterizacao import (
    ErroDeCriterizacao,
    desconto_para_empatar,
    influencia_efetiva,
    interpolar,
    pela_escala_maxima,
    pesos_por_dominancia,
    por_tabela,
    ranquear,
    varredura_de_peso,
)

ALTERNATIVAS = ["Kwid Zen", "Onix 1.0", "208 Style", "Mobi Like"]

# Passo 4 — coletado em carrosnaweb.com.br (fonte única, 2026-08)
BRUTO = {
    "Preco":         [82790, 81837, 106990, 66934],
    "Consumo":       [14.4, 13.5, 13.6, 14.5],       # urbano, gasolina (km/l)
    "Conforto":      [10, 18, 18, 7.5],              # itens: verde=1, amarelo=0,5
    "Seguranca":     [18, 20, 21, 16.5],
    "Infotenimento": [4, 11, 9, 5],
    "Confianca":     ["Baixa", "Alta", "Baixa", "Media"],
}
DE_PARA_CONFIANCA = {"Alta": 10, "Media": 7, "Baixa": 4}
ORDEM_IMPORTANCIA = [
    "Preco", "Seguranca", "Consumo", "Confianca", "Conforto", "Infotenimento",
]


@pytest.fixture
def criterizada():
    """Passo 5 com as âncoras declaradas em sala."""
    return {
        # custo: melhor (60k) -> 10, pior (110k) -> 0
        "Preco": [interpolar(v, 60_000, 110_000, 10, 0) for v in BRUTO["Preco"]],
        # faixa estreita (1 km/l): piso levantado para 5
        "Consumo": [interpolar(v, 13.5, 14.5, 5, 10) for v in BRUTO["Consumo"]],
        # escala real: 20 itens possíveis
        "Conforto": [pela_escala_maxima(v, 20) for v in BRUTO["Conforto"]],
        "Seguranca": [pela_escala_maxima(v, 21) for v in BRUTO["Seguranca"]],
        # faixa estreita: piso levantado para 5
        "Infotenimento": [interpolar(v, 4, 11, 5, 10) for v in BRUTO["Infotenimento"]],
        "Confianca": [por_tabela(r, DE_PARA_CONFIANCA) for r in BRUTO["Confianca"]],
    }


@pytest.fixture
def pesos():
    return pesos_por_dominancia(ORDEM_IMPORTANCIA)


# --------------------------------------------------------------------------
# Passo 5
# --------------------------------------------------------------------------

def test_interpolacao_reproduz_celsius_para_fahrenheit():
    """A dedução do quadro: 0°C↔32°F e 100°C↔212°F dão ci = 32 + 1,8·vi."""
    assert interpolar(0, 0, 100, 32, 212) == pytest.approx(32)
    assert interpolar(100, 0, 100, 32, 212) == pytest.approx(212)
    assert interpolar(37, 0, 100, 32, 212) == pytest.approx(98.6)


def test_formula_do_maximo_e_caso_particular_da_interpolacao():
    """Conforto com teto 20 dá ci = vi/2 pelos dois caminhos."""
    for vi in BRUTO["Conforto"]:
        assert pela_escala_maxima(vi, 20) == pytest.approx(vi / 2)
        assert interpolar(vi, 0, 20, 0, 10) == pytest.approx(vi / 2)


def test_matriz_criterizada_do_apendice(criterizada):
    esperado = {
        "Preco":         [5.442, 5.633, 0.602, 8.613],
        "Consumo":       [9.500, 5.000, 5.500, 10.000],
        "Conforto":      [5.000, 9.000, 9.000, 3.750],
        "Seguranca":     [8.571, 9.524, 10.000, 7.857],
        "Infotenimento": [5.000, 10.000, 8.571, 5.714],
        "Confianca":     [4.000, 10.000, 4.000, 7.000],
    }
    for criterio, valores in esperado.items():
        assert criterizada[criterio] == pytest.approx(valores, abs=1e-3)


def test_ancora_externa_independe_do_conjunto(criterizada):
    """Segurança ancorada no teto real (21) não muda se entrar outro carro.

    É a propriedade que imuniza contra rank reversal (cap. 11): a nota do Mobi
    é 7,857 porque ele tem 16,5 de 21 itens — não porque é o pior da amostra.
    Com min-max sobre o observado, o mesmo Mobi cairia para 0,000.
    """
    assert pela_escala_maxima(16.5, 21) == pytest.approx(7.857, abs=1e-3)
    minmax_observado = interpolar(16.5, 16.5, 21, 0, 10)
    assert minmax_observado == pytest.approx(0.0)


def test_piso_da_tabela_limita_o_estrago_do_criterio():
    """De-para 10/7/4: o pior rótulo ainda leva 40% da régua."""
    assert por_tabela("Baixa", DE_PARA_CONFIANCA) == 4
    amplitude = por_tabela("Alta", DE_PARA_CONFIANCA) - por_tabela("Baixa", DE_PARA_CONFIANCA)
    assert amplitude == 6  # e não 10


def test_rotulo_desconhecido_e_erro():
    with pytest.raises(ErroDeCriterizacao):
        por_tabela("Altíssima", DE_PARA_CONFIANCA)


def test_ancoras_iguais_sao_erro():
    with pytest.raises(ErroDeCriterizacao):
        interpolar(5, 10, 10)


# --------------------------------------------------------------------------
# Passo 6
# --------------------------------------------------------------------------

def test_pesos_por_dominancia_do_apendice(pesos):
    assert pesos["Preco"] == pytest.approx(6 / 21)
    assert pesos["Seguranca"] == pytest.approx(5 / 21)
    assert pesos["Consumo"] == pytest.approx(4 / 21)
    assert pesos["Confianca"] == pytest.approx(3 / 21)
    assert pesos["Conforto"] == pytest.approx(2 / 21)
    assert pesos["Infotenimento"] == pytest.approx(1 / 21)
    assert sum(pesos.values()) == pytest.approx(1.0)


def test_autodominancia_impede_peso_zero():
    """Sem a diagonal, o último critério sairia com peso nulo."""
    p = pesos_por_dominancia(ORDEM_IMPORTANCIA)
    assert p["Infotenimento"] > 0
    assert p["Infotenimento"] == pytest.approx(1 / 21)


def test_total_e_n_vezes_n_mais_um_sobre_dois():
    for n in (2, 3, 6, 9):
        ordem = [f"c{i}" for i in range(n)]
        p = pesos_por_dominancia(ordem)
        assert p[ordem[0]] == pytest.approx(n / (n * (n + 1) / 2))


def test_pesos_sao_menos_concentrados_que_roc():
    """Mesma ordem, distribuições diferentes: ROC exagera o primeiro (cap. 03)."""
    p = pesos_por_dominancia(ORDEM_IMPORTANCIA)
    n = len(ORDEM_IMPORTANCIA)
    roc_primeiro = (1 / n) * sum(1 / i for i in range(1, n + 1))
    assert p["Preco"] == pytest.approx(0.2857, abs=1e-4)
    assert roc_primeiro == pytest.approx(0.4083, abs=1e-4)
    assert p["Preco"] < roc_primeiro


# --------------------------------------------------------------------------
# Passo 7
# --------------------------------------------------------------------------

def test_resultado_do_exercicio(criterizada, pesos):
    ranking = ranquear(criterizada, pesos, ALTERNATIVAS)
    nomes = [nome for nome, _ in ranking]
    assert nomes == ["Mobi Like", "Onix 1.0", "Kwid Zen", "208 Style"]
    notas = dict(ranking)
    assert notas["Mobi Like"] == pytest.approx(7.866, abs=1e-3)
    assert notas["Onix 1.0"] == pytest.approx(7.591, abs=1e-3)
    assert notas["Kwid Zen"] == pytest.approx(6.691, abs=1e-3)
    assert notas["208 Style"] == pytest.approx(5.437, abs=1e-3)


def test_soma_e_media_ponderada_dao_a_mesma_ordem(criterizada, pesos):
    pontos = {"Preco": 6, "Seguranca": 5, "Consumo": 4,
              "Confianca": 3, "Conforto": 2, "Infotenimento": 1}
    por_media = [n for n, _ in ranquear(criterizada, pesos, ALTERNATIVAS)]
    por_pontos = [n for n, _ in ranquear(criterizada, pontos, ALTERNATIVAS)]
    assert por_media == por_pontos


def test_vitoria_do_mobi_e_apertada(criterizada, pesos):
    ranking = ranquear(criterizada, pesos, ALTERNATIVAS)
    margem = ranking[0][1] - ranking[1][1]
    assert margem == pytest.approx(0.275, abs=1e-3)
    assert margem / 10 < 0.03  # menos de 3% da régua


def test_mobi_vence_perdendo_em_quatro_dos_seis_criterios(criterizada):
    """O vencedor ganha só em preço e consumo — e isso basta."""
    i_mobi, i_onix = ALTERNATIVAS.index("Mobi Like"), ALTERNATIVAS.index("Onix 1.0")
    vitorias = [c for c in criterizada if criterizada[c][i_mobi] > criterizada[c][i_onix]]
    assert sorted(vitorias) == ["Consumo", "Preco"]


# --------------------------------------------------------------------------
# Passo 8
# --------------------------------------------------------------------------

def test_influencia_efetiva_desmente_o_peso_declarado(criterizada, pesos):
    """Segurança é o 2º peso declarado e o 4º em influência real."""
    infl = influencia_efetiva(criterizada, pesos)
    ordem_real = sorted(infl, key=lambda c: -infl[c])
    assert ordem_real[0] == "Preco"
    assert ordem_real.index("Seguranca") == 3
    assert infl["Preco"] == pytest.approx(0.428, abs=1e-3)
    assert infl["Seguranca"] == pytest.approx(0.095, abs=1e-3)
    # a Confiança, declarada em 4º, influencia MAIS que a Segurança
    assert infl["Confianca"] > infl["Seguranca"]


def test_desconto_que_vira_o_jogo(criterizada, pesos):
    """R$ 4.804 de desconto no Onix empatam com o Mobi (5,9% do preço)."""
    ranking = dict(ranquear(criterizada, pesos, ALTERNATIVAS))
    desconto = desconto_para_empatar(
        ranking["Mobi Like"], ranking["Onix 1.0"],
        peso_preco=pesos["Preco"], soma_pesos=sum(pesos.values()),
        reais_por_ponto=5000,
    )
    assert desconto == pytest.approx(4804, abs=5)
    preco_alvo = BRUTO["Preco"][ALTERNATIVAS.index("Onix 1.0")] - desconto
    assert preco_alvo == pytest.approx(77033, abs=5)


def test_208_esta_fora_de_alcance(criterizada, pesos):
    """Para empatar, o 208 teria de ficar mais barato que o Mobi de tabela."""
    ranking = dict(ranquear(criterizada, pesos, ALTERNATIVAS))
    desconto = desconto_para_empatar(
        ranking["Mobi Like"], ranking["208 Style"],
        peso_preco=pesos["Preco"], soma_pesos=sum(pesos.values()),
        reais_por_ponto=5000,
    )
    preco_alvo = BRUTO["Preco"][ALTERNATIVAS.index("208 Style")] - desconto
    assert preco_alvo == pytest.approx(64494, abs=10)
    assert preco_alvo < BRUTO["Preco"][ALTERNATIVAS.index("Mobi Like")]


def test_faixa_de_estabilidade_do_peso_do_preco(criterizada, pesos):
    """O Mobi reina de w=0,214 para cima; abaixo disso o Onix assume."""
    trocas = varredura_de_peso(criterizada, pesos, "Preco", ALTERNATIVAS)
    assert [v for _, v in trocas] == ["Onix 1.0", "Mobi Like"]
    fronteira = trocas[1][0]
    assert fronteira == pytest.approx(0.214, abs=1e-3)
    assert pesos["Preco"] > fronteira  # o peso declarado está do lado do Mobi


def test_piso_da_confianca_troca_o_vencedor(criterizada, pesos):
    """De-para 10/5/0 em vez de 10/7/4 e o Onix passa o Mobi por 0,011.

    A decisão foi tomada no passo 5, sobre três rótulos qualitativos — e
    decide a compra. Ninguém mudou de opinião sobre carro nenhum.
    """
    alternativo = dict(criterizada)
    alternativo["Confianca"] = [
        por_tabela(r, {"Alta": 10, "Media": 5, "Baixa": 0})
        for r in BRUTO["Confianca"]
    ]
    ranking = ranquear(alternativo, pesos, ALTERNATIVAS)
    assert ranking[0][0] == "Onix 1.0"
    assert ranking[0][1] - ranking[1][1] == pytest.approx(0.011, abs=2e-3)
