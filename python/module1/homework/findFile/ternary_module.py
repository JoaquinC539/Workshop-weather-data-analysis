import os

def locate_path(path):
    #Pista no comparar rutas absolutas o tomar la ruta completamente y no compara actual con el del archivo,
    # tu debes formar las rutas abosultas o usar rutas relativas.
    absolute_path = os.path.abspath(path)
    working_dict = os.path.abspath(os.getcwd())

    if absolute_path == working_dict:
        return 'current'
    elif absolute_path.startswith(working_dict + os.path.sep):
        return 'child'
    elif working_dict.startswith(absolute_path + os.path.sep):
        return 'parent'   
## Esta función esta bien, solo necesitas usarla mas.
path_exists = lambda path: True if os.path.exists(path) else False

def path_exists_statement(path):
    ##Pista no necesitas los ifs aqui, solo la funcion locate
    if path_exists(path):
        return f'File exists in {locate_path(path)} folder'
    else:
        return 'File does not exist'