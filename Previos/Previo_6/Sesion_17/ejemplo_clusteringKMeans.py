from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(42)  # Un seed para reproducibilidad
# Crear 100 puntos bidimensionales aleatorios entre 0 y 10
X = np.random.rand(100, 2) * 10

# Configurar subgraficos
plt.figure(figsize=(12, 5))

# Subgrafico 1: Visualizacion de puntos de datos aleatorios
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c='blue', marker='o')
plt.title('Puntos de Datos Aleatorios')
plt.xlabel('Caracteristica 1')
plt.ylabel('Caracteristica 2')

# Configuracion de K-Means con un numero de clusters (k) especifico
kmeans = KMeans(n_clusters=3)
# Ajuste del modelo
kmeans.fit(X)

# Etiquetas de los clusters y coordenadas de los centroides
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Subgrafico 2: Resultado del Clustering con K-Means
plt.subplot(1, 2, 2)
for i in range(len(X)):
    # Asignar colores a los puntos basados en el cluster asignado
    plt.scatter(X[i][0], X[i][1],
                c=('red' if labels[i] == 0 else 'blue' if labels[i] == 1 else 'green'),
                marker='o')
# Dibujar los centroides
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x', s=200, label='Centroides')
plt.title('Resultado del Clustering con K-Means')
plt.xlabel('Caracteristica 1')
plt.ylabel('Caracteristica 2')
plt.legend()

# Ajustar el diseno para evitar sobreposiciones
plt.tight_layout()
# Mostrar los subgraficos
plt.show()
