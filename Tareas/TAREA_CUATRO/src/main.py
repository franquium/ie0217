# Archivo momentaneo para probar el funcionamiento de las clases

from alergia import Alergia
from evaluacion_especifica import Evaluacion_Especifica
from tipos_de_alergias import Tipos_de_Alergias

# Para pruebas de clase Alergia 
# Crear una instancia de Alergia
alergia1 = Alergia("agua", 2048)

# Mostrar todas las alergias predefinidas
alergia1.mostrar_todas_alergias()

# Mostrar info de una alergia especifica
alergia1.mostrar_alergia_especifica("gatos")
alergia1.mostrar_alergia_especifica("birra")
print("\n")


# Para pruebas de clase Evaluacion_Especifica
# Crear una instancia con una puntuación de 7
evaluacion = Evaluacion_Especifica(7)
evaluacion.mostrar_puntuacion()
print("\n")


# Para pruebas de clase Tipo_de_Alergias
# Crear una instancia de Tipo_de_Alergias
tipo_alergias = Tipos_de_Alergias()

# Agregar algunas alergias
tipo_alergias.agregar_alergia(nombre="polen")           # Valor es: 64
tipo_alergias.agregar_alergia(valor=2)                  # Nombre es: cacahuetes
tipo_alergias.agregar_alergia(nombre="gatos", valor=128)
tipo_alergias.agregar_alergia(nombre="agua")            # Nombre no reconocido
tipo_alergias.agregar_alergia(valor=2048)               # Valor no reconocido

# Mostrar las alergias del usuario
tipo_alergias.mostrar_alergias_usuario()
print("\n")