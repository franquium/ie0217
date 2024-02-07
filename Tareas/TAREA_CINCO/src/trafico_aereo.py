import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

"""
Requisitos del Programa
1. Seleccion de Datos
2. Obtencion de Datos
3. Limpieza y Preparacion de Datos
4. Analisis de Datos
5. Visualizacion de Datos
6. Interpretacion de Resultados
7. Documentacion y Presentacion
"""

# 2. Obtencion de Datos & 3. Limpieza y Preparacion de Datos

class Obtener_Datos:
    """
    @class Obtener_Datos
    Clase para obtener y cargar los datos a partir del archivo CSV en un DataFrame de Pandas
    """
    def __init__(self, filepath):
        """
        Constructor de la clase con la ruta al archivo CSV.
        
        @param filepath: Ruta al archivo CSV.
        """
        self.filepath = filepath

    def cargas_datos(self):
        """
        Carga los datos desde el archivo CSV a un DataFrame de Pandas.
        Se implementa el manejo de excepciones para asegurar un buen comportamiento
        
        @return: DataFrame de Pandas con los datos cargados.
        """
        try:
            # Importando los datos con DataFrame de Pandas
            # Instanciando el dataframe con los datos del archivo csv
            data = pd.read_csv(self.filepath)
            print("Datos cargados exitosamente.\n")
            return data
        
        except FileNotFoundError:
            print(f"Error: El archivo {self.filepath} no fue encontrado.\n")
        except Exception as e:
            print(f"Error desconocido: {e}\n")

    # Metodos para la Limpieza y Preparacion de Datos
    def eliminar_columnas(self, datos, columnas):
        """
        Elimina una o varias columnas del DataFrame.
        
        @param datos: DataFrame de Pandas con los datos cargados.
        @param columnas: Lista de nombres de columnas a eliminar.
        
        @return: DataFrame de Pandas sin las columnas escogidas a eliminar.
        """
        # El param errors='ignore' es para suprimir el error en caso de 
        # que no se encuentre dicha columna
        datos = datos.drop(columns=columnas, errors='ignore')
         

        return datos


    def eliminar_filas_con_ceros(self, data):
        """
        Elimina las filas donde los valores de PASSENGERS, FREIGHT, MAIL, y DISTANCE son todos cero simultaneamente.
        Ya que estos valores no aportan informacion relevante.
        
        @param datos: DataFrame de Pandas con los datos cargados.
        
        @return: DataFrame de Pandas sin las filas con todos ceros en las columnas especificadas.
        """

        # Condicion booleana para identificar las filas con todos ceros
        condicion = (data['PASSENGERS'] == 0) & (data['FREIGHT'] == 0) & (data['MAIL'] == 0) & (data['DISTANCE'] == 0)
        
        # Se filtran los datos invertiendo la condicion con el Operador de NOT
        # para seleccionar las filas que no cumplen con la condicion de todos ceros
        # las cuales son nuestras filas de interes
        datos_filtrado = data[~condicion]
        

        return datos_filtrado
##################
# Fin de la clase        
###################
    


class Analisis_Datos:
    """
    @class Analisis_Datos
    Clase para 
    """
    pass


class Visualizacion_Datos:
    """
    @class Visualizacion_Datos
    Clase para 
    """
    pass





# Main
if __name__ == "__main__":

    filepath = "T_T100_MARKET_US_CARRIER_ONLY.csv"  # Nombre del archivo CSV
    data = Obtener_Datos(filepath)
    datos = data.cargas_datos()

    # print(datos.head(5))
    
    """ 
    # Lista de tipos de datos y descripcion en el archivo CSV:
    PASSENGERS: Pasajeros embarcados
    FREIGHT: Carga embarcada (libras)
    MAIL: Correo embarcado (libras)
    DISTANCE: Distancia entre aeropuertos (millas)
    UNIQUE_CARRIER: Codigo de operador único.
    AIRLINE_ID: Numero de identificacion unico para identificar una aerolínea.
    UNIQUE_CARRIER_NAME:  Nombre exclusivo del operador.
    ORIGIN_AIRPORT_ID: ID del aeropuerto de origen.
    ORIGIN: Codigo de aeropuerto de origen
    ORIGIN_CITY_NAME: Nombre de la ciudad de origen.
    DEST_AIRPORT_ID: 
    DEST: Codigo de aeropuerto de destino
    DEST_CITY_NAME: ID del aeropuerto de destino.
    MONTH: mes del vuelo
    CLASS: Clase de servicio
    DATA_SOURCE: Fuente de Datos, para estos datos todos son DU: Vuelos Domesticos de Operadores de EEUU
    """
    # Lista de columnas a eliminar con datos redundantes o innecesarios
    columnas_a_eliminar = ['UNIQUE_CARRIER', 'DATA_SOURCE', 'DEST_AIRPORT_ID', 'ORIGIN_AIRPORT_ID']
    # Eliminando columnas
    datos = data.eliminar_columnas(datos, columnas_a_eliminar)

    # Eliminando filas con ceros en todas las variables numericas de interes
    datos = data.eliminar_filas_con_ceros(datos)
    
    # print(datos.head(5))
    # print(datos.shape)


    # Codigo para verificar que funka 
    # print(datos.head(5))    # imprime los primeros 5 datos
    # print(datos.sample(3))  # imprime una muestra de 3 datos aleatorios 
    # print(datos.describe()) # imprime una descripcion general rapida de los datos numeros del DataFrame
    # print(datos.shape)      # imprime el tamanno del DataFrame
