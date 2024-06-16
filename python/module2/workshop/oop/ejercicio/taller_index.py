# clase de auto
# clase de trabajo
# print de estado de carro
# tipo de trabajo (cambio de aceite, revision, descripcion, etc)
# Enum de marca (Toyota, Hyundai)
# Clase base de cada accion (interface) para campos obligatorios



# Crear class stack para revisiones y composturas (Clase base para ser heredada para Coche)
# taller mecanico, calse coche: propiedas y atributos como marca (Enum), ano, horse power, placas, holder de composturas y revisiones ([...]), etc...

### Enum para tipo de trabajo (compostura, revision/diagnostico)

#Clase Revision, clase compostura (Clase base "trbajo" como interface o abstraccion)

from Coche import Coche
from Marca import Marca
from Diagnostico import Diagnostico
from TipoTrabajo import TipoTrabajo
from Compostura import Compostura
camryChon=Coche(2019,Marca.HONDA,"NOOB40")

primerDiag=Diagnostico("frenos")
primerDiag.set_estimate_time(1.5)
primerDiag.set_employee_number(2)
primerDiag.set_tipo_trabajo(TipoTrabajo.DIAGNOSTICO)
primerDiag.set_comentatio("No fallan frenos")

camryChon.trabajos.append(primerDiag)

segundoDiag=Diagnostico("amortiguadores")
segundoDiag.set_estimate_time(0.5)
segundoDiag.set_employee_number(3)
segundoDiag.set_tipo_trabajo(TipoTrabajo.DIAGNOSTICO)
segundoDiag.set_comentatio("Amortiguadores chorreantes de aceite")

camryChon.trabajos.append(segundoDiag)


primerCompos=Compostura("amortiguadores",250)
primerCompos.set_estimate_time(10)
primerCompos.set_employee_number(5)
primerCompos.set_tipo_trabajo(TipoTrabajo.COMPOSTURA)
primerCompos.set_comentatio("Se cambiaron amortiguadores frontales")

camryChon.trabajos.append(primerCompos)


print(camryChon.trabajos)











































































#### --------------------------------- ####

# Class Coche
#     stack = []

# Class Revision(Coche)

    # push_revison(self):
          # self.stack.push(element)

# Class Comp (Coche)



#x = Coche(5, 2019, jdiwjdiajd)
# x.get_steps()
#coche.stack.append(Revision.stack)

# => [[].[[]],[[]]] <=========== Regresas a esto

# []
# [ obj, obj, obj    ] => coche
# for x in coche.stack:
    #print(x.tipo)
    
#Tarea escribir aqui por que lo de arriba no funciona