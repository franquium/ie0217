# Ejemplos para importar modulos

# Forma 1
# importando el modulo estandar math 
import math 

# usando math.pi para obtener el valor de pi
print("El valor de Pi es:", math.pi)

# Forma 2
# importando solo Pi del modulo math 
from math import pi

# El valor de pi
print("El valor de Pi es:", pi)

# Forma 3
# importando modulo renombrandolo 
import math as m

# El valor de pi
print("El valor de Pi es:", m.pi)

# Forma 4
# importando todos los nombres del modulo math
from math import *

# El valor de pi
print("El valor de Pi es:", pi)