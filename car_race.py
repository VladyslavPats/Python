class Car:
    def __init__(self, brand, model, year, speed, power, color):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed
        self.__power = power
        self.__color = color
        self.__driver = None

    def assign_driver(self, driver):
        self.__driver = driver

    def get_driver(self):
        return self.__driver

    def get_speed(self):
        return self.__speed

    def get_power(self):
        return self.__power

    def get_info(self):
        return {
            "brand": self.__brand,
            "model": self.__model,
            "year": self.__year,
            "color": self.__color,
            "driver": self.__driver.get_name() if self.__driver else None
        }


class Driver:
    def __init__(self, name, age, driving_experience):
        self.__name = name
        self.__age = age
        self.__experience = driving_experience

    def get_experience(self):
        return self.__experience

    def get_name(self):
        return self.__name


class Race:
    def start_race(self, car1, car2):
        driver1 = car1.get_driver()
        driver2 = car2.get_driver()

        if not driver1 or not driver2:
            print("Обидві машини повинні мати призначених водіїв!")
            return None

        score1 = car1.get_speed() + car1.get_power() + driver1.get_experience()
        score2 = car2.get_speed() + car2.get_power() + driver2.get_experience()

        return car1 if score1 > score2 else car2

    def print_winner(self, winner):
        if winner:
            info = winner.get_info()
            print(f"Переможець: {info['brand']} {info['model']}, кермувальник: {info['driver']}")


car1 = Car("BMW", "X5", 2022, 250, 300, "Black")
car2 = Car("Audi", "A6", 2023, 240, 280, "White")
driver1 = Driver("John", 35, 15)
driver2 = Driver("Alice", 28, 10)

car1.assign_driver(driver1)
car2.assign_driver(driver2)

race = Race()
winner = race.start_race(car1, car2)
race.print_winner(winner)