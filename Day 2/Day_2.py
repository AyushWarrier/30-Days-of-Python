# Day 2: Variables & Data Types

'''
Today I explored how variables work in Python — they're so easy compared to other languages I've seen.
You don't need to define the type. Python figures it out based on the value you assign.
'''

# String
name = "Ayush"
language = 'Python'
print(name, language)

# Integer and Float
age = 20
height = 6.1
print(age, height)

# Boolean
learning = True
is_cool = False
print(learning, is_cool)

# NoneType
middle_name = None
print(middle_name)

'''
type() function helps check the data type of any variable.
'''

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(learning))    # <class 'bool'>
print(type(middle_name)) # <class 'NoneType'>

# int to float
x = 5
y = float(x)
print(y, type(y))

# float to int (decimal part is dropped)
a = 9.7
b = int(a)
print(b, type(b))

# number to string
num = 100
text = str(num)
print(text, type(text))

# string to int (if string contains a number)
s = "50"
n = int(s)
print(n, type(n))

'''
If you try to convert a non-numeric string to an int, Python will throw an error
'''

# Example:
# bad = int("hello")  # Uncommenting this will crash the code
