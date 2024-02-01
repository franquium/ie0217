import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 14]

# Crear un grafico de linea
plt.plot(x, y, label='Datos de ejemplo')

# Annadir una anotacion
plt.annotate('Valor maximo', xy=(5, 14), xytext=(3, 16),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

# Personalizacion adicional, como etiquetas de ejes y titulos
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafico con Anotacion')
plt.legend()

# Mostrar el grafico
plt.show()
