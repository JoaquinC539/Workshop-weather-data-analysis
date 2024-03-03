import argparse
from module_folder.exam2_module import main

def display_commands():
    choices=['Create', 'Edit', 'Display', 'Select', 'Delete', 'Status']
    descriptions = [
        'This command will initialize a task. User will be prompted to entry a description. Once created, the task will be\nmarked with a numerical ID. The task will initially will be set to "Incomplete"',
        'The edit command will change the description of a given task. User will be prompted for the numerical ID task they wish to modify.\nCaution! This command will delete the previous description!',
        'This command will diplay all tasks',
        'This command will prompt a task selection based on ID or based on completion. According to the selection,\nthe program will display the selected task(s)',
        'The user will be prompted to delete all tasks or task by ID.'
        'This function will allow the user to change the status of the task.'
    ]
    for i in range(5):
        print(choices[i])
        print(descriptions[i])
        print('') 

parser = argparse.ArgumentParser(
            description= 'Begins a program that will create, display, select task, delete task and edit according to command'
        )

parser.add_argument(
    '-o', '--operation', metavar = 'choice',
    required = True, help = display_commands(),
    choices=['create', 'edit', 'display', 'select', 'delete', 'status']
)

args = parser.parse_args()
try:
    main(args.choice)
except Exception as error:
    print(f'The program had an error: {error}\n')
finally:
    print('Goodbye!\n')