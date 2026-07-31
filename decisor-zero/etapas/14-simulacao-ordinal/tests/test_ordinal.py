"""AEO — propriedades e os números do cap. 14 / Apêndice C (semente fixa)."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.ordinal import ErroDeOrdinal, simular_aeo

ALT = ["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação"]
RK = [
    ["A4 — Estação", "A2 — Jardim", "A1 — Centro", "A3 — Parque"],   # Preço
    ["A3 — Parque", "A2 — Jardim", "A1 — Centro", "A4 — Estação"],   # Área
    ["A1 — Centro", "A4 — Estação", "A3 — Parque", "A2 — Jardim"],   # Deslocamento
    ["A3 — Parque", "A1 — Centro", "A2 — Jardim", "A4 — Estação"],   # Bairro
]


def test_dominancia_ordinal_e_respeitada_com_probabilidade_1():
    # Proposição 1 do artigo: A acima de B em TODO critério ⇒ P(A ≻ B) = 1.
    r = simular_aeo(
        ["A", "B", "C"],
        [["A", "B", "C"], ["A", "C", "B"], ["C", "A", "B"]],  # A sempre acima de B
        n_simulacoes=2_000, semente=7,
    )
    assert r["prob_par_a_par"]["A"]["B"] == 1.0
    assert r["aceitabilidade"]["B"][0] == 0.0  # dominada nunca é 1ª


def test_simetria_perfeita_da_50_50():
    r = simular_aeo(
        ["X", "Y"], [["X", "Y"], ["Y", "X"]], n_simulacoes=20_000, semente=1,
    )
    assert r["prob_par_a_par"]["X"]["Y"] == pytest.approx(0.5, abs=0.02)


def test_ancora_com_ordem_de_pesos_semente_42():
    # Números do cap. 14: A4 vence nas três regras; A1 × A2 é empate técnico.
    r = simular_aeo(ALT, RK, ordem_pesos=[0, 1, 2, 3],
                    n_simulacoes=20_000, semente=42)
    assert r["aceitabilidade"]["A4 — Estação"][0] == pytest.approx(0.3643, abs=1e-4)
    assert r["posto_esperado"]["A4 — Estação"] == pytest.approx(2.2262, abs=1e-4)
    assert r["vencedor_condorcet"] == "A4 — Estação"
    assert r["ordem_final"][0] == "A4 — Estação"
    # Empate técnico entre A1 e A2 (protocolo do artigo: faixa [0,45; 0,55]).
    assert r["prob_par_a_par"]["A1 — Centro"]["A2 — Jardim"] == pytest.approx(
        0.5004, abs=1e-4
    )


def test_ancora_sem_ordem_as_regras_divergem():
    # O achado da §7 do artigo: Condorcet e mais-1ºs elegem A3; posto esperado
    # elege A1 por margem mínima. É por isso que existe o protocolo.
    r = simular_aeo(ALT, RK, ordem_pesos=None, n_simulacoes=20_000, semente=42)
    assert r["vencedor_condorcet"] == "A3 — Parque"
    mais_primeiros = max(ALT, key=lambda a: r["aceitabilidade"][a][0])
    assert mais_primeiros == "A3 — Parque"
    assert r["ordem_final"][0] == "A1 — Centro"  # posto 1,9927 × 2,0194
    assert r["posto_esperado"]["A1 — Centro"] == pytest.approx(1.9927, abs=1e-4)
    assert r["posto_esperado"]["A3 — Parque"] == pytest.approx(2.0194, abs=1e-4)


def test_fornecedor_f2_vence_nas_tres_regras():
    falt = ["F1 — Hiperescala", "F2 — Regional", "F3 — Nicho"]
    frk = [
        ["F3 — Nicho", "F2 — Regional", "F1 — Hiperescala"],
        ["F2 — Regional", "F1 — Hiperescala", "F3 — Nicho"],
        ["F1 — Hiperescala", "F2 — Regional", "F3 — Nicho"],
        ["F3 — Nicho", "F2 — Regional", "F1 — Hiperescala"],
    ]
    r = simular_aeo(falt, frk, ordem_pesos=[0, 2, 1, 3],
                    n_simulacoes=20_000, semente=42)
    assert r["aceitabilidade"]["F2 — Regional"][0] == pytest.approx(0.5299, abs=1e-4)
    assert r["vencedor_condorcet"] == "F2 — Regional"
    assert r["ordem_final"][0] == "F2 — Regional"


def test_crencas_o_vetor_central_de_a4_e_mais_preco_centrico():
    r = simular_aeo(ALT, RK, ordem_pesos=[0, 1, 2, 3],
                    n_simulacoes=20_000, semente=42)
    w_a4 = r["pesos_centrais"]["A4 — Estação"]
    w_a1 = r["pesos_centrais"]["A1 — Centro"]
    assert w_a4[0] > w_a1[0]                       # A4 exige crer mais em Preço
    assert w_a4[0] == pytest.approx(0.4517, abs=1e-4)
    assert sum(w_a4) == pytest.approx(1.0, abs=1e-3)


def test_reprodutibilidade_da_semente():
    a = simular_aeo(ALT, RK, n_simulacoes=500, semente=99)
    b = simular_aeo(ALT, RK, n_simulacoes=500, semente=99)
    assert a == b


def test_validacoes():
    with pytest.raises(ErroDeOrdinal, match="permutação"):
        simular_aeo(["A", "B"], [["A", "A"]])
    with pytest.raises(ErroDeOrdinal, match="ordem_pesos"):
        simular_aeo(["A", "B"], [["A", "B"]], ordem_pesos=[0, 1])
