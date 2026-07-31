"""Os números do capítulo 09, verificados."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.electre import ErroDeLimiares, analisar_electre
from motor.matriz import Criterio, MatrizDecisao

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


def test_limiares_exigentes_ninguem_sobreclassifica():
    # c*=0,6 e d*=0,4: nenhuma coalizão é forte E incontestada ao mesmo tempo.
    r = analisar_electre(ANCORA, c_estrela=0.6, d_estrela=0.4)
    assert r["sobreclassifica"] == []
    assert r["kernel"] == NOMES  # o conflito é real: shortlist = todo mundo


def test_afrouxando_d_estrela_surge_a_relacao_do_capitulo():
    r = analisar_electre(ANCORA, c_estrela=0.6, d_estrela=0.65)
    assert r["sobreclassifica"] == [
        ("A1 — Centro", "A4 — Estação"),
        ("A4 — Estação", "A2 — Jardim"),
    ]
    # Kernel: sem sobreclassificador estrito → shortlist {A1, A3}.
    assert r["kernel"] == ["A1 — Centro", "A3 — Parque"]


def test_concordancia_e_discordancia_do_par_a1_a4():
    r = analisar_electre(ANCORA)
    i1, i4 = NOMES.index("A1 — Centro"), NOMES.index("A4 — Estação")
    assert r["concordancia"][i1][i4] == pytest.approx(0.65)
    assert r["discordancia"][i1][i4] == pytest.approx(0.6111, abs=1e-4)


def test_veto_bloqueia_sem_olhar_concordancia():
    # Veto de 1 ponto no Bairro: A4 (bairro 2) não pode sobreclassificar A2
    # (bairro 3) — a diferença contra atinge o veto, apesar de C=0,6.
    r = analisar_electre(
        ANCORA, c_estrela=0.6, d_estrela=0.65, vetos=[None, None, None, 1]
    )
    assert r["sobreclassifica"] == [("A1 — Centro", "A4 — Estação")]
    assert "A2 — Jardim" in r["kernel"]


def test_limiar_invalido_e_erro():
    with pytest.raises(ErroDeLimiares, match="c\\*"):
        analisar_electre(ANCORA, c_estrela=0.3)
