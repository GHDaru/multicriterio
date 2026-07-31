"""Etapa 08 — PROMETHEE: a escola europeia entra em cena.

Capítulo correspondente: livro/capitulos/08-promethee.md.

A dor deixada pelas etapas 04–07: todos os métodos até aqui COMPENSAM — déficit
em um critério se paga com sobra em outro, sempre. A escola de sobreclassificação
(outranking) constrói outra coisa: comparações PAR A PAR entre alternativas,
com funções de preferência por critério. Nesta etapa nasce motor/promethee.py
(PROMETHEE II: fluxos φ+, φ−, φ), validado contra a pymcdm.

Como rodar:
    uvicorn app:app --reload
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao
from motor.promethee import ErroDePreferencia, fluxos_promethee

app = FastAPI(title="decisor-zero — etapa 08")


class CriterioIn(BaseModel):
    nome: str
    direcao: str
    unidade: str = ""


class PrometheeIn(BaseModel):
    alternativas: list[str]
    criterios: list[CriterioIn]
    desempenhos: list[list[float]]
    pesos: list[float]
    funcao: str = "usual"
    limiares: list[float] | None = None


@app.post("/api/matriz/promethee")
def promethee(entrada: PrometheeIn) -> dict:
    try:
        matriz = MatrizDecisao(
            alternativas=entrada.alternativas,
            criterios=[Criterio(c.nome, c.direcao, c.unidade) for c in entrada.criterios],
            desempenhos=entrada.desempenhos,
            pesos=entrada.pesos,
        )
        ranking = fluxos_promethee(matriz, entrada.funcao, entrada.limiares)
    except (ErroDeModelagem, ErroDePreferencia, ValueError) as erro:
        raise HTTPException(422, str(erro)) from erro
    return {"metodo": f"promethee2/{entrada.funcao}", "ranking": ranking}


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
