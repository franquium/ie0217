import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


def calcular_RegresionLineal( data):
    """
    @brief Realiza análisis de regresión lineal en el dataset de vehículos.
    
    Esta funcion toma un DataFrame y realiza dos analisis de regresión lineal:
    con el precio como variable dependiente y como variables independientes el
    año del vehícul y otro con el kilometraje.
    Se calculan metricas de rendimiento y se visualizan los resultados.

    @param data DataFrame de Pandas que contiene los datos de vehiculos.
    """

    # #########################################################
    # Analisis 1 Relacion del precio con respecto a los annos #
    # #########################################################

    # Extraer datos de la categoria: Variable independiente
    X_simple = data['year'].values.reshape(-1, 1)

    # Extraer datos de la categoria: Variable dependiente
    y_simple = data['selling_price'].values

    # Se entrenan el modelo, con 20% datos para la prueba, un seed de 42
    X_train, X_test, y_train, y_test = train_test_split(X_simple, y_simple, test_size=0.2, random_state=42)

    # Crea y ajusta objeto del tipo de modelo RL
    model_simple = LinearRegression()
    model_simple.fit(X_train, y_train)

    # Hacen predicciones del modelo
    y_pred_simple = model_simple.predict(X_test)

    # Calculo de metricas
    print("\nPara la evaluacion de rendimiento de la Regresion Lineal \
          \nde la relacion del precio de los vehiculos con respecto a los años:")
    # Estas metricas ayudan a entender que tan bien se desempenno el modelo
    # Calcular el Error cuadratico medio
    mse_simple = mean_squared_error(y_test, y_pred_simple)
    print(f"Error cuadratico medio (MSE) en regresión lineal simple: {mse_simple:.2f}")

    # Calcular el Error absoluto medio
    mae_simple = mean_absolute_error(y_test, y_pred_simple)       
    print(f"Error medio absoluto (MAE) en regresión lineal simple: {mae_simple:.2f}")

    # Calcular el coeficiente de determinacion R^2
    """ 
    @note El coeficiente de determinacion R2 es una medida estadistica que 
        proporciona una indicación de la proporción de la variabilidad en la 
        variable de respuesta que es explicada por el modelo de regresión
        R2 = 0: El modelo no explica ninguna variabilidad.
        R2 = 1: El modelo explica toda la variabilidad
    """
    r2 = r2_score(y_test, y_pred_simple)
    print(f"El Coeficiente de Determinacion R^2: {r2:.2f}")

    # Visualizar los resultados
    plt.scatter(X_test, y_test, label='Datos de prueba', color='blue')  # Puntos de prueba
    # Para agregar las metricas en un Textbox en la grafica
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    metrics = '\n'.join((
        'MSE: '+ str(f'{mse_simple:.2f}'),
        'MAE: '+ str(f'{mae_simple:.2f}')
        ))
    plt.text(0.05, 0.80, metrics, fontsize=10,
            horizontalalignment='left', verticalalignment='center_baseline',
            transform=plt.gca().transAxes, bbox=props)
    plt.plot(X_test, y_pred_simple, label=f'Regresion Lineal (R^2={r2:.2f})', color='red')     # Linea de regresion
    plt.title('Variacion Precios de los vehiculos con respecto a los años \
            \nRegresion Lineal y Coef. de Determinacion R^2')
    plt.xlabel('X: Ano del vehiculo')
    plt.ylabel('y: Precio de venta')
    plt.legend()
    # Mostrar el grafico
    plt.show()


    # ############################################################
    # Analisis 2 Relacion del precio con respecto al kilometraje #
    # ############################################################

    # Extraer datos de la categoria: Variable independiente
    X_simple_2 = data['km_driven'].values.reshape(-1, 1)

    # Extraer datos de la categoria: Variable dependiente
    y_simple_2 = data['selling_price'].values

    # Se entrenan el modelo, con 20% datos para la prueba, un seed de 42
    X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_simple_2, y_simple_2, test_size=0.2, random_state=42)

    # Crea y ajusta objeto del tipo de modelo Regresion Lineal Simple
    model_simple_2 = LinearRegression()
    model_simple_2.fit(X_train_2, y_train_2)

    # Hacen predicciones del modelo
    y_pred_simple_2 = model_simple_2.predict(X_test_2)

    # Calculo de metricas
    print("\nPara la evaluacion de rendimiento de la Regresion Lineal \
          \nde la relacion del precio de los vehiculos con respecto al kilometraje:")
    # Estas metricas ayudan a entender que tan bien se desempenno el modelo
    # Calcular el Error cuadratico medio
    mse_simple_2 = mean_squared_error(y_test_2, y_pred_simple_2)
    print(f"Error cuadratico medio (MSE) en regresión lineal simple: {mse_simple_2:.2f}")

    # Calcular el Error absoluto medio
    mae_simple_2 = mean_absolute_error(y_test_2, y_pred_simple_2)       
    print(f"Error medio absoluto (MAE) en regresión lineal simple: {mae_simple_2:.2f}")

    # Calcular el coeficiente de determinacion R^2
    """ 
    @note El coeficiente de determinacion R2 es una medida estadistica que 
        proporciona una indicación de la proporción de la variabilidad en la 
        variable de respuesta que es explicada por el modelo de regresión
        R2 = 0: El modelo no explica ninguna variabilidad.
        R2 = 1: El modelo explica toda la variabilidad
    """
    r2_2 = r2_score(y_test_2, y_pred_simple_2)
    print(f"El Coeficiente de Determinacion R^2: {r2_2:.2f}")

    # Visualizar los resultados
    plt.scatter(X_test_2, y_test_2, label='Datos de prueba', color='red')   # Puntos de prueba
    # Para agregar las metricas en un Textbox en la grafica
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    metrics = '\n'.join((
        'MSE: '+ str(f'{mse_simple_2:.2f}'),
        'MAE: '+ str(f'{mae_simple_2:.2f}')
        ))
    plt.text(0.60, 0.80, metrics, fontsize=10,
            horizontalalignment='left', verticalalignment='center_baseline',
            transform=plt.gca().transAxes, bbox=props)
    plt.plot(X_test_2, y_pred_simple_2, label=f'Regresion Lineal (R^2={r2_2:.2f})', color='green')     # Linea de regresion
    plt.title('Variacion Precios de los vehiculos con respecto al kilometraje: \
            \nRegresion Lineal y Coef. de Determinacion R^2')
    plt.xlabel('X: Kilometraje del vehiculo')
    plt.ylabel('y: Precio de venta')
    plt.legend()
    # Mostrar el grafico
    plt.show()


def calcular_RegresionNoLineal(data):
    """
    @brief Realiza analisis de regresion no lineal en el dataset de vehiculos.
    
    Esta funcion toma un DataFrame y realiza dos analisis de regresion no lineal:
    con el precio como variable dependiente y como variables independientes el
    año del vehícul y otro con el kilometraje.
    Se calculan metricas de rendimiento y se visualizan los resultados.

    @param data DataFrame de Pandas que contiene los datos de vehiculos.
    """

    # #########################################################
    # Analisis 1 Relacion del precio con respecto a los annos #
    # #########################################################

    # Regresion No Lineal
    # Extraer datos de la categoria: Variable independiente
    X_nonlinear = data['year'].values.reshape(-1, 1)
    
    # Extraer datos de la categoria: Variable dependiente
    y_nonlinear = data['selling_price'].values

    # Se divide las variables para entrenar y probar el modelo
    # Se utiliza un 20 % del para la prueba
    # Usando un seed pseudo aleatorio de 42
    X_train_nonlinear, X_test_nonlinear, y_train_nonlinear, y_test_nonlinear = train_test_split(X_nonlinear, y_nonlinear, test_size=0.2, random_state=42)

    # Grados del polinomio de RNL
    degree = 2
    # Crear y ajustar modelo de RNL 
    model_nonlinear = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model_nonlinear.fit(X_train_nonlinear, y_train_nonlinear)

    # Predecir datos del modelo de la regresion polinomica 
    # donde X_test_nonlinear se ajusta el numero de muestras de 868
    X_test_nonlinear = np.linspace(1992, 2020, 868).reshape(868, 1)
    y_pred_nonlinear = model_nonlinear.predict(X_test_nonlinear)

    # Calculo de metricas
    print("\nPara la evaluacion de rendimiento de la Regresion No Lineal\n \
          de la relacion del precio de los vehiculos con respecto a los años:")
    # Calcula el Error Cuadratico Medio de RNL
    mse_nonlinear = mean_squared_error(y_test_nonlinear, y_pred_nonlinear)
    print(f"Error cuadrático medio (MSE) en regresión no lineal: {mse_nonlinear}")

    # Calcula el Error absoluto medio
    mae_nonlinear = mean_absolute_error(y_test_nonlinear, y_pred_nonlinear)       
    print(f"Error medio absoluto (MAE) en regresión lineal simple: {mae_nonlinear:.2f}")

    # Calcular el coeficiente de determinacion R^2
    r2_nonlinear = r2_score(y_test_nonlinear, y_pred_nonlinear)
    print(f"El Coeficiente de Determinacion R^2: {r2_nonlinear:.2f}")

    # Visualizar los resultados
    plt.scatter(X_test_nonlinear, y_test_nonlinear, label='Datos de prueba', color='blue')  # Puntos de prueba
    # Para agregar las metricas en un Textbox en la grafica
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    metrics = '\n'.join((
        'MSE: '+ str(f'{mse_nonlinear:.2f}'),
        'MAE: '+ str(f'{mae_nonlinear:.2f}')
        ))
    plt.text(0.05, 0.80, metrics, fontsize=10,
            horizontalalignment='left', verticalalignment='center_baseline',
            transform=plt.gca().transAxes, bbox=props)
    plt.plot(X_test_nonlinear, y_pred_nonlinear, label=f'Regresion Polinomica (R^2={r2_nonlinear:.2f})', color='red')     # Curva de regresion
    plt.title('Variacion Precios de los vehiculos con respecto a los años \
            \nRegresion No Lineal')
    plt.xlabel('X: Ano del vehiculo')
    plt.ylabel('y: Precio de venta')
    plt.legend()
    # Mostrar el grafico
    plt.show()

    # ############################################################
    # Analisis 2 Relacion del precio con respecto al kilometraje #
    # ############################################################

    # Regresion No Lineal
    # Extraer datos de la categoria: Variable independiente
    X_nonlinear_2 = data['km_driven'].values.reshape(-1, 1)
    
    # Extraer datos de la categoria: Variable dependiente
    y_nonlinear_2 = data['selling_price'].values

    # Se divide las variables para entrenar y probar el modelo
    # Se utiliza un 20 % del para la prueba
    # Usando un seed pseudo aleatorio de 42
    X_train_nonlinear_2, X_test_nonlinear_2, y_train_nonlinear_2, y_test_nonlinear_2 = train_test_split(X_nonlinear_2, y_nonlinear_2, test_size=0.2, random_state=42)

    # Grados del polinomio de RNL
    degree = 2
    # Crear y ajustar modelo de RNL 
    model_nonlinear_2 = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model_nonlinear_2.fit(X_train_nonlinear_2, y_train_nonlinear_2)

    # Predecir datos del modelo de la regresion polinomica 
    # donde X_test_nonlinear se ajusta el numero de muestras de 868
    # para mostrar una sola curva y no varias
    X_test_nonlinear_2 = np.linspace(1992, 2020, 868).reshape(868, 1)
    y_pred_nonlinear_2 = model_nonlinear_2.predict(X_test_nonlinear_2)

    # Calculo de metricas
    print("\nPara la evaluacion de rendimiento de la Regresion No Lineal \
          \nde la relacion del precio de los vehiculos con respecto al kilometraje:")
    # Calcula el Error Cuadratico Medio de RNL
    mse_nonlinear_2 = mean_squared_error(y_test_nonlinear_2, y_pred_nonlinear_2)
    print(f"Error cuadrático medio (MSE) en regresión no lineal: {mse_nonlinear_2}")

    # Calcula el Error absoluto medio
    mae_nonlinear_2 = mean_absolute_error(y_test_nonlinear_2, y_pred_nonlinear_2)       
    print(f"Error medio absoluto (MAE) en regresión lineal simple: {mae_nonlinear_2:.2f}")

    # Calcular el coeficiente de determinacion R^2
    r2_nonlinear_2 = r2_score(y_test_nonlinear_2, y_pred_nonlinear_2)
    print(f"El Coeficiente de Determinacion R^2: {r2_nonlinear_2:.2f}")

    # Visualizar los resultados
    plt.scatter(X_test_nonlinear_2, y_test_nonlinear_2, label='Datos de prueba', color='blue')  # Puntos de prueba
    # Para agregar las metricas en un Textbox en la grafica
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    metrics = '\n'.join((
        'MSE: '+ str(f'{mse_nonlinear_2:.2f}'),
        'MAE: '+ str(f'{mae_nonlinear_2:.2f}')
        ))
    plt.text(0.05, 0.80, metrics, fontsize=10,
            horizontalalignment='left', verticalalignment='center_baseline',
            transform=plt.gca().transAxes, bbox=props)
    plt.plot(X_test_nonlinear_2, y_pred_nonlinear_2, label=f'Regresion Polinomica (R^2={r2_nonlinear_2:.2f})', color='red')     # Curva de regresion
    plt.title('Variacion Precios de los vehiculos con respecto  al kilometraje \
            \nRegresion No Lineal')
    plt.xlabel('X: Kilometraje del vehiculo')
    plt.ylabel('y: Precio de venta')
    plt.legend()
    # Mostrar el grafico
    plt.show()

# --- Fin funcion ---- #