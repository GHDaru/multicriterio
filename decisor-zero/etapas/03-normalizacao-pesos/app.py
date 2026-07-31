"""Etapa 03 — normalização e pesos: os dois insumos que faltavam para agregar.

Capítulo correspondente: livro/capitulos/03-normalizacao-pesos.md.

A dor deixada pela etapa 02: a fronteira de Pareto do caso âncora tem quatro
alternativas em conflito — e a soma crua do cap. 01 provou que agregar escalas
brutas é absurdo. Nesta etapa nascem os dois insumos de qualquer método
compensatório: (1) motor/normalizacao.py — min-max (resolve direção, r em
[0,1]) e vetorial (preserva proporções, direção fica para o método); (2)
motor/pesos.py — rating direto, ROC, swing e entropia. Com r_ij e w_j nas
mãos, o cap. 04 finalmente agrega.

Como rodar:
    uvicorn app:app --reload      # http://localhost:8000
    pytest                        # os números do capítulo 03, verificados
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao
from motor.normalizacao import normalizar_minmax, normalizar_vetorial
from motor.pesos import (
    ErroDePesos,
    pesos_entropia,
    pesos_rating_direto,
    pesos_roc,
    pesos_swing,
)

app = FastAPI(title="decisor-zero — etapa 03")

NORMALIZACOES = {"minmax": normalizar_minmax, "vetorial": normalizar_vetorial}


def caso_ancora() -> MatrizDecisao:
    return MatrizDecisao(
        alternativas=["A1 — Centro", "A2 — Jardim", "A3 — Parque", "A4 — Estação"],
        criterios=[
            Criterio("Preço", "custo", "R$"),
            Criterio("Área", "beneficio", "m²"),
            Criterio("Deslocamento", "custo", "min"),
            Criterio("Bairro", "beneficio", "1–5"),
        ],
        desempenhos=[
            [450_000, 62, 15, 4],
            [380_000, 70, 35, 3],
            [520_000, 85, 25, 5],
            [340_000, 55, 20, 2],
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


class PesosIn(BaseModel):
    metodo: str  # rating | roc | swing | entropia
    valores: list[float] | None = None  # rating: pontos · swing: saltos
    ranking: list[int] | None = None    # roc: índices do mais ao menos importante
    matriz: MatrizIn | None = None      # entropia: o próprio problema


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


@app.post("/api/normalizar")
def normalizar(entrada: MatrizIn, metodo: str = "minmax") -> dict:
    if metodo not in NORMALIZACOES:
        raise HTTPException(422, f"normalização {metodo!r} desconhecida "
                                 f"(use {sorted(NORMALIZACOES)})")
    matriz = _montar(entrada)
    return {
        "metodo": metodo,
        "resolve_direcao": metodo == "minmax",
        "normalizada": NORMALIZACOES[metodo](matriz),
    }


@app.post("/api/pesos")
def elicitar_pesos(entrada: PesosIn) -> dict:
    try:
        if entrada.metodo == "rating":
            pesos = pesos_rating_direto(entrada.valores or [])
        elif entrada.metodo == "swing":
            pesos = pesos_swing(entrada.valores or [])
        elif entrada.metodo == "roc":
            pesos = pesos_roc(entrada.ranking or [])
        elif entrada.metodo == "entropia":
            if entrada.matriz is None:
                raise HTTPException(422, "entropia exige o campo 'matriz'")
            pesos = pesos_entropia(_montar(entrada.matriz))
        else:
            raise HTTPException(422, f"método {entrada.metodo!r} desconhecido "
                                     "(use rating, roc, swing ou entropia)")
    except ErroDePesos as erro:
        raise HTTPException(422, str(erro)) from erro
    return {"metodo": entrada.metodo, "pesos": [round(w, 6) for w in pesos]}


@app.get("/api/caso-ancora")
def api_caso_ancora() -> dict:
    matriz = caso_ancora()
    return {
        "titulo": "Escolha de apartamento",
        "alternativas": matriz.alternativas,
        "criterios": [vars(c) for c in matriz.criterios],
        "desempenhos": matriz.desempenhos,
    }


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
