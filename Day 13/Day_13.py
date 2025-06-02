# Day 13: Object-Oriented Programming (OOP)

# What is a class?
'''
A class is like a blueprint for creating objects. It defines attributes (variables) and methods (functions).
'''

# Defining a simple class
class Person:
    # Constructor (called when an object is created)
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    # Method
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Creating objects (instances) of the class
person1 = Person("Ayush", 20)
person2 = Person("Rhea", 25)

# Calling methods on objects
person1.introduce()
person2.introduce()

'''
'self' refers to the instance of the class. It allows us to access variables and methods associated with the current object.
'''

# More Concepts: Class vs Instance variables
class Student:
    college = "SICSR"  # class variable (same for all instances)

    def __init__(self, name):
        self.name = name  # instance variable (unique to each instance)

    def display(self):
        print(f"{self.name} studies at {Student.college}")

s1 = Student("Ayush")
s2 = Student("Rhea")
s1.display()
s2.display()
