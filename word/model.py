from sqlalchemy.orm import Mapped, mapped_column

from common.enum import CategoryEnum
from common.model import AliasBaseModel


class WordModel(AliasBaseModel):
    __tablename__: str = "words"

    category: Mapped[CategoryEnum]
    word: Mapped[str] = mapped_column(unique=True)
