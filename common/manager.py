from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class RequestsRepo:
    session: AsyncSession

    async def commit(self) -> None:
        try:
            await self.session.commit()
        except Exception as e:
            await self.rollback()
            raise e

    async def flush(self) -> None:
        await self.session.flush()

    async def rollback(self) -> None:
        await self.session.rollback()