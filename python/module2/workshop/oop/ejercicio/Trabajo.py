from abc import ABC,abstractmethod
from TipoTrabajo import TipoTrabajo
class Trabajo(ABC):

    @abstractmethod
    def set_estimate_time(self,tiempo:float)->None:
        return NotImplementedError("Not implemented set_estimate_time")

    @abstractmethod
    def set_employee_number(self,number:int) -> None:
        return NotImplementedError("Not implemented set_employee_number")
    
    @abstractmethod
    def set_tipo_trabajo(self,tipo_trabajo:TipoTrabajo) -> None :
        return NotImplementedError("Not implemented set_tipo_trabajo")
        
    @abstractmethod
    def set_comentatio(self,comenterio:str) -> None:
        return NotImplementedError("Not implemented set_comentario")
        
    

    