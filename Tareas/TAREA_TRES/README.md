# Tarea 2
Repositorio para la Tarea 3 del curso de Estructuras Abstractas de Datos y Algoritmos.


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

Su programa deberia correr satisfactoriamente. 


## Parte Teórica 

1. Definicion  de  Templates:  Explique  el  concepto  de  templates  en  C++  y proporcione un ejemplo simple

En C++ los templates son una característica con la cual es posible escribir código genérico con diferentes tipos de datos y estructuras de datos. Un template es usado por el compilador para crear una clase o función específica basada en el tipo de datos que se le pasa como parámetros. Tales parámetros definen los tipos de argumentos y variables dentro de la función o clase template.
El uso de templates permite crear funciones o clases que pueden trabajar con cualquier tipo de dato, esto es de importancia para la reutilización del código y reducción de la duplicación.

``` 
template <typename T>
T add(T n1, T n2) {
    return (return n1 + n2);
}

// Uso del template
int main() {
    int resultadoInt;
    double resultadoDouble;
    resultadoInt = add<int>(1, 1);
    resultadoDouble = add<double>(1.2, 1.3)
    return 0;
}
```



2. Sobrecarga de Plantillas: ¿Como se realiza la sobrecarga de funciones con plantillas en C++?.

La sobrecarga de plantillas es la capacidad de tener varias funciones con el mismo nombre pero con diferentes implementaciones de template. Esto con el objetivo de que las funciones manejen diferentes tipos de datos o diferentes números de parámetros. En el código siguiente se muestra un ejemplo de cómo es utilizado en C++.



3. Plantillas  de  Clases: Explique como se pueden utilizar plantillas en la definicion de clases en C++.

Las plantillas de clases en C++ son usadas para crear una única clase y trabajar con diferentes tipos de datos. Esto se consigue porque permiten definir una estructura de clase con la cual se puede operar cualquier tipo de dato.


4. Manejo  de  Excepciones:  Describa  los  bloques  try,  catch y  throw y  como se utilizan para el manejo de excepciones en C++.

En el manejo de excepciones en C++ se utilizan tres bloques: try,  catch y throw. Seguidamente se describe cada uno:
•	try: Con este bloque se encierra uno o más comandos que pueden generar una excepción.
•	catch: Un bloque catch puede manejar una excepción que es lanzada por un throw. Puede haber múltiples bloques catch para manejar diferentes tipos de excepciones.
•	throw: Se utiliza para lanzar una excepción cuando se detecta un error. Puede arrojar una excepción ya existente o una nueva.

 
5. Excepciones  Estandar: Nombre al menos tres excepciones estandar proporcionadas  por  C++  y  proporciona  ejemplos  de  situaciones  en  las  que  podrıan  ser utiles.

Varias clases de excepciones estándar que se pueden usar en C++ para representar diferentes tipos de errores son:
•	std::runtime_error: para representar errores que ocurren durante la ejecución.
•	std::invalid_argument: cuando se pasan argumentos inválidos a una función.
•	std::out_of_range: para indicar que un acceso a un elemento está fuera del rango válido.

A continuación, los ejemplos de uso útiles de cada uno:
•	std::runtime_error: en situaciones que una función no puede completar su tarea a causa de circunstancias imprevistas en tiempo de ejecución.
•	std::invalid_argument: esta excepción es utilizada al validar la entrada de una función pero los argumentos dados no cumplen los criterios esperados.
•	std::out_of_range: es usada en clases que manejan colecciones o arrays para intentar acceder a un índice que está fuera de los límites de la colección.


 
6. Polıtica  de  Manejo  de  Excepciones:  ¿Que  es  una  polıtica  de  manejo  de excepciones y por que es importante considerarla al diseñar software?

Es un conjunto de directrices y prácticas que un equipo de desarrollo de programas adopta para manejar errores y condiciones excepcionales en ellos. Considerar y seguir una política de manejo de excepciones es de gran importancia pues se mantiene un enfoque consistente y predecible en el manejo de los errores en todo el código. Por otro lado, se previenen fallos por comportamientos imprevistos debido a errores no manejados. Otra razón es que se facilita la comprensión y mantenimiento del código. Además, se evita que el software se detenga abruptamente, gracias a que se aumenta su robustez.

 
7. Noexcept: Explica el propo´sito de la palabra clave noexcept y c´omo se utiliza en C++

La palabra clave noexcept en C++ especifica que una función no lanzará excepciones. Se usa con el propósito de que aclarar esta situación a otros desarroladores, lo cual promueve la claridad. También para permitir al compilador realizar optimizaciones, pues la función no necesita código para manejar excepciones. Asimismo, al usarla con move semantics asegura que operaciones como el movimiento de objetos no generen excepciones y sean seguras.

 
8. Contenedores STL: Nombre cinco contenedores diferentes de la STL y explique brevemente en que situaciones serıa apropiado usar cada uno.

Cinco contenedores diferentes de la Standard Template Library (STL) y sus usos apropiados son:
•	std::vector: cuando se necesita acceso aleatorio a elementos, ya que se usa para listas de elementos que cambian de tamaño
•	std::list: útil para inserciones y eliminaciones frecuentes, pues consiste en lista doblemente enlazada
•	std::map: es una estructura de tipo diccionario basada en árboles, se usa para almacenar pares clave-valor con acceso rápido por clave.
•	std::set: para una colección de elementos únicos ordenados. Es útil para operaciones de conjunto como unión e intersección.
•	std::queue: apropiado para tareas de planificación y buffering, pues es una cola de tipo FIFO (First In, First Out).



 
9. Iteradores  en  STL: Explique el concepto de iteradores en la STL y como se utilizan para acceder a elementos en contenedores.

Los iteradores en la STL son objetos similares a punteros, con los cuales se recorren los elementos de un contenedor. Es decir, representa la posición de un elemento en un contenedor y se usa para iterar sobre tales elementos dentro del contenedor.
Para utilizarlos con un vector, por ejemplo uno llamado nums, se usan las siguientes funciones miembro:
•	nums.begin() para apuntar al primer elemento del vector
•	nums.begin()+i para apuntar al elemento en el índice i
•	nums. end () para apuntar al un elemento mas allá del elemento final del vector


 
10. Algoritmos STL: Proporcione ejemplos de al menos tres algoritmos de la STL y describa sus funciones basicas

Tres algoritmos de la STL y sus funciones básicas son:
•	sort: ordena ascendentemente los elementos en un rango. 
•	find: busca un elemento en un rango, devuelve un iterador al elemento.
•	accumulate: su función es acumular la suma de un rango de elementos. 
•	set_union: este algoritmo calcula la unión de dos conjuntos.



 
11. Algoritmos  Personalizados: ¿Como podrıa utilizar un algoritmo personalizado con la STL?

Los algoritmos personalizados en STL son funciones genéricas usadas para trabajar con contenedores. Por lo general son creadas para realizar operaciones específicas que no están cubiertas por los algoritmos estándar. Por ejemplo, un algoritmo personalizado para filtrar elementos de un contenedor basado en un criterio específico y devolver un nuevo contenedor con los resultados.

 
12. Definicion  de  Expresiones  Regulares:  Defina  que  son  las  expresiones regulares y proporcione un ejemplo simple.

Las expresiones regulares, regex o regexp, son patrones para buscar y manipular cadenas de texto fácilmente. En C++, las expresiones regulares se pueden utilizar con la biblioteca <regex>. Un ejemplo se muestra seguidamente.

``` 
#include <regex>
#include <iostream>

int main() {
    std::regex pattern("^[a-zA-Z0-9]+$"); // Patron para alfanuméricos
    std::cout << std::regex_match("Hello123", pattern); // Devuelve true
}
```

 
13. Caracteres Especiales: Enumere al menos tres caracteres especiales comunmente utilizados en expresiones regulares y describa sus funciones.

A continuación, se despliega una lista de caracteres especiales usados en expresiones regulares:
•	.: el punto coincide con cualquier caracter, excepto un salto de linea.
•	|: se usa para indicar que hay alternancias.
•	*: el asterisco representa cero o más repeticiones del elemento anterior.
•	+: este carácter representa una o más repeticiones del elemento anterior.
•	?: este sirve para indicar que el elemento anterior es opcional. 


 
14. Uso de Expresiones Regulares en C++: ¿Como se utilizan las expresiones regulares en C++? Proporciona un ejemplo.

En C++, para usar las expresiones regulares se debe utilizar la biblioteca <regex>. Esta biblioteca proporciona clases y funciones para trabajar con tales expresiones. 

``` 
#include <regex>
#include <iostream>

int main() {
    std::regex pattern("^[a-zA-Z0-9]+$"); // Patron para alfanuméricos
    std::cout << std::regex_match("Hello123", pattern); // Devuelve true
}
```

 
15. Validacion de Patrones: ¿Por que las expresiones regulares son utiles para la validacion de patrones en cadenas de texto?

Las expresiones regulares son útiles para la validación de patrones en cadenas de texto porque se pueden definir patrones complejos y flexibles para coincidir con formatos específicos. Como por ejemplo, direcciones de correo electrónico, números de teléfono, entre otros.
Por otra parte, las expresiones regulares dan una forma concisa y eficiente de validar cadenas de texto contra estos patrones. Esto a debido a que son soportadas y utilizadas en muchas áreas de la programación.



 

 