""" 
#####################################################################################################
@file calificaciones_estudiantes.py
@autor J. Antonio Franchi
@brief Programa para crear y analizar un conjunto de datos de calificaciones de estudiantes

Este programa genera un conjunto de datos de calificaciones para estudiantes (7) en diversas 
asignaturas (5) y realiza operaciones basicas de analisis estadistico como calcular promedios, 
encontrar calificaciones maximas y sumar calificaciones totales por asignatura, utilizando 
NumPy para el manejo de los datos y operaciones.

#####################################################################################################
""" 

import numpy as np 

#########################################
# Parte 1. Creacion de Datos con NumPy  #
#########################################

# Nombres de las asignaturas
asignaturas = ['Informatica', 'Matematicas', 'Filosofia', 'Historia', 'Biologia']

# Se decide tomar 7 este numero de estudiantes
estudiantes = ['Elliot', 'Tyrell', 'Angela', 'Darlene', 'Ollie', 'Shayla', 'Fernando']

# Crear un diccionario para almacenar los datos
datos_estudiantes = {}

# Generar calificaciones aleatorias entre 0 y 10 para 7 estudiantes en 5 asignaturas
# Usando un ciclo for y rand() para generar las calificaciones
for i in estudiantes:
    calificaciones = np.random.rand(len(asignaturas)) * 10
    # Redondear las calificaciones a dos decimales
    calificaciones = np.round(calificaciones, 2)
    
    datos_estudiantes[i] = dict(zip(asignaturas, calificaciones))


###################################
# Parte 2. Operaciones con NumPy  #
###################################

def operaciones(datos):
    """
    Realiza operaciones sobre el conjunto de datos de calificaciones.
    Entre las operaciones que realiza se encuentra el calculo del promedio de calificacion
    por estudiante y por asignatura.
    Tambien encuentra utilizando NumPy la calificacion maxima obtenido c/u estudiante y 
    la suma total de calificaciones por cada asignatura
    
    @param datos: Array de NumPy con las calificaciones de los estudiantes.
    
    @return: promedios_estudiantes, promedios_asignaturas, max_calificacion_estudiantes, suma_total_asignaturas
    """
    promedios_estudiantes = {}
    promedios_asignaturas = {}
    max_calificaciones_estudiantes = {}
    suma_total_asignaturas = {asignatura: 0 for asignatura in asignaturas}      # Iniciar suma total en cero

    for estudiante, calificaciones in datos_estudiantes.items():

        # Tomando la lista de valores de la calificaciones para el estudiante
        valores_notas = list(calificaciones.values())

        # Calcular el promedio de calificaciones por estudiante
        promedios_estudiantes[estudiante] = np.mean(valores_notas)
        
        # Encontrar la calificacion max obtenida por cada estudiante usando NumPy
        max_calificaciones_estudiantes[estudiante] = np.max(valores_notas)
        
        # Sumar total de calificaciones por asignatura
        for asignatura, calificacion in calificaciones.items():
            suma_total_asignaturas[asignatura] += calificacion

    
    # Calcular el promedio por asignatura
    num_estudiantes = len(datos_estudiantes)        # Numero de estudiantes
    for asignatura, suma in suma_total_asignaturas.items():
        promedios_asignaturas[asignatura] = suma / num_estudiantes
    
    return promedios_estudiantes, promedios_asignaturas, max_calificaciones_estudiantes, suma_total_asignaturas

##########################
# Parte 3. Resultados    #
##########################

# Mostrar datos creados
print("-------------------    Datos creados    -------------------")
for estudiante, notas in datos_estudiantes.items():
    print(f"{estudiante}:\n    {notas}")
print("\n")

# Mostrar los resultados de las operaciones
print("---------------   Resultados de operaciones    ---------------")
# Mostrar los resultados de las operaciones
# # Instancia de la func operaciones()
promedios_estudiantes, promedios_asignaturas, max_calificaciones_estudiantes, suma_total_asignaturas = operaciones(datos_estudiantes)

print("Promedio de calificaciones por estudiante:")
for estudiante, promedio in promedios_estudiantes.items():
    print(f"    {estudiante}: {promedio:.2f}")

print("\nPromedio de calificaciones por asignatura:")
for asignatura, promedio in promedios_asignaturas.items():
    print(f"    {asignatura}: {promedio:.2f}")

print("\nCalificación maxima obtenida por cada estudiante:")
for estudiante, max_calificacion in max_calificaciones_estudiantes.items():
    print(f"    {estudiante}: {max_calificacion}")

print("\nSuma total de calificaciones por asignatura:")
for asignatura, suma in suma_total_asignaturas.items():
    print(f"    {asignatura}: {suma:.2f}")