class TeacherMixin:
    def __init__(self, subject) -> None:
        self.subject = subject
    
    def teach(self):
        print("I am teaching %s" %(self.subject))