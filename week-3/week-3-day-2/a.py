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

animal_list = [dog, cat]
for i in animal_list:
    print(i.sound())

class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        super().area()
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        super().area()
        