from prototipo.fighter.main_character import MainCharacter
from prototipo.fighter.opponent import Opponent

class Singleton:
    main_character = MainCharacter.generate_test_character()
    opponent = Opponent.generate_test_character()