from dataclasses import dataclass

from propcache import cached_property
from sqlalchemy.ext.asyncio import AsyncSession

from word.repository import WordRepo


@dataclass
class RequestsRepo:
    session: AsyncSession

    @cached_property
    def word_repo(self):
        return WordRepo(session=self.session)

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
