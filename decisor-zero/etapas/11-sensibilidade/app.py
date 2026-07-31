"""Etapa 11 — sensibilidade: quando o ranking merece confiança?

Capítulo correspondente: livro/capitulos/11-sensibilidade.md.

A dor acumulada desde o cap. 04: vimos o pódio virar com pesos (rating × ROC ×
AHP), com funções de valor (cap. 07), com funções de preferência (cap. 08) — e
agora com a simples ENTRADA de um candidato medíocre (rank reversal). Esta
etapa transforma a desconfiança em instrumento: varredura de peso, comparação
multi-método com Spearman e ensaio de rank reversal.

Como rodar:
    uvicorn app:app --reload
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao
from motor.sensibilidade import (
    METODOS, comparar_metodos, ensaio_rank_reversal, varredura_peso,
)

app = FastAPI(title="decisor-zero — etapa 11")


class CriterioIn(BaseModel):
    nome: str
    direcao: str
    unidade: str = ""


class MatrizIn(BaseModel):
    alternativas: list[str]
    criterios: list[CriterioIn]
    desempenhos: list[list[float]]
    pesos: list[float]


def _montar(entrada: MatrizIn) -> MatrizDecisao:
    try:
        return MatrizDecisao(
            alternativas=entrada.alternativas,
            criterios=[Criterio(c.nome, c.direcao, c.unidade) for c in entrada.criterios],
            desempenhos=entrada.desempenhos,
            pesos=entrada.pesos,
        )
    except ErroDeModelagem as erro:
        raise HTTPException(422, str(erro)) from erro


@app.post("/api/matriz/varredura")
def varredura(entrada: MatrizIn, criterio: int = 0, metodo: str = "saw") -> dict:
    if metodo not in METODOS:
        raise HTTPException(422, f"método {metodo!r} desconhecido")
    return {"faixas": varredura_peso(_montar(entrada), criterio, metodo)}


@app.post("/api/matriz/comparar")
def comparar(entrada: MatrizIn) -> dict:
    return comparar_metodos(_montar(entrada))


class ReversalIn(MatrizIn):
    nome_novo: str
    desempenhos_novo: list[float]
    metodo: str = "topsis"


@app.post("/api/matriz/rank-reversal")
def rank_reversal(entrada: ReversalIn) -> dict:
    return ensaio_rank_reversal(
        _montar(entrada), entrada.nome_novo, entrada.desempenhos_novo, entrada.metodo
    )


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
