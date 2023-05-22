class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def get_full_name(self):
        return "%s %s" %(self.first_name, self.last_name)
    
    def __str__(self) -> str:
        return "%s %s is %i years old" %(self.first_name, self.last_name, self.age)
    
class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
    
    def get_student_id(self):
        return self.student_id

    def print_student_id(self):
        print(self.student_id)

    def __str__(self) -> str:
        return super().__str__() + " and has student id %s" %(self.student_id)
