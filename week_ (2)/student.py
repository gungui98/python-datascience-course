from person import Person
class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        self.student_id = student_id
        Person.__init__(self, first_name, last_name, age)
        
    def __str__(self):
        return self.first_name + " " + self.last_name + " is " + str(self.age) + " years old and has student id " + str(self.student_id)
        
    def print_student_id(self):
        print(self.student_id)
        
    def add_course(self, course):
        pass
    
    def get_student_id(self):
        return self.student_id