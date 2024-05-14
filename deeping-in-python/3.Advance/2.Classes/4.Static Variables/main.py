"""
Explanation: In Python, a static variable is a variable that is shared among all instances of a class, rather than being unique to each instance. It is also sometimes referred to as a class variable, because it belongs to the class itself rather than any particular instance of the class.
"""


class Car:
    # 👇 Static variable
    num_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # 👇 Accessing static variable
        Car.num_cars += 1


# Creating instances of Car
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")
car3 = Car("Ford", "Mustang")
car4 = Car("BMW", "X5")

print("Number of cars created:", Car.num_cars)  # 4

print("Car 1 details:", car1.brand, car1.model)  # Toyota Camry
print("Car 2 details:", car2.brand, car2.model)  # Honda Accord
print("Car 3 details:", car3.brand, car3.model)  # Ford Mustang
print("Car 4 details:", car4.brand, car4.model)  # BMW X5
