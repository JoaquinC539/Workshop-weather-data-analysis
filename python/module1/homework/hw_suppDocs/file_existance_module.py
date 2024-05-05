import os 

def main(choice):
    if choice == 'CheckExistance':
        path = input('Please enter a absolute path to check for existance:\n')
        check_existance(path)
        if check_existance(path) == False:
            choice = input(f"file '{path}' does not exist. Do you wish to create it? y/n:\n")
            if choice == 'y' or choice == 'yes':
                file_name = input('Enter a file name for your new file:\n')
                create_file(file_name)
            else:
                print('Goodbye!')
    elif choice == 'CreateFile':
        file_name = input('Chose a file name:\n')
        create_file(file_name)
    elif choice == 'Read':
        read_file()
    elif choice == 'Edit':
        edit_file()
    elif choice == 'Add':
        add_to_file()
    else:
        print('Choice not available... Select the -h flag for help')

def check_existance(path):
    try:
        if os.path.exists(path):
            print(f'Path Location: {os.path.dirname(path)} folder')
            return True
        else:
            return False
    except Exception as error:
        print('There was an error in the file existance checker: '+ error)

def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write('hello world!')
    except Exception as error:
        print(f'File failed to be created due to an error: {error}')

def read_file():
    path = input('Enter a file path to read:\n')
    if check_existance(path):
        with open(path, 'r') as file:
            content = file.read()
            print(content)
    else:
        print(f'File {path} doesnt exist')
        
def edit_file():
    path = input('Enter a file path to edit:\n')
    entry = input('Enter what you wish to edit. Caution! This action will delete previous content!\n')
    if check_existance(path):
        with open(path, 'w') as file:
            file.write(entry)
        print('Changes successfully saved')
    else:
        print(f'File {path} doesnt exist')

def add_to_file():
    path = input('Enter a file to add to:\n')
    entry = input('Enter what you wish to edit:\n')
    if check_existance(path):
        with open(path, 'a') as file:
            file.write(entry)
        print('Changes successfully saved')
    else:
        print(f'File {path} doesnt exist')