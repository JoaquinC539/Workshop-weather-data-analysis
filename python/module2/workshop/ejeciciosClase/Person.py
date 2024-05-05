
from Gender import Gender


class Person:

    id: int
    first_name: str
    last_name: str
    age: int
    gender: Gender
    
    def __init__(self, id:int, first_name:str, last_name:str, age:int, gender:Gender) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return f'Person:[ id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age}, gender: {self.gender}]'
    
    def get_first_name(self) -> str:
        return self.first_name

    def get_gender(self) -> Gender:
        return self.gender




