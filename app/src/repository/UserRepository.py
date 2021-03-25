from typing import Optional
from sqlalchemy.engine import Row
from sqlalchemy.future import select

from src.models import UserModel
from src.service.abstract.DBAbstract import DBAbstract


class UserRepository(DBAbstract):
    async def get_by_id(self, identifier: str) -> Optional[Row]:
        query = select(UserModel).filter(UserModel.id == identifier)
        result = await self.db.execute(query)
        return result.one_or_none()

    async def get_by_login(self, login: str) -> Optional[Row]:
        query = select(UserModel).filter(UserModel.login == login)
        result = await self.db.execute(query)
        return result.one_or_none()
