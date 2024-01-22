import argparse
from hw_suppDocs.modules_cli import iterate_entry

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description = 'Begins an algorithm that adds data into a .txt file, select -b to begin'
    )
    try:
        parser.add_argument(
            '-b', '-begin', metavar = 'begin',
            required = True, help = 'input an entry to add to a .txt file'
        )
        args = parser.parse_args()
        iterate_entry(args.write)

    except Exception as error:
        print(f"The error was: {error}")
    finally:
        print('Goodbye!')