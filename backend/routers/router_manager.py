from container import container
from game.schema import GameIDSchema, GameInitializeSchema
from game.service import GameService
from logger import Logger

logger = Logger.setup_logger(__name__)


class RouterManager:
    @classmethod
    async def check_health(cls) -> str:
        return "I am alive"

    @classmethod
    async def initialize_game(cls, data: GameInitializeSchema) -> GameIDSchema:
        service: GameService = await container.game_service()
        return await service.create(
            round_duration=data.round_duration,
            word_categories=data.word_categories,
        )
