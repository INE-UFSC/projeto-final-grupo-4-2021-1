from fighter.main_character.MainCharacter import MainCharacter
from fighter.opponent.Opponent import Opponent
from room.Room import Room


class Singleton:
    room: Room = None
    main_character: MainCharacter = None
    opponent: Opponent = None
    background = None
