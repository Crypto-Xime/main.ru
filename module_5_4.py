                                            # "History of construction"
                                            #  “Operator Overloading”

# Class-level attribute to store history of house names
class House:
    Houses_history = []

# Create a New instance for House
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

# Remember add the name to House_history when creating a new object
        house_name = args[0] # First letter or argument
        cls.Houses_history.append(house_name)
        return instance


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

    def __del__(self):
        # When the object is deleted, print a message
        print(f"{self.name} Has been demolished, but it will remain in history")

# Creating House objects
h1 = House('Residential complex Elbrus', 'Sokolovo-Meshcherskaya Str.', 10)
print(House.Houses_history)

h2 = House('Residential complex Akatsiya', 'Engelsa Str.', 20)
print(House.Houses_history)

h3 = House('Matryoshka Residential Complex', 'Northeastern Administrative District', 20)
print(House.Houses_history)

# Removing objects
del h2
del h3

# Checking the final state of houses_history
print(House.Houses_history)