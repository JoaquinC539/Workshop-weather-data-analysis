from Vehicle import Vehicle
import random as rd
###
class Car(Vehicle):
    longitude:int
    wheels:int
    passenger_cap:int
    doors:int
    AC:bool
    
    def __init__(self, color: str, year: int, license: bool,longitude:int,AC:bool,doors:int,passenger_cap:int,wheels:int) -> None:        
        super().__init__(color,year,license)
        self.longitude=longitude
        self.wheels=wheels
        self.passenger_cap=passenger_cap
        self.doors=doors
        self.AC=AC
    
    def oracion_color(self):
        return "The color of the car is: "+self.color
    
cars_flock:list=[]

for i in range(10):
    random_color = rd.choice(['red', 'blue', 'green', 'white', 'gray', 'black', 'pink'])
    random_year= rd.choice([1999, 2024,2014,2013,2012,2011])

    car:Car=Car(random_color,random_year,True,2,True,4,6,4)
    cars_flock.append(car)
    
for car in cars_flock:
    print(car.oracion_color())




