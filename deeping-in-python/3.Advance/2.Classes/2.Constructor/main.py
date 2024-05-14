# . __init__ is a constructor which allow us to create variables in class.

class Person:
    def __init__(self):
        self.name = "Naruto Uzumaki"
        self.age = 17
        self.location = "Konoha"

    def user_info(self):
        print("Name: %s, Age: %d, Location: %s" %
              (self.name, self.age, self.location))


# Creating an object
person = Person()
person.user_info()
