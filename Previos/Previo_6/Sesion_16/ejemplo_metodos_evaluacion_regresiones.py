import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt

# Generar datos de ejemplo para la regresion
# Usando la func random con una semilla de 42
np.random.seed(42)
# Donde se crean datos aleatorios para X & y como una func lineal de X con ruido 
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Dividir los datos en conjunto de entrenamiento y prueba
# Esto permite evaluar el modelo en datos que no ha visto antes
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y ajustar el modelo de regresion lineal
# Este es el proceso de "aprendizaje" o learning del modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
# Utilizar el modelo entrenado para predecir respuestas al conjunto de datos de prueba
y_pred = modelo.predict(X_test)

# Calcular metricas de evaluacion
# Estas metricas ayudan a entender que tan bien se desempenno el modelo
mae = mean_absolute_error(y_test, y_pred)       # Error absoluto medio
mse = mean_squared_error(y_test, y_pred)        # Error cuadratico medio
rmse = sqrt(mse)                                # Raiz del error cuadratico medio
rae = np.sum(np.abs(y_test - y_pred))  / np.sum(np.abs((y_test - np.mean(y_test))))     # Error absoluto relativo
rse = np.sum(((y_test - y_pred)**2)) / np.sum((y_test - np.mean(y_test))**2)            # # Error cuadratico relativo

# Imprimir las metricas
# Estos son valores que nos dan una medida del error de nuestras predicciones
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"RAE: {rae:.2%}")
print(f"RSE: {rse:.2%}")

# Crear grafica para visualizar los datos de prueba y las predicciones
plt.scatter(X_test, y_test, label='Datos de prueba', color='blue')
plt.plot(X_test, y_pred, label='Predicciones', color='red')
plt.title('Regresion Lineal y Errores')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

# Mostrar errores en la grafica
# Estos segmentos  ayudan a visualizar el error
for i in range(len(X_test)):
    plt.plot([X_test[i], X_test[i]], 
             [y_test[i], y_pred[i]], 
             linestyle='--', color='gray')

# Mostrar la figura con las subtramas
plt.show()  
