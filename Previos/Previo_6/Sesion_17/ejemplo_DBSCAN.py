import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

# Generar datos de ejemplo con forma de dos lunas crecientes
X, _ = make_moons(n_samples=200, noise=0.05, random_state=42)

# Configurar y ajustar el modelo DBSCAN
# donde eps: radio del vecindario  alrededor de un punto para 
# ser considerado parte de un cluster, ajusta el tamano del vecindario
# donde min_samples: numero minimo de puntos requeridos para 
# formar un cluster, ajusta la densidad requerida
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan_labels = dbscan.fit_predict(X)

# Visualizar resultados
# donde los colores indican los diferentes clusters 
# asignados por el algoritmo DBSCAN
plt.scatter(
    X[:, 0], X[:, 1], c=dbscan_labels, cmap='viridis', edgecolor='k', s=50
)
plt.title('Resultado del Clustering DBSCAN')
plt.xlabel('Caracteristica 1')
plt.ylabel('Caracteristica 2')
# Mostrar el grafico
plt.show()
