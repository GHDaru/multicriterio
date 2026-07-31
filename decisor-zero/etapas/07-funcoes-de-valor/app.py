"""Etapa 07 — MAVT: o valor não é linear (e o SAW é um caso particular).

Capítulo correspondente: livro/capitulos/07-funcoes-de-valor.md.

A dor deixada pelas etapas 04–06: todos os métodos até aqui assumem que valor
cresce LINEARMENTE com o desempenho — cada real economizado vale o mesmo. Mas
economizar de 520k para 460k não vale o mesmo que de 400k para 340k. Nesta
etapa nasce motor/valor.py: funções de valor por critério (pontos de quebra,
interpolação monótona), com dois fatos provados em teste: funções lineares
reproduzem o SAW exatamente; funções curvas mudam o pódio sem tocar nos pesos.

Como rodar:
    uvicorn app:app --reload
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao
from motor.valor import ErroDeFuncaoValor, ranquear_mavt

app = FastAPI(title="decisor-zero — etapa 07")


class CriterioIn(BaseModel):
    nome: str
    direcao: str
    unidade: str = ""


class MavtIn(BaseModel):
    alternativas: list[str]
    criterios: list[CriterioIn]
    desempenhos: list[list[float]]
    pesos: list[float]
    funcoes: dict[str, list[tuple[float, float]]]


@app.post("/api/matriz/mavt")
def mavt(entrada: MavtIn) -> dict:
    try:
        matriz = MatrizDecisao(
            alternativas=entrada.alternativas,
            criterios=[Criterio(c.nome, c.direcao, c.unidade) for c in entrada.criterios],
            desempenhos=entrada.desempenhos,
            pesos=entrada.pesos,
        )
        return {"metodo": "mavt", "ranking": ranquear_mavt(matriz, entrada.funcoes)}
    except (ErroDeModelagem, ErroDeFuncaoValor, ValueError) as erro:
        raise HTTPException(422, str(erro)) from erro


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
