import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.radius

rectangle = Rectangle(5, 10)
circle = Circle(7)

print(f"Площа прямокутника: {rectangle.get_area()}, Периметр: {rectangle.get_perimeter()}")
print(f"Площа кола: {circle.get_area()}, Довжина кола: {circle.get_circumference()}")
