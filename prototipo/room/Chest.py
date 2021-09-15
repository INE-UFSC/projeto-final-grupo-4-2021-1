from item.Item import Item


class Chest:
    # def __init__(self, items):
        # self.__items = items
    def __init__(self):
        self.__items = None

    @property
    def items(self):
        return self.__items

    def item_selection(self, item: Item):
        return self.__items[item]
