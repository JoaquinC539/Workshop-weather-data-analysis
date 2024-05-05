import json
import os
from typing import List
from Person import Person
from Gender import Gender
path_file="MOCK_DATA.json"

def load_people():
    # Cargar las tareas desde el archivo JSON
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return json.load(f)
    else:
        return []

data = load_people()
person_lambda=lambda person_data:Person(person_data["id"],person_data["first_name"],
                                        person_data['last_name'], person_data['age'],
                                        Gender.get_enum_by_value(person_data["gender"]) )
data_persons:List[Person]=list(map(person_lambda,data))

