from typing import cast

from sqlalchemy import Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class AliasBaseModel(DeclarativeBase):
    __abstract__: bool = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @classmethod
    def get_table_name(cls) -> str:
        return cls.__tablename__

    @classmethod
    def get_columns(cls) -> list[Column]:
        return cast(list[Column], list(cls.__table__.columns))
