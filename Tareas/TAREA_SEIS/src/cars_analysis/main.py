import regression
import clustering
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import requests
import os
from zipfile import ZipFile
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

# Links dados
# https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset?resource=download
# https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset?resource=download&select=CAR+DETAILS+FROM+CAR+DEKHO.csv
# https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset/download?datasetVersionNumber=1



# #########################################
# Version 1
# #########################################

# url = "https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset?resource=download"

# # respuesta = requests.get(url)

# # print(respuesta.text)

# # Datos para mi usario de Kaggle
# username = "antonck"
# key = "5a685559c7ab3e42c8abf93db8b5c6d2"

# dataset_url = 'https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset?resource=download'

# # Endpoint de la API de Kaggle para descargar datasets
# api_url = f'https://www.kaggle.com/api/v1/datasets/download/{dataset_url}'

# # Configura los encabezados de la solicitud con tu clave API
# headers = {'Authorization': f'Bearer {key}'}

# # Realiza la solicitud para descargar el dataset
# response = requests.get(api_url, headers=headers, stream=True)

# # Verifica si la solicitud fue exitosa
# if response.status_code == 200:
#     # Abre un archivo local para guardar el contenido del dataset
#     with open('dataset.zip', 'wb') as file:
#         for chunk in response.iter_content(chunk_size=128):
#             file.write(chunk)
#     print("Dataset descargado con exito.")
# else:
#     print("Error al descargar el dataset:", response.status_code)

# #########################################
# Version 2
# #########################################

# car-details-dataset
# kaggle datasets download -d akshaydattatraykhare/car-details-dataset

# # Datos para mi usario de Kaggle
# username = "antonck"
# key = "5a685559c7ab3e42c8abf93db8b5c6d2"

# dataset_name = "car-details-dataset"

# # url_kaggle = f'https://www.kaggle.com/akshaydattatraykhare/{dataset_name}/download'
# url_kaggle = f'https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset?resource=download&select=CAR+DETAILS+FROM+CAR+DEKHO.csv'

# headers = {"Authorization": f"Bearer {key}"}

# response = requests.get(url_kaggle, headers=headers,  stream=True)

# zip_filename = f'{dataset_name}.zip'
# with open(zip_filename,"wb") as zip_file:
#     zip_file.write(response.content)

# with ZipFile(zip_filename, "r") as zip_ref:
#     zip_ref.extractall("./")

# os.remove(zip_filename)

# #########################################
# Version3
# #########################################

# # Debes reemplazar 'your_kaggle_username' y 'your_kaggle_key' con tu nombre de usuario y clave de la API de Kaggle.
# kaggle_info = {
#     "UserName": "antonck",
#     "Key": "5a685559c7ab3e42c8abf93db8b5c6d2"
# }

# # URL del endpoint de la API para descargar el dataset
# dataset_url = "https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset?resource=download&select=CAR+DETAILS+FROM+CAR+DEKHO.csv"

# # Path para guardar el archivo .zip del dataset
# dataset_path = Path("car-details-dataset.zip")

# # Encabezados para la solicitud de la API
# headers = {
#     "Authorization": f"Bearer {kaggle_info['Key']}"
# }

# response = requests.get(dataset_url, headers=headers, stream=True)

# # Verifica que la solicitud fue exitosa (200)
# if response.status_code == 200:
#     with open(dataset_path, 'wb') as f:
#         f.write(response.content)
#     print(f"Dataset descargado en: {dataset_path}")
# else:
#     print(f"Error al descargar el dataset: {response.status_code}")

# #########################################
# Version 4: Chanchada usando el link Obtenido del HTML
# #########################################

# # Variable tipo string que contiene el URL
# url = 'https://www.kaggle.com/datasets/akshaydattatraykhare/car-details-dataset/download?datasetVersionNumber=1'

# # Usando  metodo get para obtener los datos
# data_web = requests.get(url)

# # # Condicion para crear dir 'data' en caso de que no exista
# # if not os.path.exists('data'):
# #     os.mkdir('data')

# # Se abre el archivo (o se crear en caso de no existir)
# # w: write o escribir
# # ruta: data/dataset.csv
# with open('dataset_car-details-dataset.csv', 'wb') as datos:
#     # Escribir los datos obtenidos del URL en el archivo de la ruta
#     datos.write(data_web.text)


# #########################################
# Version 5: Usando Kaggle
# ########################################

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

# Imprimir pa ver que funke
print(df.head(5))
print(df.shape)

# Limpieza de Datos  de Vehiculos
# Bota las columnas donde al menos un elemento falte
df.dropna()

# Imprimir pa ver que funke
print(df.head(5))
print(df.shape)

# Eliminar datos duplicados del dataset
df.drop_duplicates()

# Imprimir pa ver que funke
print(df.head(5))
print(df.shape)

print(df.describe())