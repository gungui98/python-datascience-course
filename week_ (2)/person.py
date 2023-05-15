#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return (self.first_name + " " + self.last_name)
    def __str__(self):  
        return "{0} is {1} years old".format(self.get_full_name(), self.age)

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def print_student_id(self):
        print(self.get_student_id())

    def __str__(self):
        return Person.__str__(self) + " and has student id " + str(self.get_student_id())

