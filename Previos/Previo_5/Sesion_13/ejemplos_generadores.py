# Ejm 1

def my_generator(n):
    # inicializa contador
    value = 0
    
    # loop hasta que contador menor que n
    while value < n:
        # produce los valores actuales del contador
        yield value

        # NOTA: La palabra clave yield se usa para producir un 
        # valor del generador y pausar la ejecucion de la func 
        # del generador hasta que se solicite el siguiente valor.
        
        # incrementa el contador
        value += 1

# itera sobre el objeto generador producido por my_generator
for value in my_generator(3):
    # imprime cada valor producido por generador
    print(value)


# Ejm 2

# creando el objeto generador
squares_generator = (i * i for i in range(5))

# iterando sobr el generdor e imprimiendo valores
for i in squares_generator:
    print(i)

# Ejm 3
    
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))


