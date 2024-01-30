
class Alergia:
    """ Clase Alergia
    """
    # Atributos
    # Lista de alergias predefinidas
    alergias_predefinidas = [
        ("huevos", 1),
        ("cacahuetes", 2),
        ("mariscos", 4),
        ("fresas", 8),
        ("tomates", 16),
        ("chocolate", 32),
        ("polen", 64),
        ("gatos", 128),
        ("sardina", 256),
        ("gluten", 512),
        ("huevo", 1024)
    ]

    # Metodo para iniciliar o "construir" la clase
    def __init__(self, nombre, valor_alergico):
        """ Constructor de la clase Alergia.
        @param nombre: Nombre de la alergia.
        @param valor: Valor numérico asociado a la alergia.
        """
        self.nombre  = nombre
        self.valor_alergico = valor_alergico

    # Metodos

    def __str__(self):
        """
        Metodo para representar la alergia como una cadena de texto.
        @return: Representación en cadena de la alergia.
        """
        return f"Alergia: {self.nombre} (Valor: {self.valor_alergico})"

    @classmethod
    def mostrar_todas_alergias(cls):
        """
        Metodo de clase para imprimir la informacion de todas las alergias predefinidas.
        """
        print("Lista de Alergias Predefinidas:")
        for nombre, valor_alergico in cls.alergias_predefinidas:
            print(f"{nombre} (Valor: {valor_alergico})")

    @classmethod
    def mostrar_alergia_especifica(cls, nombre_alergia):
        """
        Metodo de clase para imprimir la informacion de una alergia especifica.
        @param nombre_alergia: Nombre de la alergia a buscar.
        """
        for nombre, valor_alergico in cls.alergias_predefinidas:
            if (nombre == nombre_alergia):
               print(f"Alergia: {nombre} (Valor: {valor_alergico})") 
               return
            
        print(f"Alergia: {nombre_alergia} no encontrada.") 
                

# Probando la clase

# # Crear una instancia de Alergia
# alergia1 = Alergia("agua", 2048)

# # Mostrar todas las alergias predefinidas
# alergia1.mostrar_todas_alergias()

# # Mostrar info de una alergia especifica
# alergia1.mostrar_alergia_especifica("gatos")
# alergia1.mostrar_alergia_especifica("birra")