class Person():
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def get_full_name(self):
        return (f"{self.first_name} {self.last_name}")
    
    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name} is {self.age} years old")

class Student(Person):
    courses = []
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
    def print_student_id(self):
        print(self.student_id)
    def get_student_id(self):
        return self.student_id
    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name} is {self.age} years old and has student id {self.student_id}")
    def add_course(self, course):
        self.courses.append(course)

student = Student(first_name = "John", last_name = "Doe", age = 35, student_id = 12345)
student.print_student_id()
print(student)
assert student.__str__() == "John Doe is 35 years old and has student id 12345"
assert student.get_student_id() == 12345
assert student.get_full_name() == "John Doe"