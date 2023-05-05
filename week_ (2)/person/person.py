class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"

    
class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.courses = []

    def get_name_and_age(self):
        return f"{self.first_name} {self.last_name}, {self.age}"

    def get_student_id(self):
        return self.student_id
    
    def print_student_id(self):
        return f"{self.student_id}"

    def add_course(self, course):
        self.courses.append(course)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old and has student id {self.student_id}"