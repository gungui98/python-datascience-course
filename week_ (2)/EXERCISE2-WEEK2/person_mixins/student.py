from person import Person
from studentmixin import StudentMixin
class Student(Person, StudentMixin):
    def __init__(self, name, age, school):
        Person.__init__(self, name, age)
        StudentMixin.__init__(self, school)
