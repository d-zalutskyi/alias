from dataclasses import dataclass

from propcache import cached_property
from sqlalchemy.ext.asyncio import AsyncSession

from word.repository import WordRepo
from game.repository import GameRepo
from team.repository import TeamRepo


@dataclass
class RequestsRepo:
    session: AsyncSession

    @cached_property
    def word_repo(self):
        return WordRepo(session=self.session)

    @cached_property
    def game_repo(self) -> GameRepo:
        return GameRepo(session=self.session)

    @cached_property
    def team_repo(self) -> TeamRepo:
        return TeamRepo(session=self.session)

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
