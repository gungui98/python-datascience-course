class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} year{'s' if self.age != 1 else ''} old"
    
    def introduce(self):
        print(f"{self.__str__()}")