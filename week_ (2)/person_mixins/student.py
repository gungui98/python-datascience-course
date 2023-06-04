class StudentMixin:
    def __init__(self, school) -> None:
        self.school = school
    
    def study(self):
        print(f"I am studying at the {self.school}")