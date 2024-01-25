# Ejemplo del if
number = 10

# chequea si el numero es mayor a cero
if (number > 0):
    print('Num es positivo')
print('La sentencia if es facil :) ')

# Ejemplo del if-else
if (number > 0):
    print('Num positivo')
else:
    print('Num negativo')
print('Esta sentencia siempre se ejecuta')

# Ejemplo del elif
number = 0
if (number > 0):
    print('Num positivo')
elif (number == 0):
    print('Es cero')
else:
    print('Num negativo')
print('Esta sentencia siempre se ejecuta')

# Ejemplos de for loop
for x in 'Python':
    print(x)

# usando range() para definir un rango de valores
values = range(4)

# iterando desde i = 0 hasta i = 3
for i in values:
    print(i)

languages = ["Swift", "Python", "Go"]

for _ in languages:     # Para iterar  n-veces sin imprimir nada en particular, solo asegurarse que esta iterando
    print('Hallo')
    print('Hi')

for i in values:
    print(i)
else:
    print("No items left")

# Ejemplos de while loop

# Ejemplo 1
# programa muestra numeros desde 1 a 5

# inicializando las variables
i = 1
n = 5

# While loop
while i <= n:
    print(i)
    i = i + 1

# Ejemplo 2
# programa para calcular la suma de numeros
# hasta que el usuario ingrese un cero

total = 0

number = int(input('Ingrese un numero: ')) # Type Casting a tipo int

# sumar nums hasta que number sea cero
while (number != 0):
    total += number     # total = total + number

    # Recibe un input de numero int de nuevo
    number = int(input('Ingrese un numero: '))

print('total = ', total)

#Ejemplo 3

counter = 0

while (counter < 3):
    print('Dentro del loop')
    counter = counter + 1
else:
    print('Dentro del else')


# Ejemplos loops con break y continue

# Ejemplo 1
for i in range(5):
    if (i == 3):
        break
    print(i)

# Ejemplo 2
for i in range(5):
    if (i == 3):
        continue
    print(i)

# Ejemplo 3
# programa para encontrar los primeros 5 multiplos de 6
i = 1
while (i <= 10):
    print('6 * ', (i), '=', 6 * i)
    if (i >= 5):
        break
    
    i = i + 1 

# Ejemplo 4
# programa para imprimir primeros impares de 1 a 10
num = 0
while (num < 10):
    num += 1

    if ((num % 2) == 0 ):
        continue

    print(num) 

# Ejemplo de funcion pass 
n = 10

# usar pass dentro de la sentencia if
if n > 10:
    pass # placeholder

print('Ciao')