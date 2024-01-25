# Mas Ejemplos de Herencias de clases en Python

# Ej de sobreescritura de metodos
class Animal:
    # atributos y mets de la clase madre
    name = ""

    def eat(self):
        print("I can eat")

# hereda de Animal
class Dog(Animal):
    # sobreescribe metodo eat() 
    def eat(self):
        print("I like to eat bones")

# creando un object de subclase
labrador = Dog()

labrador.eat()

# Ej de  metodo super()
class Animal:
    name = ""

    def eat(self):
        print("I can eat")

# hereda de Animal
class Dog(Animal):
    # sobreescribe metodo eat() 
    def eat(self):
        # llamado de met. eat()  de superclase usando super()
        super().eat()
        print("I like to eat bones")

# creando un object de subclase
labrador = Dog()

labrador.eat()


# Ej de Herencia multiple

class Mammal:
    def mammal_info(self):
        print("Mamimeferos puende dar a luz directamente.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals puede aletear (flap).")

class Bat(Mammal, WingedAnimal):
    pass # Para asignarle los atributos despues

# creando un objecto de clase Bat
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()


# Ej de Herencia Multinivel

class SuperClass:
    # Super class code here

class DerivedClass1(SuperClass):
    # Derived class 1 code here

class DerivedClass2(DerivedClass1):
    # Derived class 2 code here

class SuperClass:
    def super_method(self):
        print("Super Class metodo llamado")

class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 metodo llamado")

class DerivedClass2(DerivedClass1):
    def derived2_method(self):
        print("Derived class 2 metodo llamado")

# creando un objecto de clase DerivedClass2
d2 = DerivedClass2()

d2.super_method()

d2.derived1_method()

d2.derived2_method()

