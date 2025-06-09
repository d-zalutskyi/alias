from fastapi import HTTPException

from common.enums import FindByEnum
from common.schema import IDSchema
from common.service import BaseService
from member.model import MemberModel
from team.model import TeamModel


class MemberService(BaseService):

    async def create(self, name: str, team_id: int) -> IDSchema:
        found_team: TeamModel = await self.requests_repo.team_repo.get_by(
            sorting_word=FindByEnum.ID,
            value=team_id,
        )
        if not found_team:
            raise HTTPException(
                status_code=404,
                detail="Team not found",
            )

        member: MemberModel = await self.requests_repo.member_repo.create(
            name=name,
            team_id=team_id,
            is_flush=True,
        )
        await self.requests_repo.commit()
        return IDSchema(id=member.id)
