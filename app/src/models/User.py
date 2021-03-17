from sqlalchemy import Column, String

from src.models.Base.BaseModel import BaseModel
from src.utils import Security


class UserModel(BaseModel):
    __tablename__ = 'user'

    login = Column(String(120), unique=True)
    password = Column(String(128))

    def set_password(self, password):
        self.password = Security.get_hashed_password(password).decode()

    def check_password(self, password):
        return Security.check_password(password, self.password)
