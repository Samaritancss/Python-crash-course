# super () = Function used in a child class to call methods from a parent class (superclass).
# allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius **2}cm")
    

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width **2}cm")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm")

circle = Circle(color = "Pink", is_filled = True, radius = 5)
square = Square(color = "Purple", is_filled = False, width =6)
triangle = Triangle(color = "green", is_filled = False, width = 4, height = 6)

#circle.describe()
# print(triangle.is_filled)
# print(triangle.color)
# print(f"{triangle.width}cm")
# print(f"{triangle.height}cm")
#triangle.describe()







