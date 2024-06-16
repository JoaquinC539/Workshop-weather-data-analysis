from IShape import IShape
from math import pi

class Circle(IShape):
     
    def __init__(self, radius:float) -> None:
        self.radius = radius

    def perimetro(self) -> float:
        return 2 * self.radius * pi
    
    def area(self) -> float:
        return (pi * self.radius)**2
