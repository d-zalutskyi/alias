from container import container


class BaseService:
    def __init__(self) -> None:
        self.repo = container.requests_repo
