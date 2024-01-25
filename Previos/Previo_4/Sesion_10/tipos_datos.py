# Ejemplo 1
num1 = 5
print( num1, 'es de tipo',  type(num1))

num2 = 2.0
print( num2, 'es de tipo',  type(num2))

num3 = 1+2j
print( num3, 'es de tipo',  type(num3))


# Ejemplo 2
name = 'Python'
print(name)

message = 'Python for rookies'
print(message)


# Ejemplo 3 de lista
languages = ["Swift", "Java", "Python"]

# Accesando elemento en el indice 0
print(languages[0]) # Swift

# Accesando elemento en el indice 2
print(languages[2]) # Python


# Ejemplo 4
# Creando una tupla
product = ('Microsoft', 'Xbox', 499.99)

# Accesando elemento en el indice 0
print(product[0]) # Microsoft

# Accesando elemento en el indice 1
print(product[1]) # Xbox


# Ejemplo 5 y 6
# Creando un dict llamado capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city)

print(capital_city['Nepal']) # imprime Kathmandu

# print(capital_city['Kathmandu']) # lanza mensaje de error


# Ejemplo 7 Set o Conjunto
# Creando un set llamado student_id
student_id = {112, 114, 116, 118, 115}

# Muestra los elementos de student_id
print(student_id)

# Muestra los tipos de student_id
print(type(student_id))