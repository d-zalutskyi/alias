from common.schema import IDSchema
from container import container
from game.schema import GameInitializeSchema
from game.service import GameService
from logger import Logger
from member.schema import MemberCreateSchema
from member.service import MemberService
from team.schema import TeamCreateSchema
from team.service import TeamService

logger = Logger.setup_logger(__name__)


class RouterManager:
    @classmethod
    async def check_health(cls) -> str:
        return "I am alive"

    @classmethod
    async def initialize_game(cls, data: GameInitializeSchema) -> IDSchema:
        service: GameService = await container.game_service()
        return await service.create(
            round_duration=data.round_duration,
            word_categories=data.word_categories,
        )

    @classmethod
    async def create_team(cls, data: TeamCreateSchema) -> IDSchema:
        service: TeamService = await container.team_service()
        return await service.create(
            game_id=data.game_id,
            team_name=data.team_name
        )

    @classmethod
    async def create_member(cls, data: MemberCreateSchema) -> IDSchema:
        service: MemberService = await container.member_service()
        return await service.create(
            name=data.name,
            team_id=data.team_id
        )
