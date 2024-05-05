'''

Examen: Hacer un manejador de tareas usando json, cli, modulos de funciones, funciones, lambdas y funciones integradas de python

- Crear una branch nueva de git para el examen

- Hacer una carpeta especial para el examen

- Usar cli con opciones para crear,editar, ver una tarea, ver todas las tareas, ver todas las tareas completes o faltantes y eliminar una tarea.

- Las tareas deben ser guardadas  y leidas en un archivo json

- Para filtrar tareas por completado, usar la función filter de python con apoyo de una lambda

Descripción: Se debe hacer un programa que gestione un gestor de tareas que use cli con opciones para las operaciones, para las operaciones de lectura: 
Debe pedir el tipo de lectura posteriormente, para las operaciones de editar(update y delete) debe pedir un id. Para agregar(post) debe pedir la tarea para agregar y 
ser puesta por default como no completada. En la parte de editar puede recibir solo opción para completer unicamente

- Los campos obligatorios de las tareas son id, si esta completado, tarea desripción

- El id debe ser generado automaticamente cuando se agregue una tarea, el id debe ser unico por tarea y no repetible

- El id no puede ser modificado

- CALIFICACION:

Uso de git: 3/5

Uso de kanban: 0/5

Limpieza de codigo: 8/10

Atrapo de errores y exepciones: 5/15

Validaciones de entradas/casos: 10/10

Uso de lambdas y funciones de grado superior (filter):  6/10

Funcionalidad correcta del programa: 0/45

FINAL: 32/100 Beso doble en la frente

'''

import argparse
from modules.exam_module import operation_type

parser = argparse.ArgumentParser(
    description = 'Begins a Kanban program that will create, write, edit, re-edit and delete boards for organization options are [create, clear, edit, display]'
)

try:
    parser.add_argument(

        '-o', '--operation', metavar = 'operation',
        required = True, help = 'input an entry to a .json file; options are create, clear, edit and display',
        choices = ['create', 'clear', 'edit', 'display'] 
    )
    args = parser.parse_args()
    
    operation_type(args.operation)

except Exception as error:
    print(f"The error was: {error}")
finally:
    print('Goodbye!')