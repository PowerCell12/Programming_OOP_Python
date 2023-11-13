from abc import abstractclassmethod, ABC


class Shape(ABC):
    def __init__(self):
        pass


    @abstractclassmethod
    def calculate_area(self):
        pass


    @abstractclassmethod
    def calculate_perimeter(self):
        pass

from math import pi
class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius


    def calculate_area(self):
            return self.__radius **2  * pi
    

    def calculate_perimeter(self):
         return 2 * self.__radius * pi



class Rectangle(Shape):

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
            return self.__height * self.__width
    

    def calculate_perimeter(self):
         return 2 * (self.__width + self.__height)
