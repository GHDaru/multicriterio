# ADR 0010 — Deploy do produto: Railway (backend + front) e Neon (banco)

- **Status**: Aceito · **Data**: 2026-08-13 · **Spec**: 039 (raia infra) ·
  **Direção**: Steward ("vamos colocar no ar; back no Railway, front no Vercel ou
  no Railway").

## Contexto

O livro já está publicado (GitHub Pages, ADR 0004) e é estático — não tem backend,
frontend nem banco. O que falta subir é o **produto** (`app/backend`): API FastAPI,
motor MCDA puro, persistência atrás de uma porta única (cap. 13) e um frontend que
hoje é **um arquivo** de 98 linhas de HTML+JS sem etapa de build, servido pela própria
API na rota `/`.

O Steward deixou a escolha do front em aberto (Vercel ou Railway).

## Decisão

1. **Backend e frontend no mesmo serviço do Railway**, construído pelo
   `app/backend/Dockerfile` (builder explícito, sem detecção automática de
   linguagem), com healthcheck em `/health` e política de restart on-failure
   (`app/backend/railway.json`). Root Directory do serviço: `app/backend`.
2. **Banco no Neon**, injetado por `DATABASE_URL`. Nenhuma credencial em arquivo,
   commit ou imagem (Princípio V); o `.dockerignore` exclui `.env` e `*.db`.
3. **Vercel adiado**, com critério de reversão escrito no runbook: separar o front
   passa a valer quando ele ganhar build, virar multipágina ou o tráfego de leitura
   justificar CDN.
4. **Runbook** em `app/DEPLOY.md`, com verificação obrigatória pós-deploy
   (`/health` precisa responder `banco: postgres`), rollback por redeploy do
   Railway, e dry-run de esquema por *branch* do Neon.

## Alternativas avaliadas

- **Front no Vercel agora** — rejeitada *por ora*: para um único HTML estático sem
  build, o ganho é CDN; o custo é CORS no FastAPI, duas URLs, uma variável de
  ambiente no front e dois pipelines de deploy. Complexidade sem contrapartida
  enquanto o front couber num arquivo. Registrado o gatilho de revisão (item 3).
- **Nixpacks / autodetecção do Railway** — rejeitada: o repositório é um monorepo
  (livro + trilha + produto) e a autodetecção fica ambígua; Dockerfile explícito
  torna o build reprodutível e legível para quem estuda o repositório.
- **Render / Fly.io / Cloud Run** — equivalentes tecnicamente; a escolha do Railway
  veio da direção do Steward. Nada no app depende do provedor: o único acoplamento é
  "um processo que escuta em `$PORT` e recebe `DATABASE_URL`", que é justamente o que
  o cap. 13 defende.
- **Banco no próprio Railway (plugin Postgres)** — rejeitada: o livro inteiro
  documenta o Neon (cap. 13, `.env.example`, ADR 0002), e o free tier serverless
  atende. Trocar seria contrariar o material didático sem ganho.

## Consequências

- Positivas: um deploy, uma URL, zero CORS; o produto passa a existir fora da
  máquina de quem estuda; a arquitetura "motor puro + porta de persistência" do
  cap. 13 é exercitada em produção, não só em teste.
- Custos aceitos: o front perde CDN (irrelevante nesta escala) e a imagem carrega
  Python inteiro para servir um HTML (também irrelevante).
- **Riscos declarados no runbook**: sem migrações (o start faz `create_all`, que não
  altera tabela existente — Alembic é o degrau seguinte), sem autenticação no v0
  (quem tem a URL escreve), e dependências sem pin.
- O deploy em si depende de contas e segredos do Steward: o repositório entrega
  tudo o que é versionável (Dockerfile, railway.json, runbook); a criação do projeto
  e a variável `DATABASE_URL` são passos humanos, por definição.

## Fontes

- Cap. 13 do livro (porta de persistência, `/health`, degraus de infra).
- Verificação local desta rodada: app de pé com o conjunto de arquivos exato que o
  Dockerfile copia (`decisor/` + `static/`), `/health` e `/` respondendo.
