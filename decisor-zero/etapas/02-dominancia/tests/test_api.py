"""A casca FastAPI da etapa 02: análise de dominância via API."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_dominancia_do_caso_ancora_com_a5():
    caso = client.get("/api/caso-ancora").json()
    resposta = client.post("/api/matriz/dominancia", json={
        "alternativas": caso["alternativas"],
        "criterios": caso["criterios"],
        "desempenhos": caso["desempenhos"],
    })
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["dominadas"] == {"A5 — Colina": ["A1 — Centro"]}
    assert len(corpo["fronteira_pareto"]) == 4


def test_erro_de_modelagem_continua_virando_422():
    resposta = client.post("/api/matriz/dominancia", json={
        "alternativas": ["X"],
        "criterios": [{"nome": "C", "direcao": "menor-melhor"}],
        "desempenhos": [[1]],
    })
    assert resposta.status_code == 422
    assert "direção" in resposta.json()["detail"]
