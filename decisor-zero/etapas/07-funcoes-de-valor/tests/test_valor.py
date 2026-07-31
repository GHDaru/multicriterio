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


def test_segundo_dominio_curva_de_sla():
    """Fornecedores (ADR 0007): curvas com limiar de contrato ampliam a folga de F2."""
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
    curvas = {
        "Custo mensal": [(7_500, 1.0), (9_500, 0.75), (12_000, 0.0)],
        "Latência": [(20, 1.0), (60, 0.0)],
        "SLA": [(99.0, 0.0), (99.5, 0.7), (99.95, 1.0)],
        "Suporte": [(3, 0.0), (5, 1.0)],
    }
    ranking = ranquear_mavt(fornecedores, curvas)
    escores = {l["alternativa"]: l["escore"] for l in ranking}
    assert [l["alternativa"] for l in ranking] == [
        "F2 — Regional", "F3 — Nicho", "F1 — Hiperescala",
    ]
    assert escores["F2 — Regional"] == pytest.approx(0.775, abs=1e-6)
    assert escores["F3 — Nicho"] == pytest.approx(0.55, abs=1e-6)
    assert escores["F1 — Hiperescala"] == pytest.approx(0.325, abs=1e-6)
