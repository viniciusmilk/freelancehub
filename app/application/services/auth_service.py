from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from fastapi.security import OAuth2PasswordBearer
from jwt import encode
from pwdlib import PasswordHash

from app.core.config import Settings

pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
settings = Settings()


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

