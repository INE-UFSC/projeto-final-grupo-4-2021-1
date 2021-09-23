from .TextPressable import TextPressable
from item.Item import Item
from fighter.main_character.MainCharacter import MainCharacter

class ItemTextPressable(TextPressable):
    def __init__(self, font_path: str, size: int, text: str, item: Item):
        super().__init__(font_path, size, text)
        self.__item = item

    @property
    def item(self):
        return self.__item

    def on_pressed(self):
        self.__item.use(MainCharacter())
