class StudentMixin:
    def __init__(self, school) -> None:
        self.school = school
    
    def study(self):
        print("I am studying at %s" %(self.school))