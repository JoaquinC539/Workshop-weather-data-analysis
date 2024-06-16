from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
class AutoDeColor:
    modelo:int
    color:Color
    
    def __init__(self, modelo:int, color:Color) -> None:
        self.modelo=modelo
        self.color=color
        
modelo:int=2014
color:Color=Color.BLUE

autoDeColor:AutoDeColor=AutoDeColor(modelo, color)

print(autoDeColor.color)