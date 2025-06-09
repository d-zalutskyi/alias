from common.enums import CategoryEnum
from common.service import BaseService
from game.model import GameModel
from game.schema import GameIDSchema


class GameService(BaseService):

    async def create(
            self,
            round_duration: int,
            word_categories: list[CategoryEnum],
    ) -> GameIDSchema:
        game: GameModel = await self.requests_repo.game_repo.create(
            round_duration=round_duration,
            word_categories=word_categories,
            is_flush=True,
        )
        await self.requests_repo.commit()
        return GameIDSchema(id=game.id)
