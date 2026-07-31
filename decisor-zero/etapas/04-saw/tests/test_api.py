"""A casca FastAPI da etapa 04: ranking SAW via API."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def _corpo(pesos: list[float]) -> dict:
    caso = client.get("/api/caso-ancora").json()
    return {
        "alternativas": caso["alternativas"],
        "criterios": caso["criterios"],
        "desempenhos": caso["desempenhos"],
        "pesos": pesos,
    }


def test_saw_com_rating_via_api():
    corpo = client.post("/api/matriz/saw", json=_corpo([0.35, 0.25, 0.25, 0.15])).json()
    assert corpo["ranking"][0]["alternativa"] == "A1 — Centro"


def test_saw_com_roc_via_api_troca_o_vencedor():
    caso = client.get("/api/caso-ancora").json()
    corpo = client.post("/api/matriz/saw", json=_corpo(caso["pesos_roc"])).json()
    assert corpo["ranking"][0]["alternativa"] == "A4 — Estação"
    assert corpo["ranking"][0]["escore"] == pytest.approx(0.630208, abs=1e-4)


def test_pesos_invalidos_viram_422():
    resposta = client.post("/api/matriz/saw", json=_corpo([0.7, 0.5, -0.1, -0.1]))
    assert resposta.status_code == 422
    assert "negativos" in resposta.json()["detail"]
