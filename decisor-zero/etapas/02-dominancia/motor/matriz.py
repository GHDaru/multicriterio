"""A matriz de decisão — agora com o gabarito do exercício do cap. 01 aplicado.

Diff em relação à etapa 01 (o diff é a lição): o validador de pesos passou a
rejeitar peso negativo. A checagem de soma (= 1) não bastava — pesos como
[0.7, 0.5, -0.1, -0.1] somam 1 e escapavam dela. A definição formal exige
w_j >= 0 (Hwang & Yoon, 1981, cap. 1).

Motor puro: sem FastAPI, sem I/O — testável sozinho (regra 2 do decisor-zero).
"""

from dataclasses import dataclass, field

DIRECOES = ("beneficio", "custo")


class ErroDeModelagem(ValueError):
    """A matriz viola a definição do cap. 01 — o erro diz qual regra quebrou."""


@dataclass(frozen=True)
class Criterio:
    nome: str
    direcao: str  # "beneficio" (maior é melhor) ou "custo" (menor é melhor)
    unidade: str = ""

    def __post_init__(self) -> None:
        if self.direcao not in DIRECOES:
            raise ErroDeModelagem(
                f"critério {self.nome!r}: direção {self.direcao!r} inválida "
                f"(use {DIRECOES})"
            )


@dataclass(frozen=True)
class MatrizDecisao:
    """m alternativas × n critérios, com desempenhos e (opcionalmente) pesos."""

    alternativas: list[str]
    criterios: list[Criterio]
    desempenhos: list[list[float]]  # X[i][j]: alternativa i no critério j
    pesos: list[float] | None = field(default=None)

    def __post_init__(self) -> None:
        m, n = len(self.alternativas), len(self.criterios)
        if m == 0 or n == 0:
            raise ErroDeModelagem("é preciso ao menos 1 alternativa e 1 critério")
        if len(self.desempenhos) != m:
            raise ErroDeModelagem(
                f"{m} alternativas, mas {len(self.desempenhos)} linhas de desempenho"
            )
        for i, linha in enumerate(self.desempenhos):
            if len(linha) != n:
                raise ErroDeModelagem(
                    f"linha {i} ({self.alternativas[i]!r}) tem {len(linha)} "
                    f"desempenhos para {n} critérios"
                )
        if self.pesos is not None:
            if len(self.pesos) != n:
                raise ErroDeModelagem(f"{n} critérios, mas {len(self.pesos)} pesos")
            if any(w < 0 for w in self.pesos):
                raise ErroDeModelagem("pesos não podem ser negativos (w_j >= 0)")
            if abs(sum(self.pesos) - 1.0) > 1e-9:
                raise ErroDeModelagem(
                    f"pesos devem somar 1 (somam {sum(self.pesos):.6f})"
                )

    def soma_crua(self) -> dict[str, float]:
        """A agregação ingênua do cap. 01 — mantida como memória do absurdo."""
        return {
            nome: float(sum(linha))
            for nome, linha in zip(self.alternativas, self.desempenhos)
        }

    def ranking_por(self, escores: dict[str, float]) -> list[str]:
        """Nomes das alternativas em ordem decrescente de escore."""
        return sorted(escores, key=escores.__getitem__, reverse=True)
