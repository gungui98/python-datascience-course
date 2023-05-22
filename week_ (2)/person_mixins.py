#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

class StudentMixin:
    def __init__(self, school):
        self.school = school

    def study(self):
        print(f"I am studying at {self.school}")

class TeacherMixin:
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        print(f"I am teaching {self.subject}")

