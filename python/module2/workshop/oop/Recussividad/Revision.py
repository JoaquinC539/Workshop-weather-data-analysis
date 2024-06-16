from Coche import Coche

class Revision(Coche):    
    
    def __init__(self,modelo) -> None:
        super().__init__(modelo)


    def revision(self, instruccion):
        self.push(instruccion)
        # super().__init__(modelo)
        # self.descripcion=descripcion
        