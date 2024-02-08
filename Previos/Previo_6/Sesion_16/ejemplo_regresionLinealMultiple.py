import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generamos datos de ejemplo 
# Para regresion con 3 caracteristicas y error o ruido
X, y = make_regression(n_samples=100, n_features=3, noise=20, random_state=42)

# Creamos un DataFrame para una mejor claridad visual de los datos
df = pd.DataFrame(X, columns=['Tamano', 'Habitaciones', 'Distancia Ciudad'])
df['Precio'] = y

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    df[['Tamano', 'Habitaciones', 'Distancia Ciudad']],
    df['Precio'], test_size=0.2, random_state=42)

# Creamos y ajustamos un modelo de regresion lineal multiple
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Coeficientes e intercepción del modelo
# Imprimiendolos
# Los coeficientes representan como afecta cada caracteristica en la prediccion del precio
print("Coeficientes:", modelo.coef_)
print("Intercepcion:", modelo.intercept_)

# Realizar predicciones en el Cjto de Prueba
y_pred = modelo.predict(X_test)

# Parte de Graficacion

# Visualizar la regresion lineal multiple
fig = plt.figure(figsize=(12, 6))

# Graf. 1 - Tamanno vs. Precio
ax1 = fig.add_subplot(131, projection='3d')  # Crear una subtrama 3D 
ax1.scatter(
    X_test['Tamano'], X_test['Habitaciones'],
    y_test, c='blue', marker='o', alpha=0.5
)
ax1.set_xlabel('Tamano')
ax1.set_ylabel('Habitaciones')
ax1.set_zlabel('Precio Verdadero')
ax1.set_title('Precio Verdadero vs. Tamano y Habitaciones')

# Graf 2 - Tamano vs. Precio Predicho
ax2 = fig.add_subplot(132, projection='3d')  # Crear una subtrama 3D 
ax2.scatter(
    X_test['Tamano'], X_test['Habitaciones'],
    y_pred, c='red', marker='o', alpha=0.5
)
ax2.set_xlabel('Tamano')
ax2.set_ylabel('Habitaciones')
ax2.set_zlabel('Precio Predicho')
ax2.set_title('Precio Predicho vs. Tamano y Habitaciones')

# Grf 3 - Comparacion de Precio Verdadero y Precio Predicho
ax3 = fig.add_subplot(133)  # Crear una subtrama 2D 
ax3.scatter(y_test, y_pred, c='green', alpha=0.5)
ax3.plot(
    [min(y_test), max(y_test)], [min(y_test), max(y_test)],
    linestyle='--', color='red', linewidth=2
)
ax3.set_xlabel('Precio Verdadero')
ax3.set_ylabel('Precio Predicho')
ax3.set_title('Comparacion de Precio Verdadero y Precio Predicho')

# Ajustar el layout para que no haya superposicion de subgraficas
plt.tight_layout()
# Mostrar todas las subgraficas
plt.show()
