from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, especie:str, alas:bool, patas:bool) -> None:
        self.species = especie
        self.wings = alas
        self.paws = patas
        
    @abstractmethod
    def avanzar(self) -> None:
        return NotImplementedError('Cannot instantiate abstract class')
        # pass
    
    def decir_especie(self)->None:
        print(f"Mi especie es: {self.species}")
    

