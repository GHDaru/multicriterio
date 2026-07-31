"""Etapa 10 — VIKOR e BWM: compromisso e pesos com menos perguntas.

Capítulo correspondente: livro/capitulos/10-vikor-bwm.md.

Duas dores. (1) Rankear sempre "elege" alguém — mesmo quando a vantagem do 1º
é estatisticamente ridícula; o VIKOR (Opricovic & Tzeng) formaliza quando a
resposta honesta é um CONJUNTO de compromisso. (2) O AHP exige n(n−1)/2
comparações; o BWM (Rezaei) extrai pesos de apenas 2n−3, com índice de
consistência ξ.

Como rodar:
    uvicorn app:app --reload
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.bwm import ErroDeBWM, pesos_bwm
from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao
from motor.vikor import analisar_vikor

app = FastAPI(title="decisor-zero — etapa 10")


class CriterioIn(BaseModel):
    nome: str
    direcao: str
    unidade: str = ""


class VikorIn(BaseModel):
    alternativas: list[str]
    criterios: list[CriterioIn]
    desempenhos: list[list[float]]
    pesos: list[float]
    v: float = 0.5


class BwmIn(BaseModel):
    best: int
    worst: int
    best_para_todos: list[float]
    todos_para_worst: list[float]


@app.post("/api/matriz/vikor")
def vikor(entrada: VikorIn) -> dict:
    try:
        matriz = MatrizDecisao(
            alternativas=entrada.alternativas,
            criterios=[Criterio(c.nome, c.direcao, c.unidade) for c in entrada.criterios],
            desempenhos=entrada.desempenhos,
            pesos=entrada.pesos,
        )
        return {"metodo": "vikor", **analisar_vikor(matriz, entrada.v)}
    except (ErroDeModelagem, ValueError) as erro:
        raise HTTPException(422, str(erro)) from erro


@app.post("/api/pesos/bwm")
def bwm(entrada: BwmIn) -> dict:
    try:
        return {"metodo": "bwm", **pesos_bwm(
            entrada.best, entrada.worst,
            entrada.best_para_todos, entrada.todos_para_worst,
        )}
    except ErroDeBWM as erro:
        raise HTTPException(422, str(erro)) from erro


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
