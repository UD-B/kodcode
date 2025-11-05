from abc import ABC, abstractmethod

#single responsibility principle
#1
class Book:
    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre

class Save_to_list:
    def __init__(self):
        self.title_list = []
        self.author_list = []
        self.genre_list = []
    
    def return_lists(self):
        return self.title_list, self.author_list, self.genre_list

    def add_title_list(self, title):
        self.title_list.append(title)
    
    def add_author_list(self, author):
        self.author_list.append(author)

    def add_genre_list(self, genre):
        self.genre_list.append(genre)
    

book_0 = Book("Tora", "Hashem", "All")
book_1 = Book("harry potter", "J. K. Rowling", "fantasy")
book_2 = Book("foundation", "Isaak asimov", "science fiction")
saved_to_list = Save_to_list()
# print(saved_to_list.add_title_list(book.title))
# print(saved_to_list.add_author_list(book.author))
# print(saved_to_list.add_genre_list(book.genre))
# print(saved_to_list.add_title_list(book_2.title))
# print(saved_to_list.add_author_list(book_2.author))
# print(saved_to_list.add_genre_list(book_2.genre))

saved_to_list.add_title_list(book_0.title)
saved_to_list.add_author_list(book_0.author)
saved_to_list.add_genre_list(book_0.genre)
saved_to_list.add_title_list(book_1.title)
saved_to_list.add_author_list(book_1.author)
saved_to_list.add_genre_list(book_1.genre)
saved_to_list.add_title_list(book_2.title)
saved_to_list.add_author_list(book_2.author)
saved_to_list.add_genre_list(book_2.genre)

# print(saved_to_list.return_lists())



#2f
class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

class GradeCalculator:
    def __init__(self, grades):
        self.grades = grades

    def calculate_average(self):
        return (sum(self.grades) / len(self.grades))
    
student = Student("ud", [70, 85])
student_average = GradeCalculator(student.grades)
# print(student_average.calculate_average())

#3
class Order:
    def __init__(self, items: list[str], total_price: float):
        self.items = items
        self.total_price = total_price


#open/close principle (o)
#1
class Shape(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * 3.141592
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.height * self.width

circle = Circle(5)
square = Square(5)
rectangle = Rectangle(5, 3)
# print({'circle':circle.area()}, {'square':square.area()}, {'rectangle':rectangle.area()})

#2


