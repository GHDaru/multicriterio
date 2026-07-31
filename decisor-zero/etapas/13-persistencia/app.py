"""Etapa 13 — do protótipo ao produto: a decisão sobrevive ao reload.

Capítulo correspondente: livro/capitulos/13-persistencia.md.

A dor de todas as etapas anteriores: fechou o servidor, perdeu a decisão. Esta
etapa fecha o ciclo do livro: um repositório (repositorio.py) esconde o banco
atrás de DATABASE_URL — Neon (Postgres serverless) em produção, SQLite local a
custo zero — exatamente a arquitetura do produto (app/). O decisor-zero
oficialmente virou o Decisor.

Como rodar:
    uvicorn app:app --reload            # SQLite local (custo zero)
    DATABASE_URL=postgres://... uvicorn app:app   # Neon (ver .env.example)
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from repositorio import RepositorioDecisoes

app = FastAPI(title="decisor-zero — etapa 13")
repositorio = RepositorioDecisoes()


class DecisaoIn(BaseModel):
    titulo: str
    problema: dict


@app.get("/health")
def health() -> dict:
    banco = "postgres" if "postgres" in str(repositorio.engine.url) else "sqlite"
    return {"status": "ok", "banco": banco}


@app.post("/api/decisoes", status_code=201)
def salvar(entrada: DecisaoIn) -> dict:
    novo_id = repositorio.salvar(entrada.titulo, entrada.problema)
    return {"id": novo_id}


@app.get("/api/decisoes")
def listar() -> list[dict]:
    return [
        {"id": d.id, "titulo": d.titulo, "criada_em": d.criada_em.isoformat()}
        for d in repositorio.listar()
    ]


@app.get("/api/decisoes/{decisao_id}")
def buscar(decisao_id: int) -> dict:
    registro = repositorio.buscar(decisao_id)
    if registro is None:
        raise HTTPException(404, "decisão não encontrada")
    return {"id": registro.id, "titulo": registro.titulo, "problema": registro.problema}


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
