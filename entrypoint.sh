#!/bin/sh

set -e

# ============================================================================
# FreelanceHub API - Entrypoint Script
# ============================================================================
# Este script prepara e inicia a aplicação FastAPI com as seguintes etapas:
# 1. Aguarda a disponibilidade do banco de dados PostgreSQL
# 2. Executa as migrações Alembic
# 3. Inicia o servidor Uvicorn
# ============================================================================

# Configurações padrão
DB_HOST="${DB_HOST:-database}"
DB_PORT="${DB_PORT:-5432}"
DB_USER="${POSTGRES_USER:-app_user}"
DB_NAME="${POSTGRES_DB:-freelancehub_db}"

UVICORN_HOST="${UVICORN_HOST:-0.0.0.0}"
UVICORN_PORT="${UVICORN_PORT:-8000}"

# ============================================================================
# Função auxiliar para logging
# ============================================================================
log_info() {
    echo "ℹ️  INFO: $1"
}

log_success() {
    echo "✅ SUCCESS: $1"
}

log_error() {
    echo "❌ ERROR: $1" >&2
}

log_step() {
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🔄 $1"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# ============================================================================
# 1. Aguardar banco de dados PostgreSQL
# ============================================================================
log_step "Aguardando disponibilidade do PostgreSQL"
log_info "Conectando em $DB_HOST:$DB_PORT (banco: $DB_NAME, usuário: $DB_USER)"

MAX_ATTEMPTS=30
ATTEMPT=1

while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
    if nc -z "$DB_HOST" "$DB_PORT" 2>/dev/null; then
        log_success "PostgreSQL está pronto!"
        break
    fi
    
    if [ $ATTEMPT -eq $MAX_ATTEMPTS ]; then
        log_error "PostgreSQL não respondeu após $MAX_ATTEMPTS tentativas"
        exit 1
    fi
    
    log_info "Tentativa $ATTEMPT/$MAX_ATTEMPTS - aguardando $DB_HOST:$DB_PORT..."
    sleep 1
    ATTEMPT=$((ATTEMPT + 1))
done

# ============================================================================
# 2. Executar migrações Alembic
# ============================================================================
log_step "Executando migrações do banco de dados"

if ! poetry run alembic upgrade head; then
    log_error "Falha ao executar as migrações do Alembic"
    exit 1
fi

log_success "Migrações executadas com sucesso!"

# ============================================================================
# 3. Iniciar servidor Uvicorn
# ============================================================================
log_step "Iniciando servidor FastAPI"
log_info "Servidor em http://$UVICORN_HOST:$UVICORN_PORT"
log_info "Documentação em http://$UVICORN_HOST:$UVICORN_PORT/docs"

exec poetry run uvicorn app.main:app \
    --host "$UVICORN_HOST" \
    --port "$UVICORN_PORT" \
    --workers 1