from aiohttp import web
from sqlalchemy.ext.asyncio import AsyncSession


class BaseView:
    @property
    def db(self) -> AsyncSession:
        return self.request.app['db']

    @property
    def user(self) -> dict:
        if not self.request.get('payload'):
            raise web.HTTPBadRequest(reason='Wrong request')
        return self.request['payload']['user']
