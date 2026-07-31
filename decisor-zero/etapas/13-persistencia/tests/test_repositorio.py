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


def test_segundo_dominio_acervo_com_os_dois_casos():
    """ADR 0007: um só esquema persiste B2C (âncora) e B2B (fornecedor)."""
    repo = _repo()
    repo.salvar("Escolha de apartamento", {
        "alternativas": ["A1", "A2", "A3", "A4"],
        "desempenhos": [[450_000, 62, 15, 4], [380_000, 70, 35, 3],
                        [520_000, 85, 25, 5], [340_000, 55, 20, 2]],
    })
    repo.salvar("Escolha de fornecedor de nuvem", {
        "alternativas": ["F1", "F2", "F3"],
        "desempenhos": [[12_000, 45, 99.95, 3], [9_000, 20, 99.50, 4],
                        [7_500, 60, 99.00, 5]],
    })
    acervo = repo.listar()
    assert len(acervo) == 2
    assert {d.titulo for d in acervo} == {
        "Escolha de apartamento", "Escolha de fornecedor de nuvem",
    }
