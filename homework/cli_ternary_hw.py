import argparse
from ternary_module import path_exists_statement

if __name__ == '__main__':

    try:

        parser = argparse.ArgumentParser(
            description= 'Inputs a path that returns a found/not-found sentence'
        )

        parser.add_argument(
            '-p', '--path',
            required = True, help = 'imput a path that will be checked for existance'
        )
        

        args = parser.parse_args()
        print(path_exists_statement(args.path))

    except SyntaxError:
        print('File could not due to incorrect pathing')