from person.person import Person
class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.courses = []

    def print_student_id(self):
        print(self.student_id)

    def get_student_id(self):
        return self.student_id

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"{super().__str__()} and has student id {self.student_id}"
