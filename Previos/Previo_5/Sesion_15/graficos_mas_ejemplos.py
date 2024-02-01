# Ejm 1 Senos y cosenos

import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear un grafico de lineas con dos series de datos
plt.plot(x, y1, label='Seno')
plt.plot(x, y2, label='Coseno')

# Personalizacion
plt.xlabel('Angulo (rad)')
plt.ylabel('Valor')
plt.title('Funciones Seno y Coseno')
plt.legend()

# Mostrar el grafico
plt.show()


#Ejem 2 Subtramas

# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D']
valores = [15, 8, 12, 10]
tendencia = [5, 10, 8, 13]

# Crear una figura con dos subtramas
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Subtrama 1: Grafico de barras
axs[0].bar(categorias, valores, color='royalblue')
axs[0].set_title('Grafico de Barras')

# Subtrama 2: Grafico de línea
axs[1].plot(categorias, tendencia, color='green', marker='o')
axs[1].set_title('Gráfico de Línea')

# Personalizacion adicional
for ax in axs:
    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')

# Ajustar la disposicion
plt.tight_layout()

# Mostrar la figura con ambas subtramas
plt.show()
