# 13 — Do protótipo ao produto: Neon, deploy e o fim da trilha

> **Estado da arte capturado em 2026-07** · última revisão 2026-07-31 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Implementar** persistência atrás de uma porta única (repositório), com Postgres
   serverless (Neon) em produção e SQLite local a custo zero.
2. **Aplicar** as práticas de credencial do Princípio V: `DATABASE_URL` em `.env`
   gitignored, `sslmode=require`, nada de segredo em código ou commit.
3. **Operar** o Decisor: subir com uvicorn, sonda `/health`, e o caminho de evolução
   (migrações, contas, deploy).

## O problema

Doze etapas de métodos — e toda decisão morria no reload do servidor. Um apoio à
decisão de verdade precisa lembrar: a decisão de ontem, os pesos acordados com o
comitê, o histórico que justifica a escolha perante quem auditar. Persistir é fácil;
persistir **sem acoplar o motor ao banco e sem vazar credenciais** é engenharia.

## Fundamentos

Três regras deste projeto, agora explicadas de frente:

- **Porta única** (constituição, "Restrições" §4): todo acesso a banco passa por um
  repositório; motor e rotas não conhecem SQL nem driver. Trocar de banco = trocar uma
  variável de ambiente. É a versão mínima da arquitetura hexagonal que o
  harness_engineering (nosso repositório-modelo) pratica.
- **Serverless com fallback**: o [Neon](https://neon.tech) oferece Postgres serverless
  com free tier — ideal para um produto didático. A connection string
  (`postgres://usuario:senha@ep-…aws.neon.tech/db?sslmode=require`) chega **só** por
  `DATABASE_URL`; sem a variável, o app cai em SQLite local — a trilha inteira roda a
  custo zero (Princípio VI), e os testes **nunca** tocam banco real.
- **Credencial é material radioativo** (Princípio V): `.env` gitignored,
  `.env.example` sem valores, `sslmode=require` sempre, e chave exposta = chave
  revogada — não "removida do histórico".

(Bibliografia completa e status de validação: `livro/bibliografia.md`; docs do Neon no
Apêndice A.)

## O método passo a passo

**Passo 1 — a porta.** `RepositorioDecisoes` (etapa 13) encapsula engine, criação de
tabelas e as três operações (salvar, listar, buscar). A URL `postgres://` do Neon é
adaptada para o driver (`postgresql+psycopg://`) dentro da porta — o resto do app nem
sabe que isso existe.

**Passo 2 — provisionar o Neon** (única parte com cliques): criar projeto no
console → copiar a connection string → `cp .env.example .env` → colar. Nada disso toca
o repositório git.

**Passo 3 — a prova de sobrevivência.** Salve uma decisão, derrube o processo, suba de
novo: ela continua lá. *É literalmente o teste
`test_salvar_e_buscar_sobrevive_a_nova_conexao` da etapa 13 — a "reinicialização" é um
segundo repositório apontando para o mesmo arquivo.*

**Passo 4 — operar.** `uvicorn decisor.main:app` sobe o produto; `GET /health` responde
status, banco em uso e versão — a sonda mínima para qualquer orquestrador. O produto
completo (`app/`) já nasceu com esta arquitetura na fundação; a etapa 13 a reconstrói
em miniatura para o leitor ver o mecanismo isolado.

## Quando usar (e quando não)

Esta arquitetura (porta + serverless + fallback) cobre o Decisor até longe: milhares de
decisões, um usuário por vez. Os degraus seguintes — cada um uma spec de **raia infra**
com backup, dry-run e rollback (constituição, Princípio VII): **migrações** com Alembic
quando o modelo relacional evoluir (hoje o problema vive em JSON validado — decisão
registrada no modelo v0); **contas de usuário** (que destravam a decisão em grupo do
cap. 12 no produto); **deploy gerenciado** (qualquer host que rode uvicorn e injete
`DATABASE_URL` serve — o app não sabe onde está).

### Leitura executiva

O fim da trilha é o começo do produto: os motores dos caps. 01–12 são funções puras
que não sabem que existe banco, e o banco fica atrás de uma variável de ambiente. Essa
indiferença mútua é o que permite ao Decisor trocar Neon por qualquer Postgres — ou
por nada — sem tocar uma linha de método. **O que levar** hoje: motor puro + porta de
persistência + credencial só em ambiente; se o seu apoio à decisão não sobrevive a um
reload ou vaza uma connection string, o problema não é MCDA.

## Mão na massa — decisor-zero, etapa 13

Em `decisor-zero/etapas/13-persistencia/`, nascem `repositorio.py` (a porta, com
adaptação da URL do Neon) e o mini-app com `/health`, salvar e listar — mais
`.env.example` no padrão do produto. O produto ganhou `GET /health`. Exercício de
completar: adicione `apagar(decisao_id)` ao repositório com **soft-delete** (coluna
`apagada_em`, filtro no listar) e o teste que prova que apagar é reversível — a regra
de reversibilidade do Maestro aplicada a você mesmo.

## Verificação

1. Por que os testes da etapa criam o repositório com URL explícita de SQLite
   temporário em vez de ler `DATABASE_URL`? (Dica: objetivo 2 — o que jamais pode
   acontecer num teste.)
2. O que quebraria se o motor SAW importasse o repositório? (Dica: objetivo 1 —
   pureza e testabilidade.)
3. Sua connection string do Neon vazou num commit. Quais são os dois passos, e em que
   ordem? (Dica: objetivo 2 — revogar vem antes de reescrever histórico.)

---

## Apêndice A — persistência e operação nas ferramentas

- **Neon** — connection strings, `sslmode` e free tier:
  <https://neon.tech/docs/connect/connect-from-any-app>.
- **SQLModel** (FastAPI + SQLAlchemy + Pydantic): <https://sqlmodel.tiangolo.com/>.
- **Alembic** para as futuras migrações (raia infra):
  <https://alembic.sqlalchemy.org/>.
- O workflow de CI deste repositório roda toda a trilha e o produto a cada push — a
  operação do livro vivo é, ela mesma, o exemplo final.
