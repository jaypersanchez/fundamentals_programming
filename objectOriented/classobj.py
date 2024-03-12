# Example 1: Class definition
class Dog:
    # Constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to bark
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes and calling methods of objects
print(f"{dog1.name} is {dog1.age} years old.")
dog1.bark()

print(f"{dog2.name} is {dog2.age} years old.")
dog2.bark()
