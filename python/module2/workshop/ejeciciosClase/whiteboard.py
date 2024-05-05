
class Coordinate:
    y:float
    x:float

    def __init__(self,x:float, y:float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other)->'Coordinate':
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __str__(self) -> str:
        return f"Coordinate: [x:{self.x}, [y:{self.y}]]"
    

class Pelota:

    radio: float
    material: str
    peso: float
    relleno: bool
    posicion_inincial: Coordinate
    posicion_actual:Coordinate
    coeficiente_rebote:float
    
    #foam -> 0.3
    
    #plastic -> 0.58
    
    #goma -> 0.9
    
    def __init__(self, radio: float, material:str, peso:float, relleno:bool, posicion_inicial:Coordinate) -> None:
        self.radio = radio
        self.material = material
        self.peso = peso
        self.relleno = relleno
        self.posicion_inincial = posicion_inicial
        self.posicion_actual = posicion_inicial
        if self.material == 'foam':
            self.coeficiente_rebote = 0.3
        elif self.material == 'plastic':
            self.coeficiente_rebote = 0.58
        elif self.material == 'goma':
            self.coeficiente_rebote = 0.9
        

    def botar(self, speed:float) -> None:
        y = speed * self.coeficiente_rebote
        self.posicion_actual = Coordinate(self.posicion_inincial.x, y)
        return
    
    def __str__(self) -> str:
        return f"y: {self.posicion_actual.y}"
    
pelota1 = Pelota(5, 'goma', 9.6, False, Coordinate(0, 8))
pelota2 = Pelota(5, 'plastic', 9.6, False, Coordinate(0, 4))
pelota3 = Pelota(5, 'foam', 9.6, False, Coordinate(0, 27))
pelota1.botar(4)
pelota2.botar(4)
pelota3.botar(4)
print(pelota1.posicion_actual,pelota2.posicion_actual,pelota3.posicion_actual)




