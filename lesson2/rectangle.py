"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
если это квадрат, и False в противном случае
"""
import math
from typing import Self


class Rectangle:
    width: float
    height: float


    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height


    def area(self) -> float:
        return self.width * self.height


    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


    @classmethod
    def from_diagonal(cls, diagonal: float, aspect_ratio: float) -> Self:
        height = diagonal / math.sqrt(aspect_ratio ** 2 + 1)
        width = aspect_ratio * height

        return cls(width, height)


    @staticmethod
    def is_square(width: float, height: float) -> bool:
        return width == height


# код для проверки 
rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5, 2)
print(rectangle2.area())  # 10.0128
print(rectangle2.perimeter())  # 13.42

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
