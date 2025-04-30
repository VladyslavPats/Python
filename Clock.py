class Clock:
    def __init__(self, time=0):
        if self.__check_time(time):
            self.__time = time
        else:
            self.__time = 0

    def set_time(self, time):
        if self.__check_time(time):
            self.__time = time

    def get_time(self):
        return self.__time

    @staticmethod
    def __check_time(time):
        return isinstance(time, int) and 0 <= time < 100_000


# Перевірка:
clock = Clock(0)
clock.set_time(4530)
print("Clock time:", clock.get_time())  # Виведе: Clock time: 4530
