from abc import ABC, abstractmethod


class Pressable(ABC):
    @abstractmethod
    def on_pressed(self):
        pass
