# person/person.py

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_name_and_age(self):
        return f"{self.get_full_name()}, {self.age}"
    