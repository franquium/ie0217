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




## Parte Practica 1: Interpretación de Resultados


Para esta seccion debido a que quedaba a investigacion propia del estudiante la implementacion, aplicacion y analisis se procedio a hacer un analisis no tan complejo en el numero de combinaciones a analizar pero si significativo y ejemplificativo para la tarea.


<!--- [KDnuggets](https://www.kdnuggets.com/profiling-python-code-using-timeit-and-cprofile)  -->


* Puntaje ingresado: 128 (busca un solo elemento de la lista)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.000703 s
* Puntaje ingresado: 1027 (desglosa en tres alergias de la lista)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.001517 s

