class UpdateUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id, user_data: dict):
        user_exists = self.user_repository.get_by_id(user_id)
        if not user_exists:
            raise Exception('User not found')

        for key, value in user_data.items():
            if hasattr(user_exists, key):
                setattr(user_exists, key, value)

        return self.user_repository.update(user_exists)
