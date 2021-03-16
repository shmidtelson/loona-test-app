import os
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import sessionmaker, scoped_session

from src.models import BaseModel, Base
from src.service.abstract import LoggerAbstract


class DBSession(LoggerAbstract):
    _session = None

    def __init__(self):
        super(DBSession, self).__init__()
        engine = create_engine(
            "postgresql+psycopg2://{}:{}@{}/{}".format(
                os.getenv('POSTGRES_USER'),
                os.getenv('POSTGRES_PASSWORD'),
                os.getenv('POSTGRES_HOST'),
                os.getenv('POSTGRES_DB'),
                pool_pre_ping=True,
            ),
            pool_recycle=600,
        )
        Base.metadata.create_all(engine)

        session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
        self._session = session()

    def add_model(self, model: BaseModel, need_flush: bool = False):
        self._session.add(model)

        if need_flush:
            self.commit()
            self._session.flush([model])

        return model

    def delete_model(self, model: BaseModel):
        if model is None:
            self.logger.warning(f'{__name__}: model is None')

        try:
            self._session.delete(model)
        except IntegrityError as e:
            self.logger.error(f'`{__name__}` {e}')
        except DataError as e:
            self.logger.error(f'`{__name__}` {e}')

    def query(self, *entities, **kwargs):
        return self._session.query(*entities, **kwargs)

    def rollback(self):
        self._session.rollback()

    def commit(self, flush: bool = False, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as e:
            self.logger.error(f'`{__name__}` {e}')
            raise
        except DataError as e:
            self.logger.error(f'`{__name__}` {e}')
            raise

        if flush:
            self._session.flush()

        if need_close:
            self.close()

    def flush(self):
        self._session.flush()

    def close_session(self):
        self._session.close()

    def close(self):
        try:
            self.close()
        except IntegrityError as e:
            self.logger.error(f'`{__name__}` {e}')
            raise
        except DataError as e:
            self.logger.error(f'`{__name__}` {e}')
            raise

    def __del__(self):
        self._session.close()
