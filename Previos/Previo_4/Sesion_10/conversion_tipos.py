# Ejemplo 1 Conversion implicita
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# Muestra un nuevo valor y su tipo de dato (data type) resultante
print("Valor: ", new_number)
print("Data Type: ", type(new_number))


# Ejemplo 2 Conversion explicita
num_string = '12'
num_integer = 13

print("Tipo de Dato de num_string antes del Type Casting", type(num_string))

# conversion de tipo explicita
num_string = int(num_string)

print("Tipo de Dato de num_string despues del Type Casting", type(num_string))

num_sum = num_integer + num_string

print("Suma: ", num_sum)
print("Data Type de num_sum: ", type(num_sum))
