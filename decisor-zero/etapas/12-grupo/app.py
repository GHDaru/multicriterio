"""Etapa 12 — decisão em grupo: agregar pessoas, não só critérios.

Capítulo correspondente: livro/capitulos/12-grupo.md.

A dor deixada pela etapa 11: mesmo com um ranking robusto, decisões reais têm
VÁRIOS decisores — e agregar preferências de pessoas é um problema com
armadilhas próprias (maiorias cíclicas, ditadores, manipulação). Nesta etapa
nascem Borda, Copeland e a agregação de julgamentos AHP (média geométrica).

Como rodar:
    uvicorn app:app --reload
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.grupo import ErroDeGrupo, agregar_julgamentos, borda, copeland

app = FastAPI(title="decisor-zero — etapa 12")


class RankingsIn(BaseModel):
    rankings: list[list[str]]


class JulgamentosIn(BaseModel):
    matrizes: list[list[list[float]]]


@app.post("/api/grupo/rankings")
def agregar_rankings(entrada: RankingsIn) -> dict:
    try:
        return {
            "borda": borda(entrada.rankings),
            "copeland": copeland(entrada.rankings),
        }
    except ErroDeGrupo as erro:
        raise HTTPException(422, str(erro)) from erro


@app.post("/api/grupo/julgamentos")
def aij(entrada: JulgamentosIn) -> dict:
    try:
        return agregar_julgamentos(entrada.matrizes)
    except (ErroDeGrupo, ValueError) as erro:
        raise HTTPException(422, str(erro)) from erro


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
