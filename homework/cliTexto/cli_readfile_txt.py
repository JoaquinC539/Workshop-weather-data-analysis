import argparse
from cli_module_readfile import select_option

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description = 'Begins an algorithm that adds data into a .txt file, select -b to begin'
    )
    try:
        parser.add_argument(
            #Nombre un incorrecto de metavar y banderas, aqui va el tipo de operación begin no es leer
            #Agregar choices
            '-b', '--begin', metavar = 'beginProgram', #### CHANGE NAME -o, -- operacion, methavar = operacion
            required = True, help = 'input an entry to add to a .txt file; options are begin, write and clear',
            choices = [] #### choices 'read', 'write', 'clear'
        )
        args = parser.parse_args()
        #usar valor de metaravariable no de banderas.
        select_option(args.b)
        
        

    except Exception as error:
        print(f"The error was: {error}")
    finally:
        print('Goodbye!')