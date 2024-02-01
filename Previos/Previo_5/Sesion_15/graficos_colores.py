import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 14]

# Crear un grafico de linea personalizado con colores, estilos y marcadores
plt.plot(x, y, color='blue', linestyle='--', marker='o', label='Serie A')

# Personalizacion adicional, como etiquetas de Ejes y Titulos
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafico Personalizado')
plt.legend()

# Mostrar el grafico
plt.show()
