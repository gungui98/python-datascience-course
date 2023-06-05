class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self):
        return self.get_full_name() + " is " + str(self.age) + " years old"
    
class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        
    def print_student_id(self):
        print(self.student_id)
    
    def get_student_id(self):
        return self.student_id
    
    def __str__(self):
        return self.get_full_name() + " is " + str(self.age) + " years old and has student id " + str(self.student_id)