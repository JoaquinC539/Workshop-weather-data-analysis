from typing import List
class Coche:
    modelo:int
    # revisiones:List[Revision]=[]
    
    def __init__(self, modelo) -> None:
        self.modelo = modelo
        self.stack = []
    
    def push (self, element) -> list:
        self.stack.append(element)
        return self.stack

    def pop (self):
        return self.stack.pop(-1)
        