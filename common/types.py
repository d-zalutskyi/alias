from typing import TypeVar

from common.model import AliasBaseModel

ModelType: TypeVar = TypeVar("ModelType", bound=AliasBaseModel)
