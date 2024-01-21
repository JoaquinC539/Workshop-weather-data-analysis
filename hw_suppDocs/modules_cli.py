

def validate_options(choice):
    options = ['write', 'read']
    if choice not in options:
        print('option not valid, try again')
    else:
        pass

def select_option(choice):
    if choice == 'write':
        add_txt()
    if choice == 'read':
        read_txt()
        

def add_txt():
    txt_file = open('cli.txt', 'w')
    userInp = input('Add text here...\n')
    txt_file.write(userInp)
    txt_file.close()

def read_txt():
    txt_file = open('cli.txt', 'r')
    text = txt_file.read()
    print(text)
