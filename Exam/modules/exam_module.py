import random as rd
import os
import json

# ESSENTAIL FUNCTIONS: CREATE, CLEAR, EDIT & DISPLAY

### _____________________________________________________________________________________________________________________________________________________________________ ###
                                                                     # START-UP FUNCTIONS #

x = [{'ID': 123,'hello':2,'hi':3}, {'ID':234, 'hey':4, 'greetings': 5}]

def operation_type(operation):
    if validate_operation(operation):
        if operation == 'create':
            create_board()
        elif operation == 'clear':
            clear_board()
        elif operation == 'edit':
            edit_board()
        elif operation == 'display':
            display_board()
    else:
        return 'invalid option. Select " -h" for details'

#print(operation_type('hseufhsf'))
        
validate_operation = lambda operation: True if operation == 'create' or operation == 'clear' or operation == 'edit' or operation == 'display' else False

### _____________________________________________________________________________________________________________________________________________________________________ ###
                                                                       # .JSON START-UP #
#path = 'Exam\modules\exam.json'
path = 'modules/exam.json'

def load_json():                            ### PULLS JSON DICTIONARY INFORMATION ###
    if os.path.exists(path):
        with open(path, 'r') as file:
            data = json.load(file)
            return data
    else:
        print('File not existent. Please fix path')
        return False

def append_json(message):
    with open(path, 'a') as file:
        json.dump(message, file, indent=2)

data = load_json()

#print(type(data))

### _____________________________________________________________________________________________________________________________________________________________________ ###
                                                                    # OPERATIONAL FUNCTIONS #

def prompt_msg():
    message = input('Please enter a message:\n')
    return message

def prompt_select():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    selection = input('Please select a board:\n')
    characters = []
    if len(selection) > 8 or len(selection) < 8:
        return 'Invalid ID; must be 8 characters'

    for character in selection:
        if character in alphabet:
            character = character.upper()
            characters.append(character)
        if character in numbers:
            characters.append(character)

    id = ''
    for elements in characters:
        id += elements

    return id

# print(prompt_select())

def generate_id():                              ### WILL GENERATE AN ID USING RANDOM CHARACTERS... WILL BE USED WHEN CREATING A BOARD ###
    id = ''
    charcters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(8):
        charcter = rd.choice(charcters)
        id += charcter
    return id 

def create_board():                    ### CREATES A BOARD THAT WILL CALL THE WRITE_FUNC() AT CREATION ONLY. THE EDIT FUNCTION WILL THEN EDIT THE BOARD AFTER ###
    message = prompt_msg()
    id = generate_id()                         ### PROBLEM: DOESNT SEPARATE DISCTS WITH COMMAS. PERHAPS ATTEMPT TO IMPLEMENT A LIST SORROUNDING DICTS
    
    new_board = {'ID': id, 'entry': str(message)}
    list_json = load_json()
    result = list_json.append(new_board)

    with open(path, 'w') as file:
        json.dump(result, file, indent=2)


create_board()

def edit_board():
    selection = prompt_select()
    new_message = prompt_msg()
                                                    # How to edit a selected component in JSON?
    for dictionary in data:
        if dictionary['ID'] == selection:
            dictionary['entry'] = new_message

    return 'invalid ID dictionary:', selection

#edit_board()

def select_board():                             ### THIS FUNCTION WILL SELECT A SPECIFIC BOARD TO DO AN OPERATION ON ###
    selection = prompt_select()
    
    for dictionary in data:
        if dictionary['ID'] == selection:
            return dictionary
    return f'ID: "{selection}" not found'

#print(select_board())

def display_board():
    dict = select_board()
    print('\n' + ' '*30 + '*** BOARDS ***\n')
    print(f"{dict['ID']}\n{dict['entry']}\n")

#display_board()

def caution_clear():
    caution = input('Are you sure you want to delete this board? y/n:\n')
    if caution == 'yes' or caution == 'y':
        print('Board has been deleted')
        return True
    else:
        print('Action Cancelled')
        return False

def clear_board():
    board = select_board()                # How to clear a selected board in JSON?
    if caution_clear():
        with open(path, 'w') as file:
            json.dump(board, file, indent=2)

#clear_board()

### _____________________________________________________________________________________________________________________________________________________________________ ###