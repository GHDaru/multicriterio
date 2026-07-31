"""Etapa 14 — AEO: decidir só com ordens (contribuição original do livro).

Capítulo correspondente: livro/capitulos/14-simulacao-ordinal.md; artigo
completo em livro/apendice-c-artigo-aeo.md.

A dor que motiva: os caps. 03–05 exigem NÚMEROS (pesos, valores) que o decisor
muitas vezes não tem — o que ele tem são ORDENS ("neste critério, A vem antes
de B"; "preço importa mais que área"). A AEO simula infinitas funções de
importância compatíveis com essas ordens e entrega o dossiê probabilístico:
aceitabilidade por posição, posto esperado, duelos par a par, vencedor de
Condorcet estocástico e as "crenças" (pesos centrais) que elegem cada
alternativa.

Como rodar:
    uvicorn app:app --reload
    pytest
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.ordinal import ErroDeOrdinal, simular_aeo

app = FastAPI(title="decisor-zero — etapa 14")


class AeoIn(BaseModel):
    alternativas: list[str]
    rankings_criterios: list[list[str]]
    ordem_pesos: list[int] | None = None
    n_simulacoes: int = 10_000
    semente: int | None = None


@app.post("/api/aeo")
def aeo(entrada: AeoIn) -> dict:
    if not 100 <= entrada.n_simulacoes <= 200_000:
        raise HTTPException(422, "n_simulacoes deve estar entre 100 e 200000")
    try:
        return simular_aeo(
            entrada.alternativas, entrada.rankings_criterios,
            entrada.ordem_pesos, entrada.n_simulacoes, entrada.semente,
        )
    except ErroDeOrdinal as erro:
        raise HTTPException(422, str(erro)) from erro


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
