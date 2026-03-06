# docker/Dockerfile
FROM python:3.12-slim as base

# Instala dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential libpq-dev netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos
COPY pyproject.toml poetry.lock ./

# Instala dependências do projeto (sem criar virtualenv)
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main --no-root


# Copia o restante do código da aplicação
COPY . .

# Permite execução do entrypoint
RUN chmod +x entrypoint.sh \
    && adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app

USER appuser

# Expõe a porta da aplicação
EXPOSE 8000

# Define o comando de entrada
ENTRYPOINT ["./entrypoint.sh"]