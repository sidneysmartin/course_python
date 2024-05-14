# ------- Private Modifier
# In Python, attributes and methods that start with double
# underscores __ are considered "private." This means they are not
# accessible from outside the class. However,
# Python does not enforce this access restriction strictly;

# ------- Private Modifier
# In Python, attributes and methods that start with double underscores __ are considered "private." This means they are not accessible from outside the class. However, Python does not enforce this access restriction strictly;


class MyClass:
    def __init__(self, x):
        self.__x = x  # 👈 This attribute is private

    def get_x(self):
        return self.__x  # 👈 This method is public (double underscores)


obj = MyClass(10)
print(obj.get_x())  # 10
# Accessing a private attribute (not recommended, and name-mangled)
print(obj._MyClass__x)


class Person:
    def __init__(self, name, age, gender):
        self._name = name  # protected attribute
        self.__age = age  # private attribute
        self.__gender = gender  # private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age should be greater then 0")

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ['Male', 'Female', 'Other']:
            self.__gender = gender
        else:
            print("Gender should be 'Male', 'Female' or 'Other'")


person = Person("John", 25, "Male")

print(person._name)
print(person._Person__age)
print(person._Person__gender)

person.set_age(30)

print(person.get_age(30))

# person.set_age(-1) # will raise an error
