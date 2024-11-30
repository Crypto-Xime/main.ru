                                              # "Class Inheritance."
                                            # "They're all so alike":

import math


class Figure:
    def __init__(self, name, color):
        self.name = name
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = True
        self.sides_count = 0
        self.__sides = []

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(isinstance(val, int) and 0 <= val <= 255 for val in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return f"Name: {self.name}, Color: {self.__color}"

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, (int, float)) and side > 0 for side in sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def get_perimeter(self):
        return sum(self.__sides)


class Circle(Figure):
    def __init__(self, name, color, circumference):
        super().__init__(name, color)
        self.sides_count = 1
        self.set_sides(circumference)  # The circle has one side: the circumference
        self.__radius = circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    def __init__(self, name, color, *sides):
        super().__init__(name, color)
        self.sides_count = 3
        if len(sides) == self.sides_count:
            self.set_sides(*sides)
        else:
            self.set_sides(1, 1, 1)

    def get_square(self):
        sides = self.get_sides()
        semi_perimeter = sum(sides) / 2
        return math.sqrt(
            semi_perimeter
            * (semi_perimeter - sides[0])
            * (semi_perimeter - sides[1])
            * (semi_perimeter - sides[2])
        )


class Cube(Figure):
    def __init__(self, name, color, side_length):
        super().__init__(name, color)
        self.sides_count = 12
        self.set_sides(*([side_length] * self.sides_count))

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


# Example Usage
circle = Circle("Circle1", (200, 200, 100), 31.4)
triangle = Triangle("Triangle1", (50, 100, 150), 3, 4, 5)
cube = Cube("Cube1", (255, 0, 0), 6)

# Check colors
print(circle.get_color())  # Circle color
print(triangle.get_color())  # Triangle color
print(cube.get_color())  # Cube color

# Check sides
print("Circle sides:", circle.get_sides())  # Circle sides
print("Triangle sides:", triangle.get_sides())  # Triangle sides
print("Cube sides:", cube.get_sides())  # Cube sides

# Perimeter and area
print("Circle perimeter (circumference):", circle.get_perimeter())  # Circle perimeter
print("Triangle perimeter:", triangle.get_perimeter())  # Triangle perimeter
print("Circle area:", circle.get_square())  # Circle area
print("Triangle area:", triangle.get_square())  # Triangle area

# Cube volume
print("Cube volume:", cube.get_volume())  # Cube volume



