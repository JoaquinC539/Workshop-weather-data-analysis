# def my_function_builder(n):
#     lambda_func = lambda num: n+num
#     return lambda_func
# # Returns: <function my_function_builder.<locals>.<lambda> at 0x00000256783D8C20>
# my_lambda = my_function_builder(5)
# # my lamda tiene asi = lambda num: 5+num
# result=my_lambda(6)

#print(my_lambda) # == 11

'''
Funcion anonima es una funcion pura
'''
# my_func = lambda num: num**2

# x=my_func(3)

from functools import reduce

# total = reduce(lambda accumulated, current:accumulated+current,numbers,0)

# print(total)

mi_nueva_lista = map(lambda argument:"Dani es: "+argument, ('Banana', 'Manzana', 'Kiwi'))

#print(list(mi_nueva_lista[0]))
# dani_es = lambda argument:"Dani es: " + argument
# print(dani_es("Banana"))

# for line in mi_nueva_lista:
#     print(line)

# me_gusta = lambda fruta: 'Me gusta ' + fruta
# lista = ['naranja', 'manzana', 'sandia']

def mi_map_personalizado(lambda_func,lista):
    to_retu = []
    for arg in lista:
    #    x = lambda argu: 'Me gusta ' + argu
       to_retu.append(lambda_func(arg))
    
    return to_retu

# print(mi_map_personalizado(me_gusta, lista))


##filter() recibe dos argumentos el primero es una funcion lambda o definida Y la otra es una lista o tupla en la que se itera

numbers = [2,6,8,14,58,23,64]
# filter_lambda=lambda nums: True if (nums < 15) else False

# lista_filtrada = filter(filter_lambda,numbers)

# print(list(lista_filtrada))

# print(type(lista_filtrada))

def my_filter(lambda_function, list):
    x = []
    for element in list:
        if lambda_function(bool(element)):
            x.append(element)
        else:
            pass            
    return x

filter_lambda = lambda nums: True if (nums < 15) else False

print(my_filter(filter_lambda, numbers))