"""Os números do capítulo 02, verificados (Princípio I: worked example = teste)."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.dominancia import analise_dominancia, domina
from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao

CRITERIOS = [
    Criterio("Preço", "custo", "R$"),
    Criterio("Área", "beneficio", "m²"),
    Criterio("Deslocamento", "custo", "min"),
    Criterio("Bairro", "beneficio", "1–5"),
]

ANCORA = [
    [450_000, 62, 15, 4],   # A1 — Centro
    [380_000, 70, 35, 3],   # A2 — Jardim
    [520_000, 85, 25, 5],   # A3 — Parque
    [340_000, 55, 20, 2],   # A4 — Estação
]
NOMES = ["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação"]


def com_candidato_a5() -> MatrizDecisao:
    return MatrizDecisao(
        alternativas=NOMES + ["A5 — Colina"],
        criterios=CRITERIOS,
        desempenhos=ANCORA + [[470_000, 60, 18, 3]],
    )


def test_a5_e_dominada_por_a1_e_somente_por_a1():
    # Worked example do cap. 02: A1 é mais barata (450k<470k), maior (62>60),
    # mais perto (15<18) e em bairro melhor (4>3) que A5 — dominância estrita.
    resultado = analise_dominancia(com_candidato_a5())
    assert resultado["dominadas"] == {"A5 — Colina": ["A1 — Centro"]}


def test_fronteira_de_pareto_e_o_caso_ancora_original():
    resultado = analise_dominancia(com_candidato_a5())
    assert resultado["fronteira_pareto"] == NOMES


def test_caso_ancora_original_nao_tem_dominadas():
    # A afirmação do SUMARIO ("nenhuma alternativa domina outra"), agora provada.
    matriz = MatrizDecisao(alternativas=NOMES, criterios=CRITERIOS, desempenhos=ANCORA)
    assert analise_dominancia(matriz)["dominadas"] == {}


def test_alternativas_identicas_nao_se_dominam():
    matriz = MatrizDecisao(
        alternativas=["X", "Y"],
        criterios=[Criterio("Custo", "custo")],
        desempenhos=[[100], [100]],
    )
    assert not domina(matriz, 0, 1) and not domina(matriz, 1, 0)
    assert analise_dominancia(matriz)["fronteira_pareto"] == ["X", "Y"]


def test_dominancia_respeita_a_direcao_do_criterio():
    # Em critério de custo, MENOR domina — errar a direção inverteria o veredito.
    matriz = MatrizDecisao(
        alternativas=["Barata", "Cara"],
        criterios=[Criterio("Custo", "custo"), Criterio("Qualidade", "beneficio")],
        desempenhos=[[80, 5], [100, 5]],
    )
    assert domina(matriz, 0, 1) and not domina(matriz, 1, 0)


def test_peso_negativo_agora_e_erro_de_modelagem():
    # O gabarito do exercício do cap. 01, aplicado nesta etapa (o diff é a lição):
    # [0.7, 0.5, -0.1, -0.1] soma 1 e escapava da checagem de soma.
    with pytest.raises(ErroDeModelagem, match="negativos"):
        MatrizDecisao(
            alternativas=NOMES,
            criterios=CRITERIOS,
            desempenhos=ANCORA,
            pesos=[0.7, 0.5, -0.1, -0.1],
        )
