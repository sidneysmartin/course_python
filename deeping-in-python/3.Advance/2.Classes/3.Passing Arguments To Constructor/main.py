# Passing arguments to constructor
class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def user_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}")


thrall = Person("Thrall", 37, "Azeroth")

darth_vader = Person("Darth Vader", 45, "Tatooine")

aragorn = Person("Aragorn", 87, "Middle Earth")

thrall.user_info()
darth_vader.user_info()
aragorn.user_info()
