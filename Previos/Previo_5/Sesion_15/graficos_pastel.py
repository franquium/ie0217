import matplotlib.pyplot as plt

# Datos de ejemplo
proporciones = [30, 20, 25, 15]
etiquetas = ['A', 'B', 'C', 'D']

# Grafico de pastel
plt.pie(proporciones, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightgreen', 'lightskyblue'])

# Personalizacion
plt.title('Grafico de Pastel')

# Mostrar el grafico
plt.show()
