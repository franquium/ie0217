# Ejemplo funcion greet

def greet(name = "Sin Nombre"):
    print("Hello,", name," that is lame! Maybe I should give a name")

# Lllamado de func
greet("friend")


# Ejemplo de func de sumar
def sumar(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# Lllamado de func
sumar(5, 8)


# Ejemplo de func de encontrar el cuadrado de un num
def find_square(num):
    result = num * num
    return result

# Lllamado de func 
cuadrado = find_square(2)
print("Cuadrado es:", cuadrado)


# Ejemplo de uso de funcs sqrt y pow de lib math de un num
import math

# calc la raiz cuadrada
raiz_cua = math.sqrt(4)

print("Raiz cuadrada de 4 es:", raiz_cua)

# calc potencia de
power = math.pow(2, 3)

print("2 a la 3 es:", power)


# Ejemplo de func con params tipo string

def display_info( first_name, last_name):
    print('Nombre:', first_name)
    print('Apellido:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')


# Ejemplo programa para encontrar la suma de multiples numeros
def find_sum(*numbers):     # *numbers: Para indicar que es una cantidad indeterminada de argumentos
    result = 0

    for num in numbers:
        result = result + num

    print("Suma = ", result)

# llamado a func con 3 argumentos
find_sum(1, 2, 3)

# llamado a func con 2 argumentos
find_sum(4, 9)


# Ejemplo de recursividad con el calculo de un factorial

def factorial(x):
    """Esta es una func recursiva para
    encontrar el factorial de un entero"""

    if (x == 1):
        return 1
    else:
        return (x * factorial(x-1))
    
num = 3
# llamado a func
print("El factorial de", num, "es:",factorial(num))


# Ejemplos de funciones lambda: declarar una func en medio codigo

# Ej 1 lambda sin argumentos
# Declarando una func lambda
saludar = lambda : print("Ciao, mondo!")

# llamado a func
saludar()

# Ej 2 lambda con un argumentos
# Declarando una func lambda
saludar_usr = lambda name : print('Ciao', name,"!")

# llamado a func
saludar_usr('Jonas')


# Ej 3 lambda usando como condicion de filtrar
# programa para filtrar solamente los elementos pares de una lista
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: ((x % 2) == 0), my_list))

print(new_list)

# Ej 4 lambda usando como condicion 
# programa para duplicar (valor) de cada elemento en una lista con map()
my_list2 = [1, 5, 4, 6, 8, 11, 3, 12]

new_list2 = list(map(lambda x: ( x * 2), my_list2))

print(new_list2)