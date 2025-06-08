from common.repository import BaseRepo
from team.model import TeamModel


class TeamRepo(BaseRepo[TeamModel]):
    MODEL: type[TeamModel] = TeamModel
