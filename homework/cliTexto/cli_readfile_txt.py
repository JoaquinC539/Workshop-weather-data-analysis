import argparse
from cli_module_readfile import select_option

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description = 'Begins an algorithm that manipulates data within a .txt file, start ( --operation ) to chose a type of operation [wite, read, clear]'
    )
    try:
        parser.add_argument(

            '-o', '--operacion', metavar = 'operacion',
            required = True, help = 'input an entry to a .txt file; options are write, read and clear',
            choices = ['read', 'write', 'clear'] 
        )
        args = parser.parse_args()
        
        select_option(args.operacion)

    except Exception as error:
        print(f"The error was: {error}")
    finally:
        print('Goodbye!')