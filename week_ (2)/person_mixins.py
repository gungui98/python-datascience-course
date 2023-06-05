class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} year old "
class StudentMixin:
    def __init__(self,school):
        self.school = school
    def study(self):
        return f"I am studying at the {self.school}"
    
class TeacherMixin:
    def __init__(self,subject):
        self.subject = subject
    def teach(self):
        return f"I am teaching {self.subject}"
    