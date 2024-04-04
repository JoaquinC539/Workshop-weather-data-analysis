people_data = [
{"name": "John", "height": 175, "age": 30},
{"name": "Alice", "height": 160, "age": 25},
{"name": "Bob", "height": 180, "age": 35},
{"name": "Emily", "height": 165, "age": 28},
{"name": "Michael", "height": 185, "age": 40}
]


class GetPerson:

    def __init__(self, people_list) -> None:
        self.individual = people_list

class GetData(GetPerson):

    def __init__(self, my_list:list, attribute:str, value: Union[int, float, str]) -> None:
        super().__init__(my_list)
        self.attribue = attribute
        self.value = value
        
    def getName(self):
        for person in self.individual:
            if person[self.attribue] == self.value:
                return '\n' + person['name'] + '\n'
            
        return f'\nIndividual does not exist with given attribute: {self.attribue[0].upper() + self.attribue[1:]} of {self.value}\n'
    
x = GetData(people_data, 'age', 37)
name = x.getName()
print(name)
