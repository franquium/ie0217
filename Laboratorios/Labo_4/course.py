class Course():
    # Metodo para iniciliar o "construir" la clase
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    # Metodo para desplegarr info de la clase
    def display_info(self):
        print(f"Course code: {self.course_code}\
              \nCourse name: {self.course_name}\n")