class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("僕の名前は{0}です。僕は{1}年です".format(self.name, self.age))

class StudentMixin():
    def __init__(self, school):
        self.school = school

    def study(self):
        print("{0}は勉強しています。".format(self.school))

class TeacherMixin():
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        print("{0}を教えています。".format(self.subject))

"""
class Student(Person, StudentMixin):
    def __init__(self, name, age, school):
        Person.__init__(self, name, age)
        StudentMixin.__init__(self, school)

class Teacher(Person, TeacherMixin):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        StudentMixin.__init__(self, subject)
        
student = Student("Alice", 20, "Example University")
student.introduce()
student.study()
"""
