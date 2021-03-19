from aiohttp import web
from sqlalchemy.exc import IntegrityError

from src.models.User import UserModel
from src.service.abstract.DBAbstract import DBAbstract
from src.service.abstract.LoggerAbstract import LoggerAbstract


class UserCreator(DBAbstract, LoggerAbstract):
    async def create(self, username: str, password: str) -> UserModel:
        u = UserModel()
        u.login = username
        u.set_password(password)
        self.db.add(u)
        try:
            await self.db.commit()
        except IntegrityError as e:
            self.logger.info(e, exc_info=True)
            await self.db.rollback()
            raise web.HTTPConflict(reason='User exists')
        return u
