from person import Person
class Student(Person):
    def __init__(self,first_name,last_name,age,student_id):
        super().__init__(first_name,last_name,age)
        self.student_id = student_id
    def __str__(self):
        return super().__str__() + ' and has student id ' + str(self.student_id)
    def get_student_id(self):
        return self.student_id