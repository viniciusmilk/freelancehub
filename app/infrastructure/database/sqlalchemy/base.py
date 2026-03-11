from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

# Define uma convenção de nomenclatura para as restrições do banco de dados
# Isso evita o erro "ValueError: Constraint must have a name" no SQLite
naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}


class Base(DeclarativeBase):
    """
    Base para todos os modelos do SQLAlchemy 2.0.
    Utilize uma MetaData com convenção de gnomes para garantir consistência
    entre SQLite e PostgreSQL.
    """

    metadata = MetaData(naming_convention=naming_convention)
