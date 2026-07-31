"""Repositório de decisões — Postgres (Neon) atrás de uma porta, SQLite no bolso.

Cap. 13. A regra anti-apodrecimento da constituição ("Restrições" §4) em
miniatura: o resto do app só conhece esta classe; trocar Neon por SQLite (ou
qualquer Postgres) é trocar UMA variável de ambiente. Princípio V: a connection
string vem SÓ de DATABASE_URL (.env gitignored) — nunca do código.
"""

import os
from datetime import datetime, timezone

from sqlmodel import Column, Field, JSON, Session, SQLModel, create_engine, select

URL_PADRAO_LOCAL = "sqlite:///decisor-etapa13.db"


class DecisaoSalva(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    problema: dict = Field(sa_column=Column(JSON, nullable=False))
    criada_em: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )


class RepositorioDecisoes:
    """Porta única de persistência: salvar, listar, buscar."""

    def __init__(self, url: str | None = None):
        url = url or os.environ.get("DATABASE_URL", URL_PADRAO_LOCAL)
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+psycopg://", 1)
        elif url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+psycopg://", 1)
        argumentos = {"connect_args": {"check_same_thread": False}} if url.startswith("sqlite") else {}
        self.engine = create_engine(url, **argumentos)
        SQLModel.metadata.create_all(self.engine)

    def salvar(self, titulo: str, problema: dict) -> int:
        with Session(self.engine) as sessao:
            registro = DecisaoSalva(titulo=titulo, problema=problema)
            sessao.add(registro)
            sessao.commit()
            sessao.refresh(registro)
            return registro.id

    def listar(self) -> list[DecisaoSalva]:
        with Session(self.engine) as sessao:
            return list(sessao.exec(select(DecisaoSalva)))

    def buscar(self, decisao_id: int) -> DecisaoSalva | None:
        with Session(self.engine) as sessao:
            return sessao.get(DecisaoSalva, decisao_id)
