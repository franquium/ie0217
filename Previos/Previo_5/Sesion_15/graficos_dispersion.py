import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 14]

# Crear un grafico de dispersion
plt.scatter(x, y, label='Puntos')

# Personalizacion
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafico de dispersion')
plt.legend()

# Mostrar el grafico
plt.show()
