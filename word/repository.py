from common.repository import BaseRepo
from word.model import WordModel


class WordRepo(BaseRepo[WordModel]):
    MODEL: type[WordModel] = WordModel
