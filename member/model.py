from sqlalchemy.orm import Mapped

from common.model import AliasBaseModel


class MemberModel(AliasBaseModel):
    __tablename__ = 'members'

    name: Mapped[str]
