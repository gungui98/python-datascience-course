class TeacherMixin:
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        print(f"I am teaching {self.subject}")