##### PROCESP ###########
#LEER -> AGREGAR -> ESCRIBIR


from pprint import pprint
import os
import json
import time
def load_json(pathFile):
    if( os.path.exists(pathFile) ):
        with open(pathFile, 'r') as f:
            data = json.load(f)
            return data



def add_json(pathFile,data):
    with open(pathFile,'w') as f:
        json.dump(data,f)



start_time=time.time()


def append_json(pathFile, data):
    with open(pathFile, 'a') as f:
        json.dump(data, f)




##### PROCESP ###########
#LEER -> AGREGAR -> ESCRIBIR

##### PROCESP ###########
#LEER -> AGREGAR -> ESCRIBIR


##### PROCESP ###########
#LEER -> AGREGAR/MODIFICAR -> ESCRIBIR



def search_name_injson(pathFile,name):
    data=load_json(pathFile)
    for dict in data:
        if(dict['nombre']==name):
            return dict

def find_injson_data(data, name):
    for dicts in data:
        if(dicts['nombre']==name):
            return dicts
            
def update_apodo_injson_data(data,name,newApodo):
    for dictionary in data:
        if(dictionary ['nombre']==name):
            dictionary ['apodo']=newApodo
            break
def find_all_nombres_injson(data,nombre):
    nombres=[]
    for dictionary in data:
        if(dictionary['nombre']==nombre):
            nombres.append(dictionary)
    return nombres
        
        
my_data=load_json('./myJson.json')

update_apodo_injson_data(my_data,'Danila','Palomina')
if(my_data):
    add_json('./myJson.json',my_data)
    my_new_data=load_json('./myJson.json')
    pprint(find_injson_data(my_new_data,'Danila'))
else:
    print(' No lo encontre')

# print(find_all_nombres_injson(my_data, 'Danila'))

# pprint(search_name_injson('myJson.json', 'Darbee'))
print("--- %s seconds ---" % (time.time() - start_time))