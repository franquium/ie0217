# Ejemplos de clases en Python

# Ej clase Bike
class Bike:
    name = ""
    gear = 0

# creando objecto de clase Bike
bike1 = Bike()

# accesando a los atributos y asignandoles nuevos valores
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Nombre: {bike1.name}, Gears: {bike1.gears} ")


# Ejem clase Employee
# definiendo una clase
class Employee:
    # definiendo un atributo
    employee_id = 0

# creando dos objectos de la clase Employee
employee1 = Employee()
employee2 = Employee()

# accediendo attributos usando  objeto employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# accediendo attributos usando  objeto employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")


# Ejem clase Room
# creando una clase
class Room:
    length = 0.0
    breadth = 0.0

    # metodo pa calcular area
    def calculate_area(self):
        print("Area de Cuarto =", self.length * self.breadth)

# creando objecto de la clase Room 
study_room = Room()

# asignando valores para todos los atributos
study_room.length = 42.5
study_room.breadth = 30.8

# accediendo al  metodo dentro de clase
study_room.calculate_area()


# Ejem de clase Point

class Point(object):
    def __new__(cls, *args, **kwargs):
        print("From new")
        print(cls)
        print(args)
        print(kwargs)
        # creando nuestro objecto y regresandolo como salida de la func
        obj = super().__new__(cls)
        return obj

    def __init__(self, x = 0, y = 0):
        print("De init")
        self.x = x
        self.y = y

# Ejem de clase SpPoint

class SpPoint(Point):
    MAX_Inst = 4
    Inst_created = 0

    def __new__(cls, *args, **kwargs):
        if (cls.Inst_created >= cls.MAX_Inst):
            raise ValueError("No se puede crear mas objectos")
        cls.Inst_created += 1
        return super().__new__(cls)


# Ejem de clase Person como muestra de modificadores de Acceso
# OOP: Encapsulation, Access Modifiers

class Person:
    def __init__(self, name, age):
        self.name = name  # publico: sin guion bajo: 
        self.age = age  # publico

class Person:
    def __init__(self, name, age):
        self._name = name  # protected: con un guion bajo: _
        self._age = age  # protected

class Person:
    def __init__(self, name, age):
        self.__name = name  # private: con doble guion bajo: __
        self.__age = age  # private
