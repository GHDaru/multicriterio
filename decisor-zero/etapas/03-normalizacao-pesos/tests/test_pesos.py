"""Os números do capítulo 03 (pesos), verificados."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.matriz import Criterio, MatrizDecisao
from motor.pesos import (
    ErroDePesos,
    pesos_entropia,
    pesos_rating_direto,
    pesos_roc,
    pesos_swing,
)
from tests.test_normalizacao import CASO_ANCORA


def test_rating_direto_e_a_origem_dos_pesos_do_livro():
    # Os pesos usados desde o cap. 01 vêm de um rating direto 35/25/25/15.
    assert pesos_rating_direto([35, 25, 25, 15]) == [0.35, 0.25, 0.25, 0.15]


def test_roc_para_o_ranking_preco_area_desloc_bairro():
    # w_k = (1/n)·Σ_{i=k..n} 1/i, n=4 → tabela do capítulo.
    obtido = pesos_roc([0, 1, 2, 3])
    assert obtido == pytest.approx([0.5208, 0.2708, 0.1458, 0.0625], abs=1e-4)
    assert sum(obtido) == pytest.approx(1.0)


def test_roc_devolve_pesos_na_ordem_original_das_colunas():
    # Ranking: Área (1º), Preço (2º), Bairro (3º), Deslocamento (4º).
    obtido = pesos_roc([1, 0, 3, 2])
    assert obtido[1] == pytest.approx(0.5208, abs=1e-4)  # Área, 1ª do ranking
    assert obtido[2] == pytest.approx(0.0625, abs=1e-4)  # Deslocamento, última


def test_roc_exige_permutacao_estrita():
    with pytest.raises(ErroDePesos, match="permutação"):
        pesos_roc([0, 0, 1, 2])


def test_swing_do_capitulo():
    # Saltos: Preço 100, Área 60, Deslocamento 70, Bairro 40.
    obtido = pesos_swing([100, 60, 70, 40])
    assert obtido == pytest.approx([0.3704, 0.2222, 0.2593, 0.1481], abs=1e-4)


def test_swing_exige_ancora_100():
    with pytest.raises(ErroDePesos, match="100"):
        pesos_swing([90, 60, 70, 40])


def test_entropia_do_caso_ancora():
    # Área discrimina mais (maior amplitude relativa após min-max) e recebe o
    # maior peso; Deslocamento, o menor. Preferência de ninguém foi consultada.
    obtido = pesos_entropia(CASO_ANCORA)
    assert obtido == pytest.approx([0.2365, 0.2948, 0.2178, 0.2509], abs=1e-4)
    assert max(obtido) == obtido[1] and min(obtido) == obtido[2]


def test_entropia_ignora_criterio_que_nao_discrimina():
    matriz = MatrizDecisao(
        alternativas=["X", "Y"],
        criterios=[Criterio("Empate", "beneficio"), Criterio("Custo", "custo")],
        desempenhos=[[7, 100], [7, 80]],
    )
    assert pesos_entropia(matriz) == pytest.approx([0.0, 1.0])


def test_rating_com_soma_zero_e_erro():
    with pytest.raises(ErroDePesos, match="positiva"):
        pesos_rating_direto([0, 0, 0])


def test_segundo_dominio_entropia_quase_uniforme():
    """Fornecedores (ADR 0007): colunas discriminam parecido → entropia ~uniforme."""
    fornecedores = MatrizDecisao(
        alternativas=["F1 — Hiperescala", "F2 — Regional", "F3 — Nicho"],
        criterios=[
            Criterio("Custo mensal", "custo", "R$/mês"),
            Criterio("Latência", "custo", "ms"),
            Criterio("SLA", "beneficio", "%"),
            Criterio("Suporte", "beneficio", "1–5"),
        ],
        desempenhos=[[12_000, 45, 99.95, 3], [9_000, 20, 99.50, 4], [7_500, 60, 99.00, 5]],
    )
    pesos = pesos_entropia(fornecedores)
    assert pesos == pytest.approx([0.2295, 0.2764, 0.2450, 0.2491], abs=1e-4)
    assert max(pesos) - min(pesos) < 0.05  # quase uniforme: ninguém domina a informação
