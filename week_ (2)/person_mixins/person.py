class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("My name is " + str(self.name) + " and I am " + str(self.age) + " years old")