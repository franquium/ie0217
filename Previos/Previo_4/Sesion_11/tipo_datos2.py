# Ejemplos con sets
numbers = {2, 4, 6, 6, 8, 3}
print(numbers)  

numbers = {21, 34, 54, 12}
print('Set Inicial:', numbers)

# usando add() 
numbers.add(32)

print('Set Actualizado:', numbers)

# Set
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = {'apple', 'google', 'apple'}

companies.update(tech_companies)
print(companies)

# set con lenguages
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:', languages)

# remueve 'Java' del set
removedValue = languages.discard('Java')
print('Set after remove():', languages)

# creando un set de tipo int
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# creando un set de tipo string 
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# creando un set de tipo de datos mixtos
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# creando un set vacio
empty_set = set()

# creando un diccionario vacio
empty_dictionary = {}

# comprueba el data type de empty_set
print('Data type of empty_set:', type(empty_set))

# comprueba el data type de empty_dictionary
print('Data type of empty_dictionary', type(empty_dictionary))

# ejemplos iteracion de set
fruits = {"Apple", "Peach", "Mango"}

# for loop para acceder a cada elemento de fruits
for fruit in fruits:
    print(fruit)

even_numbers = {2, 4, 6, 8}
print('Set:', even_numbers)

# encuentra un num de elementos
print('Total Elements:', len(even_numbers))



# Ejemplos con diccionarios

capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city)

# Diccionario con llaves de diferentes tipos de datos
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ", capital_city)

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ", capital_city)


# Ejemplo dict

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Diccionario Inicial: ", student_id)

# Modificando el Dict
student_id[112] = "Stan"
print("Diccionario Actualizado: ", student_id)


student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print(student_id[111])  # imprime Eric
print(student_id[113])  # imprime Butters

print("Diccionario Inicial: ", student_id)

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

# Borrando items del diccionario
del student_id[111]

print("Diccionario Actualizado ", student_id)


student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
# Borrando  Dict student_id 
del student_id

# print(student_id)     # Produce NameError porque se elimino


# Ejemplo: Test de Membresia para las llaves del Dict
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Salida: TRUE o Verdadero
print(1 in squares)     # imprime True

print(2 not in squares)     # imprime True

# Tests de Membresia para llave
print(49 in squares)    # imprime false

# Iterando sobre un Dict
for i in squares:
    print(squares[i])