from typing import TypeVar

from model import AliasBaseModel

ModelType: TypeVar = TypeVar("ModelType", bound=AliasBaseModel)
