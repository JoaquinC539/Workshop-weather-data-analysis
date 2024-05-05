import argparse
from hw_suppDocs.file_existance_module import main

parser = argparse.ArgumentParser(description = 'Inputs a path that returns a found/not-found sentence')

parser.add_argument(
    '-o', '--operation', metavar = 'choice',
    required = True, help = ('''This program runs various types of task:\n"CheckExistance": Input a absolute path and check for its existance. 
                             User will be prompted the option to create file if not existant.\n"CreateFile" will create a .txt file with a given name.
                             \nRead: Reads the content of the file\nEdit: Edits the contents of the file\nAdd: Adds text to a file'''),
    choices=['CheckExistance', 'CreateFile', 'Edit', 'Read', 'Add']
)
try:       
    args = parser.parse_args()
    print(main(args.choice))
except Exception as error:
    print(f'An error has occured: {error}')