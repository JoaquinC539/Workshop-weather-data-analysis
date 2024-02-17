from math import pi 



def mi_funcion():
    print('hola desde la funcion')

is_even = lambda num: True if (num % 2 == 0) else False
sum = lambda num1, num2: float(num1) + float(num2)
subtract = lambda num1, num2: float(num1) - float(num2)
multiply = lambda num1, num2: float(num1) * float(num2)
devide = lambda num1, num2: float(num1) / float(num2)
get_pi = lambda: pi

get_area = lambda radius: pi * (float(radius)**2)

get_perimeter = lambda radius: 2*pi * float(radius) 

def type_operation(choice):
    if(choice  == 'circulo'):
        circleOperation()
    elif choice == 'simple':
        print(simpleOperation())
    else:
        pass

def request_value():
    while True:
        radius = input('\nDa valor de radio\n')
        if(isinstance(float(radius),(int,float))):
            return radius
        else:
            print("\nValor invalido\n")
            continue
        
def request_simpleOp_value():
    numbers = []
    while True:
        num1 = input("\n Inserta el primer numero: ")
        if (isinstance(float(num1),(int,float))):
            numbers.append(num1)
            break
        else:
            continue
    while True:
        num2 = input("\n Inserta el segundo numero: ")
        if (isinstance(float(num2),(int,float))):
            numbers.append(num2)
            break
        else:
            continue
        
    return numbers

def validate_option():
    options = ['devide', 'multiply', 'sum', 'subtract']
    while True:
        userInput = input('Que tipo de operacion quieres (devide, multiply, sum, subtract)?')
        if (userInput not in options) and (userInput != '?'):
            print('This value is not valid, please try again')
            continue
        if userInput == '?':
            print('options are: devide, multiply, sum and subtract')
            continue
        else:
            return userInput

def simpleOperation():

    userInput = validate_option()
    if userInput == 'sum':
        values = request_simpleOp_value()
        result = sum(values[0],values[1])
        return result
    elif userInput == 'subtract':
        values = request_simpleOp_value()
        result = subtract(values[0],values[1])
        return result
    elif userInput == 'multiply':
        values = request_simpleOp_value()
        result = multiply(values[0],values[1])
        return result
    elif userInput == 'devide':
        values = request_simpleOp_value()
        result = devide(values[0],values[1])
        return result

def circleOperation():
    while True:
        typeCircleOperation=input(
            '\nQue tipo de operación quieres (perimetro o area)\n')
        if typeCircleOperation=='perimetro':
            radius = request_value()
            print(get_perimeter(radius))
            break
        elif typeCircleOperation=="area":
            radius = request_value()
            print(get_area(radius))
            break
        else:
            print('Opcion no disponible')
            continue


