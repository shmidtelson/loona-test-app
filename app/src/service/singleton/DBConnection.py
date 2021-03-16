from src.service.DBSession import DBSession


class DBConnection:
    _instance: DBSession = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def db(cls):
        if cls._instance is None:
            cls._instance = DBSession()
        return cls._instance
