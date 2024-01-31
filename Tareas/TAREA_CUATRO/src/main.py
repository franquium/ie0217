"""
@file main.py
@brief Programa para probar la evaluacion de alergias de una persona.

Este modulo contiene la interfaz de usuario para la gestion de alergias dentro
de la clase Interfaz_Usuario
Permite al usuario ingresar puntuaciones de alergias, ver alergias sensibles,
ingresar tipos de alergias y calcular el puntaje total. Tambien permite
agregar nuevas alergias y sus puntajes a la lista.
"""

from alergia import Alergia
from evaluacion_especifica import Evaluacion_Especifica
from tipos_de_alergias import Tipos_de_Alergias
from evaluacion_general import Evaluacion_General
import timeit
import cProfile
import pstats
import time

# Interfaz de usuario creando una clase

class Interfaz_Usuario:
    """
    @class Interfaz_Usuario
    Clase para crear una interfaz de usuario que interactúa con las clases Alergia,
    Tipo_de_Alergias y Evaluacion_General.
    """

    def es_potencia_de_dos(n):
        """
        Comprueba si un número es una potencia de dos.

        @param n (int): El nnmero a comprobar.

        @returns (bool) True si n es potencia de dos, False en caso contrario.
        """

        
        # Numero debe ser positivo para ser una potencia de dos.
        if n <= 0:
            return False

        # Realizar un AND bit a bit entre n y (n - 1).
        # Si n es una potencia de dos, este operador devolvera 0.
        resultado = n & (n - 1)

        # Si el resultado es 0, entonces n es una potencia de dos.
        # En caso contrario, no lo es.
        return resultado == 0


    @staticmethod
    def iniciar_interfaz():
        """
        Inicia la interfaz de usuario para interactuar con el sistema de evaluación de alergias.
        """
        tipo_alergias = Tipos_de_Alergias()

        while True:
            print("\n------- Sistema de Evaluacion de Alergias-------")
            print("1. Ingresar puntuacion de alergia y ver alergias sensibles")
            print("2. Ingresar tipos de alergias y calcular puntaje total")
            print("3. Agregar nueva alergia y su valor")
            print("4. Salir")
            
            opcion = input("Seleccione una opcion: ")

            # Opcion 1:
            if opcion == '1':
                puntuacion = input("Ingrese su puntuacion general de alergias: ")
                if puntuacion.isdigit():
                    start_time = timeit.default_timer()  # Iniciar el temporizador de timeit
                    evaluacion = Evaluacion_Especifica(int(puntuacion))
                    evaluacion.mostrar_puntuacion()
                    end_time = timeit.default_timer()  # Finalizar el temporizador de timeit
                    print(f"Tiempo de ejecucion Evaluacion_Especifica: {end_time - start_time} s.")
                else:
                    print("Por favor, ingrese un número válido.")
            
            # Opcion 2:
            elif opcion == '2':
                # Instancia de clase Tipo de Alergias
                tipo_alergias = Tipos_de_Alergias()
                # Permite al usuario ingresar las alergias con sus respectivos puntajes.
                while True:
                    nombre = input("Ingrese el nombre de la alergia (o 'salir' para terminar de ingresar o salte de linea si desconocido): ")
                    if nombre.lower() == 'salir':
                        break
                    # En caso de que nombre no sea string
                    if nombre.strip().isdigit(): 
                        print("Error. El nombre de la alergia debe ser un string.")
                        continue
                    valor = input("Ingrese el valor de la alergia (salte de linea si desconocido): ")
                    # Condicion para revisar que valor sea un numero
                    if valor.isdigit():
                        valor = int(valor)
                    # Para los casos de salto de linea o
                    elif valor == "":
                        valor = None
                    else:
                        print("Error. Por favor, ingrese un número entero o deje en blanco.")
                        continue

                    # Agregando a las alergias de usario para realizar los calculos posteriormente
                    tipo_alergias.agregar_alergia(nombre = nombre, valor = valor)

                    # try:
                    #     valor = int(input("Ingrese el valor de la alergia: "))
                    #     tipo_alergias.agregar_alergia(nombre = nombre, valor = valor)
                    # except ValueError:
                    #     print("Error. Por favor, ingrese un numero entero.")
                    #     continue
                
                # Mostrar las alergias ingresadas
                tipo_alergias.mostrar_alergias_usuario()

                start_time = timeit.default_timer()  # Iniciar el temporizador de timeit

                # Instancia de la clase Evaluacion General
                evaluacion_general = Evaluacion_General(tipo_alergias)
                evaluacion_general.mostrar_evaluacion_general()
                
                end_time = timeit.default_timer()  # Finalizar el temporizador de timeit
                print(f"Tiempo de ejecucion de Evaluacion_General: {end_time - start_time} s.")

            # Opcion 3:
            elif opcion == '3':
                tipo_alergias = Tipos_de_Alergias()
                nombre = input("Ingrese el nombre de la nueva alergia: ")
                try:
                    valor = int(input("Ingrese el valor de la nueva alergia: "))
                    if not Interfaz_Usuario.es_potencia_de_dos(valor) or nombre.isdigit():
                        print("Error. El valor de la alergia debe ser una potencia de 2.")
                        continue
                except ValueError:
                        print("Error. Por favor, ingrese un numero entero.")
                        continue
                
                # Agregar la nueva alergia
                tipo_alergias.agregar_alergia(nombre, valor)
                # Mostrar las alergias ingresadas
                tipo_alergias.mostrar_alergias_usuario()
                # Instancia de la clase Evaluacion General
                evaluacion_general = Evaluacion_General(tipo_alergias)
                evaluacion_general.mostrar_evaluacion_general()
            
            # Opcion 4: Salir
            elif opcion == '4':
                print("\n------- Saliendo del programa... -------")
                break
            else:
                print("Opción no es valida. Por favor, intente de nuevo.")


# Creando una funcion main que contiene la instancia de 
# la interfaz de usuario
def main():
    # Instancia de la clase interfaza
    Interfaz_Usuario.iniciar_interfaz() 


if __name__ == "__main__":
    
    # cProfile.run('main()')

    with cProfile.Profile() as profile:
        main()
    profile_result = pstats.Stats(profile)
    profile_result.sort_stats(pstats.SortKey.TIME)
    profile_result.print_stats()








##############################################################
# Old Tests
#
# # Para pruebas de clase Alergia 
# # Crear una instancia de Alergia
# alergia1 = Alergia("agua", 2048)

# # Mostrar todas las alergias predefinidas
# alergia1.mostrar_todas_alergias()

# # Mostrar info de una alergia especifica
# alergia1.mostrar_alergia_especifica("gatos")
# alergia1.mostrar_alergia_especifica("birra")
# print("\n")


# # Para pruebas de clase Evaluacion_Especifica
# # Crear una instancia con una puntuación de 7
# evaluacion = Evaluacion_Especifica(7)
# evaluacion.mostrar_puntuacion()
# print("\n")


# # Para pruebas de clase Tipo_de_Alergias
# # Crear una instancia de Tipo_de_Alergias
# tipo_alergias = Tipos_de_Alergias()

# # Agregar algunas alergias
# tipo_alergias.agregar_alergia(nombre="polen")           # Valor es: 64
# tipo_alergias.agregar_alergia(valor=2)                  # Nombre es: cacahuetes
# tipo_alergias.agregar_alergia(nombre="gatos", valor=128)
# tipo_alergias.agregar_alergia(nombre="agua")            # Nombre no reconocido
# tipo_alergias.agregar_alergia(valor=2048)               # Valor no reconocido

# # Mostrar las alergias del usuario
# tipo_alergias.mostrar_alergias_usuario()
# print("\n")
# # 

# # # # Para pruebas de clase Evaluacion_General
# # # # Usando algunas alergias al tipo_alergias
# # # evaluacion_general = Evaluacion_General(tipo_alergias)
# # # evaluacion_general.mostrar_evaluacion_general()
##############################################################