from common.repository import BaseRepo
from history.model import HistoryModel


class HistoryRepo(BaseRepo[HistoryModel]):
    MODEL: type[HistoryModel] = HistoryModel
