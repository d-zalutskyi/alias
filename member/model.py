from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from common.model import AliasBaseModel


class MemberModel(AliasBaseModel):
    __tablename__: str = 'members'

    name: Mapped[str]
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    team: Mapped["TeamModel"] = relationship(
        argument="TeamModel",
        back_populates="members",
    )
