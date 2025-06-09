from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from common.model import AliasBaseModel


class MemberModel(AliasBaseModel):
    __tablename__: str = "members"

    name: Mapped[str]
    team_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"), nullable=True)
    team: Mapped["TeamModel"] = relationship(back_populates="members")
