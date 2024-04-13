class Vehicle:
    color:str
    year:int
    license:bool
    
    def __init__(self,color:str,year:int,license:bool) -> None:
        self.color=color
        self.year=year
        self.license=license
        
    def set_color(self,color:str)->None:
        self.color=color
    
    def get_color(self)->str:
        return self.color
    
    def get_license(self)->bool:
        return self.license
    
    def set_license(self, license:bool)->None:
        self.license = license

    def get_year(self) ->int:
        return self.year

    def set_year(self, year:int) ->None:
        self.year = year

