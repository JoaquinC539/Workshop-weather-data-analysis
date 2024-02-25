from os import path
import json
from random import choice


pathFile = './tasks.json'

id_finder=lambda dictonary,id_searched: True if (dictonary["id"]==id_searched) else False

completion_finder=lambda dictonary,status: True if(dictonary["complete"]==status) else False

completion_parser=lambda boolean_status:"Completed" if(boolean_status) else "Not Completed"

json_complete=lambda option:  option=="complete" 

def main(json_choice):
    if(json_choice=="create"):
        create_nadd_post()
    elif(json_choice=="read"):
        read_options()
    elif(json_choice=="complete" or json_choice=="decomplete"):
        complete_decomplete_task(json_complete(json_choice))
    elif(json_choice=="delete"):
        delete_task()
    elif(json_choice=="edit"):
        modify_task()
        
        
def read_options():
    option=input("Do you wish to read single task, all task, or task status? (single/all/complete/notComplete):\n")
    print('')
    if(option=="single"):
        dictionary=search_task_by_id()
        if(dictionary==None):
            print ("The task doesn't exists")
            return
        cols=list(dictionary.keys())
        print(f"{cols[0]}           {cols[1]}               {completion_parser(cols[2])}")
        print(f'{list(dictionary.values())[0]}    {list(dictionary.values())[1]}    {list(dictionary.values())[2]}')
    elif(option=="all"):
        data = get_all_json()
        cols= list(data[0].keys())
        print(f"{cols[0]}   {cols[1]}   {completion_parser(cols[2])}")
        print("______________________________")
        for dictionary in data:
            print(f'{list(dictionary.values())[0]}    {list(dictionary.values())[1]}    {list(dictionary.values())[2]}')
            print('')
    elif(option=="complete" or option=="notComplete"):
        status = json_complete(option)
        data=get_all_json()
        task_finder = list(filter(lambda dictionary: completion_finder(dictionary,status),data))
        cols= list(task_finder[0].keys())
        print(f"{cols[0]}           {cols[1]}               {completion_parser(cols[2])}")

        for dictionary in task_finder:
            values = list(dictionary.values())
            print(f'{values[0]}    {values[1]}    {values[2]}')
            print('')
        
    else:
        print("Not a valid reading option")
    return


def create_nadd_post():
    try:
        if not (path.exists(pathFile)):
            with open(pathFile,'w') as file:
                task_description=get_input_task()
                new_id=generate_id()
                new_task={
                    'id': new_id,
                    'task': task_description,
                    'complete':False
                }
                new_json_list=[]
                new_json_list.append(new_task)
                json.dump(new_json_list,file, indent=2)            
            print("Your task was added successfully")
            return
        else:
            data=get_all_json()
            if(data==None):
                data=[]
            task_description=get_input_task()
            new_id=generate_id()
            new_task={
                'id': new_id,
                'task': task_description,
                'complete':False
            }
            data.append(new_task)
            with open(pathFile,'w') as file:
                json.dump(data,file,indent=2)
            print("Your task was added successfully")
            return

    except Exception as error:
        print(f"There was an unexpected error at the create and add post: {error}")      
       
        
def get_input_task():    
    task_description=input("Add you task description (it will be set as not completed): ")
    return task_description

def generate_id(): 
    id = ''
    charcters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(10):
        charcter = choice(charcters)
        id += charcter
    return id

def get_all_json():
    try:
        if(path.exists(pathFile)):
            with open(pathFile,"r") as file:
                data=json.load(file)
                return data
        else:
            return "The json file doesn't exists. To create one use the create operation to create your first task"
                
    except Exception as error:
        print(f"There was and error reading the json file: {error}")
        return
    
def id_input():

    id=input("Add your id to search/complete/decomplete/edit/delete by id: ")
    print("")
    return id

def search_task_by_id():
    try:
        data=get_all_json()
        id=id_input()
        dictionary_found=list(filter(lambda dictionary:id_finder(dictionary,id),data))
        if(len(dictionary_found)>0):
            return dictionary_found[0]
        else:
            return None
            
    except Exception as error:
        print(f"There was an error setting the completion: {error}")
        
def complete_decomplete_task(completion):
    try:
        data=get_all_json()
        if(len(data)) == 0:
            print ("There is no data")
            return
        
        id=id_input()
        id_exist=search_if_dict_by_id(data,id)
        if not (id_exist):
            print("id does not exists")
            return
           
        for dictionary in data:
            if dictionary['id'] == id:
                dictionary['complete'] = completion
                break
            dump_json(data)
            print(f"Task with the id: {id} was set to {completion_parser(completion)}")
        else:
            print("Dictionary with that id doesn't exists")
    except Exception as error:
        print(f"Hubo un error en completar la tarea: {error}")        
   
def dump_json(data):
    try:
       with open(pathFile, 'w') as file:
        json.dump(data, file,indent=2) 
    except Exception as error:
        print("There was an error at dumping the json: "+error)
        
def delete_task():
    try:
        data=get_all_json()
        id=id_input()
        id_exist=search_if_dict_by_id(data,id)
        if not (id_exist):
            print("id does not exists:", id)
            return
        data_filtered=list(filter((lambda dictionary:False if(dictionary["id"]==id) else True),data))
        dump_json(data_filtered)
        print(f"The task with the id: {id} was deleted")
    except Exception as error:
        print(f"there was an error in deleting task: {error}")
def search_if_dict_by_id(data,id):
    try:
        data_filter = list(filter((lambda dictionary: False if dictionary['id'] != id else True),data))
        if len(data_filter) == 0:
            return False
        else:
            return True
    except Exception as error:
        print(f"There was an error searching if exists by id: {error}")

def modify_task(): 
    try:   
        data=get_all_json()
        id=id_input()
        id_exist=search_if_dict_by_id(data,id)
        if not (id_exist):
            print("id does not exists:", id)
            return
        entry = input('Enter a task description:\n')
        for dictionary in data:
            if dictionary['id'] == id:
                dictionary['task'] = entry
                break
        dump_json(data)
        print('Task was edited')
    except Exception as error:
        print(f'There was an error modifying a task. Erro: {error}')