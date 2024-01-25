# Ejem: Sobrecarga de Operadores

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)

p2 = Point(2, 3)

print(p1+p2)


# Ejem: Sobrecarga de Operadores de comparacion

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # sobrecarga < operador 
    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 20)
p2 = Person("Bob", 30)

print(p1 < p2)  # imprime True
print(p2 < p1)  