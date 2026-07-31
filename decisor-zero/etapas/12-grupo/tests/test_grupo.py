"""Os números do capítulo 12, verificados."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.grupo import ErroDeGrupo, agregar_julgamentos, borda, copeland

# Worked example do cap. 12: três stakeholders ranqueiam os apartamentos.
ANA = ["A4 — Estação", "A2 — Jardim", "A1 — Centro", "A3 — Parque"]     # financeira
BIA = ["A3 — Parque", "A1 — Centro", "A2 — Jardim", "A4 — Estação"]     # qualidade
CAIO = ["A1 — Centro", "A4 — Estação", "A2 — Jardim", "A3 — Parque"]    # equilíbrio


def test_borda_do_capitulo():
    resultado = borda([ANA, BIA, CAIO])
    assert [(l["alternativa"], l["escore"]) for l in resultado] == [
        ("A1 — Centro", 6), ("A4 — Estação", 5),
        ("A2 — Jardim", 4), ("A3 — Parque", 3),
    ]


def test_copeland_do_capitulo():
    resultado = copeland([ANA, BIA, CAIO])
    assert [(l["alternativa"], l["escore"]) for l in resultado] == [
        ("A1 — Centro", 3), ("A4 — Estação", 1),
        ("A2 — Jardim", -1), ("A3 — Parque", -3),
    ]


def test_paradoxo_de_condorcet_vira_empate_geral():
    # O ciclo clássico: X>Y>Z, Y>Z>X, Z>X>Y — maiorias cíclicas.
    ciclo = [["X", "Y", "Z"], ["Y", "Z", "X"], ["Z", "X", "Y"]]
    assert all(l["escore"] == 0 for l in copeland(ciclo))
    assert all(l["escore"] == 3 for l in borda(ciclo))


def test_aij_preserva_reciprocidade_e_consistencia():
    ana = [[1, 2, 2, 3], [0.5, 1, 1, 2], [0.5, 1, 1, 2], [1 / 3, 0.5, 0.5, 1]]
    # Bia discorda: Preço vale menos, Bairro vale mais.
    bia = [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 2], [1, 0.5, 0.5, 1]]
    r = agregar_julgamentos([ana, bia])
    agregada = r["julgamentos_agregados"]
    for i in range(4):
        for j in range(4):
            assert agregada[i][j] * agregada[j][i] == pytest.approx(1.0, abs=1e-9)
    assert sum(r["pesos"]) == pytest.approx(1.0)
    assert r["consistente"] is True
    # O peso do Preço fica entre o de Ana (0,4236) e o de Bia (~igualitário).
    assert 0.25 < r["pesos"][0] < 0.4236


def test_aij_de_juizes_identicos_e_o_proprio_juiz():
    ana = [[1, 3], [1 / 3, 1]]
    r = agregar_julgamentos([ana, ana, ana])
    assert r["julgamentos_agregados"][0][1] == pytest.approx(3.0)


def test_ranking_incompativel_e_erro():
    with pytest.raises(ErroDeGrupo, match="permutação"):
        borda([["X", "Y"], ["X", "Z"]])


def test_segundo_dominio_comite_polarizado():
    """Fornecedores (ADR 0007): dois votos opostos, o terceiro desempata tudo."""
    financeiro = ["F3 — Nicho", "F2 — Regional", "F1 — Hiperescala"]
    confiabilidade = ["F1 — Hiperescala", "F2 — Regional", "F3 — Nicho"]
    latencia = ["F2 — Regional", "F3 — Nicho", "F1 — Hiperescala"]
    votos = [financeiro, confiabilidade, latencia]
    assert [(l["alternativa"], l["escore"]) for l in borda(votos)] == [
        ("F2 — Regional", 4), ("F3 — Nicho", 3), ("F1 — Hiperescala", 2),
    ]
    assert [(l["alternativa"], l["escore"]) for l in copeland(votos)] == [
        ("F2 — Regional", 2), ("F3 — Nicho", 0), ("F1 — Hiperescala", -2),
    ]
    # Financeiro e Confiabilidade são rankings perfeitamente invertidos.
    assert financeiro == list(reversed(confiabilidade))
