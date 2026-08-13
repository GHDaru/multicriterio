# Spec 039 — Colocar o produto no ar (Railway + Neon)

- **Status**: Preparada (aguarda os passos humanos de conta/segredo) · **Raia**:
  **Infra** · **Data**: 2026-08-13 · **ADR**: 0010
- **O quê**: tornar o Decisor (`app/backend`) publicamente executável — backend
  FastAPI e o frontend estático no mesmo serviço do Railway, banco no Neon via
  `DATABASE_URL`. Entregues nesta rodada: `Dockerfile`, `.dockerignore`,
  `railway.json` (builder Dockerfile + healthcheck `/health` + restart on-failure),
  runbook `app/DEPLOY.md` e ADR 0010.
- **Esclarecimento de escopo**: o **livro** não entra — é estático e já está no ar
  (GitHub Pages, ADR 0004). Só o produto sobe.
- **Constitution Check**: I ✅ · II ✅ (nenhum método novo; motor intocado) · III ✅ ·
  IV ✅ (edição 0.39) · **V ✅ crítico**: nenhuma credencial em arquivo, commit ou
  imagem; `.dockerignore` exclui `.env` e `*.db`; a connection string vive só no Neon
  e na variável do Railway; `/health` reporta o *tipo* de banco, nunca a URL ·
  VI ✅ (a trilha continua rodando a custo zero; free tier dos dois serviços) ·
  **VII ✅ raia infra**: gates de reversibilidade documentados no runbook —
  **backup/dry-run** por branch do Neon antes de mudança de esquema, **rollback** por
  redeploy do deploy anterior no Railway, e o dado sobrevive à remoção do serviço ·
  VIII n/a (não é capítulo de método).
- **Verificação feita nesta máquina** (o que dá para provar sem as contas):
  - `pytest` do produto: `22 passed`.
  - App de pé e respondendo: `/health` → `{"status":"ok","banco":"sqlite",…}`,
    `/` → 200, `/api/metodos` → os 4 métodos.
  - **Simulação da imagem**: diretório contendo *apenas* `decisor/` + `static/` +
    `requirements.txt` (exatamente o que o Dockerfile copia) sobe e responde — prova
    de que o conjunto de COPY é suficiente e que o caminho do HTML resolve.
  - `docker build` **não** executado: o sandbox tem CLI mas não tem daemon. O
    primeiro build real acontece no Railway — declarado, não escondido.
- **Passos humanos (não versionáveis)**: criar projeto no Neon, copiar a connection
  string, criar o serviço no Railway com Root Directory `app/backend`, definir
  `DATABASE_URL`, gerar domínio. Runbook: `app/DEPLOY.md`.
- **DoD**: [x] artefatos de deploy · [x] runbook com rollback e dry-run · [x] ADR
  0010 · [x] testes + build do livro verdes · [ ] deploy executado pelo Steward ·
  [ ] `/health` respondendo `banco: postgres` em produção · [ ] gate do autor.
