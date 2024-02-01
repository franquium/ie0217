import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D']
valores = [15, 8, 12, 10]

# Grafico de barras verticales
plt.bar(categorias, valores, color='royalblue')

# Personalizacion
plt.xlabel('Categoraas')
plt.ylabel('Valores')
plt.title('Grafico de Barras Verticales')

# Mostrar el grafico
plt.show()
