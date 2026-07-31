"""A casca FastAPI da etapa 05."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_prioridades_do_caso_ancora_via_api():
    julgamentos = client.get("/api/caso-ancora").json()["julgamentos"]
    corpo = client.post("/api/ahp/prioridades", json={"julgamentos": julgamentos}).json()
    assert corpo["pesos"] == pytest.approx([0.4236, 0.2270, 0.2270, 0.1223], abs=1e-4)
    assert corpo["consistente"] is True


def test_julgamentos_invalidos_viram_422():
    resposta = client.post(
        "/api/ahp/prioridades", json={"julgamentos": [[1, 2], [3, 1]]}
    )
    assert resposta.status_code == 422
    assert "recíproco" in resposta.json()["detail"]
