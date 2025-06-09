from common.schema import BaseSchema


class MemberCreateSchema(BaseSchema):
    name: str
    team_id: int
