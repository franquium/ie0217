from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Paso 1. Preparacion de datos

# Conjunto de datos usando Pandas
data = pd.read_csv('data.csv')
# Nota: elarchivo data.csv solo contiene las 13 filas que se 
# mostraban en la Sesion de clase


# Paso 2. Exploracion y preprocesamiento

# Exploracion de datos
print(data.head())

# Preprocesamiento (por ejemplo, escalamiento de caracteristicas)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Paso 3. Seleccion del numero de clusters (k)

# Metodo del Codo
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Graficar el Metodo del Codo
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Metodo del Codo para Seleccion de k')
plt.xlabel('Numero de Clusters (k)')
plt.ylabel('Inercia')
# Mostrar el grafico
plt.show()

# Paso 4. Entrenamiento del modelo K-Means

# Se asume que el numero optimo de clusters es 4.
# Segun el analisis del Metodo del Codo.
kmeans = KMeans(n_clusters=4, random_state=42)
cluster_labels = kmeans.fit_predict(scaled_data)

# Agregamos las etiquetas de cluster al conjunto de datos original
data['Cluster'] = cluster_labels


# Paso 5. Analisis de segmentos

# Analisis de segmentos
segment_analysis = data.groupby('Cluster').mean()

# Visualizacion de segmentos
plt.figure(figsize=(12, 6))
for cluster in range(4):
    plt.scatter(data[data['Cluster'] == cluster]['Frequency'], 
                data[data['Cluster'] == cluster]['Avg_Spend'], 
                label=f'Cluster {cluster}')

plt.title('Segmentacion de Clientes por Frecuencia y Gasto Promedio')
plt.xlabel('Frecuencia de Visita')
plt.ylabel('Gasto Promedio')
plt.legend()
# Mostrar el grafico
plt.show()
