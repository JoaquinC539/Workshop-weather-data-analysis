import datetime
x:int=5
fecha:datetime=datetime.datetime.now()

def suma(a:float,b:int)->int:
    a=int(a)
    print(a)
    return a+b
def hello()->None:
    print("Soy una funcion sin retorno")
print(suma(5.1,4))
hello()

l:list=list("a")
l.append("b")
tup:tuple=tuple(l)
print(tup.index("a",0,1))
print(tup)

sies:bool=bool("True")
print(sies)