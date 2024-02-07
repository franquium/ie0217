""" 
###############################################################################
@file 
@brief Programa para el Analizar y Manipular datos a partir de un archivo CSV
@autor J. Antonio Franchi

###################################################################################
""" 

#################################################################
# Para revisar los problemas de importacion de modulos de Python
# al correr: python <nombre_archivo.py>
# import sys
# print("Python interprete actual:", sys.executable)

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


"""
Requisitos del Programa
1. Seleccion de Datos
2. Obtencion de Datos
3. Limpieza y Preparacion de Datos
4. Analisis de Datos
5. Visualizacion de Datos
6. Interpretacion de Resultados
7. Documentacion y Presentacion

Ref sobre valores atipicos:

https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/

"""

# 2. Obtencion de Datos & 3. Limpieza y Preparacion de Datos

class Obtener_Datos:
    """
    @class Obtener_Datos
    Clase para obtener y cargar los datos a partir del archivo CSV en 
    un DataFrame de Pandas

    @param filepath: Ruta al archivo CSV.
    """
    def __init__(self, filepath):
        """
        Constructor de la clase con la ruta al archivo CSV.
        #
        @param filepath: Ruta al archivo CSV.
        """
        self.filepath = filepath

    def cargas_datos(self):
        """
        Carga los datos desde el archivo CSV a un DataFrame de Pandas.
        
        @return: DataFrame de Pandas con los datos cargados.
        """
        
        # Importando los datos con DataFrame de Pandas
        # Instanciando el dataframe con los datos del archivo csv
        data = pd.read_csv(self.filepath)
        print("Datos cargados exitosamente.\n")

        return data
        
  

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
    
### --- # Fin de la clase --- ###################


# 4. Analisis de Datos & 5. Visualizacion de Datos

class Analisis_Datos(Obtener_Datos):
    """
    @class Analisis_Datos
    Clase para el analisis de Datos que hereda de la clase Obtener_Datos
    """
    def __init__(self, filepath, datos):
        """
        Constructor de la clase Analisis_Datos

        @param filepath: Ruta al archivo CSV.
        @param datos: DataFrame de Pandas que contiene los datos de vuelos.
        """
        super().__init__(filepath)
        self.datos = datos


    def calcular_valores_descriptivos(self, data):
        """
        Calcula y muestra valores descriptivos estadisticas 
        descriptivas del DataFrame.
        
        @param data: DataFrame de Pandas con los datos.
        """
        print(data.describe())

    def contar_vuelos_por_aerolinea(self, data):
        """
        Generador que cuenta la cantidad de vuelos por aerolinea.
        
        @param data: DataFrame de Pandas con los datos.
        
        @yield: Tupla con el nombre de la aerolinea y la cantidad de vuelos.
        """
        # Usando el metodo value_counts() de Pandas
        conteo = data['UNIQUE_CARRIER_NAME'].value_counts()
        
        for aerolinea, cantidad_vuelos in conteo.items():
            yield aerolinea, cantidad_vuelos


    def contar_pasajeros_por_aerolinea(self, data):
        """
        Generador que da la suma total de pasajeros por aerolinea.
        
        @param data: DataFrame de Pandas con los datos.
        
        @yield: Tupla con el nombre de la aerolinea y el total de pasajeros.
        """
        # Usando los metodos de Pandas groupby() y sum()
        suma_pasajeros = data.groupby('UNIQUE_CARRIER_NAME')['PASSENGERS'].sum()
        
        for aerolinea, total_pasajeros in suma_pasajeros.items():
            yield aerolinea, total_pasajeros 


    def encontrar_patrones(self, data):
        """
        Encuentra y muestra patrones usando la correlacion entre variables
        en la relacion entre la distancia y el numero de pasajeros, y
        la relacion entre la distancia y carga,
        
        @param data: DataFrame de Pandas con los datos cargados.
        """
        print("\nCorrelacion entre distancia y pasajeros:")
        print(data[['DISTANCE', 'PASSENGERS']].corr())

        print("\nCorrelacion entre distancia y carga:")
        print(data[['DISTANCE', 'FREIGHT']].corr())


    # def identificar_tendencias_mensuales(self, data):
    #     """
    #     Identifica y muestra las tendencias mensuales de pasajeros.
        
    #     @param data: DataFrame de Pandas con los datos cargados.
    #     """
    #     tendencias_mensuales = data.groupby('MONTH')['PASSENGERS'].sum()
    #     print("\nTendencias mensuales de pasajeros:")
    #     print(tendencias_mensuales)
    #     tendencias_mensuales.plot(kind='bar')
    #     plt.title('Tendencias Mensuales de Pasajeros')
    #     plt.xlabel('Mes')
    #     plt.ylabel('Total de Pasajeros')
    #     plt.show()

    def identificar_tendencias_mensuales(self, datos):
        """
        Identifica y muestra las tendencias mensuales de pasajeros, ajusta una linea
        utilizando la funcion polyfit de NumPy y calcula el Error Cuadratico Medio Normalizado (NRMSE).
        Inspirado en la sig referencia.
        @ref: https://www.emilkhatib.com/analyzing-trends-in-data-with-pandas/

        @param data: DataFrame de Pandas con los datos cargados.
        """
        # Agrupando datos por mes y sumando pasajeros y carga
        tendencias = datos.groupby('MONTH')[['PASSENGERS', 'FREIGHT']].sum().reset_index()

        # Crear subtramas
        fig, axs = plt.subplots(1, 2, figsize=(15, 5))  # 1 fila, 2 columnas

        # Subtrama para Pasajeros
        axs[0].plot(tendencias['MONTH'], tendencias['PASSENGERS'], marker='o', label='Pasajeros')
        # Linea de tendencia para Pasajeros
        z_pasajeros = np.polyfit(tendencias['MONTH'], tendencias['PASSENGERS'], 1)
        p_pasajeros = np.poly1d(z_pasajeros)
        axs[0].plot(tendencias['MONTH'], p_pasajeros(tendencias['MONTH']), "r--", label='Linea de Tendencia')
        axs[0].set_title('Tendencias Mensuales en el Trafico de Pasajeros')
        axs[0].set_xlabel('Mes')
        axs[0].set_ylabel('Total de Pasajeros')
        axs[0].legend()
        #plt.show()

        # Subtrama para Carga
        axs[1].plot(tendencias['MONTH'], tendencias['FREIGHT'], marker='o', label='Carga', color='green')
        # Linea de tendencia para Carga
        z_carga = np.polyfit(tendencias['MONTH'], tendencias['FREIGHT'], 1)
        p_carga = np.poly1d(z_carga)
        axs[1].plot(tendencias['MONTH'], p_carga(tendencias['MONTH']), "r--", label='Linea de Tendencia')
        axs[1].set_title('Tendencias Mensuales en el Trafico de Carga')
        axs[1].set_xlabel('Mes')
        axs[1].set_ylabel('Total de Carga')
        axs[1].legend()

        # Ajustar la disposicion
        plt.tight_layout()
        # Mostrar la fig con las subtramas
        plt.show()



    def buscar_valores_atipicos(self, data, columna='PASSENGERS'):
        """
        Busca y muestra valores atipicos en la cantidad de pasajeros usando un metodo de grafico 
        de caja usando Boxplot asi como usando el metodo estadistico de los Cuartiles
        Realizado con inspiracion en la informacion obtenida en la referencia
        
        @ref: https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/

        @param data: DataFrame de Pandas con los datos cargados.
        @param columna: Nombre de la columna para buscar valores atipicos.
        """
        # Metodo grafico usando boxplot
        print("Boxplot para identificar valores atipicos en pasajeros:")
        data.boxplot(column=['PASSENGERS'])
        plt.title('Valores Atipicos en Pasajeros')
        plt.ylabel('Pasajeros')
        plt.show()

        # Metodo estadistico de los Cuartiles
        Q1 = data[columna].quantile(0.25)
        Q3 = data[columna].quantile(0.75)
        IQR = Q3 - Q1       # Rango intercuartilico
        filtro = (data[columna] < (Q1 - 1.5 * IQR)) | (data[columna] > (Q3 + 1.5 * IQR))
        valores_atipicos = data[filtro]
        print(f"Valores Atipicos en columna {columna} :")
        print(valores_atipicos)

### --- # Fin de la clase --- ###################



class Filtrar_Por_Aerolinea:
    """
    @class Filtrar_Por_Aerolinea
    Clase para implementar un interador personalizados para filtrar
    los datos de alguna aerolinea en especifico.

    @param datos: DataFrame de Pandas que contiene los datos de vuelos.
    @param aerolinea: String con el nombre de la aerolinea que se va a  filtrar.
    """

    def __init__(self, datos, aerolinea):
        """
        Constructor de la clase Filtrar_Por_Aerolinea.

        @param datos: DataFrame de Pandas que contiene los datos de vuelos.
        @param aerolinea: String con el nombre de la aerolinea especifica.
        """
        self.datos = datos
        self.aerolinea = aerolinea
        self.index = -1     # Para llevar registro de la posicion actual dentro del DataFrame

    def __iter__(self):
        """
        Metodo iterador que devuelve el propio objeto iterador.

        @return: Devuelve la instancia actual del iterador.
        """
        return self

    def __next__(self):
        """
       Metodo iterador que devuelve el siguiente elemento del iterador.

        @return: La siguiente fila del DataFrame que coincide con la aerolinea especificada.
        @raise StopIteration: Se lanza cuando no hay mas filas que coincidan o se llega al final del DataFrame.
        """
        self.index += 1
        while self.index < len(self.datos):
            if self.datos.iloc[self.index]['UNIQUE_CARRIER_NAME'] == self.aerolinea:
                return self.datos.iloc[self.index]
            self.index += 1
        raise StopIteration



### --- # Fin de la clase --- ###################




# class Visualizacion_Datos:
#     """
#     @class Visualizacion_Datos
#     Clase para 
#     """
#     pass


### --- # Fin de la clase --- ###################




# Funcion principal o Main del programa
def main():

    # Se implementa el manejo de excepciones para asegurar un buen comportamiento
    try:
        # Implementacion de 2. Obtencion de Datos & 3. Limpieza y Preparacion de Datos
        # Datos tomados de:
        # https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=GDL&QO_fu146_anzr=Nv4%20Pn44vr45
        # Para el anno 2023
        filepath = "T_T100_MARKET_US_CARRIER_ONLY.csv"  # Nombre del archivo CSV
        data = Obtener_Datos(filepath)
        datos = data.cargas_datos()

        # Condicion verificar que los datos se hayan cargado correctamente
        if datos is  not None:
            
            
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

            # Codigo para verificar que funka 
            # print(datos.head(5))    # imprime los primeros 5 datos
            # print(datos.sample(3))  # imprime una muestra de 3 datos aleatorios 
            # print(datos.describe()) # imprime una descripcion general rapida de los datos numeros del DataFrame
            # print(datos.shape)      # imprime el tamanno del DataFrame


            # Implementacion de 4. Analisis de Datos

            # Para analizar datos
            # Instanciando la clase Analizar_Datos
            analizador = Analisis_Datos(filepath, datos)
            
            # Metodos para analizar datos
            # Instanciando Metodo calcular valores descriptivos
            valores_descrip = analizador.calcular_valores_descriptivos(datos)


            # Instanciando Metodo para calcular la cantidad de vuelos por aerolinea
            cantidad_vuelos_por_aerolinea = analizador.contar_vuelos_por_aerolinea(datos)
            # Usando un ciclo para imprimir los resultados
            for aerolinea, cantidad_vuelos in analizador.contar_vuelos_por_aerolinea(datos):
                print(f'\nPara la aerolinea: {aerolinea} \nLa cantidad de vuelos es: {cantidad_vuelos}')

            # Instanciando Metodo para calcular la cantidad de pasajeros por aerolinea
            pasajeros_aerolinea = analizador.contar_pasajeros_por_aerolinea(datos)
            # Usando un ciclo para imprimir los resultados
            for aerolinea, total_pasajeros in analizador.contar_pasajeros_por_aerolinea(datos):
                print(f'\nPara la aerolinea: {aerolinea} \nEl numero total de pasajeros es: {total_pasajeros}')
            
            # Instanciando Metodo encontrar patrones mediante la correlacion entre variables
            analizador.encontrar_patrones(datos)

            analizador.identificar_tendencias_mensuales(datos)
            analizador.buscar_valores_atipicos(datos)

            # Para filtrar por una aerolinea en particular
            # Instanciando la clase Filtrar_Por_Aerolinea
            filtro = Filtrar_Por_Aerolinea(datos, 'American Airlines Inc.')
            max_filas = 3       # Numero para indicar el numero maximo de filas a imprimir (para no imprimir todo)
            contador_filas = 0  # Inicializando un contador para las filas

            # print(f'\nImprimiendo solamente: {max_filas} filas (para evitar imprimir todo) de datos completas del filtrado: \n')
            # for i in filtro:
                
            #     if (contador_filas < max_filas):
            #         print(i)
            #         contador_filas += 1
            #     else:
            #         break
        

        # En caso de que no se carguen los datos del CSV        
        else:
            raise ValueError
    



    # Excepciones
    except FileNotFoundError:
            print(f"Error: El archivo {filepath} no fue encontrado.\n")
    except ValueError:
            print(f"Error de carga: Los datos no se han cargado correctamente.")
    except Exception as e:         
<<<<<<< HEAD
        print(f"Error desconocido: {e}\n")
=======
            print(f"Error desconocido: {e}\n")
>>>>>>> 9f1ac0e62614417688651a371f5a581017c902d4



# Llamado de la funcion main
if __name__ == "__main__":
    main()