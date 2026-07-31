"""Etapa 06 — TOPSIS: perto do ideal, longe do anti-ideal.

Capítulo correspondente: livro/capitulos/06-topsis.md.

A dor deixada pela etapa 05: o SAW compara alternativas com uma régua aditiva —
mas há outra intuição legítima: a melhor alternativa é a que fica MAIS PERTO da
solução ideal e MAIS LONGE da pior. Nesta etapa nasce motor/topsis.py
(normalização vetorial do cap. 03 + geometria de distâncias). No caso âncora,
TOPSIS e SAW concordam — a discórdia entre métodos fica para o cap. 11.

Como rodar:
    uvicorn app:app --reload
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao
from motor.saw import ranquear_saw
from motor.topsis import ranquear_topsis

app = FastAPI(title="decisor-zero — etapa 06")


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


@app.post("/api/matriz/topsis")
def topsis(entrada: MatrizIn) -> dict:
    matriz = _montar(entrada)
    return {
        "metodo": "topsis",
        "ranking": ranquear_topsis(matriz),
        "saw_para_comparar": ranquear_saw(matriz),
    }


@app.get("/api/caso-ancora")
def caso() -> dict:
    return {
        "alternativas": ["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação"],
        "criterios": [
            {"nome": "Preço", "direcao": "custo", "unidade": "R$"},
            {"nome": "Área", "direcao": "beneficio", "unidade": "m²"},
            {"nome": "Deslocamento", "direcao": "custo", "unidade": "min"},
            {"nome": "Bairro", "direcao": "beneficio", "unidade": "1–5"},
        ],
        "desempenhos": [
            [450_000, 62, 15, 4], [380_000, 70, 35, 3],
            [520_000, 85, 25, 5], [340_000, 55, 20, 2],
        ],
        "pesos": [0.35, 0.25, 0.25, 0.15],
    }


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
