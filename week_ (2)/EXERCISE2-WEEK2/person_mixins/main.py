from person import Person
from student import Student
from teacher import Teacher
from studentmixin import StudentMixin
from teachermixin import TeacherMixin
student = Student("John Doe", 20, "University of Amsterdam")
teacher = Teacher("Jane Smith", 35, "Python")

student.introduce()  # My name is John Doe and I am 20 years old
student.study()      # I am studying at University of Amsterdam

teacher.introduce()  # My name is Jane Smith and I am 35 years old
teacher.teach()      # I am teaching Python
