import attr

from common.manager import RequestsRepo


@attr.s(auto_attribs=True)
class BaseService:
    requests_repo: RequestsRepo
