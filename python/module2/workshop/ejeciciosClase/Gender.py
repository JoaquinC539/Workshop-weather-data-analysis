from enum import Enum

class Gender(Enum):
    MALE="Male"
    FEMALE="Female"
    POLYGENDER="Polygender"
    NONBINARY = "Non-binary"
    QUEER = 'Genderqueer'
    BIGENDER = 'Bigender'
    
    
    def get_enum_by_value(value):
        for member in Gender:
            if member.value==value:
                return member
            