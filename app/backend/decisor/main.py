"""Decisor — API do produto (v0).

Backend FastAPI; banco Postgres (Neon) via DATABASE_URL com fallback SQLite
(ver bd.py); motor MCDA puro em decisor/motor/. Método disponível no v0: SAW.
Os próximos entram um a um conforme os capítulos do livro ficam prontos
(constituição, Princípio II: nenhum método sem capítulo + teste).

Como rodar:
    cd app/backend
    uvicorn decisor.main:app --reload    # http://localhost:8000
"""

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlmodel import Session, select

from decisor.bd import criar_tabelas, get_sessao
from decisor.modelos import Decisao
from decisor.motor.comparar import comparar_metodos
from decisor.motor.dominancia import analise_dominancia
from decisor.motor.ahp import ErroDeJulgamentos, prioridades_ahp
from decisor.motor.pesos import (
    ErroDePesos,
    pesos_entropia,
    pesos_rating_direto,
    pesos_roc,
    pesos_swing,
)
from decisor.motor.promethee import ranquear_promethee2
from decisor.motor.saw import ranquear_saw
from decisor.motor.topsis import ranquear_topsis
from decisor.motor.vikor import ranquear_vikor
from decisor.motor.tipos import Problema

METODOS = {"saw": ranquear_saw, "topsis": ranquear_topsis,
           "promethee2": ranquear_promethee2, "vikor": ranquear_vikor}


@asynccontextmanager
async def ciclo_de_vida(_: FastAPI):
    criar_tabelas()
    yield


app = FastAPI(title="Decisor", version="0.1.0", lifespan=ciclo_de_vida)


class DecisaoIn(BaseModel):
    titulo: str
    problema: Problema


class DecisaoOut(BaseModel):
    id: int
    titulo: str
    problema: Problema


@app.post("/api/decisoes", response_model=DecisaoOut, status_code=201)
def criar_decisao(entrada: DecisaoIn, sessao: Session = Depends(get_sessao)):
    registro = Decisao(titulo=entrada.titulo, problema=entrada.problema.model_dump())
    sessao.add(registro)
    sessao.commit()
    sessao.refresh(registro)
    return DecisaoOut(id=registro.id, titulo=registro.titulo, problema=entrada.problema)


@app.get("/api/decisoes", response_model=list[DecisaoOut])
def listar_decisoes(sessao: Session = Depends(get_sessao)):
    registros = sessao.exec(select(Decisao)).all()
    return [
        DecisaoOut(id=r.id, titulo=r.titulo, problema=Problema(**r.problema))
        for r in registros
    ]


@app.get("/api/decisoes/{decisao_id}", response_model=DecisaoOut)
def obter_decisao(decisao_id: int, sessao: Session = Depends(get_sessao)):
    registro = sessao.get(Decisao, decisao_id)
    if registro is None:
        raise HTTPException(404, "decisão não encontrada")
    return DecisaoOut(
        id=registro.id, titulo=registro.titulo, problema=Problema(**registro.problema)
    )


@app.get("/api/metodos")
def listar_metodos() -> dict:
    return {
        "metodos": [
            {"id": "saw", "nome": "SAW — Simple Additive Weighting",
             "capitulo": "04", "exige_pesos": True},
            {"id": "topsis", "nome": "TOPSIS — proximidade ao ideal",
             "capitulo": "06", "exige_pesos": True},
            {"id": "promethee2", "nome": "PROMETHEE II — fluxos de sobreclassificação",
             "capitulo": "08", "exige_pesos": True},
            {"id": "vikor", "nome": "VIKOR — solução de compromisso (Q: menor é melhor)",
             "capitulo": "10", "exige_pesos": True},
        ]
    }


class RankingIn(BaseModel):
    pesos: list[float] | None = None  # sobrescreve os pesos salvos (cap. 04)


@app.post("/api/decisoes/{decisao_id}/ranking")
def ranquear(
    decisao_id: int,
    metodo: str = "saw",
    entrada: RankingIn | None = None,
    sessao: Session = Depends(get_sessao),
) -> dict:
    registro = sessao.get(Decisao, decisao_id)
    if registro is None:
        raise HTTPException(404, "decisão não encontrada")
    if metodo not in METODOS:
        raise HTTPException(422, f"método {metodo!r} indisponível (ver /api/metodos)")
    dados = dict(registro.problema)
    if entrada is not None and entrada.pesos is not None:
        dados["pesos"] = entrada.pesos  # revalidado pelo Problema abaixo
    try:
        problema = Problema(**dados)
    except ValueError as erro:
        raise HTTPException(422, str(erro)) from erro
    try:
        ranking = METODOS[metodo](problema)
    except ValueError as erro:
        raise HTTPException(422, str(erro)) from erro
    return {"decisao": registro.titulo, "metodo": metodo, "ranking": ranking}


class PesosIn(BaseModel):
    metodo: str  # rating | roc | swing | entropia
    valores: list[float] | None = None  # rating: pontos · swing: saltos
    ranking: list[int] | None = None    # roc: índices, do mais ao menos importante
    problema: Problema | None = None    # entropia: o próprio problema
    julgamentos: list[list[float]] | None = None  # ahp: comparações par a par


@app.post("/api/pesos")
def elicitar_pesos(entrada: PesosIn) -> dict:
    """Elicitação de pesos (cap. 03) — stateless, não exige decisão salva."""
    try:
        if entrada.metodo == "rating":
            pesos = pesos_rating_direto(entrada.valores or [])
        elif entrada.metodo == "swing":
            pesos = pesos_swing(entrada.valores or [])
        elif entrada.metodo == "roc":
            pesos = pesos_roc(entrada.ranking or [])
        elif entrada.metodo == "ahp":
            if entrada.julgamentos is None:
                raise HTTPException(422, "ahp exige o campo 'julgamentos'")
            resultado = prioridades_ahp(entrada.julgamentos)
            if not resultado["consistente"]:
                raise HTTPException(
                    422,
                    f"julgamentos inconsistentes (CR={resultado['cr']:.3f} > 0.10) — "
                    "revise antes de usar (cap. 05)",
                )
            pesos = resultado["pesos"]
        elif entrada.metodo == "entropia":
            if entrada.problema is None:
                raise HTTPException(422, "entropia exige o campo 'problema'")
            pesos = pesos_entropia(entrada.problema)
        else:
            raise HTTPException(422, f"método {entrada.metodo!r} desconhecido "
                                     "(use rating, roc, swing, entropia ou ahp)")
    except (ErroDePesos, ErroDeJulgamentos) as erro:
        raise HTTPException(422, str(erro)) from erro
    return {"metodo": entrada.metodo, "pesos": [round(w, 6) for w in pesos]}


@app.post("/api/decisoes/{decisao_id}/comparar")
def comparar(decisao_id: int, sessao: Session = Depends(get_sessao)) -> dict:
    """Rankings pelos 4 métodos + correlação de Spearman (cap. 11)."""
    registro = sessao.get(Decisao, decisao_id)
    if registro is None:
        raise HTTPException(404, "decisão não encontrada")
    problema = Problema(**registro.problema)
    if problema.pesos is None:
        raise HTTPException(422, "a comparação exige pesos (ver cap. 03)")
    return {"decisao": registro.titulo, **comparar_metodos(problema)}


@app.post("/api/decisoes/{decisao_id}/dominancia")
def dominancia(decisao_id: int, sessao: Session = Depends(get_sessao)) -> dict:
    """Dominadas e fronteira de Pareto — a analise sem pesos do cap. 02."""
    registro = sessao.get(Decisao, decisao_id)
    if registro is None:
        raise HTTPException(404, "decisão não encontrada")
    resultado = analise_dominancia(Problema(**registro.problema))
    return {"decisao": registro.titulo, **resultado}


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).resolve().parents[1] / "static" / "index.html").read_text(
        encoding="utf-8"
    )
