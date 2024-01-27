import argparse
from cli_module_readfile import select_option

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description = 'Begins an algorithm that adds data into a .txt file, select -b to begin'
    )
    try:
        parser.add_argument(
            '-b', '-begin', metavar = 'beginProgram',
            required = True, help = 'input an entry to add to a .txt file; options are begin, write and clear'
        )
        args = parser.parse_args()
        select_option(args.b)
        

    except Exception as error:
        print(f"The error was: {error}")
    finally:
        print('Goodbye!')