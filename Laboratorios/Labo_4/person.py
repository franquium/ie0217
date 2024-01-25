class Person:
    # Metodo para iniciliar o "construir" la clase
    def __init__(self, name, age):
        self.name  = name
        self.age = age
    
    # Metodo para Mostrar info de la clase Person
    def display_info(self):
        print(f"Name: {self.name} \nAge: {self.age}")
