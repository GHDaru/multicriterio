"""Etapa 00 — os dois domínios do livro servidos pelo chassi."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_caso_ancora_igual_ao_livro():
    corpo = client.get("/api/caso-ancora").json()
    assert corpo["alternativas"][2]["desempenhos"] == [520_000, 85, 25, 5]


def test_caso_fornecedor_igual_ao_livro():
    corpo = client.get("/api/caso-fornecedor").json()
    assert [a["nome"] for a in corpo["alternativas"]] == [
        "F1 — Hiperescala", "F2 — Regional", "F3 — Nicho",
    ]
    assert corpo["alternativas"][1]["desempenhos"] == [9_000, 20, 99.50, 4]
