from common.repository import BaseRepo
from member.model import MemberModel


class MemberRepo(BaseRepo[MemberModel]):
    MODEL: type[MemberModel] = MemberModel
