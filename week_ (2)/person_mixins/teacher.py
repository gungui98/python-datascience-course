class TeacherMixin:
    
    def __init__(self,subject):
        self.subject = subject
        
    def teach(self):
        return f"I am teaching {self.subject} "
    
   

