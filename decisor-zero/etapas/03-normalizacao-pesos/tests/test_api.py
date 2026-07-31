"""A casca FastAPI da etapa 03: normalização e elicitação de pesos via API."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def _matriz_ancora() -> dict:
    caso = client.get("/api/caso-ancora").json()
    return {
        "alternativas": caso["alternativas"],
        "criterios": caso["criterios"],
        "desempenhos": caso["desempenhos"],
    }


def test_normalizar_minmax_resolve_direcao():
    corpo = client.post("/api/normalizar?metodo=minmax", json=_matriz_ancora()).json()
    assert corpo["resolve_direcao"] is True
    assert corpo["normalizada"][3][0] == 1.0  # A4, a mais barata


def test_normalizar_vetorial_avisa_que_nao_resolve_direcao():
    corpo = client.post("/api/normalizar?metodo=vetorial", json=_matriz_ancora()).json()
    assert corpo["resolve_direcao"] is False


def test_pesos_roc_via_api():
    corpo = client.post("/api/pesos", json={"metodo": "roc", "ranking": [0, 1, 2, 3]}).json()
    assert corpo["pesos"] == pytest.approx([0.5208, 0.2708, 0.1458, 0.0625], abs=1e-4)


def test_pesos_entropia_via_api():
    corpo = client.post(
        "/api/pesos", json={"metodo": "entropia", "matriz": _matriz_ancora()}
    ).json()
    assert corpo["pesos"] == pytest.approx([0.2365, 0.2948, 0.2178, 0.2509], abs=1e-4)


def test_erro_de_pesos_vira_422_legivel():
    resposta = client.post("/api/pesos", json={"metodo": "swing", "valores": [90, 60]})
    assert resposta.status_code == 422
    assert "100" in resposta.json()["detail"]
