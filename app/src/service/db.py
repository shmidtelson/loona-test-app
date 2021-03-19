import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.models import Base


class Database:
    @staticmethod
    async def init_pg(app):
        engine = create_async_engine(
            "postgresql+asyncpg://{}:{}@{}/{}".format(
                os.getenv('POSTGRES_USER'),
                os.getenv('POSTGRES_PASSWORD'),
                os.getenv('POSTGRES_HOST'),
                os.getenv('POSTGRES_DB'),
            ),
            echo=True,
        )
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        # expire_on_commit=False will prevent attributes from being expired
        # after commit.
        async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )

        app['db'] = async_session()

    @staticmethod
    async def close_pg(app):
        await app['db'].close()
