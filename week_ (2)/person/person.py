
class Person:
    def __init__(self, first_name, last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def first_name(self):
        return self.first_name
    
    def last_name(self):
        return self.last_name
   
    def age(self):
        return self.age
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self) :
        return f"{self.first_name} {self.last_name}" + f" is {self.age} years old"
        
