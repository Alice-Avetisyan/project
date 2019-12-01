from math import pi


class Circle:
    """This a derived class"""

    def __init__(self, theRadius, thePI):
        self.radius = theRadius
        self.pi = thePI

    def area(self):
        print(self.pi * self.radius**2)

    def area_test(self):
        print(pi * self.radius**2)


circle = Circle(2.25, 3.141592)
circle.area()
circle.area_test()