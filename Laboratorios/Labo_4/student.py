from person import Person

class Student(Person):
    def __init__(self, name, age, student_id):
        # Para "instanciar" el constructor de la clase base
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    # Metodo para matricular curso
    def enroll_course(self, course):
        self.courses.append(course)

    # Metodo para Mostrar info de la clase Student
    def display_info(self):
        super().display_info()      # \ para multiples lineas
        print(f"Student ID: {self.student_id} \
               \nCourses: {', '.join(self.courses)}")

