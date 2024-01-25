# Ejemplos de alcance o Scope de las variables en Python

# Ej 1
# Declarando variable global
message = 'Ciao'

def greet():
    # declarando variable local
    print('Local', message)

greet()
print('Global', message)

# Ej 2
# func externa
def outer():
    message = 'local'

    # func anidada
    def inner():

        # declarando variable no local
        nonlocal message

        message = 'nonlocal'
        print("inner: ", message)
    
    inner()
    print("outer: ", message)

outer()

# Ej 3 Cambio de var global
c = 1

def add():

    # usando el keyword global
    global c

    # aumentando c por 2
    c = c + 2

    print(c)

add()


# Ej 4

def outer_funct():
    num = 20

    def inner_funct():
        global num
        num = 25

    print("Antes de llamar inner_funct", num)
    inner_funct()
    print("Despues de llamar inner_funct", num)

outer_funct()
print("Afuera de ambas funciones", num)
