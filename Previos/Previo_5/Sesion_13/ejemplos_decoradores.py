# Ejmplos de Decoradores

# Ejm 1

def make_pretty(func):
    # define la func interna
    def inner():
        # agrega comportamiento adiciones para decorar func
        print("Me decoraron")
        # regresa func original
        func()
    # regresa func interna
    return inner

# define func ordinary
def ordinary():
    print("Soy ordinary")

# decorar la func ordinary 
decorated_func = make_pretty(ordinary)

# llamado de la func decorada
decorated_func()

# Ejm 2

def make_pretty(func):
    def inner():
        print("Me decoraron")
        func()
    return inner

@make_pretty
def ordinary():
    print("Soy ordinary")

ordinary()


# Ejm 3

def smart_divide(func):
    def inner(a, b):
        print("Voy a dividir", a, "y", b)
        if b == 0:
            print("Opa! No se pueda dividir")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2, 5)

divide(2, 0)


# Ejm 4: Para encadenar decoradores

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("Hello")
