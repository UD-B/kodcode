class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Student:
    def __init__(self, name, grades: list[int]):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        count = 0
        for i in self.grades:
            count += i
        average = count / len(self.grades)
        return average
    
class Book:
    def __init__(self, title, author, pages, is_read: bool):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True

    def info(self):
        print(f"the book {self.title} by the author {self.author} is about blah blah blah.")

class Counter:
    def __init__(self, count = 0):
        self.count = count

    def increase(self):
        self.count += 1

    def decrease(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_value(self):
        print(self.count)

class ShoppingItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
    
class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def set_time(self, sec):
        self.seconds = sec

    def get_time(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        return f"{minutes}:{seconds}"
    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birth_day(self):
        self.age += 1

    def introduce(self):
        return f"hi my name is {self.name} and i'm {self.age} years old."