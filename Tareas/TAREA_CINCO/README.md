# Tarea 5
Repositorio para la Tarea 5 del curso de Estructuras Abstractas de Datos y Algoritmos.


## Para correr el programa

Para correr el programa desde la terminal de VSCode u otra, primero tiene que verificar que tenga instalado el Python 3.9 en su dispositivo o alguna version posterior, para ello corra en la terminal:

```bash
python --version
```

Ademas asegurarse de terner instalado las lib de Pandas, MatPlotLib, Seaborn

De no aparacer un mensaje en terminal indicando la version instalada junto con otra info en un cajetin, proceda a instalarlo segun su OS, recuerde GIYF.

Seguidamente, verifique que tenga instalado el Make en su dispositivo, para ello corra en la terminal:

```bash
make --version
```

De no aparacer un mensaje en terminal indicando la version instalada junto con otra info en un cajetin, proceda a instalarlo segun su OS, recuerde GIYF.

Una vez verificado lo anterior, proceda acceder desde su terminal el directorio src con los archivos, y para correr el programa escriba en la terminal el comando:

```bash
make 
```

Su programa deberia correr satisfactoriamente. 

### Nota Importante



## Parte Teórica 

### Iteradores

1. ¿Qué es un iterador en Python y cuál es su propósito?
 
 Un iterador es en Python es un objeto que implementa los metodos `__iter__() ` y `__next__()`
 es un metodo que permite recorrer los elementos dentro de un contendeor, como una lista, tupla, etc de manera secuencial sin necesidad de conocer la estructura interna del contenedor.


2. Explique la diferencia entre un iterable y un iterador.

Un iterable es cualquier objeto en Python sobre el cual se puede iterar, es decir, que puede ser usado en un cilo for, y utiliza el metodo `__iter__() `. Mientras que un iterador es el objeto que realiza la iteracion efectiva, utilizaa el método `__next__()` que devuelve el siguiente elemento en la secuencia.

### Excepciones

3. Defina qué es una excepción en Python.

Una excepcion en Python es un "evento" que ocurre durante la ejecucion de un programa que interrumpe el flujo normal de las instrucciones del programa.


4. ¿Cuál es el propósito de la cláusula `try...except` en el manejo de excepciones?

La cláusula try...except se utiliza para capturar y manejar excepciones en Python. 
Permite definir un bloque de código a "probar" (try) y especificar una o mas respuestas ante determinadas excepciones (except). Esto se hace para prevenir la terminacion abrupta del programa y permite una recuperacion o manejo adecuado del error. A continuación, ejemplo para gestionarlas:

```
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("División por cero.")
```
 
5. Explica la diferencia entre las cláusulas except y finally en el manejo de excepcione

La cláusula except se permite captar y manejar excepciones específicas o generales que ocurren dentro del bloque try. Mientras que la cláusula finally se ejecuta siempre, tanto si ocurrió una excepción o no en el bloque try. Generalmente se usa para realizar acciones de limpieza, como el cierre de archivos o la liberación de recursos externos.




### Generadores
 
6. ¿Qué es un generador en Python y cuál es su ventaja sobre las listas tradicionales?

Los generadores funciones para crear iteradores en Python. Utilizan la declaración yield para devolver datos (en vez de return). 
Cuando un generador es llamado, retoma donde lo dejó (recuerda todos los datos y el punto exacto de ejecución). 

La ventaja sobre las listas tradicionales es que estos consumen menos memoria, especialmente con secuencias grandes. Ya que no se almacenan todos los elementos a la vez en la memoria


7. Explique cómo se puede crear un generador usando la función yield.

Se crea un generador definiendo una función con def pero en lugar de la declaración de retorno, se usa la declaración yield. Con ella se produce un valor del generador y se pausa la ejecución de la función hasta que se solicite el siguiente valor. Cada vez que la función generadora se reanuda después de un yield, continúa su ejecución desde el punto donde se detuvo.
Ejemplo:

```
# generador de el cuadrado de un numero
def elevar_al_cuadrado(nums):
    for num in nums:
        yield num**2
```

 
8. ¿Cuándo es más apropiado usar generadores en lugar de listas?

Es apropiado usar generadores al trabajar con secuencias de datos grandes, que no se requieren almacenar completamente en la memoria. O al hacer una evaluación perezosa para mejorar la eficiencia del programa. 


### Pandas

9. ¿Cuál es la diferencia entre una Serie y un DataFrame en Pandas?

En Pandas una Serie es un arreglo unidimensional en el que se puede almacenar datos de cualquier tipo con etiquetas o indice. Mientras que un DataFrame es una estructura de datos bidimensional. Un DataFrame es similar a una tabla de base de datos o una hoja de calculo. Solo una columna de un DataFrame es una Serie, lo cual implica que un DataFrame está formado por varias Series.


 
10. Explica cómo manejar valores nulos o faltantes en un DataFrame.

Pandas posee varias funciones para manejar este tipo de valores. Para eliminar filas o columnas con valores nulos existe `dropna()`.  Por otra parte, para reemplazar los valores nulos con un valor específico o un método de interpolación es posible usar `fillna()`.


11. ¿Cuál es la diferencia entre loc y iloc en Pandas?

Ambas se usan para acceder a un grupo de filas y columnas, en el caso de loc se accede por etiquetas o una matriz booleana. En cambio, con iloc se accede por posición numérica (índices enteros).



## Parte Practica 1:  Analisis de Datos & Interpretación de Resultados


En esta seccion se hace una interpretacion de los resultados obtenidos al realizar el analisis de datos y la visualizacion de datos.

1. Primero para el calculo de los valores descriptivos se utliza el metodo de Pandas `.describe()`, los resultados que se obtienen son los siguientes:

```
          PASSENGERS       FREIGHT          MAIL       DISTANCE     AIRLINE_ID          MONTH
count  241955.000000  2.419550e+05  2.419550e+05  241955.000000  241955.000000  241955.000000
mean     3257.298841  1.245503e+05  3.321432e+03     995.827708   20243.158290       5.523320
std      6393.819478  7.733412e+05  3.718061e+04    1016.028333     670.211065       2.862242
min         0.000000  0.000000e+00  0.000000e+00       0.000000   19393.000000       1.000000
25%         6.000000  0.000000e+00  0.000000e+00     335.000000   19805.000000       3.000000
50%       439.000000  0.000000e+00  0.000000e+00     742.000000   20272.000000       6.000000
75%      3981.000000  2.193000e+03  0.000000e+00    1262.000000   20416.000000       8.000000
max     95703.000000  9.589923e+07  2.570979e+06   10908.000000   22119.000000      10.000000

```

Se puede observar que el promedio para pasajeros (passengers) tiene un 3257.30 mientras que el valor maximo es de 95703
lo cual nos hace indicar que hay datos atipicos o anomalos en los datos obtenidos (mas adelante se discutira mas sobre esto) ademas de que para un vuelo comercial tener 95703 pasajeros no se ve como algo fisicamente posible, en la pagina de la base de datos no se encontro al momento de redaccion una explicacion de estos numeros tan inusualmente grandes. Pero como ejercicio academico vamos a hacer una suspension de juicio, y tratar los datos como datos nada mas.

`Nota Importante: Se puede argumentar Mutatis Muntatis lo expuesto para pasajeros tanto para la Carga (Freight) o Correo (Mail)`

<!--- [KDnuggets](https://www.kdnuggets.com/profiling-python-code-using-timeit-and-cprofile)  -->

2. Para el conteo del cantidad de vuelos por aerolinea se utiliza el metodo `contar_vuelos_por_aerolinea()`,  donde se encontro que la aerolinea con mayor cantidad de vuelos fue `Southwest Airlines Co.` con 37858 vuelos, mientras que el minimo lo obtuvo `Polaris Aviation Solutions, LLC` con 9 vuelos.

Para el conteo de la cantidad depasajeros por aerolinea se utiliza el metodo `contar_pasajeros_por_aerolinea()` debido a lo mencionado previamente sobre la cantidad de pasajeros entra dudas de que estos datos sean confiables.

La impresion de resultados para estos donde conteo se muestra a continuacion de forma ilustrativa (con unos pocos casos):

```
Algunos resultados de contar_vuelos_por_aerolinea():

Para la aerolinea: Southwest Airlines Co.
La cantidad de vuelos es: 37858

Para la aerolinea: United Air Lines Inc.
La cantidad de vuelos es: 18918

...

Para la aerolinea: Polaris Aviation Solutions, LLC
La cantidad de vuelos es: 9


Algunos resultados de contar_pasajeros_por_aerolinea():

Para la aerolinea: JetBlue Airways
El numero total de pasajeros es: 35982600.0

Para la aerolinea: Junipogo, LLC
El numero total de pasajeros es: 398.0

Para la aerolinea: KENAI AVIATION OPERATIONS, LLC
El numero total de pasajeros es: 7271.0

Para la aerolinea: KaiserAir, Inc.
El numero total de pasajeros es: 5869.0

```


3. Para encontrar patrones se utiliza el metodo `encontrar_patrones()` donde se decicio calcular la correlacion, usando el metodo .corr() de SciPy,  entre variables, particularmente en dos ejemplos: entre la distancia y el numero de pasajeros, y entre la distancia y la carga, si se modifica ligeramente el codigo del metodo se podria calcular la correlacion entre los datos distintos datos que el usario o programador desee. Los resultados obtenidos fueron los siguientes:

```
Correlacion entre distancia y pasajeros:
            DISTANCE  PASSENGERS
DISTANCE    1.000000    0.074611
PASSENGERS  0.074611    1.000000

Correlacion entre distancia y carga:
          DISTANCE   FREIGHT
DISTANCE  1.000000  0.178639
FREIGHT   0.178639  1.000000
```

Usando el hecho que entre mas cercanos sus valores a cero la correlacion entre las variables sera mas debil, y entre mas cercanos sus valores a 1 o -1 la correlacion sera mas fuerte, se puede inferir que no hay una relación lineal fuerte entre la distancia de los vuelos y el número de pasajeros o la cantidad de carga.


4. Para buscar o indetificar tendencias en los datos, se decide hacerlo a lo largo del transcurso del tiempo, en este caso el paso de los meses,  se utiliza el metodo `identificar_tendencias_mensuales`, y se realiza un analisis inspirado en los encontrado en la referencia [KDnuggets](https://www.emilkhatib.com/analyzing-trends-in-data-with-pandas/), donde se agrupan los datos por cada mes y luego se suman, se grafican usar las herramientas de MatPlotLib y con polyfit de Numpy se encuentra una linea de tendencia sobre los datos para ver como se compartan. En el codigo se implementa para ver las tendencias de pasajeros mensualmente y la carga mensualmente.

5. Para la busqueda de valores atipicos o anomalos, se utiliza el metodo `buscar_valores_atipicos()`, dentro del cual se implementan dos metodos para encontrar valores anomalos, uno grafica usando la herramienta `boxplot()` donde se crea un grafico de caja, en el cual los valoes que se encuentran mas arriba de los bigotes son considerados anomalos.
Tambien se utiliza un metodo estadisticos de los [Cuartiles ](https://careerfoundry.com/en/blog/data-analytics/how-to-find-outliers/) donde los resultados para el caso de la columna de pasajeros (PASSENGERS) que se imprimen son de la sig. forma:

```
Valores Atipicos en columna PASSENGERS :
        PASSENGERS   FREIGHT      MAIL  DISTANCE  AIRLINE_ID     UNIQUE_CARRIER_NAME ORIGIN ORIGIN_CITY_NAME DEST DEST_CITY_NAME  MONTH CLASS
220272      9944.0       0.0       0.0     301.0       20409         JetBlue Airways    BUF      Buffalo, NY  JFK   New York, NY      7     F
220273      9944.0       0.0       0.0     899.0       19977   United Air Lines Inc.    YYC  Calgary, Canada  DEN     Denver, CO      3     F
220274      9944.0     609.0       0.0     493.0       19805  American Airlines Inc.    PHX      Phoenix, AZ  FAT     Fresno, CA      9     F
220275      9945.0      62.0   13275.0    1788.0       19805  American Airlines Inc.    TPA        Tampa, FL  PHX    Phoenix, AZ      4     F
220276      9945.0   17155.0       0.0     484.0       19393  Southwest Airlines Co.    ATL      Atlanta, GA  STL  St. Louis, MO      3     F
...            ...       ...       ...       ...         ...                     ...    ...              ...  ...            ...    ...   ...
242211     87271.0  482563.0  243944.0    1448.0       19930    Alaska Airlines Inc.    SEA      Seattle, WA  ANC  Anchorage, AK      6     F
242212     88718.0  502356.0  339715.0    1448.0       19930    Alaska Airlines Inc.    SEA      Seattle, WA  ANC  Anchorage, AK      8     F
242213     92946.0  631910.0   20381.0    1448.0       19930    Alaska Airlines Inc.    ANC    Anchorage, AK  SEA    Seattle, WA      8     F
242214     93849.0  482976.0  199958.0    1448.0       19930    Alaska Airlines Inc.    SEA      Seattle, WA  ANC  Anchorage, AK      7     F
242215     95703.0  417923.0   14863.0    1448.0       19930    Alaska Airlines Inc.    ANC    Anchorage, AK  SEA    Seattle, WA      7     F

[21944 rows x 12 columns]
```

En los resultados se pueden apreciar lo que se discutio previamente cuando se utilizo el metodo `describe()` sobre el valor maximo encontrado para pasajeros de 95703, tambien podemos apreciar que para cantidades de pasajeros mayores a 9944 se pueden considerar anomalos.

6. Para filtrar los datos por el nombre de una aerolinea en especifico se utilizo los generadores de la clase `Filtrar_Por_Aerolinea` implementada en el codigo, la cual es una clase  iterador o para iterar. 
Para el ejemplo de la aerolinea `American Airlines Inc.` se puede ver al correr el codigo.

7. Para la visualizacion grafica de Datos, previamente se menciono como los metodos,  `identificar_tendencias_mensuales` y `buscar_valores_atipicos()` utiliza la lib de MatPlotLib para ayudarse en la graficacion, el uso de la lib Seaborn se utiliza en los metodos  creados`histograma_seaborn()` y `scatterplot_seaborn()`, el primero permite hacer un histograma de frecuencia de la columna de datos escogida, en el codigo de main se implementa con los datos de distancia (DISTANCE), y el otro metodo permite hacer una distribucion de dispersion entre dos columnas de datos escogidas, para ver su si presentar alguna relacion, en el codigo de main se implementa con los datos de distancia (DISTANCE) y la carga (FREIGHT), si se hace por ejemplo para la distancias y los meses, se obtiene una distribucion de dispersion que asemeja el comportamiento y tendencias de la grafica obtenida con el metodo `identificar_tendencias_mensuales()`.

8. Cabe mencionar que tambien se implemento en la func main de manera exitosa el Manejo de Excepciones