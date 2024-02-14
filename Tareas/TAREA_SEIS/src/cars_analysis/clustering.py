import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def calcular_clustering( data):
    """
    @brief Realiza analisis de clustering en el dataset utilizando KMeans.
    
    Esta funcion toma un DataFrame, selecciona caracteristicas numericas para el clustering,
    evalaa el numero optimo de clusters usando el Metodo del Codo y el Metodo de la Silueta,
    y luego aplica el algoritmo KMeans para formar clusters. 
    Finalmente, visualiza los resultados.

    @param data DataFrame de Pandas que contiene los datos de vehiculos.
    """

    # Extraer datos de la columnas con valores numericos
    X_cluster = data[['year','selling_price', 'km_driven']]


    # Paso: Seleccion del numero de clusters (k)
    # Se hace para el metodo del Codo y el de la Silueta

    # Metodo del Codo 
    # Lista para almacenar los valores de inercia 
    # para diferentes valores de k (numero de clusters).
    inertia = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_cluster)
        inertia.append(kmeans.inertia_)

    # Graficar el Metodo del Codo
    # donde visualizando se toma el punto de inflexion
    plt.plot(range(1, 11), inertia, marker='o')
    plt.title('Metodo del Codo para Seleccion de k')
    plt.xlabel('Numero de Clusters (k)')
    plt.ylabel('Inercia')
    # Mostrar el grafico
    plt.show() 
    """ @note Con el metodo del Codo y la grafica se toma k = 4
    """

    # Metodo de Silueta para diferentes valores de k 
    # Lista para almacenar los puntajes de silueta 
    # para diferentes valores de k.
    silhouette_scores = []
    for k in range(2, 20):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_cluster)
        score = silhouette_score(X_cluster, kmeans.labels_)
        silhouette_scores.append(score)

    # print(f'Silueta es: {silhouette_scores}')

    # Graficar el metodo de la Silueta
    # se toma el valor para el que Coef. sea mas cercano a 1
    plt.plot(range(2, 20), silhouette_scores, marker='o')
    plt.title('Metodo de la Silueta')
    plt.xlabel('Numero de Clusters (k)')
    plt.ylabel('Coeficiente de Silueta')
    # Mostrar el grafico
    plt.show()
    """ @note Con el metodo de la Silueta y la grafica se toma k = 2
    """

    # Paso: Entrenamiento del modelo K-Means s
    # segun el analisis del Met. del Codo

    # Se asume que el numero optimo de clusters es 4.
    # Segun el analisis del Metodo del Codo,

    # Segun el analisis del Metodo del Codo
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_cluster)

    # Agregamos las etiquetas de cluster al conjunto de datos original
    data['Cluster_Kmeans_Codo'] = cluster_labels

    # Grafica de los clusters con KMeans
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # Crear un subplot 3D
    ax.scatter( data['selling_price'], data['year'], data['km_driven'], c=data['Cluster_Kmeans_Codo'], cmap='plasma', marker='o')
    # Titulos yLeyenda 
    ax.set_title('Clusters usando K-means para k = 4 (Met. Codo)')
    ax.set_xlabel('Precio de Venta')
    ax.set_ylabel('Año')
    ax.set_zlabel('Kilometraje')
    # Mostrar el grafico
    plt.show()


    # Paso: Entrenamiento del modelo K-Means 
    # segun el analisis del Met. de la Silueta

    # Se asume que el numero optimo de clusters es 2.
    # Segun el analisis del Metodo de la Silueta

    # Segun el analisis del Metodo de la Silueta
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_cluster)

    # Agregamos las etiquetas de cluster al conjunto de datos original
    data['Cluster_Kmeans_Silueta'] = cluster_labels

    # Gráfica de los clusters con KMeans
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # Crear un subplot 3D
    ax.scatter( data['selling_price'], data['year'], data['km_driven'], c=data['Cluster_Kmeans_Silueta'], cmap='cividis', marker='o')
    # Titulos yLeyenda 
    ax.set_title('Clusters usando K-means para k = 2 (Met. Silueta)')
    ax.set_xlabel('Precio de Venta')
    ax.set_ylabel('Año')
    ax.set_zlabel('Kilometraje')
    # Mostrar el grafico
    plt.show()

# --- Fin funcion ---- #