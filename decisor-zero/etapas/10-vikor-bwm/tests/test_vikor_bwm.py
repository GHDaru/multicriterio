"""Os números do capítulo 10, verificados — VIKOR validado contra a pymcdm."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.bwm import ErroDeBWM, pesos_bwm
from motor.matriz import Criterio, MatrizDecisao
from motor.vikor import analisar_vikor

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


def test_q_do_capitulo():
    r = analisar_vikor(ANCORA)
    q = {l["alternativa"]: l["escore"] for l in r["ranking"]}
    assert q["A1 — Centro"] == pytest.approx(0.0, abs=1e-6)
    assert q["A4 — Estação"] == pytest.approx(0.168367, abs=1e-6)
    assert q["A3 — Parque"] == pytest.approx(0.6, abs=1e-6)
    assert q["A2 — Jardim"] == pytest.approx(0.632653, abs=1e-6)


def test_conjunto_de_compromisso_do_capitulo():
    # Q(A4) − Q(A1) = 0,168 < DQ = 1/3: vantagem NÃO aceitável → compromisso
    # {A1, A4}, mesmo com A1 líder estável em S e R.
    r = analisar_vikor(ANCORA)
    assert r["dq"] == pytest.approx(1 / 3, abs=1e-6)
    assert r["vantagem_aceitavel"] is False
    assert r["estavel"] is True
    assert r["conjunto_compromisso"] == ["A1 — Centro", "A4 — Estação"]


def test_validacao_cruzada_vikor_com_pymcdm():
    np = pytest.importorskip("numpy")
    metodos = pytest.importorskip("pymcdm.methods")
    vikor = metodos.VIKOR(v=0.5)
    deles = vikor(np.array(DESEMPENHOS, dtype=float),
                  np.array([0.35, 0.25, 0.25, 0.15]), np.array([-1, 1, -1, 1]))
    nossos = {l["alternativa"]: l["escore"] for l in analisar_vikor(ANCORA)["ranking"]}
    for nome, q in zip(NOMES, deles):
        assert nossos[nome] == pytest.approx(float(q), abs=1e-6)


def test_bwm_consistente_fecha_em_forma_exata():
    # Best = Preço, worst = Bairro; a_Bj·a_jW = a_BW = 4 para todo j → ξ = 0 e
    # pesos exatos (4/9, 2/9, 2/9, 1/9).
    r = pesos_bwm(0, 3, [1, 2, 2, 4], [4, 2, 2, 1])
    assert r["xi"] == pytest.approx(0.0, abs=1e-6)
    assert r["pesos"] == pytest.approx([4 / 9, 2 / 9, 2 / 9, 1 / 9], abs=1e-4)


def test_bwm_inconsistente_tem_xi_positivo():
    r = pesos_bwm(0, 3, [1, 2, 3, 4], [4, 3, 2, 1])
    assert r["xi"] > 0.01
    assert sum(r["pesos"]) == pytest.approx(1.0, abs=1e-6)


def test_bwm_valida_entradas():
    with pytest.raises(ErroDeBWM, match="diferentes"):
        pesos_bwm(0, 0, [1, 2], [2, 1])


def test_segundo_dominio_dq_alto_com_poucas_alternativas():
    """Fornecedores (ADR 0007): vitória robusta que ainda assim não passa no C1."""
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
    r = analisar_vikor(fornecedores)
    q = {l["alternativa"]: l["escore"] for l in r["ranking"]}
    assert q["F2 — Regional"] == pytest.approx(0.0, abs=1e-6)
    assert q["F3 — Nicho"] == pytest.approx(0.395702, abs=1e-6)
    assert q["F1 — Hiperescala"] == pytest.approx(1.0, abs=1e-6)
    # m = 3 → DQ = 0,5: até 0,3957 de vantagem "não basta" para o C1.
    assert r["dq"] == pytest.approx(0.5)
    assert r["vantagem_aceitavel"] is False and r["estavel"] is True
    assert r["conjunto_compromisso"] == ["F2 — Regional", "F3 — Nicho"]
