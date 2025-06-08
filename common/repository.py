from typing import Generic, Any

from sqlalchemy import select, update, Select, Result, Executable, ScalarResult, Update
from sqlalchemy.ext.asyncio import AsyncSession

from common.enum import FindByEnum
from common.types import ModelType


class BaseRepo(Generic[ModelType]):
    MODEL: type[ModelType]

    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def get_by(
            self,
            sorting_word: FindByEnum,
            value: Any,
            many: bool = False
    ) -> ModelType | list[ModelType] | None:
        stmt: Select = (
            select(self.MODEL)
            .where(getattr(self.MODEL, sorting_word.value) == value)
        )
        result: Result = await self.session.execute(stmt)
        if many:
            return result.scalars().all()

        return result.scalar_one_or_none()

    async def get_by_extended(
            self,
            filters: dict[FindByEnum, Any],
            many: bool = False,
            unique: bool = False,
            order_by: str | None = None,
            limit: int | None = None,
            offset: int | None = None,
            options: list[Any] | None = None
    ) -> ModelType | list[ModelType] | None:
        stmt: Select = select(self.MODEL)

        if options:
            for opt in options:
                stmt: Executable = stmt.options(opt)

        for field, value in filters.items():
            column: Any = getattr(self.MODEL, field.value)
            if isinstance(value, (list, tuple, set)):
                stmt = stmt.where(column.in_(value))
            else:
                stmt = stmt.where(column == value)

        if order_by:
            stmt = stmt.order_by(getattr(self.MODEL, order_by))

        if limit is not None:  # limit=0 -> python interprets like False
            stmt = stmt.limit(limit)

        if offset is not None:  # offset=0 -> python interprets like False
            stmt = stmt.offset(offset)

        result: Result = await self.session.execute(stmt)
        scalars: ScalarResult = result.unique().scalars() if unique else result.scalars()
        return scalars.all() if many else scalars.first()

    async def update_by(
            self,
            sorting_word: FindByEnum | None,
            value: Any | None,
            update_data: dict[str, Any],
            is_return: bool = False,
    ) -> ModelType | None:
        stmt: Update = (
            update(self.MODEL)
            .where(getattr(self.MODEL, sorting_word.value) == value)
            .values(**update_data)
        )

        if is_return:
            stmt: Executable = stmt.returning(self.MODEL)

        result: Result = await self.session.execute(stmt)
        await self.session.flush()

        return result.scalar_one_or_none() if is_return else None

    async def create(self, is_flush: bool = False, **kwargs) -> ModelType | None:
        model: type[ModelType] = self.MODEL(**kwargs)
        self.session.add(model)
        if is_flush:
            await self.session.flush()
            return model

        return None
