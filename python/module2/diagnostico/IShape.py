from abc import ABC, abstractmethod
#Interfaz
class IShape(ABC):
    
    @abstractmethod
    def perimetro(self) -> float:
        return NotImplementedError('Cant implement interface method')

    @abstractmethod
    def area(self) -> float:
        return NotImplementedError('Cant implement interface method')

