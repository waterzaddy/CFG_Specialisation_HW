import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = (self.a + self.b) * 2
        print("Consider me implemented", perim)
        return perim


class Square(Rectangle):
    def __init__(self, a):
        self.a = a
        self.b = a


triangle_1 = Triangle(5, 5, 10)
print(triangle_1.calc_perimeter())

rectangle_1 = Rectangle(5, 10)
print(rectangle_1.calc_perimeter())

square_1 = Square(5)
print(square_1.calc_perimeter())
