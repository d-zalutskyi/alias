from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, relationship, mapped_column

from common.enum import CategoryEnum
from common.model import AliasBaseModel


class GameModel(AliasBaseModel):
    __tablename__: str = "games"

    round_duration: Mapped[int]  # seconds
    word_categories: Mapped[list[CategoryEnum]] = mapped_column(ARRAY(CategoryEnum))
    teams: Mapped[list["TeamModel"]] = relationship(
        argument="TeamModel",
        back_populates="game",
    )
