from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(42)  # Un seed para reproducibilidad
# 100 puntos bidimensionales en un rango de 0 a 10
X = np.random.rand(100, 2) * 10

# Calcular la inercia para diferentes valores de k
inercias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inercias.append(kmeans.inertia_)

# Graficar el metodo del codo
plt.plot(range(1, 11), inercias, marker='o')
plt.title('Metodo del Codo')
plt.xlabel('Numero de Clusters (k)')
plt.ylabel('Inercia')
# Mostrar el grafico
plt.show()
