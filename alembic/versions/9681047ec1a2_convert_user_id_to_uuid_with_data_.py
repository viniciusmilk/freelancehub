"""convert_user_id_to_uuid_with_data_migration

Revision ID: 9681047ec1a2
Revises: a1e1421b4214
Create Date: 2026-03-09 16:56:03.448732

"""
from typing import Sequence, Union
import uuid

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9681047ec1a2'
down_revision: Union[str, Sequence[str], None] = 'a1e1421b4214'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Para SQLite: adicionar coluna UUID temporária
    op.add_column('users', sa.Column('new_id', sa.String(length=36), nullable=True))
    
    # Gerar UUIDs para registros existentes
    connection = op.get_bind()
    
    # Buscar todos os usuários
    result = connection.execute(sa.text("SELECT id FROM users"))
    for row in result:
        old_id = row[0]
        new_uuid = str(uuid.uuid4())
        connection.execute(
            sa.text(f"UPDATE users SET new_id = '{new_uuid}' WHERE id = {old_id}")
        )
    
    # SQLite não suporta dropar colunas diretamente, então precisamos:
    # 1. Criar tabela nova
    op.create_table('users_new',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password_hash', sa.String(), nullable=False),
        sa.Column('role', sa.String(), nullable=False),
        sa.Column('oauth_provider', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # 2. Copiar dados
    connection.execute(sa.text("""
        INSERT INTO users_new (id, username, email, password_hash, role, oauth_provider, created_at, updated_at)
        SELECT new_id, username, email, password_hash, role, oauth_provider, created_at, updated_at
        FROM users
    """))
    
    # 3. Dropar tabela antiga e renomear a nova
    op.drop_table('users')
    op.rename_table('users_new', 'users')


def downgrade() -> None:
    """Downgrade schema."""
    # Adicionar coluna temporária integer
    op.add_column('users', sa.Column('new_id', sa.Integer(), nullable=True))
    
    # Gerar IDs sequenciais
    connection = op.get_bind()
    result = connection.execute(sa.text("SELECT id FROM users ORDER BY created_at"))
    
    for i, row in enumerate(result, 1):
        user_id = row[0]
        connection.execute(
            sa.text(f"UPDATE users SET new_id = {i} WHERE id = '{user_id}'")
        )
    
    # Criar tabela nova com ID integer
    op.create_table('users_new',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password_hash', sa.String(), nullable=False),
        sa.Column('role', sa.String(), nullable=False),
        sa.Column('oauth_provider', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Copiar dados
    connection.execute(sa.text("""
        INSERT INTO users_new (id, username, email, password_hash, role, oauth_provider, created_at, updated_at)
        SELECT new_id, username, email, password_hash, role, oauth_provider, created_at, updated_at
        FROM users
    """))
    
    # Dropar tabela antiga e renomear
    op.drop_table('users')
    op.rename_table('users_new', 'users')
