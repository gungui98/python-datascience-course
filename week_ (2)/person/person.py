class Person:
    def __init__(self, first_name:str, last_name:str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self):
        return (self.get_full_name()+' is '+ str(self.age)+ " years old")
    def get_full_name(self):
        return(str(self.first_name)+' '+str(self.last_name))
