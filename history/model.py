from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from common.model import AliasBaseModel
from history.enum import HistoryTypeEnum
from history.types import HistoryScoreTD


class HistoryModel(AliasBaseModel):
    __tablename__: str = "history"

    type: Mapped[HistoryTypeEnum]
    score_metadata: Mapped[HistoryScoreTD | None] = mapped_column(JSONB, nullable=True)
    used_words: Mapped[list[str]]
