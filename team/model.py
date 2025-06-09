from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from common.model import AliasBaseModel


class TeamModel(AliasBaseModel):
    __tablename__: str = "teams"

    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    game: Mapped["GameModel"] = relationship(back_populates="teams")
    name: Mapped[str]
    members: Mapped[list["MemberModel"]] = relationship(back_populates="team")
