import datetime

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, TIMESTAMP
import uuid

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)
