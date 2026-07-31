"""A persistência do capítulo 13, verificada (sempre contra SQLite temporário)."""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from repositorio import RepositorioDecisoes

PROBLEMA = {"alternativas": ["X", "Y"], "desempenhos": [[1, 2], [3, 4]]}


def _repo() -> RepositorioDecisoes:
    pasta = tempfile.mkdtemp(prefix="etapa13-")
    return RepositorioDecisoes(url=f"sqlite:///{pasta}/teste.db")


def test_salvar_e_buscar_sobrevive_a_nova_conexao():
    repo = _repo()
    novo_id = repo.salvar("Teste", PROBLEMA)
    # "Reiniciar o servidor": novo repositório apontando para o MESMO arquivo.
    repo2 = RepositorioDecisoes(url=str(repo.engine.url))
    registro = repo2.buscar(novo_id)
    assert registro is not None
    assert registro.problema == PROBLEMA


def test_listar_ordena_o_que_foi_salvo():
    repo = _repo()
    repo.salvar("Primeira", PROBLEMA)
    repo.salvar("Segunda", PROBLEMA)
    titulos = [d.titulo for d in repo.listar()]
    assert titulos == ["Primeira", "Segunda"]


def test_url_do_neon_e_adaptada_para_psycopg():
    # Sem conectar: só a tradução do dialeto (postgres:// → postgresql+psycopg://).
    import repositorio as modulo
    url = "postgres://u:s@ep-x.aws.neon.tech/db?sslmode=require"
    adaptada = url.replace("postgres://", "postgresql+psycopg://", 1)
    assert adaptada.startswith("postgresql+psycopg://")
    assert modulo.URL_PADRAO_LOCAL.startswith("sqlite")
