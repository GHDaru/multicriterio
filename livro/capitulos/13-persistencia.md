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

## Segundo domínio — o acervo de decisões

O fecho dos dois fios do livro: as decisões do apartamento **e** do fornecedor
convivem no mesmo repositório — o modelo v0 (problema em JSON validado) não precisou
saber que uma é B2C com 4 alternativas e a outra B2B com 3. É a recompensa da anatomia
única do cap. 01: um só esquema persiste qualquer problema multicritério bem modelado.
E é também o embrião do **acervo**: com as decisões guardadas, os caps. 11–12 ganham
matéria-prima histórica (comparar decisões, reusar pesos elicitados, auditar escolhas
passadas). *Teste `test_segundo_dominio_acervo_com_os_dois_casos` da etapa 13.*

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

## Apêndice B — gabarito comentado da Verificação

1. Porque teste que lê `DATABASE_URL` herda o ambiente de quem o roda — e um dia esse
   ambiente será a produção. URL explícita de SQLite temporário torna impossível, por
   construção, um teste tocar banco real (Princípio V aplicado à suíte).
2. O motor deixaria de ser puro: importar o repositório arrasta engine, driver e
   ambiente para dentro do cálculo — os testes de método passariam a exigir banco, a
   validação cruzada com pymcdm ficaria lenta e frágil, e trocar de banco passaria a
   "tocar o motor". A seta de dependência é rotas → motor e rotas → repositório; nunca
   motor → repositório.
3. Primeiro **revogar** a credencial no Neon (a chave vazada já é pública — cada
   minuto conta); só depois limpar o histórico do git (rebase/filtro) e trocar o
   `.env`. A ordem inversa deixa uma chave válida exposta enquanto você reescreve
   commits.
