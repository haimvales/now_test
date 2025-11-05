from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass

# Concrete subclasses
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * (self.radius ** 2)
    def get_perimeter(self):
        return 2 * 3.14 * self.radius
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
if __name__ == '__main__':
    shapes = [
    Rectangle(4, 5),
    Circle(3)
 ]
    for shape in shapes:
        print(shape)
        print("→ area:")
        print(shape.get_area() )
        print("perimeter:")
        print(shape.get_perimeter())