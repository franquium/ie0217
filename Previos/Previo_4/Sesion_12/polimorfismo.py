# Ejm de polimorfismo clase Polygon y otras

class Polygon:
    # metodo para renderizar una figura
    def render(self):
        print("Renderianzado Polygon...")

class Square(Polygon):
    # renderianzado Square
    def render(self):
        print("Renderianzado Square...")

class Circle(Polygon):
    # renderianzado circle
    def render(self):
        print("Renderianzado Circle...")

# creando un objecto de clase Square
s1 = Square()
s1.render()

# ccreando un objecto de clase Circle
c1 = Circle()
c1.render()



# Ejm de clase Shape, Square y Circle

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "Soy una figura bi-dimensional."

    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Cuadrado (Square) tiene cada uno de sus angulos a 90 grados."

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
