'''

Examen: Hacer un manejador de tareas usando json, cli, modulos de funciones, funciones, lambdas y funciones integradas de python

- Crear una branch nueva de git para el examen (Listo)

- Hacer una carpeta especial para el examen (Listo)

- Getsionar errores inesperados y tener control de los errores

- Separar funciones del cli 

- Usar cli con opciones para crear,editar, ver una tarea, ver todas las tareas, ver todas las tareas completes o faltantes y eliminar una tarea (Listo).

- Las tareas deben ser guardadas  y leidas en un archivo json

- Para filtrar tareas por completado, usar la función filter de python con apoyo de una lambda

Descripción: Se debe hacer un programa que gestione un gestor de tareas que use cli con opciones para las operaciones, para las operaciones de lectura: 
Debe pedir el tipo de lectura posteriormente, para las operaciones de editar(update y delete) debe pedir un id. Para agregar(post) debe pedir la tarea para agregar y 
ser puesta por default como no completada. En la parte de editar puede recibir solo opción para completer unicamente

- Los campos obligatorios de las tareas son id, si esta completado, tarea desripción

- El id debe ser generado automaticamente cuando se agregue una tarea, el id debe ser unico por tarea y no repetible

- El id no puede ser modificado

'''
import argparse
from modules.modules import main

if __name__=="__main__":
    
    parser=argparse.ArgumentParser(
        description='Aplication for control of personal assignments to do'
    )
    
    parser.add_argument(
        '-o',
        '--operation',
        metavar="operation",
        required=True,
        help="Type of operation: ['read','create','edit','delete',complete]",
        choices=["read","create","edit","delete","complete","decomplete"]
    )
    
    args=parser.parse_args()
    
    main(args.operation)
    

