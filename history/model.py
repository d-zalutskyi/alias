from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from common.model import AliasBaseModel
from history.enums import HistoryTypeEnum
from history.types import HistoryScoreTD


class HistoryModel(AliasBaseModel):
    __tablename__: str = "history"

    type: Mapped[HistoryTypeEnum]
    score_metadata: Mapped[HistoryScoreTD | None] = mapped_column(JSONB, nullable=True)
    used_words: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
