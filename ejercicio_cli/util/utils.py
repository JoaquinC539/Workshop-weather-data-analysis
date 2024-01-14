from math import pi

def mi_funcion():
    print('hola desde la funcion')

is_even = lambda num: True if (num % 2 == 0) else False
sum = lambda num1, num2: num1 + num2
subtract = lambda num1, num2: num1 - num2
multiply = lambda num1, num2: num1 * num2
get_pi = lambda: pi

get_area = lambda radius: pi * (radius**2)

get_perimeter = lambda radius: 2*pi * radius

def type_operation(choice):
    if(choice  == 'circle'):
        print("circle operacion")
        circleOperation()
    else:
        pass

def request_value():
    while True:
        radius = input('\nDa valor de radio\n')
        if(radius.isdigit()):
            return radius
        else:
            print("\nValor invalido\n")
            continue
        

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


