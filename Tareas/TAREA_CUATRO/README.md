# Tarea 4
Repositorio para la Tarea 4 del curso de Estructuras Abstractas de Datos y Algoritmos.


## Para correr el programa

Para correr el programa desde la terminal de VSCode u otra, primero tiene que verificar que tenga instalado el Python 3.9 en su dispositivo o alguna version posterior, para ello corra en la terminal:

```bash
python --version
```

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

> Para ver el funcionamiento de la Parte Practica 2 con las lista de 50 alergias modificar el documento alergia.py (comentar y descomentar) segun lo indicado en la documentacion y comentarios presente en el dicho archivo.



## Parte Teórica 

1. Explique la diferencia entre una lista y una tupla en Python

Las listas y las tuplas son colecciones de elementos de diferentes tipos. En las listas pueden ocurrir cambios en sus elementos. Al contrario, en una tupla no se puede cambiar sus elementos después de creada. Por lo tanto, las tuplas son útiles para asegurar que los datos permanezcan constantes e iterar a través de una tupla es más rápido que con una lista. Seguidamente se muestran otras diferencias con respecto a la sintaxis:

•	Listas: Se definen con corchetes [], por ejemplo: mi_lista = [1, 2, 3].

•	Tuplas: Se definen con paréntesis (), por ejemplo: mi_tupla = (1, 2, 3).


2. ¿Qué es la sobrecarga de operadores en Python y cómo se implementa?

La sobrecarga de operadores permite que los operadores estándar de Python (como +, -, *, /) tengan un significado diferente según el tipo de operandos. Se implementa mediante métodos especiales en las clases. Por ejemplo, para sobrecargar el operador +, se define el método `__add__` en la clase. 

Por ejemplo:

```
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        x = self.x + otro.x 
        y = self.y + otro.y	
        return Punto(x, y)
```


3. Explique el concepto de “alcanzabilidad” (scope) de una variable en Python.

El alcance de una variable se refiere a la región del programa donde la variable es reconocida. Python tiene dos tipos de alcances: el local, donde la variable es reconocida solo dentro de la función o bloque donde es declarada y el global, donde la variable es reconocida a lo largo de todo el programa.


4. ¿Qué es un decorador en Python y cuál es su función principal?

Un decorador modifica el comportamiento de otra función. Se usa para extender o alterar las funcionalidades de funciones o métodos sin cambiar su código. Se aplica con el símbolo @ seguido del nombre del decorador antes de la definición de la función. 

 
5. ¿Cómo se gestionan las excepciones en Python? Proporcione ejemplos de uso de bloques try, except y finally.

Los errores detectados durante la ejecución del programa corresponden a las excepciones en Python. A continuación, ejemplos para gestionarlas:

```
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("División por cero.")
finally:
    print("Este bloque se ejecuta siempre.")
```

 
6. ¿Qué son los generadores en Python y para qué se utilizan?

Los generadores funciones para crear iteradores en Python. Utilizan la declaración yield para devolver datos (en vez de return). 
Cuando un generador es llamado, retoma donde lo dejó (recuerda todos los datos y el punto exacto de ejecución). 
Se utilizan para trabajar con conjuntos grandes de datos, ya que no necesitan almacenar todos los elementos en memoria. Por esta razón son más eficientes que las funciones normales o las listas.

 
7. Explique la diferencia entre `__init__` y `__call__` en clases de Python.

En Python `__init__`permite construir una clase y se llama automáticamente al crear una nueva instancia de tal clase. También es usada para iniciar atributos del objeto.
 Mientras `__call__` hace que una instancia de la clase se comporte como función y se llama cuando la instancia es “llamada” como función. 



 
8. ¿Cómo se organizan los módulos y paquetes en Python? ¿Qué es `__init__.py`?

Los módulos en Python son archivos de Python que contienen definiciones y declaraciones de Python. Un paquete es una forma de organizar módulos jerárquicamente mediante directorios. 
Ahora, el archivo__init__.py es de gran importancia pues un directorio debe contener el para ser considerado por Python como un paquete. El archivo `__init__.py` puede estar vacío, pero es fundamental para que Python importe módulos o subpaquetes de ese paquete.


9. Explique la diferencia entre métodos append() e extend() en listas de Python.

En las listas append() permite agregar un elemento al final de la lista. Si se añade una lista con append(), esta se agrega como un único elemento. Por otra parte, extend() extiende la lista agregando elementos de un iterable al final. Si se usa extend() con otra lista, sus elementos se añaden individualmente.

 
10. ¿Cuál es la diferencia entre un método de clase y un método estático en Python?

Un método de clase (@classmethod) recibe la clase como primer argumento en lugar de la instancia de la clase (self). Se denota como cls. Puede modificar el estado de la clase, esto afecta a todas las instancias de la clase. Crea fábricas de objetos o métodos que afectan a toda la clase.

Mientras que un método estático (@staticmethod) no recibe un argumento implícito especial (self o cls). Es como una función regular, pero pertenece al espacio de nombres de la clase. Se emplea para funciones que tienen una relación lógica con la clase, pero que no necesitan acceder a sus propiedades o métodos.


11. Hable sobre las diferencias entre herencia simple y herencia múltiple en Python

Seguidamente se anotan las principales características de los tipos de herencia en Python, las cuales son diferencias fundamentales entre ambas.

•	Herencia Simple: una nueva clase (subclase) se deriva de una única clase padre o principal (superclase). La subclase hereda atributos y métodos de la clase principal. Esto facilita la comprensión y el mantenimiento del código.

•	Herencia Múltiple: la subclase se crea a partir de más de una clase principal. La subclase hereda atributos y métodos de todas las superclases. Para resolver el orden para acceder a tales atributos y métodos se usa el método MRO (Method Resolution Order). Estas características pueden generar mucha complejidad, por ejemplo, al considerar que se tengan atributos o métodos con nombres iguales en las clases padres.


12. ¿Cómo se manejan los errores de importación de módulos en Python?

Cuando Python no puede encontrar el módulo o los elementos dentro del módulo que se intenta importar se producen errores de importación. Estos se manejan utilizando bloques try-except.
Por ejemplo:

```
try:
    import modulo_que_no_existe
except ModuleNotFoundError as e:
    print("Hubo un error:", e)
```
 

13. ¿Cuál es la diferencia entre una clase y un objeto en Python?

En Python una clase es una plantilla o molde para crear objetos, pues consiste en un conjunto de atributos y métodos para caracterizar a un objeto. 
Mientras que un objeto es una instancia de una clase, es una entidad con un estado y comportamiento definidos por su clase.
Una analogía para mejorar la comprensión de estas definiciones es que la clase es un plano arquitectonico (blueprint) de una casa, mientras que la casa construida corresponde al objeto. A partir de un boceto se pueden elaborar muchas casas. Del mismo modo es posible crear muchos objetos de una clase.

 
14. Hable sobre la diferencia entre una clase abstracta y una interfaz en Python.

En Python una clase abstracta define un 'blueprint' o boceto para otras clases, pero no se puede instanciar directamente. Se crea usando el módulo abc. Además, este tipo de clase puede tener métodos implementados y métodos abstractos (sin implementación).
Por otra parte, una interfaz es un concepto relacionado con la definición de un conjunto de métodos. En este lenguaje no se tienen interfaces de forma nativa como otros lenguajes, pero se pueden simular usando clases abstractas con métodos abstractos. Una clase abstracta con solo métodos abstractos puede considerarse una interfaz.


 
15. Explique el concepto de sobreescritura de métodos en Python y cómo se realiza.

La sobreescritura de métodos ocurre cuando una clase hija o subclase proporciona una implementación específica de un método que ya está definido en su clase padre o superclase. De esta forma se puede modificar o extender el comportamiento del método heredado. Seguidamente se muestra un ejemplo de cómo se realiza:

```
class Padre:
    def saludar(self):
        print("Hola desde la clase Padre")

class Hijo(Padre):
    def saludar(self):
        print("Hola desde la clase Hijo")
```



## Parte Practica 2: Sobre Medicion de tiempo de ejecucion y Perfilado del Codigo


Para esta seccion debido a que quedaba a investigacion propia del estudiante la implementacion, aplicacion y analisis se procedio a hacer un analisis no tan complejo en el numero de combinaciones a analizar pero si significativo y ejemplificativo para la tarea.

Se realizo basado en los ejemplos y teoria sobre el tema encontrados en la siguiente pagina web: 
[KDnuggets](https://www.kdnuggets.com/profiling-python-code-using-timeit-and-cprofile)

### Medicion de Tiempo de Ejecucion

Para esta seccion se hace uso del modulo `timeit` basado a lo que se encontro en las referencias  que se recomienda usar en fragmentos de codigo cortos, se procede a usar el temporizador `default_timer()` del modulo para medir el tiempo entre que se ejecutan un fragmento de codigo, la sintaxis es de la forma:

```
start_time = timeit.default_timer()  # Iniciar el temporizador de timeit

# <Codigo a medir va aqui>

end_time = timeit.default_timer()  # Finalizar el temporizador de timeit
print(f"Tiempo de ejecucion: {end_time - start_time} s.")
```

Se decide usar el timeit para medir el tiempo de cuando la instanciacion y uso de los metodos de la clase Evaluacion_Especifica.
 Para medir Evaluacion_Especifica, se realiza la opcion 1 del Menu `Ingresar puntuacion de alergia y ver alergias sensibles` dado que se puede realizar a casi las misma velocidad de parte del usuario y para estandarizarlo:

Usando la lista predefinida con las 11 alergias iniciales (`alergias_predefinidas`):

* Puntaje ingresado: 128 (busca un solo elemento de la lista)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.000703 s
* Puntaje ingresado: 1027 (desglosa en tres alergias de la lista)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.001517 s

Usando la lista predefinida con las 50 alergias:

* Puntaje ingresado: 128 (busca un solo elemento de la lista)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.000981 s
* Puntaje ingresado: 1027 (desglosa en tres alergias de la lista)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.001698 s
* Puntaje ingresado: 562949953421312 (busca un solo elemento de la lista, pero con entrada de 15 digitos)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.000943 s
* Puntaje ingresado: 565149513547776 (desglosa en tres alergias de la lista, pero cada una contiene 9 o mas digitos en su valor)
    * Se obtiene un tiempo de ejecuccion es de aprox: 0.001734 s


### Perfilado del Codigo

Para esta seccion se hace uso del modulo `cProfile` basado a lo que se encontro en las referencias se decide hacer el profilling ordenando los resultos por tiempo de ejecucion, para ello se utiliza sort_stats, se utliliza el siguiente codigo como plantilla:

```
with cProfile.Profile() as profile:
        main() # <Funcion principal que contiene el llamado a la interfaz del programa>
    profile_result = pstats.Stats(profile)
    profile_result.sort_stats(pstats.SortKey.TIME)
    profile_result.print_stats()
```

Usando el codigo para la prueba la opcion 1 del Menu `Ingresar puntuacion de alergia y ver alergias sensibles` y seguidamente de volver al menu se digita 4 para salir del programa, en este caso procurando que se realicer a casi las misma velocidad de parte del usuario y para estandarizarlo:

Usando la lista predefinida con las 11 alergias iniciales (`alergias_predefinidas`):

* Puntaje ingresado: 128 (busca un solo elemento de la lista)
    * Se obtiene que se llaman 30 funciones en un tiempo de ejecuccion es de aprox: 3.544 s
    * Donde el informe de profilling es de la forma:
     
    ```
        30 function calls in 3.544 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    3.539    1.180    3.539    1.180 {built-in method builtins.input}
       15    0.005    0.000    0.005    0.000 {built-in method builtins.print}
        1    0.000    0.000    3.544    3.544 c:\...\TAREA_CUATRO\src\main.py:53(iniciar_interfaz)
        1    0.000    0.000    0.001    0.001 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:35(mostrar_puntuacion)
        1    0.000    0.000    3.544    3.544 c:\...\TAREA_CUATRO\src\main.py:158(main)
        1    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:19(evaluar_alergias)
        1    0.000    0.000    0.000    0.000 C:\Program Files\Inkscape\lib\python3.9\cProfile.py:117(__exit__)
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:11(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\tipos_de_alergias.py:10(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      ```

De este datos se puedes aprenciar que para este programa el mayor consumo de tiempo se encuentra al pedirle al usuario que ingrese datos, toma 3.359 s equivalente al 99.86 % del tiempo, ademas se ve que se llama el pedir datos 3 veces (primera vez: digitar la opcion 1, 2da vez: digitar el puntaje, 3ra vez: digitar la opcion 4: salir).

 Ademas se puede apreciar en ncalls los diferentes llamados de funciones o metodos, de las que se llaman una vez, se puede apreciar el llamado al metodo evaluar_alergias de la clase Evaluacion_Especifica (en el archivo evaluacion_especifica.py).
Las funciones que mas se llaman como se puede apreciar es la funcion print() que se llama 15 veces y esos llamados consumen 0.005 s del tiempo total.

Para el caso donde: 

* Puntaje ingresado: 1027 (desglosa en tres alergias de la lista)
   * Se obtiene que se llaman 34 funciones en un tiempo de ejecuccion es de aprox: 5.041 s
    * Donde el informe de profilling es de la forma:

    ```
             34 function calls in 5.041 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    5.037    1.679    5.037    1.679 {built-in method builtins.input}
       17    0.005    0.000    0.005    0.000 {built-in method builtins.print}
        1    0.000    0.000    5.041    5.041 c:\...\TAREA_CUATRO\src\main.py:53(iniciar_interfaz)
        1    0.000    0.000    0.001    0.001 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:35(mostrar_puntuacion)
        1    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:19(evaluar_alergias)
        1    0.000    0.000    5.041    5.041 c:\...\TAREA_CUATRO\src\main.py:158(main)
        1    0.000    0.000    0.000    0.000 C:\Program Files\Inkscape\lib\python3.9\cProfile.py:117(__exit__)
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:11(__init__)
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\tipos_de_alergias.py:10(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    ```

De este datos se puedes aprenciar que para este caso ademas de aumentar el tiempo de ejecucion a 5.041 s tambien aunmentarl el numero de funciones llamadas a 34 programa, donde se llaman 2 veces mas (17) a la funcion print y dos veces mas (3) a la funcion append, para agregar las alergias que antes eran 1 y ahora son 3. 

Para este se caso, se vuelve a ver que se llama el pedir datos 3 veces (primera vez: digitar la opcion 1, 2da vez: digitar el puntaje, 3ra vez: digitar la opcion 4: salir).
Asi como que metodo evaluar_alergias de la clase Evaluacion_Especifica (en el archivo evaluacion_especifica.py) se llama una vez.



Usando la lista predefinida con las 50 alergias:



* Puntaje ingresado: 562949953421312 (busca un solo elemento de la lista, pero con entrada de 15 digitos)
    * Se obtiene que se llaman 30 funciones en un tiempo de ejecuccion es de aprox: 17.329 s
    * Donde el informe de profilling es de la forma:


    ```
             30 function calls in 17.329 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3   17.324    5.775   17.324    5.775 {built-in method builtins.input}
       15    0.005    0.000    0.005    0.000 {built-in method builtins.print}
        1    0.000    0.000   17.329   17.329 c:\...\TAREA_CUATRO\src\main.py:53(iniciar_interfaz)
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:19(evaluar_alergias)
        1    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
        1    0.000    0.000    0.001    0.001 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:35(mostrar_puntuacion)
        1    0.000    0.000    0.000    0.000 C:\Program Files\Inkscape\lib\python3.9\cProfile.py:117(__exit__)
        1    0.000    0.000   17.329   17.329 c:\...\TAREA_CUATRO\src\main.py:158(main)     
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:11(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\tipos_de_alergias.py:10(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

    ```

Se puede apreciar que es analogo al caso hecho con la lista de 11 alergias donde solamente busca un solo elemento de la lista y que la diferencia tan grande en el tiempo de ejecuccion se debe al tiempo que le toma al usuario ingresar los datos, en este caso el puntaje alergico que en este caso es un numero de 15 digitos. No se ve niguna diferencia (en el informe de profilling) en los demas tiempo de ejecucion para el caso de la opcion 1.



* Puntaje ingresado: 565149513547776 (desglosa en tres alergias de la lista,pero cada una contiene 9 o mas digitos en su valor)
    * Se obtiene que se llaman 34 funciones en un tiempo de ejecuccion es de aprox: 19.737 s
    * Donde el informe de profilling es de la forma:


    ```
            34 function calls in 19.737 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3   19.732    6.577   19.732    6.577 {built-in method builtins.input}
       17    0.005    0.000    0.005    0.000 {built-in method builtins.print}
        1    0.000    0.000   19.737   19.737 c:\...\TAREA_CUATRO\src\main.py:53(iniciar_interfaz)
        1    0.000    0.000    0.001    0.001 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:35(mostrar_puntuacion)
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:19(evaluar_alergias)
        1    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
        1    0.000    0.000   19.737   19.737 c:\...\TAREA_CUATRO\src\main.py:158(main)      
        1    0.000    0.000    0.000    0.000 C:\Program Files\Inkscape\lib\python3.9\cProfile.py:117(__exit__)
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\evaluacion_especifica.py:11(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
        1    0.000    0.000    0.000    0.000 c:\...\TAREA_CUATRO\src\tipos_de_alergias.py:10(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

    ```

Se puede apreciar que es analogo al caso hecho con la lista de 11 alergias donde se desglosa en tres alergias de la lista y que la diferencia tan grande en el tiempo de ejecuccion se debe al tiempo que le toma al usuario ingresar los datos, en este caso el puntaje alergico que en este caso es un numero de 15 digitos. No se ve niguna diferencia (en el informe de profilling) en los demas tiempo de ejecucion para el caso de la opcion 1.