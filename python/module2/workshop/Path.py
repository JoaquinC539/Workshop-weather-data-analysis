class Path:
    pathFile:str=None
    
    def __init__(self,pathFile:str=None) -> None:
        if(pathFile==None):
            pass
        else:
            self.pathFile=pathFile
        
    def updatePathFile(self,pathFile:str)->None:
        self.pathFile=pathFile
        
    def getPathFile(self)->str:
        return self.pathFile
        
path:Path=Path()

def my_func()->None:
    path.updatePathFile("./i.py")
    print(path.getPathFile())
my_func()


    
    