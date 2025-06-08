from common.repository import BaseRepo
from game.model import GameModel


class GameRepo(BaseRepo[GameModel]):
    MODEL: type[GameModel] = GameModel
