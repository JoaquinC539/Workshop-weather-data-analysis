class DaniCabesaException(Exception):
    print("Soy el error personalizado")
    pass

x = 7

# try:
#     raise DaniCabesaException("El problema es problema")
#     # raise Exception("Dani es cabesa")
#     # print(x/0)
# except ZeroDivisionError as error:
#     print("Uy "+error)
# # except NameError:
# #     print("La variable no existe")
# except Exception as error:
#     print(f"El error es: {error}")
# finally:
#     print("Dany es un cabeSa")


try:
    user=input("Inserta caulquier valor\n")
    user = int(user)
    print(type(user))
    if(type(user)=='str'):
        print("Esto es un string")
except Exception as error:
    print(error)

