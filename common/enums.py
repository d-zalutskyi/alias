from enum import StrEnum


class CategoryEnum(StrEnum):
    PEOPLE = "people"
    ANIMALS = "animals"
    FOOD = "food"
    OBJECTS = "objects"
    ACTIONS = "actions"
    PLACES = "places"
    SPORTS = "sports"
    TECH = "tech"
    EMOTIONS = "emotions"
    FUN = "fun"
    EIGHTEEN_PLUS = "eighteen_plus"


class FindByEnum(StrEnum):
    ID = "id"
    CATEGORY = "category"
