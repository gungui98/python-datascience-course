class StudentMixin:
    def __init__(self, school):
        self.school = school
    
    def study(self) :
        return f"I am studying at the {self.school}"