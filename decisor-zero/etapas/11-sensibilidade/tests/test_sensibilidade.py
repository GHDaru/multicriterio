"""Os números do capítulo 11, verificados."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from motor.matriz import Criterio, MatrizDecisao
from motor.sensibilidade import (
    comparar_metodos, spearman, ensaio_rank_reversal, varredura_peso,
)

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


def test_varredura_do_peso_do_preco_no_saw():
    # O reinado de A1 é uma janela estreita: [0,316; 0,358). Nosso 0,35 está
    # dentro — por 0,008.
    faixas = varredura_peso(ANCORA, indice=0, metodo="saw")
    assert faixas == [
        {"a_partir_de": 0.0, "vencedor": "A3 — Parque"},
        {"a_partir_de": 0.316, "vencedor": "A1 — Centro"},
        {"a_partir_de": 0.358, "vencedor": "A4 — Estação"},
    ]


def test_com_estes_pesos_os_quatro_metodos_concordam_totalmente():
    resultado = comparar_metodos(ANCORA)
    ordem_saw = resultado["rankings"]["saw"]
    assert all(ordem == ordem_saw for ordem in resultado["rankings"].values())
    assert all(
        rho == 1.0
        for linha in resultado["spearman"].values()
        for rho in linha.values()
    )


def test_rank_reversal_no_topsis_com_alternativa_de_ultimo_lugar():
    # A5 (430k, 59 m², 24 min, bairro 1) entra e termina em ÚLTIMO — e ainda
    # assim inverte A4 e A3 no miolo do pódio (as âncoras ideal/anti-ideal
    # mudaram). García-Cascales & Lamata (2012).
    r = ensaio_rank_reversal(ANCORA, "A5 — Colinas", [430_000, 59, 24, 1], "topsis")
    assert r["antes"] == ["A1 — Centro", "A4 — Estação", "A3 — Parque", "A2 — Jardim"]
    assert r["depois_completa"][-1] == "A5 — Colinas"
    assert r["ordem_relativa_depois"] == [
        "A1 — Centro", "A3 — Parque", "A4 — Estação", "A2 — Jardim",
    ]
    assert r["houve_reversao"] is True


def test_o_mesmo_a5_vira_o_vencedor_do_saw():
    # Mais forte ainda: o min-max é relativo ao conjunto (o bairro 1 de A5
    # estica a amplitude da coluna) — e o VENCEDOR do SAW troca (A1 → A4).
    r = ensaio_rank_reversal(ANCORA, "A5 — Colinas", [430_000, 59, 24, 1], "saw")
    assert r["houve_reversao"] is True
    assert r["ordem_relativa_depois"][0] == "A4 — Estação"


def test_spearman_casos_limite():
    assert spearman(["a", "b", "c"], ["a", "b", "c"]) == 1.0
    assert spearman(["a", "b", "c"], ["c", "b", "a"]) == -1.0
