
import os
import json

# __________________________________________________________ GLOBALS ____________________________________________________________ #

pathFile = './tasks.json'

numerical_id = 1

# ____________________________________________________________ MAIN ____________________________________________________________ #

def validate_path_format(input_path):

    if not isinstance(input_path, str):
        print("Error: Input should be a string representing a path.")
        return False
    
    path = os.path.normpath(input_path)
    if os.path.isabs(path):
        return True
    
    else:
        print("Error: The provided path is not in a valid format.")

    return False

def command_selection(choice):
    choice = choice.strip().lower()
    if validate_choice(choice):
        if choice == 'create':
            create_task()
        elif choice == 'display':
            display_tasks()
        elif choice == 'select':
            select_task()
        elif choice == 'edit':
            edit_task()
        elif choice == 'delete':
            delete_task()
        elif choice == 'status':
            change_status()

def main(choice):
    command_selection(choice)

# _____________________________________________________ JSON / Utility _____________________________________________________ #

def load_json():
    try:
        if os.path.exists(pathFile):
            with open(pathFile,"r") as file:
                data = json.load(file)
                return data
        else:
            return "JSON file not existant. Utilize the create command to initalize a task"
    except Exception as error:
            print(f"There was and error reading the json file: {error}")

def validate_choice(choice):
    choices=['create', 'edit', 'display', 'select', 'delete', 'status', '']
    if choice not in choices:
        print(f'Invalid selection: {choice}. Use -h flag for available commands.')
        return False
    else:
        return True

def prompt_entry():
    entry = input('Please enter a description:\n')
    if entry == '':
        return False
    return entry

def input_isinteger(str):
    try:
        int(str)
        return True
    except ValueError:
        print('Input not acceptable. Must be a number without decimals.\n')
        return False

def caution_delete():
    choice = input('Are you sure you wish to delete this task? y/n:\n')
    choice = choice.strip().lower()
    if choice == 'y' or choice == 'yes' or choice == 'yeah':
        return True
    else:
        return False

# _____________________________________________________ COMMAND FUNCTIONS _____________________________________________________ #

def create_task():
    # global numerical_id
    try:

        if not os.path.exists(pathFile):
            with open(pathFile, 'w') as file:
                description = prompt_entry()
                if description:
                    initialize_arrray = {}
                    task = {'id': 1,#numerical_id,
                            'description': description,
                            'completion': False
                            }
                    initialize_arrray['tasks'] = [task]
                    json.dump(initialize_arrray, file, indent=2)
                    print('Task added\n')

                else:
                    print('Action canceled.\n')

        else:
            data = load_json()
            if data == None:
                data = {'tasks':[]}
            description = prompt_entry()
            if description:
                task = {'id': len(data['tasks']) + 1,#numerical_id,
                            'description': description,
                            'completion': False
                            }
                data['tasks'].append(task)
                with open (pathFile, 'w') as file:
                    json.dump(data, file, indent=2)
                print('Task added\n')

            else:
                print('Action canceled.\n')

        # numerical_id += 1 # Error here, the global variable doesnt increase in value
    except Exception as error:
        print(f'Error ocurred when creating a task: {error}')

def display_tasks():
    try:
        data = load_json()
        if data != None:
            for i in range(len(data['tasks'])):
                values = list((data['tasks'][i]).values())
                print(f'Numerical ID:                 {values[0]}')
                print(f'Description:                  {values[1]}')
                if values[2] == True:
                    print(f'Status:                       Completed')
                else:
                    print(f'Status:                       Incomplete')
                print('___________________________________________\n')
        else:
            print('The file is empty. Please use the "Create" command to add a task\n')

    except Exception:
        print(f'Cannot display information on a non-existent file. Please create a task beforehand.\n')

def select_task():
    data = load_json()
    try:

        if (data != None) or (os.path.exists(pathFile)):
            choice = input('Please pick an option for selection. This may be by "numerical id" or "completion status" of the tasks :\n')
            choice = choice.strip().lower()
            choice_by_id = ['id', 'numerical id', 'num', 'number', 'numerical']
            choice_by_status = ['completion', 'status', 'completion status']
            if choice in choice_by_id:
                selected_id = input('Select a numerical id from a task to display\n')
                selected_id = selected_id.strip()
                if input_isinteger(selected_id):
                    selected_id = int(selected_id)
                    print('___________________________________________\n')
                    for dict in data['tasks']:
                        if dict['id'] == selected_id:
                            values = list(dict.values())
                            print(f'Numerical ID:                 {values[0]}')
                            print(f'Description:                  {values[1]}')
                            if values[2] == True:
                                print(f'Status:                       Completed')
                            else:
                                print(f'Status:                       Incomplete')
                            print('___________________________________________\n')
                            
                    print('ID not found. Please try again or use the display command to visualize your tasks.\n')
            
            elif choice in choice_by_status:
                select_status = input('Do you wish to display "Completed" or "Incompleted"?\n')
                select_status = select_status.strip().lower()
    
                if select_status == 'completed':
                    completed_task_list = [index for index in range(len(data['tasks'])) if data['tasks'][index]['completion'] == True]
                    print('___________________________________________\n')
                    for index in completed_task_list:

                        values = list((data['tasks'][index]).values())
                        print(f'Numerical ID:                 {values[0]}')
                        print(f'Description:                  {values[1]}')
                        print(f'Status:                       Completed')
                        print('___________________________________________\n')


                elif select_status == 'incompleted':
                    incompleted_task_list = [index for index in range(len(data['tasks'])) if data['tasks'][index]['completion'] == False]
                    print('___________________________________________\n')
                    for index in incompleted_task_list:

                        values = list((data['tasks'][index]).values())
                        print(f'Numerical ID:                 {values[0]}')
                        print(f'Description:                  {values[1]}')
                        print(f'Status:                       Incompleted')
                        print('___________________________________________\n')

                else:
                    print('Invalid choice. Please check spelling. Options are "completed" or "incompleted"\n')

            else:
                print('Option not available. Options are "numerical id" or "completion status".\n')
        else:
            if data != None:
                print('May not select task from an empty file. For assistance, use the -h flag.')
            elif not os.path.exists(pathFile):
                print('May not select a task from a non-existant file. For assistance, use the -h flag.')

    except Exception as error:
        print(f'Error occured when selecting a task... Error: {error}')

def delete_task():
    try:
        count = 0
        data = load_json()
        id_selection = input('Select a task by numerical id to delete:\n')
        if input_isinteger(id_selection):

            id_selection = int(id_selection)
            # CHECK IF ID EXISTS
            for dict in data['tasks']:
                if dict['id'] == id_selection:
                    count += 1
            if count > 0:
                if caution_delete():
                    new_data = {'tasks':[]}
                    for dict in data['tasks']:
                            if dict['id'] != id_selection:
                                new_data['tasks'].append(dict)
                    with open(pathFile, 'w') as file:
                        json.dump(new_data, file, indent=2)
                    print('Task deleted successfully.\n')

                else:
                    print('Action canceled')

            else:
                print("ID doesn't exist.\n")

    except Exception as error:
        print(f'There was an error when deleting a task. Error: {error}')

def edit_task():
    try:
        count = 0
        data = load_json()
        id_selection = input('Select a task by numerical id to edit:\n')
        if input_isinteger(id_selection):
            id_selection = int(id_selection)
            # CHECK IF ID EXISTS
            for dict in data['tasks']:
                if dict['id'] == id_selection:
                    count += 1
            if count > 0:

                entry = input('Write an entry to change:\n')
                new_data = {'tasks':[]}
                for task in data['tasks']:
                    if task['id'] == id_selection:
                        task['description'] = entry
                    new_data['tasks'].append(task)

                with open(pathFile, 'w') as file:
                    json.dump(new_data, file, indent=2)
                print('Changes saved successfully.\n')

            else:
                print("ID doesn't exist")
        
    except Exception as error:
        print(f'There was an error when editing a task: {error}')

def change_status():
    try:
        count = 0
        data = load_json()
        id_selection = input('Select a task by numerical id to change task status:\n')
        if input_isinteger(id_selection):
            id_selection = int(id_selection)
            # CHECK IF ID EXISTS
            for dict in data['tasks']:
                if dict['id'] == id_selection:
                    count += 1
            if count > 0:

                status = input('Change status. Options ---> "Complete" or "Incomplete".\n')
                status = status.strip().lower()
                new_data = {'tasks':[]}
                if status == "complete":
                    for task in data['tasks']:
                        if task['id'] == id_selection:
                            task['completion'] = True
                        new_data['tasks'].append(task)
                elif status == "incomplete":
                    for task in data['tasks']:
                        if task['id'] == id_selection:
                            task['completion'] = False
                        new_data['tasks'].append(task)
                else:
                    print('Option not available. Please check spelling.\n')

                with open(pathFile, 'w') as file:
                    json.dump(new_data, file, indent=2)
                print('Changes saved successfully.\n')
    except Exception as error:
        print(f'There was an error when changing the status. Error: {error}')