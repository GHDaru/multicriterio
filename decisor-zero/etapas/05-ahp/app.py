"""Etapa 05 — AHP: pesos que nascem de comparações par a par.

Capítulo correspondente: livro/capitulos/05-ahp.md.

A dor deixada pela etapa 04: o vencedor pertence ao vetor w — mas de onde vem
um w defensável quando o decisor não consegue dar notas? O AHP (Saaty)
responde com comparações par a par ("Preço é 2× mais importante que Área") e,
crucialmente, com um DETECTOR de julgamentos incoerentes: a razão de
consistência. Nesta etapa nasce motor/ahp.py; a API expõe /api/ahp/prioridades
e a página deixa editar os julgamentos e ver pesos + CR na hora.

Como rodar:
    uvicorn app:app --reload      # http://localhost:8000
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.ahp import ErroDeJulgamentos, prioridades_ahp

app = FastAPI(title="decisor-zero — etapa 05")

JULGAMENTOS_ANCORA = [
    [1, 2, 2, 3],
    [0.5, 1, 1, 2],
    [0.5, 1, 1, 2],
    [1 / 3, 0.5, 0.5, 1],
]
CRITERIOS = ["Preço", "Área", "Deslocamento", "Bairro"]


class JulgamentosIn(BaseModel):
    julgamentos: list[list[float]]


@app.post("/api/ahp/prioridades")
def prioridades(entrada: JulgamentosIn) -> dict:
    try:
        r = prioridades_ahp(entrada.julgamentos)
    except ErroDeJulgamentos as erro:
        raise HTTPException(422, str(erro)) from erro
    return {
        "pesos": [round(w, 6) for w in r["pesos"]],
        "lambda_max": round(r["lambda_max"], 6),
        "cr": None if r["cr"] is None else round(r["cr"], 6),
        "consistente": r["consistente"],
    }


@app.get("/api/caso-ancora")
def caso() -> dict:
    return {"criterios": CRITERIOS, "julgamentos": JULGAMENTOS_ANCORA}


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
