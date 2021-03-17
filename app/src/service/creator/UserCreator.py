from src.models.User import UserModel
from src.service.abstract import DBAbstract


class UserCreator(DBAbstract.DBAbstract):
    def create(self, username: str, password: str) -> UserModel:
        if username == '' or password == '':
            raise Exception('Username and password are empty')
        u = UserModel()
        u.login = username
        u.set_password(password)
        self.db.add_model(u, need_flush=True)
        return u
