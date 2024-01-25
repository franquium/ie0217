from person import Person

class Teacher(Person):
    # Metodo para iniciliar o "construir" la clase
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.courses_taught = []

     # Metodo para asignar un curso
    def assign_course(self, course):
        self.courses_taught.append(course)

     # Metodo para Mostrar info de la clase Teacher
    def display_info(self):
        super().display_info()
        print(f"Employee ID:  {self.employee_id} \
              \nCourses taught: {', '.join(self.courses_taught)}\n")