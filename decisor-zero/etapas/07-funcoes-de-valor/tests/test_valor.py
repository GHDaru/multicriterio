"""Os números do capítulo 07, verificados."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.matriz import Criterio, MatrizDecisao
from motor.saw import ranquear_saw
from motor.valor import ErroDeFuncaoValor, ranquear_mavt, valor

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

LINEARES = {
    "Preço": [(340_000, 1.0), (520_000, 0.0)],
    "Área": [(55, 0.0), (85, 1.0)],
    "Deslocamento": [(15, 1.0), (35, 0.0)],
    "Bairro": [(2, 0.0), (5, 1.0)],
}
CURVAS = {
    "Preço": [(340_000, 1.0), (400_000, 0.8), (520_000, 0.0)],
    "Área": [(55, 0.0), (70, 0.8), (85, 1.0)],
    "Deslocamento": [(15, 1.0), (35, 0.0)],
    "Bairro": [(2, 0.0), (5, 1.0)],
}


def test_funcoes_lineares_reproduzem_o_saw():
    # Propriedade central do cap. 07: MAVT linear ancorado em min/max ≡ SAW min-max.
    mavt = {l["alternativa"]: l["escore"] for l in ranquear_mavt(ANCORA, LINEARES)}
    saw = {l["alternativa"]: l["escore"] for l in ranquear_saw(ANCORA)}
    for nome in NOMES:
        assert mavt[nome] == pytest.approx(saw[nome], abs=1e-6)


def test_curvas_do_capitulo_mudam_o_podio_sem_tocar_nos_pesos():
    ranking = ranquear_mavt(ANCORA, CURVAS)
    assert [l["alternativa"] for l in ranking] == [
        "A1 — Centro", "A2 — Jardim", "A4 — Estação", "A3 — Parque",
    ]
    escores = {l["alternativa"]: l["escore"] for l in ranking}
    assert escores["A1 — Centro"] == pytest.approx(0.606667, abs=1e-6)
    assert escores["A2 — Jardim"] == pytest.approx(0.553333, abs=1e-6)
    assert escores["A4 — Estação"] == pytest.approx(0.5375, abs=1e-6)
    assert escores["A3 — Parque"] == pytest.approx(0.525, abs=1e-6)


def test_interpolacao_e_bordas():
    f = [(0, 0.0), (10, 1.0)]
    assert valor(f, 5) == pytest.approx(0.5)
    assert valor(f, -3) == 0.0 and valor(f, 99) == 1.0


def test_funcao_nao_monotona_e_erro():
    with pytest.raises(ErroDeFuncaoValor, match="monótona"):
        ranquear_mavt(ANCORA, {**LINEARES, "Área": [(55, 0.0), (70, 1.0), (85, 0.5)]})


def test_falta_funcao_e_erro():
    incompleto = {k: v for k, v in LINEARES.items() if k != "Bairro"}
    with pytest.raises(ErroDeFuncaoValor, match="Bairro"):
        ranquear_mavt(ANCORA, incompleto)
