from common.schema import BaseSchema


class TeamCreateSchema(BaseSchema):
    game_id: int
    team_name: str
