from math import pi
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return f"the {self.brand} {self.model} moving"
    
class Car(Vehicle):
    def move(self):
        return f"the {self.brand} {self.model} drives"
    
class Plane(Vehicle):
    def move(self):
        return f"{self.brand} {self.model} flies"
    
a_vehicle = Vehicle("toyota", "land cruiser")
a_car = Car("toyota", "4runner")
a_plane = Plane("my", "plane")

# print(a_vehicle.move())
# print(a_car.move())
# print(a_plane.move())

class Animals:
    def sound(self):
        return f"the animal makes a sound"
class Dog(Animals):
    def sound(self):
        return f"woof"
class Cat(Animals):
    def sound(self):
        return f"meow"
    
dog = Dog()
cat = Cat()

# animal_list = [dog, cat]
# for i in animal_list:
#     print(i.sound())

class Shape:
    def area(self):
        raise NotImplementedError
    
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
    
rectangle = Rectangle(5, 5)
circle = Circle(5)
# print(rectangle.area(), circle.area())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_total_salary(self):
        return self.salary

class Manager(Employee):
    def add_bonus(self, bonus):
        self.salary += bonus
    def get_total_salary(self):
        return self.salary

class Developer(Employee):
    def add_overtime_payment(self, pay):
        self.salary += pay
    def get_total_salary(self):
        return self.salary

# udbrk = Employee("ud", 10000)
# udb = Manager("ud", 11000)
# ud = Developer("ud", 12000)
# udb.add_bonus(10000)
# ud.add_overtime_payment(10000)
# print(udbrk.get_total_salary())
# print(udb.get_total_salary())
# print(ud.get_total_salary())

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
class SavingsAccount(Account):

    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def interest(self):
        self.balance += self.interest_rate * self.balance
        return self.balance

my = SavingsAccount(10000, 0.1)
# print(my.interest())

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"book: {self.title}, author: {self.author}"
    
class Ebook(Book):
    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size
    def file_size_MB(self):
        return f"file size is {self.size}"
    def display_info(self):
        return super().display_info() + f', size: {self.size}'
    
obj = Ebook("book", "writer", 1.2)
print(obj.display_info())