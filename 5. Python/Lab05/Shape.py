from abc import ABC, abstractmethod
from typing import override

# shape
#   abstract method : area(), perimeter()
#   override __str__ to return "Shape :(type=recangle)"


class CombinedShape():
    def __init__(self, area: float) -> None:
        """
        Initialize a CombinedShape with a given area.
        return : 
            None
        """
        self.area = area

class Shape(ABC):
    def __init__(self, dim1: float, dim2: float):
        """
        Initialize a Shape with two dimensions.
        return :
            None
        """
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        """
        pass

    def __add__(self, other: 'Shape') -> CombinedShape:
        """
        Combine two shapes by adding their areas.
        paramter : 
            Shape
        return :
            CombinedShape
        """
        area = self.area() + other.area()
        return CombinedShape(area)
    
    def __eq__(self, other: 'Shape') -> bool:
        """
        Compare two shapes based on their area.
        parameters :
            Shape
        return :
            bool
        """
        return self.area() == other.area()
    
    @override
    def __str__(self):
        """
        Return a string representation of the Shape.
        return :
            str
        """
        return f"Shape(type={self.__class__.__name__})"




# Rectangle class inheriting from Shape
#   attributes: width, height

# Circle class inheriting from Shape
#  attributes: radius

# Triangle class inheriting from Shape
# attributes: a, b, c

# override __str__
# implement area() and perimeter() methods

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a Rectangle with width and height.
        parameters :
            width , height
        return :
            None
        """
        super().__init__(width, height)

    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        return :
            area
        """
        return self.dim1 * self.dim2
    
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.
        return :
            perimeter
        """
        return 2 * (self.dim1 + self.dim2)
    
    def __str__(self) -> str:
        """
        Return a string representation of the Rectangle.
        return :
            str > message
        """
        return f"Rectangle: area={self.area()}, perimeter={self.perimeter()}"
    
class Circle(Shape):
    def __init__(self, radius: float) -> None:
        """
        Initialize a Circle with a given radius.
        parameters :
            radius

        """
        super().__init__(radius, radius)
    
    def area(self) -> float:
        """
        Calculate the area of the circle.
        return :
            area
        """
        return 3.14 * self.dim1 * self.dim2
    
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the circle.
        return :
            perimeter
        """
        return 2 * 3.14 * self.dim1

    def __str__(self) -> str:
        """
        Return a string representation of the Circle.
        return :
            str > message
        """
        return f"Circle: area={self.area()}, perimeter={self.perimeter()}"
    

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Initialize a Triangle with three sides a, b, and c.
        parameters :
            a, b, c
        """
        super().__init__(a, b)
        self.c = c

    def area(self) -> float:
       """
        Calculate the area of the triangle using Heron's formula.
        return :
            area
       """
       semi_perimeter = self.perimeter() / 2
       return (semi_perimeter * (semi_perimeter - self.dim1) * (semi_perimeter - self.dim2) * (semi_perimeter - self.c)) ** 0.5

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the triangle.
        return :
            perimeter
        """
        return self.dim1 + self.dim2 + self.c

    def __str__(self) -> str:
        """
        Return a string representation of the Triangle.
        return :
            str > message
        """
        return f"Triangle: area={self.area()}, perimeter={self.perimeter()}"
 
   

if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Triangle(3, 4, 5),
    ]


    print(f"Shape 1 and Shape 2 are equal: {shapes[0] == shapes[1]}")

    combined_shape = shapes[0] + shapes[1]
    print(f"Combined Shape Area: {combined_shape.area}")

    for shape in shapes:
        print(shape)
