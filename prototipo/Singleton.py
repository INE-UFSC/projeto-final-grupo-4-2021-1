from fighter.main_character.MainCharacter import MainCharacter
from fighter.opponent.Opponent import Opponent

class Singleton:
    main_character: MainCharacter = None
    opponent : Opponent = None
    background = None