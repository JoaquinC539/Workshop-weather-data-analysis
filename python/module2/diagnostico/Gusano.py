from Animal import Animal

class Gusano(Animal):
    def __init__(self, nombre:str, raza:str, edad:int) -> None:
        super().__init__(especie='insecto', alas=False, patas=False)
        self.name = nombre
        self.race = raza
        self.age = edad

    def avanzar(self) -> None:
        print('El gusano se arrastra con su cuerpo')