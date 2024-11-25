                                    # "Edible, inedible":

# What happened: The predator tried to eat the flower and died, the mammal ate the fruit and got full.

# Parent class Animal

class Animal:
    def __init__(self, name):
        self.alive = True # Animals are alive by default
        self.fed = False # Animals are not fed by default
        self.name = name  # Each animal has a unique name

    def eat(self, food):
        raise NotImplementedError("Subclass must implement abstract method.")

# Parent class Plant

class Plant:
    def __init__(self, name):
        self.edible = False # Plants are not edible by default
        self.name = name # Each plant has a unique name

# Mammal class inheriting from Animal

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self, food):
        if food.edible:
            print(f"{self.name} ate {food.name}")
            self.fed = True

        else:
            print(f"{self.name} did not eat {food.name}")
            self.alive = False

# Predator class inheriting from Animal
class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self, food):
        if food.edible:
            print(f"{self.name} ate {food.name}")
            self.fed = True
        else:
            print(f"{self.name} did not eat {food.name}")
            self.alive = False

# Flower class inheriting from Plant

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

# Fruit class inheriting from Plant

class Fruits(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Overriding the default value to True for fruits

if __name__ == '__main__':
        a1 = Predator('The Wolf of Wall Street')
        a2 = Mammal('Hachiko')

        p1 = Flower('Seven-flowered flower')
        p2 = Fruits('A Clockwork Orange')

# Testing functionality

        print(a1.name)
        print(p1.name)

        print(a1.alive)
        print(a1.fed)

        a1.eat(p1)
        a2.eat(p2)

        print(a1.alive)
        print(a2.fed)