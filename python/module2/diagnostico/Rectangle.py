from IShape import IShape

class Rectangle(IShape):
    
    def __init__(self, width:float, length:float) -> None:
        self.width = width
        self.lenght = length

    def perimetro(self) -> float:
        return 2 * (self.lenght + self.width)
    
    def area(self) -> float:
        return self.lenght * self.width
    



