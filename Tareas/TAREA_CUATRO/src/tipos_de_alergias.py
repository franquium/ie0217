
from alergia import Alergia

class Tipos_de_Alergias:
    """
    @class Tipos_de_Alergias
    Clase permite agregar y gestionar las alergias especificas de un usuario,
    basandose tanto en nombres como en valores numericos.
    """
    def __init__(self)-> None:
         """
        Constructor de la clase Tipos_de_Alergias.
        """
         self.alergias_usuario = []
         self.nombres_no_encontrados = []
         self.valores_no_encontrados = []

    def agregar_alergia(self, nombre = None, valor = None):
        """
        @brief Agrega una alergia a la lista del usuario.
 
        @param nombre Nombre de la alergia a agregar. Puede ser nulo si se proporciona un valor.
        @param valor Valor numerico de la alergia a agregar. Puede ser nulo si se proporciona un nombre.
 
        """

        if nombre and valor:
            # Si se proporciona tanto el nombre como el valor, se agrega directamente a la lista.
            self.alergias_usuario.append((nombre, valor))
        elif nombre:
            # Creando la variable booleana encontrado para evitar que se 
            # agreguen a la lista cuando si se encuentran
            encontrado = False
            # Ciclo por si solo se proporciona el nombre, 
            # se busca el valor correspondiente en las alergias predefinidas.
            for nombre_predefinido, valor_predefinido in Alergia.alergias_predefinidas:
                if (nombre_predefinido == nombre):
                    self.alergias_usuario.append((nombre, valor_predefinido))
                    encontrado = True   # Cambia a True
                    break
            if not encontrado:
                    # Si no se encuentra el nombre 
                    self.nombres_no_encontrados.append(nombre)
                    # print(f"Alergia '{nombre}' no encontrada.")

       

        elif valor:
            # Creando la variable booleana encontrado para evitar que se 
            # agreguen a la lista cuando si se encuentran
            encontrado = False
            # Ciclo por si solo se proporciona el valor,
            # se busca el nombre correspondiente en las alergias predefinidas.
            for nombre_predefinido, valor_predefinido in Alergia.alergias_predefinidas:
                if (valor_predefinido == valor):
                    self.alergias_usuario.append((nombre_predefinido, valor))
                    encontrado = True   # Cambia a True
                    break
            if not encontrado:
                    # Si no se encuentra el valor
                    self.valores_no_encontrados.append(valor)
                    # print(f"Valor '{valor}' no encontrado para ninguna alergia.")

        else:
            # Si no se encuentra un match, se muestra un mensaje de error.
            print("Nombre o valor de alergia requerido.")

    def mostrar_alergias_usuario(self):
        """
        @brief Muestra las alergias del usuario.

        Imprime todas las alergias que el usuario ha agregado, 
        incluyendo tanto el nombre como el valor numerico.
        """

        print("Alergias ingresadas por el Usuario:")
        for nombre, valor in self.alergias_usuario:
            print(f"{nombre} (Valor: {valor})")
        
        if self.nombres_no_encontrados:
            print("\nNombres de Alergias no encontrados:")
            for nombre in self.nombres_no_encontrados:
                print(nombre)

        if self.valores_no_encontrados:
            print("\nValores de Alergias no encontrados:")
            for valor in self.valores_no_encontrados:
                print(valor)



