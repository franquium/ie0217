# Archivo momentaneo para probar el funcionamiento de las clases

from alergia import Alergia
from evaluacion_especifica import Evaluacion_Especifica

# Crear una instancia de Alergia
alergia1 = Alergia("agua", 2048)

# Mostrar todas las alergias predefinidas
alergia1.mostrar_todas_alergias()

# Mostrar info de una alergia especifica
alergia1.mostrar_alergia_especifica("gatos")
alergia1.mostrar_alergia_especifica("birra")
print("\n")

# Crear una instancia con una puntuación de 7
evaluacion = Evaluacion_Especifica(7)
evaluacion.mostrar_puntuacion()
print("\n")