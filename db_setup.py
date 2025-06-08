from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


from common.model import AliasBaseModel
from config import config


class DatabaseSetup:
    @classmethod
    async def setup(
        cls, echo: bool = False, expire: bool = False
    ) -> async_sessionmaker[AsyncSession]:
        engine: AsyncEngine = cls._create_engine(echo=echo)
        await cls._create_all(engine=engine)
        return cls._create_session_pool(engine=engine, expire=expire)

    @classmethod
    def _create_engine(cls, echo: bool = False) -> AsyncEngine:
        return create_async_engine(
            url=config.database_connection,
            query_cache_size=1200,
            pool_size=20,
            max_overflow=200,
            future=True,
            echo=echo,
        )

    @classmethod
    def _create_session_pool(
        cls, engine: AsyncEngine, expire: bool = False
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind=engine, expire_on_commit=expire)

    @classmethod
    async def _create_all(cls, engine: AsyncEngine):
        async with engine.begin() as conn:
            await conn.run_sync(AliasBaseModel.metadata.create_all)
        await engine.dispose()
