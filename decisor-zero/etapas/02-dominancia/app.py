"""Etapa 02 — dominância: o que dá para decidir sem nenhum método.

Capítulo correspondente: livro/capitulos/02-estruturacao-dominancia.md.

A dor deixada pela etapa 01: a matriz validada mostra o conflito, mas nada
descarta as alternativas que NENHUMA preferência racional escolheria. Nesta
etapa nascem duas coisas: (1) a correção do peso negativo em motor/matriz.py —
o gabarito do exercício do cap. 01, e o diff é a lição; (2) o módulo
motor/dominancia.py, que identifica alternativas dominadas e devolve a
fronteira de Pareto. No caso âncora, o candidato A5 (Colina) entra em cena
para ser eliminado por A1 antes de qualquer cálculo de pesos.

Como rodar:
    uvicorn app:app --reload      # http://localhost:8000
    pytest                        # os números do capítulo 02, verificados
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.dominancia import analise_dominancia
from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao

app = FastAPI(title="decisor-zero — etapa 02")

CRITERIOS_ANCORA = [
    Criterio("Preço", "custo", "R$"),
    Criterio("Área", "beneficio", "m²"),
    Criterio("Deslocamento", "custo", "min"),
    Criterio("Bairro", "beneficio", "1–5"),
]


def caso_ancora_com_candidato() -> MatrizDecisao:
    """O caso âncora + A5 (Colina), o candidato que o cap. 02 elimina."""
    return MatrizDecisao(
        alternativas=[
            "A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação",
            "A5 — Colina",
        ],
        criterios=CRITERIOS_ANCORA,
        desempenhos=[
            [450_000, 62, 15, 4],
            [380_000, 70, 35, 3],
            [520_000, 85, 25, 5],
            [340_000, 55, 20, 2],
            [470_000, 60, 18, 3],
        ],
    )


class CriterioIn(BaseModel):
    nome: str
    direcao: str
    unidade: str = ""


class MatrizIn(BaseModel):
    alternativas: list[str]
    criterios: list[CriterioIn]
    desempenhos: list[list[float]]
    pesos: list[float] | None = None


def _montar(entrada: MatrizIn) -> MatrizDecisao:
    try:
        return MatrizDecisao(
            alternativas=entrada.alternativas,
            criterios=[Criterio(c.nome, c.direcao, c.unidade) for c in entrada.criterios],
            desempenhos=entrada.desempenhos,
            pesos=entrada.pesos,
        )
    except ErroDeModelagem as erro:
        raise HTTPException(status_code=422, detail=str(erro)) from erro


@app.post("/api/matriz/dominancia")
def dominancia(entrada: MatrizIn) -> dict:
    """Dominadas (com suas dominadoras) e fronteira de Pareto do problema."""
    return analise_dominancia(_montar(entrada))


@app.get("/api/caso-ancora")
def api_caso_ancora() -> dict:
    matriz = caso_ancora_com_candidato()
    return {
        "titulo": "Escolha de apartamento (+ candidato A5)",
        "alternativas": matriz.alternativas,
        "criterios": [vars(c) for c in matriz.criterios],
        "desempenhos": matriz.desempenhos,
    }


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
