import matplotlib.pyplot as plt

# Datos de ejemplo
datos = [15, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90]


# Grafico de caja
plt.boxplot(datos)

# Personalizacion
plt.ylabel('Valores')
plt.title('Grafico de Caja')

# Mostrar el grafico
plt.show()
