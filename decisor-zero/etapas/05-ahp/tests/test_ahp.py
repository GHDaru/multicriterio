"""Os números do capítulo 05, verificados."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.ahp import ErroDeJulgamentos, prioridades_ahp
from motor.matriz import Criterio, MatrizDecisao
from motor.saw import ranquear_saw

# Worked example do cap. 05: comparações par a par dos 4 critérios do caso
# âncora (Preço, Área, Deslocamento, Bairro), escala de Saaty.
JULGAMENTOS = [
    [1, 2, 2, 3],
    [1 / 2, 1, 1, 2],
    [1 / 2, 1, 1, 2],
    [1 / 3, 1 / 2, 1 / 2, 1],
]


def test_prioridades_do_capitulo():
    r = prioridades_ahp(JULGAMENTOS)
    assert r["pesos"] == pytest.approx([0.4236, 0.2270, 0.2270, 0.1223], abs=1e-4)
    assert sum(r["pesos"]) == pytest.approx(1.0)
    # Área e Deslocamento receberam julgamentos idênticos → pesos idênticos.
    assert r["pesos"][1] == pytest.approx(r["pesos"][2], abs=1e-9)


def test_consistencia_do_capitulo():
    r = prioridades_ahp(JULGAMENTOS)
    assert r["lambda_max"] == pytest.approx(4.0104, abs=1e-4)
    assert r["cr"] == pytest.approx(0.0038, abs=1e-4)
    assert r["consistente"] is True


def test_matriz_ciclica_e_reprovada():
    # a12·a23 = 3·(1/5) = 0,6 ≠ a13 = 5 → julgamentos cíclicos, CR alto.
    ciclica = [[1, 3, 5], [1 / 3, 1, 1 / 5], [1 / 5, 5, 1]]
    r = prioridades_ahp(ciclica)
    assert r["cr"] == pytest.approx(0.4488, abs=1e-3)
    assert r["consistente"] is False


def test_matriz_perfeitamente_consistente_tem_cr_zero():
    # a_ij = w_i/w_j exata → λmax = n e CR = 0.
    w = [0.5, 0.3, 0.2]
    exata = [[wi / wj for wj in w] for wi in w]
    r = prioridades_ahp(exata)
    assert r["cr"] == pytest.approx(0.0, abs=1e-9)
    assert r["pesos"] == pytest.approx(w, abs=1e-9)


def test_reciproco_violado_e_erro():
    with pytest.raises(ErroDeJulgamentos, match="recíproco"):
        prioridades_ahp([[1, 2], [3, 1]])


def test_ranking_saw_com_pesos_ahp():
    # Fechando o ciclo do capítulo: pesos AHP alimentam o SAW do cap. 04.
    pesos = prioridades_ahp(JULGAMENTOS)["pesos"]
    matriz = MatrizDecisao(
        alternativas=["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação"],
        criterios=[
            Criterio("Preço", "custo"), Criterio("Área", "beneficio"),
            Criterio("Deslocamento", "custo"), Criterio("Bairro", "beneficio"),
        ],
        desempenhos=[
            [450_000, 62, 15, 4], [380_000, 70, 35, 3],
            [520_000, 85, 25, 5], [340_000, 55, 20, 2],
        ],
        pesos=pesos,
    )
    ranking = ranquear_saw(matriz)
    assert [l["alternativa"] for l in ranking] == [
        "A4 — Estação", "A1 — Centro", "A2 — Jardim", "A3 — Parque",
    ]
    assert ranking[0]["escore"] == pytest.approx(0.593870, abs=1e-5)


def test_segundo_dominio_prioridades_do_cto():
    """Fornecedores (ADR 0007): outro domínio, outro vetor — mesma mecânica."""
    julgamentos_cto = [
        [1, 3, 2, 3],
        [1 / 3, 1, 1 / 2, 1],
        [1 / 2, 2, 1, 2],
        [1 / 3, 1, 1 / 2, 1],
    ]
    r = prioridades_ahp(julgamentos_cto)
    assert r["pesos"] == pytest.approx([0.4554, 0.1409, 0.2628, 0.1409], abs=1e-4)
    assert r["cr"] == pytest.approx(0.0038, abs=1e-3)
    assert r["consistente"] is True
    # Latência e Suporte: julgamentos idênticos ⇒ pesos idênticos.
    assert r["pesos"][1] == pytest.approx(r["pesos"][3], abs=1e-9)
