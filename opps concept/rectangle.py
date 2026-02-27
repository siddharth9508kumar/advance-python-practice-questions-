class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
r1 = Rectangle(5, 3)
print("Area of the rectangle:", r1.area())  