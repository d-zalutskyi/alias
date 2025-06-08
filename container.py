from dependency_injector import containers, providers
from common.manager import RequestsRepo
from common.service import BaseService
from db_setup import DatabaseSetup


class Container(containers.DeclarativeContainer):
    session_factory = providers.Resource(
        DatabaseSetup.setup,
        echo=True,
        expire=False,
    )
    db_session = providers.Resource(
        lambda session_factory: session_factory(),
        session_factory=session_factory,
    )
    requests_repo = providers.Factory(
        RequestsRepo,
        session=db_session,
    )
    base_service = providers.Factory(
        BaseService,
        requests_repo=requests_repo,
    )

container = Container()