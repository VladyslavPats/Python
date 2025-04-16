class Point:
    def __init__(self, coordinate_x=0, coordinate_y=0, color='black'):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.color = color

points = [Point(0, 0, 'red') for _ in range(1000)]

print(f"Кількість точок: {len(points)}")
points[2].coordinate_x = 10
print(f"Нова координата X третьої точки: {points[2].coordinate_x}")
