import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import requests
import os

# Cargar datos
# Obtener datos de https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv
# y almacenarlos en data/dataset.csv

# Variable tipo string que contiene el URL
url = 'https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv'

# Usando  metodo get para obtener los datos
data_web = requests.get(url)

# Condicio para crear dir 'data' en caso de que no exista
if not os.path.exists('data'):
    os.mkdir('data')

# Se abre el archivo (o se crear en caso de no existir)
# w: write o escribir
# ruta: data/dataset.csv
with open('data/dataset.csv', 'w') as datos:
    # Escribir los datos obtenidos del URL en el archivo de la ruta
    datos.write(data_web.text)

# print(type(datos))

# Crear DataFrame de pandas con los datos CSV
data = pd.read_csv("data/dataset.csv")

# -----------
#     1
# -----------

# Se extraen los datos en las caterogia media_income y se transforma la forma (reshape) de los datos
# para un array de arrays (dimension 1x1). Se le pasa -1 para que el interprete detecte el tamano del
# array automaticamente, se realiza por compatabilidad con metodo train_test_split:
# x = [1 , 2, 3, 4, 5] --> [[1], [2], [3], [4], [5]]
X_simple = data['median_income'].values.reshape(-1, 1)

# Extraer datos de la categoria
y_simple = data['median_house_value'].values

# Se entrenan el modelo, con 20% datos para la prueba, un seed de 42
X_train, X_test, y_train, y_test = train_test_split(X_simple, y_simple, test_size=0.2, random_state=42)

# Crea y ajusta objeto del tipo de modelo RL
model_simple = LinearRegression()
model_simple.fit(X_train, y_train)

# Hacen predicciones del modelo
y_pred_simple = model_simple.predict(X_test)

# Se obtiene el MSE con simple de la prediccion con respecto a los datos de prueba
mse_simple = mean_squared_error(y_test, y_pred_simple)
print(f"Error cuadrático medio (MSE) en regresión lineal simple: {mse_simple}")

# -----------
#     2
# -----------

# Extrayendo los datos de las columnas de DF
# Variables independientes
X_multiple = data[['median_income', 'housing_median_age', 'population']]
# Variable dependientes
y_multiple = data['median_house_value'].values

# Se divide las variables para entrenar y probar el modelo
# Se utiliza un 20 % del para la prueba
# Usando un seed pseudo aleatorio de 42
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(X_multiple, y_multiple, test_size=0.2, random_state=42)

# Se crea el objeto con el modelo de RL y se ajusta
model_multiple = LinearRegression()
model_multiple.fit(X_train_multi, y_train_multi)

# Se hacen las predicciones del modelo 
y_pred_multiple = model_multiple.predict(X_test_multi)

# Se calcula la metrica de evaluacion: Error Cuadratico Medio Multiple
# Entre el modelo entrenado y con la prueba
mse_multiple = mean_squared_error(y_test_multi, y_pred_multiple)
# Imprime el valor del MSE en pantalla
print(f"Error cuadrático medio (MSE) en regresión lineal múltiple: {mse_multiple}")

# -----------
#     3
# -----------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Regresion No Lineal
# Obtener datos de las columnas 
X_nonlinear = data['housing_median_age'].values.reshape(-1, 1)
y_nonlinear = data['median_house_value'].values

# Se divide las variables para entrenar y probar el modelo
# Se utiliza un 20 % del para la prueba
# Usando un seed pseudo aleatorio de 42
X_train_nonlinear, X_test_nonlinear, y_train_nonlinear, y_test_nonlinear = train_test_split(X_nonlinear, y_nonlinear, test_size=0.2, random_state=42)


degree = 2
model_nonlinear = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model_nonlinear.fit(X_train_nonlinear, y_train_nonlinear)


y_pred_nonlinear = model_nonlinear.predict(X_test_nonlinear)


mse_nonlinear = mean_squared_error(y_test_nonlinear, y_pred_nonlinear)
print(f"Error cuadrático medio (MSE) en regresión no lineal: {mse_nonlinear}")

# -----------
#     4
# -----------
from sklearn.linear_model import Ridge, Lasso


model_ridge = Ridge(alpha=1.0)
model_ridge.fit(X_train_multi, y_train_multi)


model_lasso = Lasso(alpha=1.0)
model_lasso.fit(X_train_multi, y_train_multi)

# -----------
#     5
# -----------
from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt


X_cluster = data[['longitude', 'latitude']]


kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data['cluster_kmeans'] = kmeans.fit_predict(X_cluster)


dbscan = DBSCAN(eps=0.5, min_samples=5)
data['cluster_dbscan'] = dbscan.fit_predict(X_cluster)


plt.scatter(data['longitude'], data['latitude'], c=data['cluster_kmeans'], cmap='viridis', marker='.')
plt.title('Clusters usando K-means')
plt.show()

plt.scatter(data['longitude'], data['latitude'], c=data['cluster_dbscan'], cmap='viridis', marker='.')
plt.title('Clusters usando DBSCAN')
plt.show()
