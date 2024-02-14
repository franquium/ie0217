import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# import requests
# import os
from zipfile import ZipFile
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
import regression as rl      # Importando los modelos de Regresion Lineal
import clustering as cl      # Importando los algoritmos de Clustering

# Links dados
# https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset?resource=download
# https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset?resource=download&select=CAR+DETAILS+FROM+CAR+DEKHO.csv
# https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset/download?datasetVersionNumber=1


# ###########################################
# Seccion: Solicitud de Datos usando Kaggle #
# ###########################################

# Configuracio API key de Kaggle
api = KaggleApi()
api.authenticate()

# Descargar el dataset especificando el nombre
"""
@note se debe tener el archivo 'kaggle.json' en el dir '.kaggle'
de su computadora, donde el archivo 'kaggle.json es de la forma:

    {"username":"antonck","key":"5a685559c7ab3e42c8abf93db8b5c6d2"}

"""
dataset_name = "akshaydattatraykhare/car-details-dataset"
api.dataset_download_files(dataset_name, path="./", unzip=True)



# Crear DataFrame de pandas con los datos CSV
df = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")
print("Datos cargados exitosamente.\n")
# print(type(df))

# #####################################################
# Seccion: Analisis y Limpieza de Datos  de Vehiculos #
# #####################################################

# Analisis exploratorio de los datos usando el metodo describe()
print(df.describe())

# Bota las columnas donde al menos un elemento falte
df.dropna()

# # Imprimir pa ver que funke
# print(df.head(5))
# print(df.shape)

# Eliminar datos duplicados del dataset
df.drop_duplicates()

# Imprimir pa ver que funke
print(df.head(5))
print(df.shape)


# ###################################################
# Seccion: Analisis de Regresion Lineal y No Lineal #
# ###################################################

# Instanciando el metodo de calcular_RegresionLineal()
# del archivo regression.py
rl.calcular_RegresionLineal( df)