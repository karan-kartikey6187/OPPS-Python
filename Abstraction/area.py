from abc import ABC,abstractmethod
import math

class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shapes):
    def area(self,radius):
        pi=math.pi
        print(f"Area Of a Circle is {pi*radius**2}")  

class Square(Shapes):
    def area(self,side):
        print(f"Area Of a Square is {side**2}")
 
class Rectangle(Shapes):
    def area(self,length,width):
        print(f"Area Of a Rectangle is {length*width}")

cirlce=Circle()
cirlce.area(5)
square=Square()
square.area(9)
rectangle=Rectangle()
rectangle.area(4,6)