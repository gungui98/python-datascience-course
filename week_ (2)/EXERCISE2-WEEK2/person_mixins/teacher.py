from person import Person
from teachermixin import TeacherMixin
class Teacher(Person, TeacherMixin):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        TeacherMixin.__init__(self, subject)
