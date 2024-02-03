def validate_options(choice):
    choiceList = ['write', 'read', 'clear']
    if choice not in choiceList:
        return False
    else:
        return True

def caution_clear():
    clear = False
    while True:
        caution = input('Do you wish to clear this file?\nPress y to confirm, n to cancel\n')
        if caution == 'y':
            clear = True
            return clear
        else:
            return clear

# __________________________________________________________________________________________________________________________________________________________________________#

def add_txt():
    txt_file = open('cli.txt', 'a')
    userInp = input('Add text here...\n')
    txt_file.write(userInp)
    #Agregar un print que diga que se escribio correctamente
    txt_file.close()

def read_txt():
    txt_file = open('cli.txt', 'r')
    text = txt_file.read()
    print(text)
    txt_file.close()

def clear_txt():
    if caution_clear() == True:
        txt_file = open('cli.txt', 'w')
        txt_file.close()
        print('File has been cleared')
    else:
        pass

# __________________________________________________________________________________________________________________________________________________________________________#

def select_option(choice):
    if validate_options(choice) == False:
        print('Invalid Option')
    else:
        if choice == 'write':
            add_txt()
        if choice == 'read':
            read_txt()
        if choice == 'clear':
            clear_txt()
        return choice