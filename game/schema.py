from common.enums import CategoryEnum
from common.schema import BaseSchema


class GameInitializeSchema(BaseSchema):
    round_duration: int
    word_categories: list[CategoryEnum]


class GameIDSchema(BaseSchema):
    id: int
