class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("My name is %s and I am %i years old" %(self.name, self.age))

    