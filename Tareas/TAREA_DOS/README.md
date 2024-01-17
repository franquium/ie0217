# Tarea 2
Repositorio para la Tarea 2 del curso de Estructuras Abstractas de Datos y Algoritmos.


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


## Parte Teórica 

1. Conceptos Fundamentales: Deﬁne qué es la programación orientada a objetos y explica sus principios fundamentales.

Es un paradigma de programación en el que el código se organiza en “objetos”, es decir, de instancias de clases, que se relacionan entre sí para formar sistemas complejos. En la OOP se lleva a cabo la encapsulación de datos para ocultar los detalles de implementación de los objetos y facilitar el uso del código.
Entre las principales características están la facilidad para hacer cambios en el código, debido a que no se requiere modificar todo el sistema. En este mismo sentido, la OOP facilita los procesos de mantenimiento y de reutilizar códigos existentes. Además, al haber una independencia entre objetos se aumenta la seguridad del programa. 


2. Herencia: Explica el concepto de herencia en programación orientada a objetos y proporciona un ejemplo práctico.

En OOP, la herencia consiste en crear una nueva clase a partir de otra ya existente, donde la nueva posee características de la clase original. Esto trae beneficios en la reutilización del código. 



3. Encapsulamiento: ¿Qué es el encapsulamiento en OOP y por qué es importante?
Proporciona ejemplos de como se implementa en C++.

El encapsulamiento permite ocultar los detalles de implementación de los objetos, de modo que se exponga únicamente la interfaz para interactuar con él. Esto es de importancia para facilitar el uso del código y aumentar la seguridad.


4. Polimorﬁsmo: Describe el polimorﬁsmo y proporciona ejemplos de polimorﬁsmo de tipo y polimorﬁsmo de operador en C++.

El polimorfismo consiste en que objetos de distintas clases respondan a una misma interfaz de manera distinta. Es la capacidad de llamar a funciones distintas con un mismo nombre. Estas funciones pueden actuar sobre objetos distintos dentro de una jerarquía de clases, sin tener que especificar el tipo exacto de los objetos.
En C++ existen el polimorfismo de tipo y el de operador. En el primero, los objetos de distintas clases son tratados de manera uniforme ya que pertenecen a una misma jerarquía de clases. En el de operador, el operador actúa de manera diferente según el tipo de dato que manipula. Por ejemplo, el operador de suma 

 
5. Abstraccion: ¿Cómo se relaciona la abstracción con la programación orientada a objetos? Proporciona ejemplos de cómo aplicar la abstraccion en un contexto de programación.

En la OOP es posible crear abstracciones con las cuales se simplifican modelos de la realidad considerando los aspectos relevantes para el problema. 

 
6. Clases y Objetos: Diferencia entre una clase y un objeto en programacion orientada a objetos. Proporciona un ejemplo de cada uno.

La clase consiste en una especie de plantilla o molde en la que se definen los atributos y métodos de un tipo de objeto. Las clases se construyen para crear objetos. Por otro lado, un objeto es una instancia de una clase. Un objeto posee propiedades (datos) y funcionalidades (métodos).

 
7. Metodos Virtuales: Explica la importancia de los metodos virtuales en C++ y como se utilizan en la implementacion de polimorﬁsmo.

Los métodos virtuales con necesarios para implementar el polimorfismo. Como los métodos pueden producir cambios en las propiedades del objeto y también generar eventos con nuevos mensajes para otros objetos del sistema, entonces son fundamentales para la sustitución dinámica, para generar el polimorfismo de tipo y la creación de jerarquías de clases.  
Para implementar el polimorfismo primero se debe declarar métodos virtuales en la clase base. Posteriormente, se debe sobreescribir los métodos virtuales en clases derivadas y finalmente usar punteros o referencias.


 
8. Constructores y Destructores: ¿Cual es el proposito de un constructor y un destructor en una clase? Proporciona ejemplos de su uso.

Los constructores son funciones de miembros de las clases que construyen objetos de tal clase, esto asignando memoria o la inicialización de objetos. 
Los destructores son las funciones que destruyen objetos de una clase por medio de limpieza o desasignación de memoria para objetos.


 
9. Sobrecarga de Operadores: Explica que es la sobrecarga de operadores y proporciona un ejemplo de como se implementa en C++.

Es una característica que hace posible a los desarrolladores definir el comportamiento de los operadores del lenguaje para trabajar con objetos de una clase personalizada. Es decir, los resultados de operaciones con operadores como +, -, entre otros, son establecidos por el programador

 
10. Templates: Describe el concepto de templates en C++. ¿En qu´e situaciones serıa util utilizar templates?

Son unas construcciones que genera código genérico que pueden trabajar con diferentes tipos de datos y estructuras de estos. Es decir, las templates permite escribir funciones y clases para ser usadas con distintos tipos de datos sin necesidad de escribir código específico para cada uno de esos tipos. Lo cual es muy útil en situaciones que se requiera reutilizar código, también para crear estructuras de datos en las que se puedan almacenar elementos de cualquier tipo, 
Las plantillas permiten definir operaciones de una clase o una función y especificar en qué tipos deben funcionar esas operaciones. Esto puede ser útil en la implementación de funciones y clases que operen con matrices y vectores de variados tipos.


 
11. ¿Que es la memoria dinamica en C++ y cuando se utiliza comunmente?

Es la memoria que se reserva durante el tiempo de ejecución. Generalmente es usada para almacenar grandes volúmenes de datos, cuya cantidad exacta se desconoce al implementar el programa. Para usar la memoria dinámica se usan punteros.

 
12. Explique la diferencia entre new y malloc en C++. ¿Cuando deberıa utilizar uno sobre el otro?

El operador new asigna memoria a una variable en heap y devuelve un puntero al tipo de dato solicitado. Al reservar memoria con new hay que liberarla con delete cuando ya no se requiere usarla más. Por otro lado, malloc también se utiliza para asignar un bloque de memoria en el heap pero es una función, no un operador. Al usar malloc se devuelve un puntero void* al inicio de la memoria asignada y este debe convertirlo al tipo de dato que necesite. Para liberar memoria en este caso se usa free. Esto ayuda a evitar las fugas de memoria.

 
13. ¿Que es una fuga de memoria (memory leak) y como puede evitarse en programas en C++?

Una fuga de memoria es un error de software que ocurre cuando un bloque de memoria reservada no es liberado en un programa de computación. Generalmente ocurre porque se pierden todas las referencias a esa área de memoria antes de liberarse.

 
14. Explique el concepto de punteros inteligentes (smart pointers) y proporcione ejemplos de su uso.

Los punteros inteligentes son objetos en C++ que actúan como punteros, pero proporcionan una gestión automática de la memoria. Esto significa que el puntero inteligente es responsable de eliminar la memoria que el puntero sin formato especifica. De esta forma, se utilizan para asegurarse de que los programas están libres de memoria y de pérdidas de recursos.
Por ejemplo, algunos punteros inteligentes de la biblioteca estándar de C++ tienen una función miembro de restablecimiento que libera la propiedad del puntero. Esto es útil cuando se quiere liberar la memoria que es propiedad del puntero inteligente antes de que el puntero inteligente salga del ámbito
 
15. ¿Cual es la diferencia entre deletey delete[] en C++? ¿En qu´e contexto se utilizarıa cada uno?

En el caso de delete (para objetos individuales): Se utiliza para liberar la memoria asignada a un solo objeto utilizando. Asimismo, se utiliza con un puntero a un solo objeto creado con new.
Por otro lado, delete[] (para arreglos): Se utiliza para liberar la memoria asignada a un arreglo de objetos utilizando new[]. Se utiliza con un puntero a un arreglo de objetos creado con new[].


 
16. ¿Que es un algoritmo de ordenamiento y por que son importantes en programacion?

Los algoritmos de clasificación se usan para organizar los elementos de un arreglo o lista en un orden específico. Son fundamentales en programación porque tienen que ver con la eficiencia de una vasta cantidad de operaciones de manipulación y procesamiento de datos. 
 

 17. Explique el funcionamiento del algoritmo de ordenamiento "Bubble Sort". ¿Cual es su complejidad temporal en el peor caso?

Este algoritmo de ordenamiento simple recorre el arreglo varias veces comparando elementos adyacentes, si estos están en orden incorrecto, el algoritmo los intercambia. Este proceso continúa hasta que no se realicen más intercambios. 
Su complejidad es O(n^2) en el peor de los casos.

 
18. Describa el algoritmo de ordenamiento "QuickSort". ¿Cual es su ventaja principal sobre otros algoritmos de ordenamiento?

Es un método de ordenamiento cuyo algoritmo consiste en elegir un elemento pivote del arreglo y dividir el arreglo alrededor de ese elemento. Los elementos menores a este se colocan a su izquierda, y todos los elementos mayores se colocan a su derecha. Luego, el proceso se repite recursivamente para los sub-arreglos antes y después del pivote hasta que todo el arreglo esté ordenado.
QuickSort tiene la gran ventaja de ser más rápido que otros algoritmos de ordenamiento y su complejidad temporal promedio es O(n log n).


 
19. ¿Cual es la diferencia entre un algoritmo de ordenamiento estable y uno inestable?
Proporcione ejemplos de cada uno.

Un algoritmo de ordenamiento estable conserva el orden relativo original de elementos con claves iguales, mientras que un algoritmo inestable no garantiza tal preservación. Las claves son los valores que determinan el orden.
Un ejemplo de algoritmo estable es Bubble Sort, pues mantiene el orden relativo de elementos con la misma clave. Al contrario, el algoritmo Selection Sort es un ejemplo de inestable, no garantiza que el orden relativo original de elementos con la misma clave se conserve después del nuevo ordenamiento.

 
20. Hable sobre el algoritmo de ordenamiento "Merge Sort". ¿Cual es su complejidad temporal y en que situaciones es preferible su uso?

Este algoritmo de ordenamiento estable consiste en dividir un arreglo en partes iguales, hasta que cada arreglo tenga solo un elemento. Seguidamente ordena por separado cada una de las partes y después mezcla ambas partes manteniendo el ordenamiento. 
Su complejidad temporal es O(n log n). Se utiliza preferiblemente en listas enlazadas.

 