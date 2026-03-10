class DeleteUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id):
        self.user_repository.delete(user_id)
