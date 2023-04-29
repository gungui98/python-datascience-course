class TeacherMixin:
    def __init__(self, subject):
        self.subject = subject
    def teach(self):
        print("I am teaching " + str(self.subject))