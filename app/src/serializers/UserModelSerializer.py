import json

from src.models import UserModel


class UserModelSerializer:
    def __init__(self, user: UserModel):
        self.id = str(user.id)
        self.login = user.login

    def serialize(self):
        return self.__dict__
