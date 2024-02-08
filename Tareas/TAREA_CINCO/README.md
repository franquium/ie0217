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


### Generadores
 
6. ¿Qué es un generador en Python y cuál es su ventaja sobre las listas tradicionales?

Los generadores funciones para crear iteradores en Python. Utilizan la declaración yield para devolver datos (en vez de return). 
Cuando un generador es llamado, retoma donde lo dejó (recuerda todos los datos y el punto exacto de ejecución). 
 
7. Explique cómo se puede crear un generador usando la función yield.



 
8. ¿Cuándo es más apropiado usar generadores en lugar de listas?


### Pandas

9. ¿Cuál es la diferencia entre una Serie y un DataFrame en Pandas?

 
10. Explica cómo manejar valores nulos o faltantes en un DataFrame.

11. ¿Cuál es la diferencia entre loc y iloc en Pandas?




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


<!--- [KDnuggets](https://www.kdnuggets.com/profiling-python-code-using-timeit-and-cprofile)  -->


* Puntaje ingresado: 128 (busca un solo elemento de la lista)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.000703 s
* Puntaje ingresado: 1027 (desglosa en tres alergias de la lista)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.001517 s




