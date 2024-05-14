# -------- Constructor Inheritance
# The constructor in the "parent" class is already available to the child class by default.

class Animal:
    def __init__(self, breed, size, color, speed):
        self.breed = breed
        self.size = size
        self.color = color
        self.speed = speed
        print("Parent Constructor")
        print(f"Breed: {self.breed}, Size: {self.size}, Color: {
              self.color}, Speed: {self.speed}")

# Constructor Overriding
# If we write constructors on both classes, The parent constructor will be no longer
# available to the child class because we're overriding it.


class Dog(Animal):
    def __init__(self, animal_name):
        self.animal_name = animal_name
        print("Child Constructor")
        print(f"Animal Name: {self.animal_name}")

    def bark(self):
        print("woff woff")


buddy = Dog("Dog")
buddy.bark()
