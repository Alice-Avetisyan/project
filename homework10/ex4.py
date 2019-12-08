class Circle:
    def __init__(self, theRadius, thePI):
        self.radius = theRadius
        self.pi = thePI

    def area(self):
        try:
            print(self.pi * self.radius**2)
        except TypeError:
            print("One of the items you have entered is not a number")


circle = Circle(2.25, 3.141592)
circle.area()
circle2 = Circle(4.6, 'TEXT')
circle2.area()
