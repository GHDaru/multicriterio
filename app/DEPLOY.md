# Deploy do Decisor — Railway + Neon

> Runbook operacional (ADR 0010, spec 039). O **livro** não entra aqui: ele é
> estático e já vive no GitHub Pages. Isto sobe o **produto** (`app/backend`):
> API FastAPI + a página estática que ela serve em `/`.
>
> **Princípio V**: a connection string nunca entra em arquivo, commit, print ou
> mensagem. Ela existe em dois lugares e só neles: no painel do Neon e na variável
> de ambiente do Railway.

## O que sobe

| Peça | Onde | Como |
|---|---|---|
| Backend (FastAPI) | Railway | `app/backend/Dockerfile` |
| Frontend (`static/index.html`) | Railway, no mesmo serviço | servido pela rota `/` |
| Banco (Postgres) | Neon | injetado por `DATABASE_URL` |

Sem `DATABASE_URL`, o app cai em SQLite local — ótimo para desenvolvimento, **errado
em produção**: o disco do contêiner é efêmero e a decisão salva some no próximo
deploy. Por isso o passo 1 vem antes do passo 2.

## 1. Banco (Neon)

1. <https://neon.tech> → novo projeto (região mais perto do Railway que você
   escolher — hoje o app faz poucas consultas, mas latência de banco é o custo fixo
   de toda requisição).
2. **Connect** → copie a connection string (`postgresql://…?sslmode=require`).
3. Não cole em lugar nenhum ainda. Ela vai direto no passo 2.4.

## 2. Backend + frontend (Railway)

1. <https://railway.app> → **New Project** → *Deploy from GitHub repo* →
   `GHDaru/multicriterio`.
2. Em **Settings → Root Directory**, defina `app/backend`. É o que faz o Railway
   enxergar o `railway.json` e o `Dockerfile` (o repositório é um monorepo: livro,
   trilha e produto convivem).
3. O build é por Dockerfile — sem detecção mágica de linguagem. O healthcheck já vem
   configurado para `/health`.
4. **Variables** → `DATABASE_URL` = a string do passo 1.2. É a única variável
   obrigatória. (`PORT` o Railway injeta sozinho; o Dockerfile a respeita.)
5. **Settings → Networking → Generate Domain** para ter a URL pública.

## 3. Verificação (não pule)

```bash
curl https://SEU-APP.up.railway.app/health
```

Deve responder `{"status":"ok","banco":"postgres","versao":"0.1.0"}`.

**Se vier `"banco":"sqlite"`, pare**: a `DATABASE_URL` não chegou ao processo. O app
está de pé, mas gravando em disco efêmero. Confira a variável e refaça o deploy.

Depois: abra a URL raiz (a página do Decisor deve carregar), crie uma decisão,
**force um redeploy** e confira que ela continua lá. É o teste de sobrevivência do
cap. 13 rodando em produção de verdade.

## 4. Rollback

- **Aplicação**: Railway → *Deployments* → escolha o deploy anterior → **Redeploy**.
  O Railway mantém as imagens; a volta é de um clique e não depende de rebuild.
- **Banco**: o Neon tem *branching* e restauração por ponto no tempo. Antes de
  qualquer mudança de esquema, crie uma **branch** do banco e aponte um deploy de
  teste para ela — é o dry-run barato.
- **Desligar**: remover o serviço no Railway não toca o Neon. Os dados sobrevivem ao
  app.

## 5. Limites conhecidos (honestidade operacional)

- **Não há migrações.** O app chama `criar_tabelas()` no start (SQLModel
  `create_all`): cria o que falta, mas **não altera** tabela existente. Enquanto o
  problema vive em JSON validado isso basta; no dia em que o modelo relacional
  evoluir, entra Alembic — é o degrau registrado no cap. 13 e continua sendo uma
  spec de raia infra própria.
- **Sem autenticação.** O v0 não tem contas: quem tem a URL lê e escreve as decisões.
  Para uso além de demonstração, contas de usuário vêm antes de divulgar o link.
- **Dependências sem pin.** `requirements.txt` usa `>=`; dois builds em datas
  diferentes podem trazer versões diferentes. Para deploy reprodutível, congelar as
  versões é a próxima melhoria.

## 6. Quando mover o frontend para o Vercel

Hoje não compensa (ADR 0010): o front é um arquivo estático servido pela própria API,
sem build, sem CORS, com uma URL só. A conta vira quando **qualquer** destes for
verdade: o front ganhar etapa de build (React/Vite), passar a ter várias páginas ou
rotas próprias, ou o tráfego de leitura justificar CDN. Aí o caminho é: publicar
`static/` (ou o `dist/`) no Vercel, configurar `CORS` no FastAPI para o domínio do
front, e apontar a base da API por variável de ambiente do front.
