class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __str__(self):
        return f"{self.x}, {self.y}"

class Line:
    count = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
        Line.count += 1

    def show(self):
        print(self.a, " ", self.b)

    @classmethod
    def how_many(cls):
        return cls.count

    @staticmethod
    def is_horizontal(self):
        if self.a.y == self.b.y:
            return True
        else:
            return False

    @staticmethod    
    def is_vertical(self):
        if self.a.x == self.b.x:
            print(self.a.x)
            print(self.b.x)
            return True
        else:
            return False
        

point_1 = Point(1, 5)
point_2 = Point(3, 5)

line = Line(point_1, point_2)

Line.show(line)
print(Line.how_many())
print(Line.is_horizontal(line))
print(Line.is_vertical(line))