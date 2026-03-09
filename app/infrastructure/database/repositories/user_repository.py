from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.entities.users import User
from app.infrastructure.database.models import UserModel


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User):
        user_model = UserModel(
            username=user.username,
            email=user.email,
            password_hash=user.password_hash,
            role=user.role,
            oauth_provider=user.oauth_provider,
        )
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)

        # Converter para entidade User
        return User(
            id=user_model.id,
            username=user_model.username,
            email=user_model.email,
            password_hash=user_model.password_hash,
            role=user_model.role,
            oauth_provider=user_model.oauth_provider,
            created_at=user_model.created_at,
        )

    def get_by_email(self, email: str):
        stmt = select(UserModel).where(UserModel.email == email)
        result = self.session.execute(stmt)

        model = result.scalars().one_or_none()
        if not model:
            return None

        return User(
            id=model.id,
            username=model.username,
            email=model.email,
            password_hash=model.password_hash,
            role=model.role,
            oauth_provider=model.oauth_provider,
            created_at=model.created_at,
        )

    def get_all(self):
        stmt = select(UserModel)
        result = self.session.execute(stmt)
        models = result.scalars().all()
        return [
            User(
                id=model.id,
                username=model.username,
                email=model.email,
                password_hash=model.password_hash,
                role=model.role,
                oauth_provider=model.oauth_provider,
                created_at=model.created_at,
            )
            for model in models
        ]
