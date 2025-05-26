# Day 6: Functions & Scope

# Defining a Simple Function
def greet():
    print("Hello from a function!")

# Calling the Function
greet()

# Function with Parameters
def greet_user(name):
    print("Hi", name)

greet_user("Ayush")
greet_user("Python Learner")

# Function with Return Value
def square(number):
    return number * number

result = square(5)
print("Square of 5 is:", result)

# Function with Multiple Parameters
def add(x, y):
    return x + y

print("Sum of 3 and 4:", add(3, 4))

# Default Parameters
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()
welcome("Ayush")

# Keyword Arguments
def describe_pet(animal, name):
    print(f"{name} is a {animal}.")

describe_pet(animal="dog", name="Tommy")

# Variable Scope
'''
Scope = where a variable exists in the code.

Local Scope → Inside a function  
Global Scope → Outside all functions
'''

# Example of Local Scope
def show_number():
    num = 42  # local variable
    print("Inside function:", num)

show_number()
# print(num)  # This caused an error because num is local

# Example of Global Scope
language = "Python"  # global variable

def print_language():
    print("I’m learning", language)

print_language()

# Modifying Global Variables Inside a Function
count = 0

def increase_count():
    global count
    count += 1

increase_count()
print("Count:", count)

'''
- def is used to define a function.
- return sends a value back from the function.
'''
