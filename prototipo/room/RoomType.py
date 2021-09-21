from enum import Enum


class RoomType(Enum):
    COMBAT = ("Combat Room", "START_COMBAT")
    TREASURE = ("Treasure Room", "TREASURE_ROOM")
    HEAL = ("Heal Room", "HEAL_ROOM")
