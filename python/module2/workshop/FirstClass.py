class First:
    color:str
    nariz:bool
    boca:bool

    
    def __init__(self,color:str,nariz:bool, boca:bool) ->None:
        self.color=color
        self.nariz=nariz
        self.boca=boca
    
    def getColor(self)->str:
        return self.color

choice:str=input("Quieres que el First tenga boca y/n")
boca:bool=False
if(choice.lower()=="y"):
    boca=True   
    
first:First=First("red",True,boca)
print(first.boca)
print(first.getColor())




            
        