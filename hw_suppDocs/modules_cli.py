
def validate_options():
    options = ['write', 'read', 'clear', '']
    while True:
        userInput = input('Do you wish to read, write or clear from a file? (press "?" for help)\n')
        if (userInput not in options) and (userInput != '?') and (userInput != ''):
            print('This is not a valid option, please try again')
            continue
        elif userInput == '?':
            print('options are: "read", "write" or "clear"; leave blank to exit the program')
            continue
        else:
            return userInput

def select_option():
    choice = validate_options()
    if choice == 'write':
        add_txt()
    if choice == 'read':
        read_txt()
    if choice == 'clear':
        clear_txt()
    return choice

def iterate_entry():
    while select_option() != '':
        pass
        
# __________________________________________________________________________________________________________________________________________________________________________#
        
def add_txt():
    #List of values to create new line
    #newLineChars = [70, 140]
    #Open files to append characters as well as to read the length of each character
    txt_file = open('cli.txt', 'a')
    #txt_file = open('cli.txt', 'r')
    #text = txt_file.read()
    #Finds the length of the line
    #text_charcters = len(text)
    #Prompts user to append to entry
    userInp = input('Add text here...\n')
    txt_file.write(userInp)
    #### IF LENGTH OF CHARACTERS REACHES A CERTAIN AMOUNT, CREATE A NEW LINE, use len, and if len less than or equal to a certain amount IN A LIST, create a line \n
    #If the entry is larger than 70 characters, create a new line
    # for chars in text_charcters:
    #     count += 1
    #     if count % 70 == 0:
    #         print('')



    txt_file.close()

def read_txt():
    txt_file = open('cli.txt', 'r')
    text = txt_file.read()
    print(text)

def clear_txt():
    if caution_clear() == True:
        txt_file = open('cli.txt', 'w')
        txt_file.close()
        print('File has been cleared')
    else:
        pass

def caution_clear():
    clear = False
    while True:
        caution = input('Do you wish to clear this file?\nPress y to confirm, n to cancel\n')
        if caution == 'y':
            clear = True
            return clear
        else:
            return clear