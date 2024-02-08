import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline


# Usando la func random con una semilla de 42
np.random.seed(42)
# # Generar datos de ejemplo no lineales 
X = 2 * np.random.rand(100, 1)
y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1)

# Visualizar los datos no lineales
plt.scatter(X, y)
plt.title('Datos de Regresion No Lineal')
plt.xlabel('X')
plt.ylabel('y')

# Mostrar el grafico
plt.show()

# Aplicar regresion polinomica de segundo grado
# para ajustar los datos no lineales
grado_polinomio = 2
modelo_polinomico = make_pipeline(
    PolynomialFeatures(grado_polinomio), LinearRegression())
modelo_polinomico.fit(X, y)

# Crear datos para visualizar de la regresion polinomica
X_test = np.linspace(0, 2, 100).reshape(100, 1)
y_pred = modelo_polinomico.predict(X_test)

# Visualizar los datos y la curva de ajuste polinomico
plt.scatter(X, y)
plt.plot(X_test, y_pred, color='red', label=f'Regresion Polinomica (grado {grado_polinomio})')
plt.title('Regresion Polinomica')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

# Mostrar el grafico
plt.show()

