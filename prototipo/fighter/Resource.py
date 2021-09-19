
class Resource:
    "Manages the values of a especific Resource, such as HP (HealthPoints) or AP (ActionPoints). Ensures that it's values are not less than 0, nor the current value is greater than the max value"
    def __init__(self, max, current):
        self.__max = max
        self.__current = current

    @property
    def max(self):
        return self.__max

    @property
    def current(self):
        return self.__current

    def increase_current(self, amount: int):
        "Increase the current value by the given amount. Ensures that it's not greater than the max value nor less than 0"
        self.__current += int(amount)
        if self.__current > self.__max:
            self.__current = self.__max

        elif self.__current < 0:
            self.__current = 0

    def increase_max(self, amount: int):
        "Increase the max value by the given amount. Ensures that it's not less than 0 and updates the current value accordingly"
        self.__max += int(amount)
        if self.__max < 0:
            self.__max = 0
        self.increase_current(amount)

    def decrease_current(self, amount: int):
        "Decrease the current value by the given amount. Ensures that it's not less than 0"
        self.__current -= int(amount)
        if self.__current < 0:
            self.__current = 0

    def decrease_max(self, amount: int):
        "Decrease the max value by the given amount. Ensures that it's not less than 0 and updates the current value accordingly"
        current_percetange = self.current/self.max
        self.__max -= int(amount)
        if self.__max < 0:
            self.__max = 0
        self.__current = current_percetange * self.__max
    
    def is_zero(self):
        return self.__current == 0