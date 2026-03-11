from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from ....core.config import settings

engine = create_engine(settings.database_url, echo=True)

SessionLocal = sessionmaker(engine, class_=Session, expire_on_commit=False)
