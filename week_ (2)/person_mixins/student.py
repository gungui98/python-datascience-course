class StudentMixin:
    def __init__(self, school):
        self.school = school

    def study(self):
        print(f"I am studying at {self.school}")
