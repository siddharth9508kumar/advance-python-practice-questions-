class Circle:
    def __init__(self, n):
        self.radius = n
    def area(self):
        area = 3.14 * (self.radius ** 2)
        print(f"Area of the circle: {area}")
    def circumference(self):
        circumference = 2 * 3.14 * self.radius
        print(f"Circumference of the circle: {circumference}")
circle1 = Circle(5)
circle1.area()  
circle1.circumference()



