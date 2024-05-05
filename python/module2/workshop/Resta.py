class Resta:
    x:int=10    
    t:int
    
    def __init__(self) -> None:
        pass
    
    def llamado_resta(self,a:int,b:int)->int:
        return self.resta(a,b)
    @classmethod
    def resta(cls, a:int, b:int)->int:
        print(cls.resta_cuadrada(100,1))
        return a-b
    
    @classmethod
    def resta_cuadrada(cls,a:int,b:int)->int:
        a=a*a
        b=b*b
        return a-b
    
    
    
resta:Resta = Resta()
print(Resta.resta(10,5))

print(Resta.x)
#print(Resta.t) #Error al estar indefinido