from Animal import Animal


class Perro(Animal):
    def __init__(self, nombre:str, raza:str, edad:int) -> None:
        super().__init__(especie='canino', alas=False, patas=True)
        self.name = nombre
        self.race = raza
        self.age = edad

    def ladrar(self) -> None:
        print('WOOOOOOFFFF!')

    def avanzar(self) -> None:
        print('El perro camina con sus cuatro patas')
