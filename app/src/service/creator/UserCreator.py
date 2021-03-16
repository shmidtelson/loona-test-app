from src.models.Player import PlayerModel
from src.service.abstract import DBAbstract


class UserCreator(DBAbstract.DBAbstract):
    def create(self, username: str, password: str) -> UserModel:
        if username == '' or password == '':
            raise Exception('Username and password are empty')
        u = PlayerModel()
        u.login = username
        u.set_password(password)
        self.db.commit()
        self.db.flush()
        return u
