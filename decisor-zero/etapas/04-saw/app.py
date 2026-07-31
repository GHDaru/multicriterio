"""Etapa 04 — SAW: o primeiro ranking completo do livro.

Capítulo correspondente: livro/capitulos/04-saw.md.

A dor deixada pela etapa 03: temos matriz validada, fronteira de Pareto,
normalização e quatro jeitos de obter pesos — mas ainda nenhum ranking. Nesta
etapa nasce motor/saw.py, a agregação aditiva que junta tudo: escore_i =
Σ_j w_j · r_ij sobre a matriz min-max. E a página entrega a lição central do
capítulo: o MESMO problema com pesos de rating direto elege A1; com pesos ROC
elege A4. O método é o mesmo — quem decide é o vetor w.

Como rodar:
    uvicorn app:app --reload      # http://localhost:8000
    pytest                        # os números do capítulo 04 + validação pymcdm
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from motor.matriz import Criterio, ErroDeModelagem, MatrizDecisao
from motor.pesos import pesos_roc
from motor.saw import ranquear_saw

app = FastAPI(title="decisor-zero — etapa 04")

PESOS_RATING = [0.35, 0.25, 0.25, 0.15]  # cap. 03: rating direto 35/25/25/15


def caso_ancora(pesos: list[float] | None = None) -> MatrizDecisao:
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
        pesos=pesos or PESOS_RATING,
    )


class CriterioIn(BaseModel):
    nome: str
    direcao: str
    unidade: str = ""


class MatrizIn(BaseModel):
    alternativas: list[str]
    criterios: list[CriterioIn]
    desempenhos: list[list[float]]
    pesos: list[float]  # SAW exige pesos — aqui o campo é obrigatório


@app.post("/api/matriz/saw")
def saw(entrada: MatrizIn) -> dict:
    try:
        matriz = MatrizDecisao(
            alternativas=entrada.alternativas,
            criterios=[Criterio(c.nome, c.direcao, c.unidade) for c in entrada.criterios],
            desempenhos=entrada.desempenhos,
            pesos=entrada.pesos,
        )
    except ErroDeModelagem as erro:
        raise HTTPException(422, str(erro)) from erro
    return {"metodo": "saw", "pesos": entrada.pesos, "ranking": ranquear_saw(matriz)}


@app.get("/api/caso-ancora")
def api_caso_ancora() -> dict:
    matriz = caso_ancora()
    return {
        "titulo": "Escolha de apartamento",
        "alternativas": matriz.alternativas,
        "criterios": [vars(c) for c in matriz.criterios],
        "desempenhos": matriz.desempenhos,
        "pesos_rating": PESOS_RATING,
        # Sem arredondar: com 6 casas a soma vira 0,999999 e o validador (Σw=1)
        # rejeita — a exibição arredonda, o dado não.
        "pesos_roc": pesos_roc([0, 1, 2, 3]),
    }


@app.get("/", response_class=HTMLResponse)
def pagina() -> str:
    return (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
