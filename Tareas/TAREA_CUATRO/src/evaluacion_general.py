
from alergia import Alergia
from evaluacion_especifica import Evaluacion_Especifica
from tipos_de_alergias import Tipos_de_Alergias

class Evaluacion_General:
    """
    @class Evaluacion_General
    Clase toma todas las alergias ingresadas por el usuario, ya evaluadas con su respectivo
    nombre y valor, y calcula la puntuacion general de alergias del usuario.
    """
    def __init__(self, tipo_de_alergias):
        """
        Constructor de la clase EvaluacionGeneral.
        @param tipo_de_alergias: Instancia de la clase Tipo_de_Alergias con las alergias del usuario.
        """
        self.tipo_de_alergias = tipo_de_alergias
        self.puntuacion_general = self.calcular_puntuacion_general()
        self.promedio = self.calcular_promedios()
        #self.promedio_desconocido = self.calcular_promedio_desconocido()

    def calcular_puntuacion_general(self):
        """
        Calcula la puntuacion general de alergias del usuario.
        @return: Puntuacion general de alergias.
        """
        puntuacion = 0
        for _, valor in self.tipo_de_alergias.alergias_usuario:
            puntuacion += valor
        return puntuacion

    def calcular_promedios(self):
        """
        Calcula el promedio de los valores de la alergias que se pudieron determinar,
        asi como de lo desconocido.
        @return: Promedio de lo conocido y lo desconocido.
        """

        total_conocido = 0
        total_desconocido = 0

        # Para sumar los valores de las alergias conocidas
        for _, valor in self.tipo_de_alergias.alergias_usuario:
            total_conocido += valor

        # Para sumar los valores de las alergias desconocidas
        for i in self.tipo_de_alergias.valores_no_encontrados:
            total_desconocido += i

        # Para medir el largo N de elementos a promediar
        n_conocido = len(self.tipo_de_alergias.alergias_usuario)
        n_desconocido = len(self.tipo_de_alergias.valores_no_encontrados)

        if n_conocido > 0:
            promedio_conocido = total_conocido / n_conocido 
            #print(f"Promedio de Puntuacion para Alergias Conocidas: \n{promedio_conocido:.2f}")
        else:
            promedio_conocido = 0
            print(f"Error. No se puede calcular el promedio de alergias conocidadas")
        
        if n_desconocido > 0:
            promedio_desconocido = total_desconocido / n_desconocido 
            #print(f"Promedio de Puntuacion para Alergias desconocidas: \n{promedio_desconocido:.2f}")
        else:
            promedio_desconocido = 0
            #print(f"Error. No se puede calcular el promedio de alergias desconocidadas")

        return promedio_conocido, promedio_desconocido    

    def mostrar_evaluacion_general(self):
        """
        Imprime la puntuacion general y el desglose de alergias.
        """
        print(f"Puntuacion General de Alergias: \n{self.puntuacion_general}\n")
        # print("Alergias No encontradas:")
        # Para las alergias con nombre pero sin puntuacion
        if self.tipo_de_alergias.nombres_no_encontrados:
            print("\nAlergias con nombre pero sin puntuacion conocida:")
            for nombre in self.tipo_de_alergias.nombres_no_encontrados:
                print(nombre)
        # Para las alergias con valor pero sin nombre
        if self.tipo_de_alergias.valores_no_encontrados:
            print("\nResultados Desconocidos:")
            for valor in self.tipo_de_alergias.valores_no_encontrados:
                print(valor)

        # Para imprimir los promedios
        # Promedios de alergias conocidas
        if (self.promedio[0] > 0):
            print(f"\nPromedio de Alergias Conocidas: {self.promedio[0]:.2f}")
        else:
            print(f"Error. No se puede calcular el promedio de alergias conocidadas")

        # Promedios de alergias desconocidas
        if (self.promedio[1] > 0):
             print(f"Promedio de Alergias Desconocidas: {self.promedio[1]:.2f}")
        else:
            return
        
       


