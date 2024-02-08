import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generar datos de ejemplo 
# Usando la func random con una semilla de 42
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # 100 puntos aleatorios para la variable independiente
y = 4 + 3 * X + np.random.randn(100, 1)  # Respuesta lineal con ruido añadido

# Crear un modelo de la regresion lineal e inicializandolo
modelo = LinearRegression()

# Ajustar el modelo a los datos generados
modelo.fit(X, y)

# Imprimir el coeficiente y intercepcion
# donde el coeficiente es la pendiente de la linea 
# y la intercepcion es el corte en  eje y
print("Coeficiente:", modelo.coef_[0][0])
print("Intercepcion:", modelo.intercept_[0])

# Visualizar la regres lin de los datos
# junto la linea de regresion ajustada
plt.scatter(X, y)                                         # Graficar los datos como puntos
plt.plot(X, modelo.predict(X), color='red', linewidth=3)  # Graficar la linea de regresion
plt.title('Regresion Lineal')                             # Titulo de la img
plt.xlabel('X')                                           # Etiqueta del eje X
plt.ylabel('y')                                           # Etiqueta del eje Y

# Mostrar el grafico
plt.show()  