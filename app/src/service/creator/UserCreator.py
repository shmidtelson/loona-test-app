from src.models.User import UserModel


class UserCreator(DBAbstarct):
    def create(self, username: str, password: str) -> UserModel:
        u = UserModel()
        u.login = username
        u.set_password(password)

        return u