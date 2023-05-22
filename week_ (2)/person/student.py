from .person import Person
class Student(Person):
    def __init__(self, first_name:str, last_name:str, age:int, student_id):
        self.student_id= student_id
        Person.__init__(self, first_name, last_name, age)
        pass
    def print_student_id(self):
        print(self.student_id)
        
    def __str__(self):
        return(Person.__str__(self)+" and has student id "+ str(self.student_id))
    
    def get_student_id(self):
        return int(self.student_id)
