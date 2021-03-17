from src.models import UserModel
from src.service.abstract.DBAbstract import DBAbstract


class UserRepository(DBAbstract):
    def get_by_login(self, login: str) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.login == login).first()
