from abc import ABC

from src.service.DBSession import DBSession
from src.service.singleton.DBConnection import DBConnection


class DBAbstract(ABC):
    db: DBSession

    def __init__(self):
        self.db = DBConnection.db()

        super(DBAbstract, self).__init__()
