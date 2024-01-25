# Ejemplos de listas

import random
print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd','e']

# saca un item random de list1
print(random.choice(list1))

# Baraja o mezcla la lista
random.shuffle(list1)

# imprimir la lista mezclada
print(list1)

# imprime elemento random
print(random.random())

# Ejemplo acceder elementos de la lista
# Ejemplo 3 de lista
languages = [ "Python", "Swift", "C++"]

# Accesando elemento en el indice 0
print(languages[0]) # Python

# Accesando elemento en el indice 2
print(languages[2]) # C++

# Accesando elemento en el indice 0
print(languages[-1]) # C++

# Accesando elemento en el indice 2
print(languages[-3]) # Python

# Ejemplo slicing de listas

my_list = ['h', 'e', 'l', 'l','o','o','o']

# imprimir del index 1 al 3
print(my_list[1:3])

# imprimir del index 3 hasta el final
print(my_list[3:])

# imprimir del inicio hasta el final
print(my_list[:])


# Ejemplos de manipulacion de listas

numbers = [21, 34, 54, 12]
print("Antes Append:", numbers)

# usando metodo append
numbers.append(32)
print("Despues Append:", numbers)

languages = ['Python', 'Swift', 'C++']

# Cambiando el tercer lang por 'C'
languages[2] = 'C'
print(languages)  # ['Python', 'Swift', 'C']

prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)

even_numbers = [4, 6, 8]
print("List2:", even_numbers)

# uniendo dos lists
prime_numbers.extend(even_numbers)
print("List despues append:", prime_numbers)

# list de langs mas grande
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# borrando segundo item
del languages[1]
print(languages)  # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

# borrando ultimo item
del languages[-1]
print(languages)  # ['Python', 'C++', 'C', 'Java', 'Rust']

# borrando primeros dos items
del languages[0:2]
print(languages)  # ['C', 'Java', 'Rust']

# list de langs original
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# eliminando 'Python' de la list
languages.remove('Python')
print(languages)  # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']


# Ejemplos iterando sobre listas


languages = ['Python', 'Swift', 'C++']
# Iteraando sobre la list
for language in languages:
    print(language)

# Membresia en la lista con in
languages = ['Python', 'Swift', 'C++']
print('C' in languages)  # False
print('Python' in languages)  # True

# Largo de la lista
languages = ['Python', 'Swift', 'C++']
print("List: ", languages)
print("Total Elements: ", len(languages))  # 3

# List comprehensions o listas de comprension
numbers = [number*number for number in range(1, 6)]
print(numbers)  # Salida es: [1, 4, 9, 16, 25]  Ojo revisarlo bien


# Ejemplos con tuplas: se usan para elementos heterogeneos, son inmutables

# Diferentes tipes de tuplas
# tupla vacia
my_tuple = ()
print(my_tuple)

# Tupla con ints
my_tuple = (1, 2, 3)
print(my_tuple)

# tupla con datatypes mixtos
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# tupla anidada
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)


# Ejemplos variable tipo string

name = "Python"
print(name)
message = "I love Python."
print(message)

greet = 'hello'
# accede al 1er elemento del indice
print(greet[1])  # "e"

greet = 'hello'
# accede al 4to elemento al final aka anteantepenultimo
print(greet[-4])  # "e"

greet = 'Hello'
# accede al char de 1 al 3  del index
print(greet[1:4])  # "ell"

message = 'Hola Amigos'
# message[0] = 'H'      # Da un TypeError
print(message)

message = 'Hola Amigos'
# asignar nuevo string a la var message 
message = 'Hello Friends'
print(message);  # imprime "Hello Friends"

# String multilinea
message = """
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
"""
print(message)


# Ejemplo de comparacion de strings
# String comparison
str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# compara str1 y str2
print(str1 == str2)

# compara str1 y str3
print(str1 == str3)

print('a' in 'program')  # True
print('at' not in 'battle')  # False

# Concatenacion de Strings
greet = "Hello, "
name = "Jack"
# usando operador +
result = greet + name
print(result)

# Iteracion de Strings
greet = 'Hello'
# iterando sobre greet
for letter in greet:
    print(letter)

# Largo de un String
greet = 'Hello'
# cuenta el largo del string greet
print(len(greet))

