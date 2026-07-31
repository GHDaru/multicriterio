"""Etapa 09 — ELECTRE I: quando NÃO compensar.

Capítulo correspondente: livro/capitulos/09-electre.md.

A dor deixada pela etapa 08: o PROMETHEE II ainda soma tudo num φ — um déficit
grave continua compensável. O ELECTRE I (Roy, 1968) aceita "a sobreclassifica
b" só quando a coalizão a favor é forte (concordância >= c*) E nenhum critério
contra grita alto demais (discordância <= d*), com VETOS incondicionais. A
saída é uma shortlist (kernel), não um ranking — e isso é feature.

Como rodar:
    uvicorn app:app --reload
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.electre import ErroDeLimiares, analisar_electre
from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao

app = FastAPI(title="decisor-zero — etapa 09")


class CriterioIn(BaseModel):
    nome: str
    direcao: str
    unidade: str = ""


class ElectreIn(BaseModel):
    alternativas: list[str]
    criterios: list[CriterioIn]
    desempenhos: list[list[float]]
    pesos: list[float]
    c_estrela: float = 0.6
    d_estrela: float = 0.4
    vetos: list[float | None] | None = None


@app.post("/api/matriz/electre")
def electre(entrada: ElectreIn) -> dict:
    try:
        matriz = MatrizDecisao(
            alternativas=entrada.alternativas,
            criterios=[Criterio(c.nome, c.direcao, c.unidade) for c in entrada.criterios],
            desempenhos=entrada.desempenhos,
            pesos=entrada.pesos,
        )
        return {
            "metodo": "electre1",
            **analisar_electre(matriz, entrada.c_estrela, entrada.d_estrela, entrada.vetos),
        }
    except (ErroDeModelagem, ErroDeLimiares, ValueError) as erro:
        raise HTTPException(422, str(erro)) from erro


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
