                            # Task "Evolution Error":

import random

# Parent class Animal
print("-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-")
class Animal:
    def __init__(self, name, speed):
        self.live = True # Animals live when they are born
        self.name = name # Each animal has a unique name
        self._DEGREE_OF_DANGER = 0 # Degree of danger the animal represents
        self.sound = None # Each animal has a unique sound
        self._cords = [0, 0, 0]  # Coordinates in space (x, y, z)
        self.speed = speed  # Speed of movement for the animal

    def move(self, dx, dy, dz):
        if self._cords[2] + dz < 0:
            print("It's to deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful, I don't like confrontation :(")
        else:
            print("Be careful, get away!!"
                  "I'm attacking you O_O")

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print(f"{self.name} makes no sound.")

# Bird class inheriting from Animal

class Bird(Animal):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.beak = True # Birds have a beak

# Random number of eggs from 1 to 6

    @staticmethod
    def lay_eggs():
        eggs = random.randint(1,6)
        print(f"Here are(is) {eggs} eggs for you")

# AquaticAnimal class inheriting from Animal

class AquaticAnimal(Animal):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self._DEGREE_OF_DANGER = 3

# Diving decreases the z coordinate, speed is reduced by half

    def dive_in(self, dz):
        dz = abs(dz)
        self.move(0, 0, -dz)  # Use the move method but reduce speed
        self.speed /= 2  # Reduce speed while diving

# PoisonousAnimal class inheriting from Animal

class PoisonousAnimal(Animal):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self._DEGREE_OF_DANGER = 8 # Poisonous Animals are consider very dangerous

# Duckbill class inheriting from Bird, AquaticAnimal, PoisonousAnimal

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        # Initialize Animal and Bird
        super().__init__("Duckbill", speed)
        # Initialize AquaticAnimal
        AquaticAnimal.__init__(self, "Duckbill", speed)
        # Initialize PoisonousAnimal
        PoisonousAnimal.__init__(self, "Duckbill", speed)
        # Unique sound for Duckbill
        self.sound = "Click-click-click"

# Testing the functionality
if __name__ == '__main__':

# Create a Duckbill object
    db = Duckbill(10)

# Test the attributes and methods
    print(db.live)
    print(db.beak)
    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()  # X: 10 Y: 20 Z: 30

    db.dive_in(6)
    db.get_cords()  # X: 10 Y: 20 Z: 0

# Static method call (no need to create an instance)
    Duckbill.lay_eggs()

# Additional descriptive outputs
    print("\nAs a result, we should get a live platypus with a beak,"
          "attacking and making strange sounds.")
    print("After which the platypus maneuvers and dives.")
    print("Now the platypus is safe, it lays eggs for future offspring.")
    print("-*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-")
