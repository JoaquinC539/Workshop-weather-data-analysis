import random as rd
import os
import json

# ESSENTAIL FUNCTIONS: CREATE, CLEAR, EDIT & DISPLAY

### _____________________________________________________________________________________________________________________________________________________________________ ###
                                                                     # START-UP FUNCTIONS #
x = [{'boardID': 123,'hello':2,'hi':3}, {'boardID':234, 'hey':4, 'greetings': 5}]

def operation_type(operation, message, selection, new_message):
    if validate_operation(operation):
        if operation == 'create':
            create_board(message)
        elif operation == 'clear':
            clear_board()
        elif operation == 'edit':
            edit_board(selection, new_message)
        elif operation == 'display':
            display_board()
    else:
        return 'invalid option. Select " -h" for details'

def validate_operation(operation):
    choices = ['create', 'clear', 'edit', 'display']
    if operation in choices:
        return True
    else:
        return False

### _____________________________________________________________________________________________________________________________________________________________________ ###
                                                                       # .JSON START-UP #
path = 'Exam\modules\exam.json'

def load_json():                            ### PULLS JSON DICTIONARY INFORMATION ###
    if os.path.exists(path):
        with open(path, 'r') as file:
            data = json.load(file)
            return data
    else:
        print('File not existent. Please fix path')
        return False

def append_json(data):
    with open(path, 'a') as file:
        json.dump(data, file, indent=2)

data = load_json()

### _____________________________________________________________________________________________________________________________________________________________________ ###
                                                                    # OPERATIONAL FUNCTIONS #

def generate_id():                              ### WILL GENERATE AN ID USING RANDOM CHARACTERS... WILL BE USED WHEN CREATING A BOARD ###
    id = ''
    charcters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    for i in range(8):
        charcter = rd.choice(charcters)
        id += charcter
    return id 

def create_board(messsage):                    ### CREATES A BOARD THAT WILL CALL THE WRITE_FUNC() AT CREATION ONLY. THE EDIT FUNCTION WILL THEN EDIT THE BOARD AFTER ###
    id = generate_id()                         ### PROBLEM: DOESNT SEPARATE DISCTS WITH COMMAS. PERHAPS ATTEMPT TO IMPLEMENT A LIST SORROUNDING DICTS
    new_board = {'boardID': id, 'entry': str(messsage)}
    append_json(new_board)

create_board('hi')

def select_board(selection):                             ### THIS FUNCTION WILL SELECT A SPECIFIC BOARD TO DO AN OPERATION ON ###
    data = load_json()
    for dictionary in data:
        if dictionary['boardID'] == selection:
            return dictionary
    return f'ID: "{selection}" not found'

#print(select_board('HZE4RXK4'))

def edit_board(selection, new_entry):
    data = load_json()
    board = select_board(selection)
                                                    # How to edit a selected component in JSON?
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)

    return board

#print(edit_board('HZE4RXK4', 'hi world'))

def display_board():
    data = load_json()
    print('\n' + ' '*30 + '*** BOARDS ***\n')
    for dicts in data:
        print(f'ID: {dicts['boardID']}\n{dicts['entry']}\n')

#display_board()

def clear_board(selection):
    board = select_board(selection)                # How to clear a selected board in JSON?
    with open(path, 'w') as file:
        json.dump(board, file, indent=2)
    return 'file has been deleted'

#clear_board('123ABC')

def caution_clear():
    caution = input('Are you sure you want to delete this board? y/n:\n')
    if caution == 'yes' or caution == 'y':
        print('Board has been deleted')
        pass # Clear board here
    else:
        print('Auction Cancelled')


### _____________________________________________________________________________________________________________________________________________________________________ ###

# def main():
#     load_json()
#     x = []
#     append_json(x)
