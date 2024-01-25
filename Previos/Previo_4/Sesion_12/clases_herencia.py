# Ejemplos de Herencia de Clases en Python

# Ejm 1 clase Animal y Dog
class Animal:
    # atributo y  metodo de la clase madre
    name = ""

    def eat(self):
        print("I can eat")

# hereda de Animal
class Dog(Animal):
    # nuevo metodo en subclase
    def display(self):
        # accede a atributo name de superclase usando self
        print("My name is ", self.name)

# creando un objecto de la subclase
labrador = Dog()

# accede a atributo y metodo de superclase
labrador.name = "Rohu"
labrador.eat()

# llamado a metodo de subclase 
labrador.display()


# Ejm 2 clase Polugon y Triangle
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Ingrese lado "+str(i+1)+": ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Lado", i+1, "es", self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calcular el semiperimetro
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('El area del triangulo es %0.2f' %area)

# creando una instancia de la clase Triangle
t = Triangle()

# Prompting al usr para que ingrese los lados del triangulo
t.inputSides()

# Mostrar los lados del triangulo
t.dispSides()

# Calcular e imprimir  el area del triangulo
t.findArea()

