import argparse
from ternary_module import path_exists_statement

if __name__ == '__main__':

    try:

        ## El cli recibe el nombre de un archivo con su extensión no un path
        
        parser = argparse.ArgumentParser(
            description= 'Inputs a path that returns a found/not-found sentence'
        )

        parser.add_argument(
            '-p', '--path', metavar = 'file',
            required = True, help = 'imput a path that will be checked for existance'
        )
        ##Usar metavar parainterpretar el valor al ser compilado por el parser (parse_args()) no dejas
        #a ala interpetación de python a las banderas

        args = parser.parse_args()
        print(path_exists_statement(args.path))

    except SyntaxError:
        print('File could not due to incorrect pathing')