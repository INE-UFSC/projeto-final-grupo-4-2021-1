from fighter.opponent.Opponent import Opponent
from fighter.main_character.MainCharacter import MainCharacter

class Singleton:
    main_character: MainCharacter = None
    opponent: Opponent = None
    background = None