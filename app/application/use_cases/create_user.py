from app.application.services.auth_service import get_password_hash
from app.domain.entities.users import User


class CreateUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_data):
        user_exists = self.user_repository.get_by_email(user_data.email)
        if user_exists:
            raise Exception('User with this email already exists')

        password_hash = get_password_hash(user_data.password)
        print(f'PASSWORD HASH: {password_hash}')

        user = User(
            id=None,  # Será gerado pelo banco
            username=user_data.username,
            email=user_data.email,
            password_hash=password_hash,
            role=user_data.role,
            oauth_provider=None,
            created_at=None,  # Será definido pelo banco
        )
        return self.user_repository.create(user)
