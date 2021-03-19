from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession


class DBAbstract(ABC):
    db: AsyncSession = None

    def __init__(self, db: AsyncSession):
        super(DBAbstract, self).__init__()
        self.db = db
