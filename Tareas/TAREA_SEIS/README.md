# Tarea 6
Repositorio para la Tarea 6 del curso de Estructuras Abstractas de Datos y Algoritmos.


## Para correr el programa

Para correr el programa desde la terminal de VSCode u otra, primero tiene que verificar que tenga instalado el Python 3.9 en su dispositivo o alguna version posterior, para ello corra en la terminal:

```bash
python --version
```
De no aparacer un mensaje en terminal indicando la version instalada junto con otra info en un cajetin, proceda a instalarlo segun su OS, recuerde GIYF.

Ademas asegurarse de terner instalado las lib de Pandas, MatPlotLib, Numpy, etc. Para esta particularmente asegurarse de instalar la lib Kaggle para el poder descargar los datos apropiadamente, usar el comando

```bash
pip install kaggle
```

Una vez instalado, ir al dir `.kaggle` dentro de su carpeta de usuario en WN, y dentro de ese carpeta pegar el archivo `kaggle.json` que contiene el API Token generado para cada usuario en la plataforma de Kaggle, en cado de necesitar ayuda se puede consultar este tutorial [tutorial](https://www.youtube.com/watch?v=92q7msmbxO0/) o GIYF.


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

### Regresion

1.	¿Que es la regresion lineal y como se diferencia de la regresion no lineal?

La regresión lineal es un método estadístico que modela la relación entre una variable dependiente y una o más variables independientes asumiendo una relación lineal. Se diferencia de la regresión no lineal en que esta última modela la relación con ecuaciones que no son líneas rectas (o planos), permitiendo capturar relaciones más complejas entre las variables.


2. ¿Que son los coeficientes de regresion y que informacion proporcionan sobre la relacion entre las variables?

Los coeficientes de regresión son valores que multiplican a las variables independientes en la ecuación de regresión. Proporcionan información sobre la dirección (pendiente) de la relación entre cada variable independiente y la variable dependiente. Un coeficiente positivo indica una relación directa, mientras que un coeficiente negativo indica una relación inversa.


3. Que  es  el  error  cuadratico  medio  (MSE)  y  como  se  utiliza  para  evaluar  la  precision de un modelo de regresion?

El error cuadrático medio (MSE) es una medida que calcula el promedio de los cuadrados de los errores entre los valores reales o obsersavors y los predichos por el modelo. Se utiliza para evaluar la precisión de un modelo de regresión; valores más bajos de MSE indican un mejor ajuste del modelo a los datos.


4. Cual  es  la  diferencia  entre  regresion  simple  y  regresion  multiple  y  cuando  se  utiliza cada una?

La regresión simple modela la relación entre una variable dependiente y una sola variable independiente. La regresión múltiple, por otro lado, utiliza dos o más variables independientes para predecir la variable dependiente. Se utiliza regresión simple cuando se quiere entender la relación entre dos variables, y regresión múltiple cuando se quiere predecir una variable basándose en múltiples factores o causas.


### Clustering

1. Que es el clustering y cual es su objetivo principal en el analisis de datos? 

El clustering es una técnica de aprendizaje automático no supervisado que agrupa datos en clusters o cúmulos basándose en su similitud. Su objetivo principal es identificar patrones en un conjunto de datos, agrupando objetos similares juntos.


2. Describa brevemente los algoritmos K-Means y DBSCAN y como funcionan. 

K-Means es un algoritmo de clustering que divide un conjunto de datos en K clusters, asignando cada punto al centroide más cercano y ajustando los centroides hasta que la asignación no cambie. 
Mientras que DBSCAN agrupa puntos que están densamente agrupados y marca como outliers (valores atípicos) los puntos en regiones de baja densidad. Funciona expandiendo clusters a partir de puntos centrales basándose en la densidad.


3. Que es la inercia en el contexto del clustering y como se utiliza para evaluar la calidad de un agrupamiento?

La inercia es una medida que cuantifica la suma de las distancias al cuadrado de cada objeto del cluster a su centroide. Se utiliza para evaluar la calidad de un cluster; valores más bajos de inercia indican clusters más cohesivos y mejor definidos.


4. Que son los centroides y como se utilizan en el algoritmo K-Means?

Los centroides son los puntos centrales de cada cluster en el algoritmo K-Means. Representan el promedio de todos los puntos asignados a ese cluster. Se utilizan para determinar la pertenencia de los puntos a los clusters y se ajustan iterativamente hasta que la asignación de puntos a clusters ya no cambia significativamente.


5. Escriba la diferencia entre datos estructurados y no estructurados para an´alisis de datos

Los datos estructurados están organizados en un formato definido, como tablas con columnas y filas, lo que facilita su almacenamiento, consulta y análisis. Los datos no estructurados, como textos e imágenes, no tienen un formato predefinido, lo que hace más complejo su procesamiento y análisis.



### Paquetes en Python (__init__.py):
 
1. Que es un paquete en Python y como se diferencia de un modulo?

Un paquete en Python es una forma de organizar módulos (archivos Python) en directorios, permitiendo estructurar mejor el código. Un módulo es un solo archivo Python, mientras que un paquete es una colección de módulos en un directorio que contiene un archivo `__init__.py`.


2. Cual es la funcion del archivo `__init__.py` dentro de un paquete de Python?

El archivo `__init__.py` indica a Python que el directorio debe ser tratado como un paquete. Puede estar vacío o contener código de inicialización para el paquete, como importaciones.


3. Como se importa un modulo o funcion desde un paquete en Python?

Se utiliza la sintaxis `from paquete import modulo` o `from paquete.modulo import funcion` para importar módulos o funciones específicas desde un paquete.


4. Que es la variable `__all__` en el archivo `__init__.py` y cual es su proposito?

La variable `__all__` define una lista de nombres de módulos o atributos que serán importados cuando se use `from paquete import *`. Su propósito es limitar lo que se importa para evitar incluir módulos o atributos no deseados.


5. Cual es la ventaja de organizar el codigo en paquetes y modulos en Python?

 La organización del código en paquetes y módulos mejora la modularidad, reusabilidad y mantenibilidad del código. Además, facilita la organización lógica del código y ayuda en la colaboración y distribución de y en proyectos más grandes.


### Python HTTP y Servicios Web (API)

1. Que es una API y cual es su funcion en el contexto de los servicios web?

Una API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y especificaciones que permite a diferentes aplicaciones comunicarse entre sí. En el contexto de los servicios web, facilita la interacción entre diferentes sistemas y plataformas a través de la web, permitiendo el acceso y manipulación de datos de manera estandarizada.


2. Cual es la diferencia entre una API RESTful y una API SOAP?

Una API RESTful es una API que sigue los principios de la arquitectura REST ( Representational State Transfer), utilizando HTTP para las operaciones sobre los recursos. Es simple y utiliza formatos como JSON o XML. 
SOAP (Protocolo Simple de Acceso a Objetos) es un protocolo más estricto y complejo que utiliza XML para el intercambio de mensajes, ofreciendo más características como seguridad y transacciones.


3. Describa los pasos basicos para consumir una API utilizando Python.

Para consumir una API con Python, generalmente se siguen estos pasos: 
     a. Importar un módulo para realizar solicitudes HTTP, como `requests`.
     b. Definir la URL de la API y los parámetros necesarios para la solicitud.
     c. Realizar la solicitud a la API (GET, POST, etc.) y capturar la respuesta.
     d. Procesar la respuesta, que suele estar en formato JSON o XML.
     e. Utilizar los datos obtenidos en la aplicación.


4. Que es la autenticacion de API y por que es importante?

La autenticación de API es el proceso de verificar la identidad de una solicitud a una API, asegurando que solo los usuarios o aplicaciones autorizados puedan acceder a ella. Es importante para la seguridad, controlando el acceso a recursos sensibles y previniendo el uso no autorizado.


5. Cual es el papel de los verbos HTTP (GET, POST, PUT, DELETE) en las solicitudes a una API y HTTP?

Los verbos HTTP definen la acción que se desea realizar sobre los recursos en una API, permiten una interacción clara y estandarizada con la API.
GET se usa para solicitar datos, POST para enviar datos y crear recursos, PUT para actualizar recursos existentes, y DELETE para eliminar recursos.
