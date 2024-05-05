import os
import json

# import sys
# import os
# print(os.path.dirname(__file__))
# ruta_relativa=os.path.join(os.path.dirname(__file__),'..')
# ruta_absoluta=os.path.abspath(ruta_relativa)
# print(ruta_relativa)
# print(ruta_absoluta)
# print(sys.path)
# sys.path.append(ruta_absoluta)
# print(sys.path)

# from workshop.ternaryOp import mayor16

# print(mayor16(18))


def config():
    try:
        # tasks_exists=input("Do you have a previous tasks file? Y/N")
        # new_task=  True if (tasks_exists.lower().strip() =="y") else False
        local_pathfile="./tasks_config.json"
        if(os.path.exists(local_pathfile)):
            with open(local_pathfile,"r") as file:
                data=json.load(file)
                return data["pathFile"]
        else:
            relative_path=input("Using relative path annotation, insert the location of the file tasks.json (insert './' to\n specify that the file is here or create it here if doesn't exists)")
            
            relative_parts=relative_path.split("/")            
            
            relative_route=os.path.join(__file__,*relative_parts)
            
            absolute_route=os.path.abspath(relative_route)
            
            file_path=os.path.abspath(os.path.join(absolute_route,".","tasks.json"))
            
            if(os.path.exists(file_path)):
                with open("./tasks_config.json","w") as file:
                    data={
                        "pathFile":file_path
                    }
                    json.dump(data,file)
                return file_path
            else:
                print("The tasks wasn't found")
                return
    except Exception as error:
        print("There was an error getting or generating path file: "+error)
        return
config()