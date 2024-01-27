import os

def locate_path(path):
    absolute_path = os.path.abspath(path)
    working_dict = os.path.abspath(os.getcwd())

    if absolute_path == working_dict:
        return 'current'
    elif absolute_path.startswith(working_dict + os.path.sep):
        return 'child'
    elif working_dict.startswith(absolute_path + os.path.sep):
        return 'parent'   

path_exists = lambda path: True if os.path.exists(path) else False

def path_exists_statement(path):
    if path_exists(path):
        return f'File exists in {locate_path(path)} folder'
    else:
        return 'File does not exist'