from fastapi import HTTPException

from common.enums import FindByEnum
from common.service import BaseService
from common.schema import IDSchema
from game.model import GameModel
from team.model import TeamModel


class TeamService(BaseService):

    async def create(self, game_id: int, team_name: str) -> IDSchema:
        found_game: GameModel = await self.requests_repo.game_repo.get_by(
            sorting_word=FindByEnum.ID,
            value=game_id,
        )
        if not found_game:
            raise HTTPException(
                status_code=404,
                detail="Game not found",
            )

        team: TeamModel = await self.requests_repo.team_repo.create(
            game_id=game_id,
            name=team_name,
            is_flush=True,
        )
        await self.requests_repo.commit()
        return IDSchema(id=team.id)
