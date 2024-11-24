                                            #  “Special class methods”.
class House:
    def __init__(self, name, address, number_of_floors, ):
        self.name = name
        self.address = address
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(f"Arrived at floor {floor}")

            else:
                print("This floor does not exist.")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Name: {self.name}, Number of floors: {self.number_of_floors}"

# __eq__ method for equality comparison

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

# __add__ method for adding floors

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.address, self.number_of_floors + other)
        return NotImplemented

# __iadd__ method for in-place addition (+= operator)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        return NotImplemented

# __radd__ method for reverse addition (if the left-hand side is an integer)

    def __radd__(self, other):
        if isinstance(other, int):
            return House(self.name, self.address, self.number_of_floors + other)
        return NotImplemented

# Comparison operators

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

# Creating House objects
h1 = House('Residential complex Elbrus', 'Sokolovo-Meshcherskaya Str.', 10)
h2 = House('Residential complex Akatsiya', 'Engelsa Str.', 20)

# Printing the objects
print(h1)
print(h2)

# Testing __eq__ (equality comparison)
print(h1 == h2)

# Testing __add__ (addition of floors)
h1 = h1 + 10  # Adding 10 floors
print(h1)

# Testing equality after addition
print(h1 == h2)

# Testing __iadd__ (in-place addition)
h1 += 10  # In-place addition (+=)
print(h1)

# Testing __radd__ (reverse addition)
h2 = 10 + h2  # Reverse addition (10 + h2)
print(h2)

# Comparison tests
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__