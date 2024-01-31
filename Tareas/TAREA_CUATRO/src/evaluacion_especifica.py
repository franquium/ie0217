
from alergia import Alergia

class Evaluacion_Especifica:
    """
    """

    def __init__(self, puntuacion_general):
        """
        Constructor de la clase Evaluacion_Especifica.
        @param puntuacion_general: Puntuacion general de alergias de una persona.
        """
        self.puntuacion_general = puntuacion_general
        self.alergias_personales = self.evaluar_alergias()

    def evaluar_alergias(self):
        """
        Evalua las alergias basadas en la puntuacion general.
        @return: Lista de alergias a las que la persona es alergica.
        """
        alergias = []
        for nombre, valor_alergico in Alergia.alergias_predefinidas:
            """ @note: Usando las mascara AND bit a bit
                    Si el resultado de esta operacion AND es diferente de cero, significa 
                    que la puntuacion general incluye esa alergia especifica, y por lo tanto, 
                    se agrega a la lista alergias
            """
            if (self.puntuacion_general & valor_alergico):
                alergias.append((nombre, valor_alergico))
        return alergias

    def mostrar_puntuacion(self):
        """
        Imprime la puntuacion general y el desglose.
        """
        print(f"Puntuacion General de Alergias: {self.puntuacion_general}")
        print("Alergias Detectadas:")
        for nombre, valor_alergico in self.alergias_personales:
            print(f"{nombre} (Valor: {valor_alergico})")


