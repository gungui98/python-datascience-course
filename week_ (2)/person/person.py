class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"
    
class Student(Person):
    course = []
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
    def print_student_id(self):
        print(self.student_id)
    def add_course(self, course):
        self.course.append(course)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} is {self.age} years old and has student id {self.student_id}"
    def get_student_id(self):
        return self.student_id
    def get_name_and_age(self):
        return f"{self.first_name} {self.last_name}, {self.age}"