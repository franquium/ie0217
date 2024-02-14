import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
# from math import sqrt

def calcular_RegresionLineal():
    pass
    

# --- Fin funcion ---- #

def calcular_RegresionNoLineal():
    pass
    

# --- Fin funcion ---- #

# Crear DataFrame de pandas con los datos CSV
data = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
print("Datos cargados exitosamente.\n")

# #############
# Analisis 1 Relacion del precio con respecto a los annos
# #############

# Extraer datos de la categoria: Variable independiente
X_simple = data['year'].values.reshape(-1, 1)

# Extraer datos de la categoria: Variable dependiente
y_simple = data['selling_price'].values

# Se entrenan el modelo, con 20% datos para la prueba, un seed de 42
X_train, X_test, y_train, y_test = train_test_split(X_simple, y_simple, test_size=0.2, random_state=42)

# Crea y ajusta objeto del tipo de modelo RL
model_simple = LinearRegression()
model_simple.fit(X_train, y_train)

# Hacen predicciones del modelo
y_pred_simple = model_simple.predict(X_test)

# Estas metricas ayudan a entender que tan bien se desempenno el modelo
# Se obtiene el MSE con simple de la prediccion con respecto a los datos de prueba
mse_simple = mean_squared_error(y_test, y_pred_simple)
print(f"Error cuadrático medio (MSE) en regresión lineal simple: {mse_simple:.2f}")

# Error absoluto medio
mae_simple = mean_absolute_error(y_test, y_pred_simple)       
print(f"MAE: {mae_simple:.2f}")

# Calcular el coeficiente de determinacion R^2
""" 
@note El coeficiente de determinacion R2 es una medida estadistica que 
      proporciona una indicación de la proporción de la variabilidad en la 
      variable de respuesta que es explicada por el modelo de regresión
      R2 = 0: El modelo no explica ninguna variabilidad.
      R2 = 1: El modelo explica toda la variabilidad
"""
r2 = r2_score(y_test, y_pred_simple)
print(f"Coef R2: {r2:.2f}")

# Visualizar los resultados
plt.scatter(X_test, y_test, label='Datos de prueba', color='blue')                  # Puntos de prueba
# Para agregar las metricas en un Textbox en la grafica
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
metrics = '\n'.join((
    'MSE: '+ str(f'{mse_simple:.2f}'),
   'MAE: '+ str(f'{mae_simple:.2f}')
    ))
plt.text(0.05, 0.80, metrics, fontsize=10,
        horizontalalignment='left', verticalalignment='center_baseline',
        transform=plt.gca().transAxes, bbox=props)
plt.plot(X_test, y_pred_simple, label=f'Regresion Lineal (R^2={r2:.2f})', color='red')     # Linea de regresion
plt.title('Variacion Precios de los vehiculos con respecto a los anos: \
          \nRegresion Lineal y Coef. de Determinacion R^2')
plt.xlabel('X: Ano del vehiculo')
plt.ylabel('y: Precio de venta')
plt.legend()
# Mostrar el grafico
plt.show()


# #############
# Analisis 2 Relacion del precio con respecto al kilometraje
# #############

# Extraer datos de la categoria: Variable independiente
X_simple_2 = data['km_driven'].values.reshape(-1, 1)

# Extraer datos de la categoria: Variable dependiente
y_simple_2 = data['selling_price'].values

# Se entrenan el modelo, con 20% datos para la prueba, un seed de 42
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_simple_2, y_simple_2, test_size=0.2, random_state=42)

# Crea y ajusta objeto del tipo de modelo Regresion Lineal Simple
model_simple_2 = LinearRegression()
model_simple_2.fit(X_train_2, y_train_2)

# Hacen predicciones del modelo
y_pred_simple_2 = model_simple_2.predict(X_test_2)

# Estas metricas ayudan a entender que tan bien se desempenno el modelo
# Se obtiene el MSE con simple de la prediccion con respecto a los datos de prueba
mse_simple_2 = mean_squared_error(y_test_2, y_pred_simple_2)
print(f"MSE: {mse_simple_2:.2f}")

# Error absoluto medio
mae_simple_2 = mean_absolute_error(y_test_2, y_pred_simple_2)       
print(f"MAE: {mae_simple_2:.2f}")

# Calcular el coeficiente de determinacion R^2
""" 
@note El coeficiente de determinacion R2 es una medida estadistica que 
      proporciona una indicación de la proporción de la variabilidad en la 
      variable de respuesta que es explicada por el modelo de regresión
      R2 = 0: El modelo no explica ninguna variabilidad.
      R2 = 1: El modelo explica toda la variabilidad
"""
r2_2 = r2_score(y_test_2, y_pred_simple_2)
print(f"Coef R2: {r2_2:.2f}")

# Visualizar los resultados
plt.scatter(X_test_2, y_test_2, label='Datos de prueba', color='red')                  # Puntos de prueba
# Para agregar las metricas en un Textbox en la grafica
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
metrics = '\n'.join((
    'MSE: '+ str(f'{mse_simple_2:.2f}'),
   'MAE: '+ str(f'{mae_simple_2:.2f}')
    ))
plt.text(0.60, 0.80, metrics, fontsize=10,
        horizontalalignment='left', verticalalignment='center_baseline',
        transform=plt.gca().transAxes, bbox=props)
plt.plot(X_test_2, y_pred_simple_2, label=f'Regresion Lineal (R^2={r2_2:.2f})', color='green')     # Linea de regresion
plt.title('Variacion Precios de los vehiculos con respecto al kilometraje: \
          \nRegresion Lineal y Coef. de Determinacion R^2')
plt.xlabel('X: Kilometraje del vehiculo')
plt.ylabel('y: Precio de venta')
plt.legend()
# Mostrar el grafico
plt.show()