"""Dominância no produto: motor puro + rota (worked example do cap. 02)."""

from fastapi.testclient import TestClient

from decisor.main import app
from decisor.motor.dominancia import analise_dominancia
from decisor.motor.tipos import Problema

CRITERIOS = [
    {"nome": "Preço", "direcao": "custo", "unidade": "R$"},
    {"nome": "Área", "direcao": "beneficio", "unidade": "m²"},
    {"nome": "Deslocamento", "direcao": "custo", "unidade": "min"},
    {"nome": "Bairro", "direcao": "beneficio", "unidade": "1–5"},
]
DESEMPENHOS_COM_A5 = [
    [450_000, 62, 15, 4],
    [380_000, 70, 35, 3],
    [520_000, 85, 25, 5],
    [340_000, 55, 20, 2],
    [470_000, 60, 18, 3],
]
NOMES = ["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação", "A5 — Colina"]


def test_motor_reproduz_o_worked_example_do_capitulo_02():
    problema = Problema(
        alternativas=NOMES, criterios=CRITERIOS, desempenhos=DESEMPENHOS_COM_A5
    )
    resultado = analise_dominancia(problema)
    assert resultado["dominadas"] == {"A5 — Colina": ["A1 — Centro"]}
    assert resultado["fronteira_pareto"] == NOMES[:4]


def test_rota_de_dominancia_ponta_a_ponta():
    with TestClient(app) as client:
        decisao_id = client.post("/api/decisoes", json={
            "titulo": "Apartamento com candidato A5",
            "problema": {
                "alternativas": NOMES,
                "criterios": CRITERIOS,
                "desempenhos": DESEMPENHOS_COM_A5,
            },
        }).json()["id"]
        resposta = client.post(f"/api/decisoes/{decisao_id}/dominancia")
        assert resposta.status_code == 200
        corpo = resposta.json()
        assert corpo["dominadas"] == {"A5 — Colina": ["A1 — Centro"]}
        assert corpo["fronteira_pareto"] == NOMES[:4]
