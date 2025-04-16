class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Рік випуску: {self.year}")

    def change_model(self, new_model):
        self.model = new_model
        print(f"Модель змінено на {self.model}")

    def calculate_age(self):
        current_year = 2025
        age = current_year - self.year
        return age

car1 = Car("Toyota", "Corolla", 2015)
car1.display_info()
car1.change_model("Camry")
print(f"Вік автомобіля: {car1.calculate_age()} років")
