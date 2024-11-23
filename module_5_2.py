class House:
    def __init__(self, name, address, number_of_floors):
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
        return f"Name: {self.name}, number of floors: {self.number_of_floors}"

# Creating House objects
h1 = House('Residential complex Elbrus', 'Sokolovo-Meshcherskaya Str.', 10)
h2 = House('Residential complex Akatsiya', 'Engelsa Str.', 20)

# __str__ (printing the objects directly)
print(h1)
print(h2)

# __len__ (using len() to get the number of floors)
print(len(h1))
print(len(h2))
