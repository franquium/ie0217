import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 14]

# Crear un grafico de linea
plt.plot(x, y)

# Personalizacion
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Línea Simple')

# Guardar el grafico como imagen (por ejemplo, en formato PNG)
plt.savefig('grafico.png')

# Mostrar el grafico
plt.show()
