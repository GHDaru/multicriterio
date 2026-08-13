# Imagem do Decisor (backend FastAPI + frontend estático servido em /).
# Deploy: Railway (ADR 0010). O banco NÃO vive aqui — chega por DATABASE_URL
# (Princípio V: nenhuma credencial em arquivo ou imagem).

FROM python:3.12-slim

# Não gera .pyc e não bufferiza log (Railway lê stdout).
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Camada de dependências separada: só reinstala quando requirements muda.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# O app: motor puro + rotas + a página estática que main.py serve em "/".
COPY decisor/ ./decisor/
COPY static/ ./static/

# Usuário sem privilégios (a imagem não precisa escrever nada em produção;
# com DATABASE_URL definida, nem o SQLite de fallback é criado).
RUN useradd --create-home --uid 1000 decisor && chown -R decisor:decisor /app
USER decisor

EXPOSE 8000

# Railway injeta PORT; o default cobre `docker run -p 8000:8000` local.
CMD uvicorn decisor.main:app --host 0.0.0.0 --port ${PORT:-8000}
