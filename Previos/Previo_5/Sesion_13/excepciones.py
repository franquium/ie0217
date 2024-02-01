# Ejemplos de excepciones en Python

# Ejm 1

try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
# Excepcion
except:
    print("Error: Denominador no puede ser 0.")
# Finally siempre se corre
finally:
    print("Este es el bloque finally.")

# Ejm 2
    
try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("Denominador no puede ser 0.")
except IndexError:
    print("Index Out of Bound.")

# Ejm 3
# programa para imprimir el reciproco de numeros pares
try:
    num = int(input("Ingrese un numero: "))
    assert num % 2 == 0
except:
    print("No es un numero par!")
else:
    reciprocal = 1/num
    print(reciprocal)


# Ejm de Excepciones definidas por Usuario
class InvalidAgeException(Exception):
    "Se levanta cuando el valor de entrada es menor a 18"
    pass

# numero a adivinar
number = 18

try:
    input_num = int(input("Ingrese un numero: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible para Votar")
except InvalidAgeException:
    print("Excepcion occurrida: Invalid Age")

# Ejm 
    
class SalaryNotInRangeError(Exception):
    """ Se levanta Excepcion por errores en las entradas de salario.

    Atributos:
        salary -- salario ingresado que causa el error
        message -- explicacion del error
    """

    def __init__(self, salary, message="Salario fuera del rango (5000, 15000)"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

salary = int(input("Ingresa cantidad de salario: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)


