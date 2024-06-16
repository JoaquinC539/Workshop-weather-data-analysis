from Persona import Persona
import random as rd

class Alcoholic(Persona):
    Drogas: bool
    Alcoholic:bool
    Fumador: bool

    def __init__(self, Nombre:str,Edad:int, Nacionalidad:str, Altura:int, Familia:bool, Drogas:bool=False, Fumador:bool=False, Educacion:str = None)  -> None:
        super().__init__(Nombre,Edad, Nacionalidad, Altura, Familia, Educacion)

        self.Drogas = Drogas
        self.Alcoholic = True
        self.Fumador = Fumador

    def get_life_expectancy(self):
        if self.Alcoholic:
            self.Life_expect_average -=10
        if self.Drogas:
            self.Life_expect_average -= 20
        if self.Fumador:
            self.Life_expect_average -= 5
        
        return self.Life_expect_average
        
nombres=["John","Jack","Jane","Kevin","Steve","Peter","Karla","Laura","Robert"]
edades = [31, 21, 57, 34, 23, 86, 45, 39, 19,17,28,29,10]
nacionalidades=["USA","Mex","Arg","Esp","Vzl"]
alturas=[1.4, 2.3, 2.1, 1.9, 2.0, 2.6, 2.5, 5.7]

alcoholicos:list = []

for i in range(10):
    name = rd.choice(nombres)
    edad = rd.choice(edades)
    nacionalidad = rd.choice(nacionalidades)
    altura = rd.choice(alturas)
    drogas:bool=rd.choice([True,False])
    fumador:bool=rd.choice([True,False])
    familia:bool=rd.choice([True,False,None])

    alcoholico=Alcoholic(name, edad, nacionalidad, altura, familia, drogas, fumador)
    alcoholicos.append(alcoholico)

for alcoholico in alcoholicos:
    alc:Alcoholic=alcoholico
    # print(alc.Nombre)
    print(alc.Drogas)
    print(alc.Fumador)
    print(alc.get_life_expectancy())
    print("******************************")
    # print(alcoholico.get_life_expectancy())






    


