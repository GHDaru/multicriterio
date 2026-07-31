"""Os números do capítulo 04, verificados — incluindo a virada de ranking."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.matriz import Criterio, MatrizDecisao
from motor.pesos import pesos_roc
from motor.saw import ranquear_saw

CRITERIOS = [
    Criterio("Preço", "custo", "R$"),
    Criterio("Área", "beneficio", "m²"),
    Criterio("Deslocamento", "custo", "min"),
    Criterio("Bairro", "beneficio", "1–5"),
]
DESEMPENHOS = [
    [450_000, 62, 15, 4],
    [380_000, 70, 35, 3],
    [520_000, 85, 25, 5],
    [340_000, 55, 20, 2],
]
NOMES = ["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação"]


def ancora(pesos: list[float]) -> MatrizDecisao:
    return MatrizDecisao(
        alternativas=NOMES, criterios=CRITERIOS, desempenhos=DESEMPENHOS, pesos=pesos
    )


def test_saw_com_rating_direto_reproduz_a_tabela_do_capitulo():
    # Pesos do cap. 03 (rating 35/25/25/15): A1 vence por margem apertada.
    ranking = ranquear_saw(ancora([0.35, 0.25, 0.25, 0.15]))
    assert [linha["alternativa"] for linha in ranking] == [
        "A1 — Centro", "A4 — Estação", "A3 — Parque", "A2 — Jardim",
    ]
    escores = {linha["alternativa"]: linha["escore"] for linha in ranking}
    assert escores["A1 — Centro"] == pytest.approx(0.544444, abs=1e-6)
    assert escores["A4 — Estação"] == pytest.approx(0.5375, abs=1e-6)
    assert escores["A3 — Parque"] == pytest.approx(0.525, abs=1e-6)
    assert escores["A2 — Jardim"] == pytest.approx(0.447222, abs=1e-6)


def test_saw_com_pesos_roc_troca_o_vencedor():
    # A lição central do cap. 04: mesmo problema, pesos ROC → A4 dispara.
    ranking = ranquear_saw(ancora(pesos_roc([0, 1, 2, 3])))
    assert [linha["alternativa"] for linha in ranking] == [
        "A4 — Estação", "A2 — Jardim", "A1 — Centro", "A3 — Parque",
    ]
    escores = {linha["alternativa"]: linha["escore"] for linha in ranking}
    assert escores["A4 — Estação"] == pytest.approx(0.630208, abs=1e-6)
    assert escores["A2 — Jardim"] == pytest.approx(0.561343, abs=1e-6)
    assert escores["A1 — Centro"] == pytest.approx(0.453241, abs=1e-6)
    assert escores["A3 — Parque"] == pytest.approx(0.406250, abs=1e-6)


def test_saw_sem_pesos_aponta_para_o_cap_03():
    matriz = MatrizDecisao(
        alternativas=NOMES, criterios=CRITERIOS, desempenhos=DESEMPENHOS
    )
    with pytest.raises(ValueError, match="cap. 03"):
        ranquear_saw(matriz)


def test_validacao_cruzada_com_pymcdm():
    """Princípio I: nossos escores batem com a biblioteca de referência.

    pymcdm (Kizielewicz, Shekhovtsov & Sałabun — SoftwareX 22:101368) com
    WSM + normalização min-max e types (-1, 1, -1, 1).
    """
    np = pytest.importorskip("numpy")
    pymcdm_methods = pytest.importorskip("pymcdm.methods")
    from pymcdm import normalizations

    wsm = pymcdm_methods.WSM(normalization_function=normalizations.minmax_normalization)
    X = np.array(DESEMPENHOS, dtype=float)
    types = np.array([-1, 1, -1, 1])
    for pesos in ([0.35, 0.25, 0.25, 0.15], pesos_roc([0, 1, 2, 3])):
        deles = wsm(X, np.array(pesos), types)
        nossos = {l["alternativa"]: l["escore"] for l in ranquear_saw(ancora(pesos))}
        for nome, escore_deles in zip(NOMES, deles):
            assert nossos[nome] == pytest.approx(float(escore_deles), abs=1e-6)
