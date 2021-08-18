from Fighter import Fighter

class Opponent(Fighter):
    def __init__(self, stats: Stats, hp: Resource, ap: Resource, equipment: Equipment, buffs: dict[bufftarget, dict[DamageType, multiplier]], info: OpponentInfo, behavior: Behavior, skills: list = []):
        self.__info = info
        self.__behavior = behavior
        super().__init__(stats, hp, ap, equipment, buffs, skills)

    @property
    def info(self):
        return self.__info

    @property
    def behavior(self):
        return self.__behavior

    def use_skill(self):
        super().use_skill(self.__behavior.choose_skill)
