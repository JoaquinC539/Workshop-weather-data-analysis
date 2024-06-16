from Perro import Perro
from Gusano import Gusano
from Animal import Animal
#Abstract
#############################


# dog = Perro('Pablo', 'Golden Retriver', 6)

# dog.ladrar()
# dog.avanzar()
# dog.decir_especie()

# worm = Gusano('Peter', 'Tierra', 1)

# worm.avanzar()


#Interface
###################################
from Rectangle import Rectangle
from IShape import IShape

rectangulo:IShape = Rectangle(5,6)
print(rectangulo.area())


