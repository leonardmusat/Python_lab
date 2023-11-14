import math
class Shape:
    def __init__(self):
        self.name = "Shape"

    def area(self):
        return 1

    def peramiter(self):
        return 1


class Round(Shape):
    def __init__(self, radius):
        Shape.__init__(self)
        self.name = "Round"
        self.radius = radius
        self.pi = 3.14

    def area(self):
        return 1

    def perimeter(self):
        return 1


class Circle(Round):
    def __init__(self, radius):
        Round.__init__(self,radius)
        self.name = "Circle"

    def area(self):
        return self.pi * self.radius * self.radius

    def perimeter(self):
        return self.pi * self.radius * 2

class Elipse(Round):
    def __init__(self, radius1, radius2):
        Round.__init__(self, radius1)
        self.name = "Elipse"
        self.radius2 = radius2

    def area(self):
        return self.radius * self.radius2 * self.pi

    def perimeter(self):
        term1 = self.radius2 * self.radius2 + self.radius + self.radius
        term2 = math.sqrt(term1 / 2)
        term3 = 2 * self.pi * term2
        return term3


ellipse = Elipse(4, 8)
print("The area of the ", ellipse.name, "is ", ellipse.area())
print("The perimeter of the ", ellipse.name, "is ", ellipse.perimeter())

circle = Circle(4)
print("The area of the ", circle.name, "is ", circle.area())
print("The perimeter of the ", circle.name, "is ", circle.perimeter())


class Parallelogram(Shape):
    def __init__(self, edges):
        Shape.__init__(self)
        self.edges = edges

    def area(self):
        return 1

    def perimeter(self):
        perimeter = 0
        for edge in self.edges:
            perimeter = perimeter + edge
        return perimeter


class Square(Parallelogram):
    def __init__(self, edges):
        Parallelogram.__init__(self, edges)
        self.name = "Square"

    def area(self):
        return self.edges[0] * self.edges[1]


class Triangle(Parallelogram):
    def __init__(self, edges, base, height):
        Parallelogram.__init__(self, edges)
        self.name = "Triangle"
        self.height = height
        self.base = base

    def area(self):
        return (self.base * self.height)/2


square = Square([4,4,4,4])
print("The area of the ", square.name, "is ", square.area())
print("The perimeter of the ", square.name, "is ", square.perimeter())

triangle = Triangle([5, 8, 5], 8, 3)
print("The area of the ", triangle.name, "is ", triangle.area())
print("The perimeter of the ", triangle.name, "is ", triangle.perimeter())


