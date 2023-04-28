from person.person import Person
class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def print_student_id(self):
        return self.student_id
    
    def add_course(self,course):
        return
    
    def get_student_id(self):
        return self.student_id
    def __str__(self):
        return f"{self.first_name} {self.last_name}" + f" is {self.age} years old" + " and has student id " + str(self.student_id)
    
        
    