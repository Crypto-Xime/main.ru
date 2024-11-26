                                        # "Change cannot be received":

# Vehicle class
class Vehicle:
    _Color_Variants = ['Blue', 'White', 'Red', 'Grey', 'Pink', 'Black']  # Color variants

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.model = model
        self.color = color  # Use 'color' for instance attribute
        self.engine_power = engine_power

    def get_model(self):
        return f"Model: {self.model}"

    def get_horsepower(self):
        return f"Engine Power: {self.engine_power}"

    def get_color(self):
        return f"Color: {self.color}"  # Access self.color, not self.__Color

    def print_information(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Owner: {self.owner}")

    # Change the color only if it is in the _Color_Variants list and set color
    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self._Color_Variants]:
            self.color = new_color
        else:
            print(f"Can't change color to {new_color} in the current contract.")

# Sedan class that inherits from Vehicle
class Sedan(Vehicle):
    __Passenger_Limit = 5  # Limit of passengers for Sedan

    def __init__(self, owner, model, color, engine_power):
        # Initialize the Sedan class with the parent Vehicle's constructor
        super().__init__(owner, model, color, engine_power)

# Testing the functionality
if __name__ == '__main__':
    # Create an instance of the Sedan class
    vehicle1 = Sedan('Anton', 'Toyota Mark II', 'Black', 500)

    # Print initial properties
    vehicle1.print_information()

    # Try changing the color to a non-existent color (Pink)
    vehicle1.set_color('Pink')

    # Try changing the color to a valid color (BLACK)
    vehicle1.set_color('BLACK')

    # Change the owner
    vehicle1.owner = 'Vasyok'

    # Print updated properties
    vehicle1.print_information()







