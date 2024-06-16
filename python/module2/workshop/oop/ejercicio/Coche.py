from Marca import Marca
from typing import List
from Trabajo import Trabajo

class Coche:
    modelo:int
    marca: Marca
    placas: str
    trabajos:List[Trabajo]
    

    def __init__(self, modelo:int,marca:Marca,placas:str) -> None:
        self.modelo=modelo
        self.marca = marca
        self.placas = placas
        self.carro = list()
        
    def calcular_cobro(self)->float:
        #calcular con self.trabajos 
        pass
    
