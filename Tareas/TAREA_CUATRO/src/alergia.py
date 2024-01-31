
class Alergia:
    """ 
    @class Alergia
    Clase para crear los datos de las distintas alergias
    """
    # Atributos
    """
    # Para la Parte Practica 1
    # @note: se comenta la lista de alergias_predefinidas de 50 alergias (lista debajo de esta)
    # y se descomenta esta segun las pruebas a realizas
    """
    # Lista de alergias predefinidas de 11 alergias
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

    """
    # Para la Parte Practica 2
    # @note: se comenta la lista de alergias_predefinidas de 11 alergias (lista arriba de esta)
    # y se descomenta esta segun las pruebas a realizas
    """
#     # Lista de alergias predefinidas de 50 alergias
#     alergias_predefinidas = [
#     ("huevos", 1),
#     ("cacahuetes", 2),
#     ("mariscos", 4),
#     ("fresas", 8),
#     ("tomates", 16),
#     ("chocolate", 32),
#     ("polen", 64),
#     ("gatos", 128),
#     ("sardina", 256),
#     ("gluten", 512),
#     ("huevo", 1024),
#     ("nueces", 2048),
#     ("leche", 4096),
#     ("soja", 8192),
#     ("miel", 16384),
#     ("piña", 32768),
#     ("ajo", 65536),
#     ("maíz", 131072),
#     ("kiwi", 262144),
#     ("menta", 524288),
#     ("gambas", 1048576),
#     ("apio", 2097152),
#     ("pescado", 4194304),
#     ("manzanas", 8388608),
#     ("cilantro", 16777216),
#     ("aguacate", 33554432),
#     ("zanahorias", 67108864),
#     ("berenjenas", 134217728),
#     ("lentejas", 268435456),
#     ("almendras", 536870912),
#     ("canela", 1073741824),
#     ("altramuces", 2147483648),
#     ("mantequilla", 4294967296),
#     ("pepino", 8589934592),
#     ("cangrejo", 17179869184),
#     ("almejas", 34359738368),
#     ("anacardos", 68719476736),
#     ("coliflor", 137438953472),
#     ("pimienta", 274877906944),
#     ("arándanos", 549755813888),
#     ("pera", 1099511627776),
#     ("cerveza", 2199023255552),
#     ("guisantes", 4398046511104),
#     ("ciruelas", 8796093022208),
#     ("trigo", 17592186044416),
#     ("higos", 35184372088832),
#     ("centeno", 70368744177664),
#     ("pistachos", 140737488355328),
#     ("cangrejo de río", 281474976710656),
#     ("col", 562949953421312)
# ]

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
                
