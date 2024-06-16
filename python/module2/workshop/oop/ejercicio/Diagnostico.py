from Trabajo import Trabajo
from TipoTrabajo import TipoTrabajo

class Diagnostico(Trabajo):
    
    estimated_time:float
    employee_number:int
    tipo_trabajo: TipoTrabajo
    pieza_revisada:str
    comentario:str
    
    def __init__(self, pieza_revisada:str) -> None:
        self.pieza_revisada = pieza_revisada
        self.comentario = ''
        self.estimated_time = None
        self.employee_number = None
        self.tipo_trabajo = None   
     
    def set_estimate_time(self,tiempo: float) -> None:
        self.estimated_time = tiempo

    def set_employee_number(self,number:int) -> None:
        self.employee_number=number

    def set_tipo_trabajo(self,tipo_trabajo:TipoTrabajo) -> None:
        self.tipo_trabajo=tipo_trabajo

    def set_comentatio(self, comenterio: str) -> None:
        self.comentario = comenterio