from abc import ABC, abstractmethod
from math import pi
#A
#1
class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

class Car(Vehicle):
    def drive(self):
        print(f"this car can go {self.max_speed} km/h")

class Motorcycle(Vehicle):
    def drive(self):
        print(f"this motorcycle can go {self.max_speed} km/h")

car = Car(180)
motorcycle = Motorcycle(150)
# car.drive()
# motorcycle.drive()

#2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def manage(self):
        print(f"{self.name} manage if you want to get your {self.salary}")

class Developer(Employee):
    def write_code(self):
        print(f"{self.name} write code if you want to get your {self.salary}")

manager = Manager("UD", "80,000.00 total after taxes")
developer = Developer("ud", "90,000.00 total after taxes")
# manager.manage()
# developer.write_code()

#3
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * pi

# rectangle = Rectangle(5, 3)
# circle = Circle(5)
# print(rectangle.area())
# print(circle.area())

#4
class Payment:
    def __init__(self, method_name):
        self.method_name = method_name
    
class CreditCardPayment(Payment):
    def pay(self, amount):
        pass

class PayPalPayment(Payment):
    def pay(self, amount):
        pass

#B
#5
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

# class Car: