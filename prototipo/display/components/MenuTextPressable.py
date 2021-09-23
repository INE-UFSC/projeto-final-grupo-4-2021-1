from .TextPressable import TextPressable

class MenuTextPressable(TextPressable):
    def __init__(self, font_path: str, size: int, text: str, next_state: str):
        super().__init__(font_path, size, text)
        self.__next_state = next_state

    @property
    def item(self):
        return self.__item

    def on_pressed(self):
        return self.__next_state
