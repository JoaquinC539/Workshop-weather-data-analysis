import sys
import os
print(os.path.dirname(__file__))
ruta_relativa=os.path.join(os.path.dirname(__file__),'..')
ruta_absoluta=os.path.abspath(ruta_relativa)
print(ruta_relativa)
print(ruta_absoluta)
print(sys.path)
sys.path.append(ruta_absoluta)
print(sys.path)

from workshop.ternaryOp import mayor16

print(mayor16(18))