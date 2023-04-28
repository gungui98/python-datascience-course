class StudentMixin:
    def __init__(self, school):
        self.school = school
    def study(self):
        print("I am studying at " + str(self.school))