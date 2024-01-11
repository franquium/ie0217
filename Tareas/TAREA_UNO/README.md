# Tarea 1
Repositorio para la Tarea 1 del curso de Estructuras Abstractas de Datos y Algoritmos.


## Para correr el programa

Para correr el programa desde la terminal de VSCode u otra, primero tiene que verificar que tenga instalado el compilar g++ en su dispositivo, para ello corra en la terminal:

```bash
g++ --version
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

Su programa deberia correr satisfactoriamente. ``` Mischief managed! :-)```


## Parte Teórica C++



1. ¿Cual es la principal diferencia entre C y C++?

La principal diferencia entre C y C++ consiste en que en el lenguaje C está orientado a la programación estructurada, es decir, en un conjunto de sentencias o instrucciones que se ejecutan una por una. En este lenguaje se procesan unos datos de entrada para obtener unos de salida. Mientras que C++ es un lenguaje de programación orientada a objetos, en el que se crean los objetos para luego solicitarles que hagan los métodos por sí solos. [1]

2. ¿Cuales son las diferencias fundamentales entre un lenguaje de programacion compilado y uno interpretado?
Proporcione ejemplos de situaciones en las que serıa mas optimo utilizar un lenguaje compilado y otras en las que serıa mas adecuado un lenguaje interpretado.

Entre las principales diferencias se encuentran:

El lenguaje compilado usa un compilador para convertir el código fuente en código de máquina, mientras que el lenguaje interpretado requiere de un intérprete.
Al utilizar lenguaje compilado, la CPU puede ejecutar el archivo ejecutable directamente, mientras que en el interpretado se ejecuta directamente línea a línea el código. Esto implica que el compilado por lo general es más rápido. 
Con respecto a errores, en el interpretado un intérprete informa solo un error a la vez, lo que facilita la depuración. Al contrario, en lenguajes compilados un compilador informa de todos los errores presentes en el programa al compilar, esto impide la compilación y dificulta la depuración.

Los lenguajes compilados serian optimo para aplicaciones donde la velocidad y estabilidad son fundamentales, por ejemplo codigos de submarinos nucleares o carros self-driving. Mientras que un lenguaje interpretados son mas adecuados para programas cortos, sencillos y demostrativos, como los codigos hechos en Python por distintas comunidades de diversas areas cientificas desde estadistica a ciencias sociales.
[2]


3. Explique que es un linker en el contexto de un lenguaje de programacion compilado
¿Cual es su funcion principal y por que es esencial en el proceso de compilacion?

El linker es un programa encargado de combinar diferentes archivos con código objeto (objetos generados en los primeros pasos de la compilación) en un único archivo (el ejecutable). Esto por medio de eliminar los recursos que no necesita y enlazar el código objeto con sus bibliotecas. 

El linker entonces es esencial debido a que permite la conversión del código de un lenguaje de alto nivel a un ejecutable que entienda el dispositivo.


4. Describa las diferencias clave entre los tipos de datos derivados y primarios en C++.

Los primarios son los datos incorporados o predefinidos y pueden ser utilizados por el usuario directamente para declarar variables, por ejemplo: entero, personaje, booleano, punto flotante, entre otros. Los derivados se originan de datos primitivos y son de cuatro tipos: función, formación, puntero y referencia. [3]

5. Defina que significa inicializar y declarar una variable.

Para poder usar una variable en un programa, hay que definirla con un tipo y un identificador (nombre para la variable). En C y C++ todas las variables se deben declarar antes de su uso, si no, se producirá un error de compilación.

Declarar una variable significa indicarle a la computadora que existe. Dentro de una variable podemos luego guardar un valor.  Inicializar una variable significa declarar una variable y guardar información en ella.


6. ¿Que es la sobrecarga de funciones en C++ y cuales son sus beneficios?
La sobrecarga de funciones en C++ consiste en que se puedeespecificar más de una función con el mismo nombre en el mismo scope.
Entre sus beneficios estan promover la reutilización de nombres de función, mejora la legibilidad del codigo y evita el sobreuso de nombres de funciones.
[4]


7. ¿Que es un puntero y como se utiliza? Explique con un ejemplo de la vida real.

Un puntero es una variable que almacena la dirección de memoria de otra variable, se utilizan para acceder y manipular los datos mediante la direccion de memoria en vez del valor real de la variable. 
Un ejemplo de la vida real como analogica puede ser la cuenta en banco, donde el puntero seria el numero de cuenta de una persona.


8. ¿Una variable global almacena el valor original de una operacion en una funcion o una copia? Explique su respuesta. Explique por que se elige usar variables globales en lugar de locales en ciertos contextos.

Una variable global almacena el valor original en todo el programa. Cuando una función realiza una operación que afecta a una variable global, la variable global se modifica directamente; no se crea una copia de la variable. La variable global mantiene su valor original, y cualquier cambio realizado por la función se reflejará en ese valor original en todo el programa.

Las variables globales se eligen en ciertos contextos cuando se necesita que una variable mantenga su valor entre llamadas a funciones o cuando múltiples funciones deben acceder a la misma información compartida.


9. Investigue y explique tres metodos comunes de la biblioteca string en C++.

length(): El método length() se utiliza para obtener la longitud (cantidad de caracteres) de un string o cadena.

empty(): El método empty() se utiliza para validar si un string esta vacio o no.

atoi(): El método atoi() se utiliza convierte una cadena o string en una variable tipo int.


10. ¿Cual es la principal diferencia entre un bucle do-while y un bucle while?

La diferencia consiste en el cual momento se verifica la condicion, donde para un while la condicion se verifica antes de ejecturar el bloque de codigo del loop, mientras que para un do-while se verifica después de ejecutar el bloque de codigo.
[4]


11. ¿Es permitido almacenar funciones en una estructura en C++? En el caso de los datos,
¿se pueden encapsular en miembros privados y publicos dentro de una estructura?
Explique su respuesta.

No se puede almacenar funciones en una estructura. Pero se puede obtener un resultado similar usando punteros a funciones, donde se puede tener un puntero a función como miembro de una estructura y asignarle una función como valor. Esto te permite llamar a la función a través del puntero almacenado en la estructura.


12. Explique por que es util y comun dividir el codigo en archivos .hpp, .cpp y main.cpp
en C++. Describa el proposito especıfico de cada tipo de archivo.

Dividir el código es util y beneficioso ya que permite una compilación más eficiente, ya que si requiere hacer una modificación, al estar el código dividido, no es necesario recompilar la totalidad del código, sino solo una parte. 
Tambien, mejora la organización del código, lo cual facilita los procesos de búsqueda dentro del código. Ademas, otra utilidad es que permite dividir tareas entre distintas personas o equipos.
[5]


13. Defina que es el Type Casting en C++ y explique su utilidad. Proporcione ejemplos de situaciones en las que se emplea el Type Casting y como se realiza.

El type casting en C++ es el proceso de convertir un tipo de dato a otro. Puede ser implícito o explícito, y se utiliza para asegurar que el tipo de dato de una expresión sea compatible con el tipo de dato esperado en un contexto particular. Ejemplos en los que se utiliza el Type casting son el casting de punteros, para convertir un puntero de un tipo a otro, y casting de referencias,para convertir una referencia de un tipo a otro.


14. ¿Por que la sentencia goto no es recomendable en programacion moderna? Mencione ejemplos de como se pueden lograr los mismos resultados sin el uso de goto.

Debido a que la sentencia goto puede interferir con la secuencia normal del programa. Puede ser sustituida la necesidad de una sentencia goto por una sentencia break, una sentencia continue o una llamada a función puede eliminar 


15. ¿Donde y como se guardan las variables que se crean en C++? Explique la diferencia
entre el almacenamiento de variables locales y globales.

Las variables locales se almacenan en la pila (stack) de memoria. Tienen un tiempo de vida limitado y se destruyen automáticamente cuando la función en la que se declaran sale de su ámbito.

Por otro lado, las variables globales se almacenan en la sección de datos de memoria. Tienen un tiempo de vida que abarca toda la ejecución del programa y se inicializan antes de que se ejecute la función main(). Pueden ser accedidas desde cualquier parte del programa. Se crean al inicio del programa y se destruyen al final.


16. ¿Cual es la diferencia entre pasar parametros por valor, por referencia y por puntero?

En el paso por valor la función recibe una copia del valor del argumento. Es seguro y garantiza que la función no pueda modificar el valor original, pero puede ser ineficiente para grandes conjuntos de datos.
En el paso por referencia la función recibe una referencia al argumento original y en el paso por puntero la función recibe un puntero al argumento original. Estos son más eficientes, pero el programador debe tener cuidado para evitar efectos secundarios no deseados y cambios inesperados en los datos fuera de la función.
El paso por referencia tiene una sintaxis más limpia que el paso por puntero, pero el paso por puntero permite trabajar explícitamente con direcciones de memoria.


17. Cuando se usa un puntero para apuntar a un arreglo en C++, ¿a que valor o direccion apunta inicialmente? Describa como serıa la forma de acceder a todos los datos de ese arreglo mediante el puntero.

Cuando se usa un puntero para apuntar a un arreglo en C++, el puntero inicialmente apunta a la primera dirección de memoria del arreglo o a dirección de memoria del primer elemento del arreglo.
Para acceder a los datos del arreglo mediante el puntero, se puede utilizar la aritmética de punteros.



18. Explique para que son empleados los punteros dobles en C++. Proporcione ejemplos de situaciones en las que los punteros dobles son necesarios o beneficiosos.

Los punteros dobles en C++ se utilizan para apuntar a otros punteros. Son beneficiosos en situaciones donde necesitas manipular o acceder a punteros desde otros punteros. Por ejemplo, la asignación dinámica de memoria para matrices bidimensionales.



19. ¿Cual es la diferencia entre un break y un continue en los bucles de C++?

break: significa detener la ejecución de un loop y salirse de él. 
continue: sirve para detener o omitir la iteración actual y continuar con la siguiente iteración del loop.


20. ¿Para que se utiliza la directiva #ifndef?

La directiva #ifndef en C++ se utiliza para verificar si una macro (normalmente un identificador) no ha sido definida previamente en el código. Si el identificador especificado no está definido como una macro, las líneas de código inmediatamente después de la condición se ejecutan.


21. ¿Que es el puntero this en C++?

El puntero this en C++ es un puntero implícito que apunta al objeto actual dentro de una clase o método miembro de una clase.


22. ¿Que es un puntero nullptr?

La palabra clave nullptr representa un valor de puntero nulo. Se utiliza un valor de puntero nulo para indicar que un tipo de identificador de objeto no apunta a un objeto.



23. ¿Cual es la diferencia entre un arreglo y una lista en C++?

Los arreglos son estructuras de datos estáticas, hay que declarar su tamaño antes de utilizarlos. Mientras que las listas son estructuras de datos que pueden ir creciendo conforme se vaya requiriendo dinamicamente.


24. ¿Que es una funcion prototipo?

Una función prototipo es una declaración de una función, es una declaración previa de una función pero sin el cuerpo, que proporciona información sobre la existencia de la función antes de que se defina o se utilice en el programa principal.


25. ¿Investigue que es un memory leak?

Un memory leak o fuga de memoria consiste en un problema en programación en el que una aplicación utiliza memoria dinámica pero no la libera adecuadamente cuando ya no la necesita, lo que provoca que la memoria asignada sea inaccesible y no se pueda utilizar. 




## Parte Teórica Automatización 




1. ¿Que suelen contener las variables CC, CFLAGS, CXXFLAGS y LDFLAGS en un makefile?

CC: es la variable que especifica cual compilador se va a utilizar.
CFLAGS: es la variable que especifica las banderas o opciones que se pasaran al compilador a la hora de compilar los archivos del codigo.
CXXFLAGS: es una variable similar CFLAGS pero para el compilador de C++.
LDFLAGS: es la variable que contiene las opciones que se le van a pasar el linker.

2. ¿De que se compone una regla en un Makefile?

Se compone de un Target, Prerequisitos y Comandos.

3. Defina que es un target y como se relaciona con sus prerequisitos.
Un target es el nombre de un archivo que se generara usando el programa make, i.e. el programa ejecutable. Se relaciona con los prerequisitos de la forma en que los prerequisitos son los archivos necesarios para que se puede construir un target.

4. ¿Para que se utiliza la bandera -I, -c y -o del compilador gcc?

-l: Se usa para indicarle al compilador que se agregue el directorio especificado a la lista de directorios.
-c: Se usa para indicarle al compilador que compile los archivos fuente en un ejectuable pero sin enlazar estos archivos.
-o: Se usa para especificarle al compilador el nombre del archivo de salida despues de compilar.

5. ¿Como se definen y se utilizan las variables en un Makefile? ¿Que utilidad tienen?

Una variable se define asi:

```nombre_variable= lista palabras a las cual la variable sustituye```

Se utiliza asi:
``` $(nombre_variable)```

Entre sus utilidades estan que facilitan la escritura  evitan la repeticion de escribir listas de palabras multiples veces.


6. ¿Que utilidad tiene un @ en un Makefile?

El simbolo de arroba @ tiene la utilidad de que permite suprimir la impresion del comando que se esta usando en la terminal.

7. ¿Para que se utiliza .PHONY en un Makefile?
Se utiliza para especificar los objetivos que no son archivos, pueden ser comandos como por ejemplo: clean y all.


### Referencias

[1] https://cipsa.net/diferencia-c-cplus-introduccion-funciones/ 
[2] https://www.unir.net/ingenieria/revista/lenguajes-programacion-interpretados/
[3] https://barcelonageeks.com/tipos-de-datos-c/ 
[4] Material del curso en MV.
[5] https://www.genbeta.com/desarrollo/estructura-del-codigo-fuente-en-c 




```

En palabras del profeta Borgues: "Qué parida!"

```