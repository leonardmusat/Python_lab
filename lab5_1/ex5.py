class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        Animal.__init__(self, name, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        return self.name + "gives birth to live young."

class Bird(Animal):
    def __init__(self, name, habitat, feather_color):
        Animal.__init__(self, name, habitat)
        self.feather_color = feather_color

    def fly(self):
        return self.name + "is flying."

class Fish(Animal):
    def __init__(self, name, habitat, scaly_color):
        Animal.__init__(self, name, habitat)
        self.scaly_color = scaly_color

    def swim(self):
        return self.name + "is swimming."

# Example usage:
mammal = Mammal("Lion", "Grasslands", "Golden")
bird = Bird("Eagle", "Mountains", "Brown")
fish = Fish("Goldfish", "Aquarium", "Orange")

print(mammal.give_birth())
print(bird.fly())
print(fish.swim())