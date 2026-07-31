"""Pesos no produto: motor + rota stateless (worked examples do cap. 03)."""

import pytest
from fastapi.testclient import TestClient

from decisor.main import app
from decisor.motor.pesos import pesos_entropia
from decisor.motor.tipos import Problema

PROBLEMA_ANCORA = {
    "alternativas": ["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação"],
    "criterios": [
        {"nome": "Preço", "direcao": "custo", "unidade": "R$"},
        {"nome": "Área", "direcao": "beneficio", "unidade": "m²"},
        {"nome": "Deslocamento", "direcao": "custo", "unidade": "min"},
        {"nome": "Bairro", "direcao": "beneficio", "unidade": "1–5"},
    ],
    "desempenhos": [
        [450_000, 62, 15, 4],
        [380_000, 70, 35, 3],
        [520_000, 85, 25, 5],
        [340_000, 55, 20, 2],
    ],
}


def test_entropia_do_caso_ancora_no_motor():
    obtido = pesos_entropia(Problema(**PROBLEMA_ANCORA))
    assert obtido == pytest.approx([0.2365, 0.2948, 0.2178, 0.2509], abs=1e-4)


def test_rota_de_pesos_roc_e_swing():
    with TestClient(app) as client:
        roc = client.post("/api/pesos", json={"metodo": "roc", "ranking": [0, 1, 2, 3]})
        assert roc.status_code == 200
        assert roc.json()["pesos"] == pytest.approx(
            [0.5208, 0.2708, 0.1458, 0.0625], abs=1e-4
        )
        swing = client.post(
            "/api/pesos", json={"metodo": "swing", "valores": [100, 60, 70, 40]}
        )
        assert swing.json()["pesos"] == pytest.approx(
            [0.3704, 0.2222, 0.2593, 0.1481], abs=1e-4
        )


def test_rota_de_pesos_entropia_exige_problema():
    with TestClient(app) as client:
        sem = client.post("/api/pesos", json={"metodo": "entropia"})
        assert sem.status_code == 422
        com = client.post(
            "/api/pesos", json={"metodo": "entropia", "problema": PROBLEMA_ANCORA}
        )
        assert com.status_code == 200
        assert com.json()["pesos"][1] == pytest.approx(0.2948, abs=1e-4)


def test_erro_de_elicitacao_vira_422():
    with TestClient(app) as client:
        resposta = client.post("/api/pesos", json={"metodo": "swing", "valores": [90, 10]})
        assert resposta.status_code == 422
        assert "100" in resposta.json()["detail"]
