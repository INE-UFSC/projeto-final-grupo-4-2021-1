from .IconButton import IconButton

class MenuIconButton(IconButton):
    def __init__(self, icon_path: str, next_state: str, rect=None):
        self.__next_state = next_state
        super().__init__(icon_path, rect=rect)

    def on_pressed(self):
        return self.__next_state