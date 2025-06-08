from typing import TypedDict


class HistoryTeamScoreTD(TypedDict):
    id: int
    score: int


class HistoryScoreTD(TypedDict):
    scores: list[HistoryTeamScoreTD]
