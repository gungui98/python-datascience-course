
# person/student.py

from person.person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.courses = []
    
    def print_student_id(self):
        print(f"Student ID: {self.student_id}")
    
    def add_course(self, course):
        self.courses.append(course)
        
    def get_student_id(self):
        return self.student_id
