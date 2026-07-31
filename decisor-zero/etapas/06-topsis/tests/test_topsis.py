"""Os números do capítulo 06, verificados — e validados contra a pymcdm."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.matriz import Criterio, MatrizDecisao
from motor.topsis import ranquear_topsis

CRITERIOS = [
    Criterio("Preço", "custo", "R$"), Criterio("Área", "beneficio", "m²"),
    Criterio("Deslocamento", "custo", "min"), Criterio("Bairro", "beneficio", "1–5"),
]
DESEMPENHOS = [
    [450_000, 62, 15, 4], [380_000, 70, 35, 3],
    [520_000, 85, 25, 5], [340_000, 55, 20, 2],
]
NOMES = ["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação"]
ANCORA = MatrizDecisao(
    alternativas=NOMES, criterios=CRITERIOS, desempenhos=DESEMPENHOS,
    pesos=[0.35, 0.25, 0.25, 0.15],
)


def test_proximidades_do_capitulo():
    escores = {l["alternativa"]: l["escore"] for l in ranquear_topsis(ANCORA)}
    assert escores["A1 — Centro"] == pytest.approx(0.635886, abs=1e-6)
    assert escores["A2 — Jardim"] == pytest.approx(0.370699, abs=1e-6)
    assert escores["A3 — Parque"] == pytest.approx(0.518889, abs=1e-6)
    assert escores["A4 — Estação"] == pytest.approx(0.551440, abs=1e-6)


def test_ranking_coincide_com_saw_neste_problema():
    # Com os MESMOS pesos, TOPSIS e SAW concordam aqui (A1>A4>A3>A2) —
    # concordância é propriedade deste problema, não garantia (cap. 11).
    ordem = [l["alternativa"] for l in ranquear_topsis(ANCORA)]
    assert ordem == ["A1 — Centro", "A4 — Estação", "A3 — Parque", "A2 — Jardim"]


def test_validacao_cruzada_com_pymcdm():
    np = pytest.importorskip("numpy")
    metodos = pytest.importorskip("pymcdm.methods")
    from pymcdm import normalizations
    topsis = metodos.TOPSIS(normalization_function=normalizations.vector_normalization)
    deles = topsis(np.array(DESEMPENHOS, dtype=float),
                   np.array([0.35, 0.25, 0.25, 0.15]), np.array([-1, 1, -1, 1]))
    nossos = {l["alternativa"]: l["escore"] for l in ranquear_topsis(ANCORA)}
    for nome, escore in zip(NOMES, deles):
        assert nossos[nome] == pytest.approx(float(escore), abs=1e-6)


def test_alternativa_igual_ao_ideal_tem_proximidade_1():
    dominante = MatrizDecisao(
        alternativas=["Ideal", "Pior"],
        criterios=[Criterio("Custo", "custo"), Criterio("Qualidade", "beneficio")],
        desempenhos=[[10, 9], [100, 1]],
        pesos=[0.5, 0.5],
    )
    ranking = ranquear_topsis(dominante)
    assert ranking[0]["alternativa"] == "Ideal"
    assert ranking[0]["escore"] == pytest.approx(1.0)


def test_sem_pesos_e_erro():
    sem = MatrizDecisao(alternativas=NOMES, criterios=CRITERIOS, desempenhos=DESEMPENHOS)
    with pytest.raises(ValueError, match="pesos"):
        ranquear_topsis(sem)


def test_segundo_dominio_f2_tres_quartos_do_ideal():
    """Fornecedores (ADR 0007): C confirma o pódio do SAW com folga geométrica."""
    fornecedores = MatrizDecisao(
        alternativas=["F1 — Hiperescala", "F2 — Regional", "F3 — Nicho"],
        criterios=[
            Criterio("Custo mensal", "custo", "R$/mês"),
            Criterio("Latência", "custo", "ms"),
            Criterio("SLA", "beneficio", "%"),
            Criterio("Suporte", "beneficio", "1–5"),
        ],
        desempenhos=[[12_000, 45, 99.95, 3], [9_000, 20, 99.50, 4], [7_500, 60, 99.00, 5]],
        pesos=[0.40, 0.20, 0.25, 0.15],
    )
    escores = {l["alternativa"]: l["escore"] for l in ranquear_topsis(fornecedores)}
    assert escores["F2 — Regional"] == pytest.approx(0.753637, abs=1e-6)
    assert escores["F3 — Nicho"] == pytest.approx(0.528235, abs=1e-6)
    assert escores["F1 — Hiperescala"] == pytest.approx(0.226368, abs=1e-6)
    np = pytest.importorskip("numpy")
    metodos = pytest.importorskip("pymcdm.methods")
    from pymcdm import normalizations
    topsis = metodos.TOPSIS(normalization_function=normalizations.vector_normalization)
    deles = topsis(
        np.array(fornecedores.desempenhos, dtype=float),
        np.array(fornecedores.pesos), np.array([-1, -1, 1, 1]),
    )
    for nome, c in zip(fornecedores.alternativas, deles):
        assert escores[nome] == pytest.approx(float(c), abs=1e-6)
