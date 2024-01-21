import argparse
from hw_suppDocs.modules_cli import select_option

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description = 'Excribe nombres sobre un expediente .txt, select -w to writre an entry or -r to read the text file'
    )
    try:
        parser.add_argument(
            '-w', 'write', metavar = 'input',
            required = True, help = 'input an entry to add to a .txt file'
    
        )
        parser.add_argument(
            '-r', '-read', metavar = 'read file',
            required = True, help = 'reads .txt file... if file is empty, it will return None. To add an entry to the file, please select the -read option'

        )

        args = parser.parse_args()
        select_option(args.x)

    except Exception as error:
        print(f"The error was: {error}")
    finally:
        print('Goodbye!')