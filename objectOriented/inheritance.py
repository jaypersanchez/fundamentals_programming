# Example 2: Inheritance
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Cow(Animal):
    def make_sound(self):
        print("Moo")

# Creating objects of the derived classes
cat = Cat("Cat")
cow = Cow("Cow")

# Calling the method of the base class
print(f"{cat.species} says:")
cat.make_sound()

print(f"{cow.species} says:")
cow.make_sound()
