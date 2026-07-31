"""Os números do capítulo 08, verificados — e validados contra a pymcdm."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.matriz import Criterio, MatrizDecisao
from motor.promethee import ErroDePreferencia, fluxos_promethee

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


def test_fluxos_do_capitulo_funcao_usual():
    fluxos = {l["alternativa"]: l for l in fluxos_promethee(ANCORA)}
    assert fluxos["A1 — Centro"]["escore"] == pytest.approx(0.1, abs=1e-6)
    assert fluxos["A4 — Estação"]["escore"] == pytest.approx(0.033333, abs=1e-6)
    assert fluxos["A3 — Parque"]["escore"] == pytest.approx(-0.033333, abs=1e-6)
    assert fluxos["A2 — Jardim"]["escore"] == pytest.approx(-0.1, abs=1e-6)


def test_fluxos_liquidos_somam_zero():
    # Propriedade do PROMETHEE II: Σφ = 0 (todo ganho de um é perda de outro).
    assert sum(l["escore"] for l in fluxos_promethee(ANCORA)) == pytest.approx(0, abs=1e-9)


def test_validacao_cruzada_com_pymcdm():
    np = pytest.importorskip("numpy")
    metodos = pytest.importorskip("pymcdm.methods")
    p2 = metodos.PROMETHEE_II("usual")
    deles = p2(np.array(DESEMPENHOS, dtype=float),
               np.array([0.35, 0.25, 0.25, 0.15]), np.array([-1, 1, -1, 1]))
    nossos = {l["alternativa"]: l["escore"] for l in fluxos_promethee(ANCORA)}
    for nome, phi in zip(NOMES, deles):
        assert nossos[nome] == pytest.approx(float(phi), abs=1e-6)


def test_vshape_encolhe_os_fluxos_brutos_mas_nao_necessariamente_o_liquido():
    # P_vshape(d) <= P_usual(d) para todo d, logo φ+ e φ− encolhem um a um.
    # O φ líquido, porém, pode até crescer (as vantagens grandes sobrevivem ao
    # limiar; as pequenas dos rivais evaporam) — fato usado no cap. 08.
    limiares = [200_000, 30, 20, 3]
    suave = {l["alternativa"]: l for l in fluxos_promethee(ANCORA, "vshape", limiares)}
    duro = {l["alternativa"]: l for l in fluxos_promethee(ANCORA)}
    for nome in NOMES:
        assert suave[nome]["fluxo_positivo"] <= duro[nome]["fluxo_positivo"] + 1e-9
        assert suave[nome]["fluxo_negativo"] <= duro[nome]["fluxo_negativo"] + 1e-9
    # A3 é o exemplo concreto: φ = −0,0333 (usual) → +0,0406 (vshape).
    assert suave["A3 — Parque"]["escore"] == pytest.approx(0.040556, abs=1e-6)
    assert duro["A3 — Parque"]["escore"] == pytest.approx(-0.033333, abs=1e-6)


def test_vshape_sem_limiar_e_erro():
    with pytest.raises(ErroDePreferencia, match="limiar"):
        fluxos_promethee(ANCORA, "vshape")
