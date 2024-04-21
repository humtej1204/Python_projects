from src.infrastructure.repository.user_repository import UserRepository

class AppContext():
    def __init__(self, db):
        self._user_repository = UserRepository(db)
        
    @property
    def user_repository(self):
        return self._user_repository