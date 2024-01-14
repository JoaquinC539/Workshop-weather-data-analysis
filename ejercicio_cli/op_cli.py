import argparse
from util.utils import type_operation
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description= 'Tomar argumentos y hacer operacion respectivamente'
    )

    parser.add_argument(
        '-o', '--operacion', metavar = 'operacion',
        required = True, help = 'Operacion simple que toma argumentos',
        choices = ['simple', 'circulo']
    )
    
    args = parser.parse_args()
    print(args.operacion)
    type_operation(args.operacion)