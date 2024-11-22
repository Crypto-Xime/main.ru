                            # "Developer is not only a developer"

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

Hotel = House('Elbrus Residential Complex', 30, 16)

# Call the go_to method
Hotel.go_to(5)  # Testing a valid floor
print()  # For readability
Hotel.go_to(35)  # Testing an invalid floor