class Persona:
    Nombre:str
    Edad:int
    Nacionalidad:str
    Altura:float
    Familia:bool
    Educacion:str
    Life_expect_average = 80

    def __init__(self,Nombre:str, Edad:int, Nacionalidad:str, Altura:float, Familia:bool, Educacion:str=None) -> None:
        if Educacion is not None:
            self.Educacion = Educacion
        self.Edad = Edad
        self.Nacionalidad = Nacionalidad
        self.Altura = Altura
        self.Familia = Familia


