# Ejms de interadores

# Ejm 1

# definiendo una lista
my_list = [4, 7, 0]

# creando un iterador de la lista
iterator = iter(my_list)

# agrrando el 1er elemento del iterador
print(next(iterator))  # imprime 4

# agrrando el 2do elemento del iterador
print(next(iterator))  # imprime 7

# agrrando el 3ro elemento del iterador
print(next(iterator))  # imprime 0


# Ejm 2

# definiendo una lista
my_list = [4, 7, 0]

for element in my_list:
    print(element)


# Ejm 3 de interadores personalidados

class PowTwo:
    """Clase para implementar un iterador de potencias de dos"""

    # Constructor de la clase
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# Ejm 4 de interadores personalidados
# creando un objecto
numbers = PowTwo(3)

# creando un iterable del objecto
i = iter(numbers)

# Usando next para obtener el siguiente elemento iterador
print(next(i))  # imprime 1
print(next(i))  # imprime 2
print(next(i))  # imprime 4
print(next(i))  # imprimes 8
print(next(i))  # levante excepcion StopIteration

