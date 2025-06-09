from common.enums import CategoryEnum
from common.schema import IDSchema
from common.service import BaseService
from game.model import GameModel


class GameService(BaseService):

    async def create(
            self,
            round_duration: int,
            word_categories: list[CategoryEnum],
    ) -> IDSchema:
        game: GameModel = await self.requests_repo.game_repo.create(
            round_duration=round_duration,
            word_categories=word_categories,
            is_flush=True,
        )
        await self.requests_repo.commit()
        return IDSchema(id=game.id)
