# Ejemplos de closures: funcs anidadas

# Ejm 1
def greet(name):
    # func interna
    def display_name():
        print("Hi", name)

    # llamado func interna
    display_name()

# Llamado func externa
greet("Jon Wick")


# Ejm 2

def greet():
    # variable defina afuera de func interna
    name = "Jon"
    
    # regresa una func anidada anonima
    return lambda: "Hi " + name

# llamado de func externa
message = greet()

# llamado de func interna
print(message())


# Ejm 3

def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# llamado de func externa
odd = calculate()

# llamado de func interna
print(odd())
print(odd())
print(odd())

# llamado de func externa de nuevo
odd2 = calculate()
print(odd2())


# Ejm 4

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplicador de 3
times3 = make_multiplier_of(3)

# Multiplicador de 5
times5 = make_multiplier_of(5)

# Salida: 27
print(times3(9))

# Salida: 15
print(times5(3))

# Salida: 30
print(times5(times3(2)))

