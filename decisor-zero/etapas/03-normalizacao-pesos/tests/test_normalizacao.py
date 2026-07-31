"""Os números do capítulo 03 (normalização), verificados."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.matriz import Criterio, MatrizDecisao
from motor.normalizacao import normalizar_minmax, normalizar_vetorial

CASO_ANCORA = MatrizDecisao(
    alternativas=["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação"],
    criterios=[
        Criterio("Preço", "custo", "R$"),
        Criterio("Área", "beneficio", "m²"),
        Criterio("Deslocamento", "custo", "min"),
        Criterio("Bairro", "beneficio", "1–5"),
    ],
    desempenhos=[
        [450_000, 62, 15, 4],
        [380_000, 70, 35, 3],
        [520_000, 85, 25, 5],
        [340_000, 55, 20, 2],
    ],
)


def test_minmax_reproduz_a_tabela_do_capitulo():
    esperado = [
        [0.3889, 0.2333, 1.0, 0.6667],
        [0.7778, 0.5, 0.0, 0.3333],
        [0.0, 1.0, 0.5, 1.0],
        [1.0, 0.0, 0.75, 0.0],
    ]
    obtido = normalizar_minmax(CASO_ANCORA)
    for linha_o, linha_e in zip(obtido, esperado):
        assert linha_o == pytest.approx(linha_e, abs=1e-4)


def test_minmax_da_1_ao_melhor_de_cada_criterio_mesmo_em_custo():
    obtido = normalizar_minmax(CASO_ANCORA)
    assert obtido[3][0] == 1.0  # A4: mais barata
    assert obtido[0][2] == 1.0  # A1: mais perto


def test_vetorial_reproduz_a_tabela_do_capitulo():
    esperado = [
        [0.5256, 0.4499, 0.3015, 0.5443],
        [0.4439, 0.5079, 0.7035, 0.4082],
        [0.6074, 0.6168, 0.5025, 0.6804],
        [0.3972, 0.3991, 0.4020, 0.2722],
    ]
    obtido = normalizar_vetorial(CASO_ANCORA)
    for linha_o, linha_e in zip(obtido, esperado):
        assert linha_o == pytest.approx(linha_e, abs=1e-4)


def test_vetorial_nao_resolve_direcao():
    # No Preço (custo), o MAIOR valor cru continua com o maior r — a direção
    # fica para o método (TOPSIS, cap. 06). Quem esquecer isso soma errado.
    obtido = normalizar_vetorial(CASO_ANCORA)
    assert obtido[2][0] == max(linha[0] for linha in obtido)  # A3, a mais cara


def test_vetorial_cada_coluna_tem_norma_unitaria():
    obtido = normalizar_vetorial(CASO_ANCORA)
    for j in range(4):
        norma2 = sum(linha[j] ** 2 for linha in obtido)
        assert norma2 == pytest.approx(1.0, abs=1e-12)


def test_criterio_constante_nao_explode():
    empatada = MatrizDecisao(
        alternativas=["X", "Y"],
        criterios=[Criterio("Empate", "beneficio")],
        desempenhos=[[7], [7]],
    )
    assert normalizar_minmax(empatada) == [[0.0], [0.0]]
