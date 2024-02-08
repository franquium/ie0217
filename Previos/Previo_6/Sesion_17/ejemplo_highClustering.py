import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering

# Generar datos de ejemplo con tres centros
X, y = make_blobs(n_samples=50, centers=3, random_state=42, cluster_std=1.0)

# Configuracion de Clustering Jerarquico con enlace completo
# El metodo complete considera la distancia maxima 
# entre puntos de dos clusters
Z = linkage(X, method='complete')

# Visualizar el dendrograma 
# para entender la estructura jerarquica de los clusters
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title('Dendrograma Clustering Jerarquico')
plt.xlabel('Indice del Punto de Datos')
plt.ylabel('Distancia')
plt.show()

# Configuracion de Clustering Jerarquico con scikit-learn
# donde n_clusters define el numero de clusters a buscar
agg_clustering = AgglomerativeClustering(n_clusters=3)
agg_labels = agg_clustering.fit_predict(X)

# Visualizar resultados del clustering
# donde los colores representan los clusters encontrados por el algoritmo
plt.scatter(
    X[:, 0], X[:, 1], c=agg_labels, cmap='viridis', edgecolor='k', s=50
)
plt.title('Resultado del Clustering Jerarquico')
plt.xlabel('Caracteristica 1')
plt.ylabel('Caracteristica 2')
# Mostrar el grafico
plt.show()
