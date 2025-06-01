# Day 12: Modules & Packages

'''
Today I learned how Python modules and packages work. 
This helps in organizing code and reusing functions across different files.
'''

# --- Built-in Modules ---

import math
import random
import datetime

print("Square root of 16:", math.sqrt(16))
print("Random number between 1 and 10:", random.randint(1, 10))
print("Current date and time:", datetime.datetime.now())

'''
Python comes with many built-in modules like math, random, datetime, os, sys, etc. I used random in the Day 10 Mini Project that I built.
'''

# --- Creating a Custom Module ---

'''
I'll try creating my own module.
I'll create a separate file called `my_utils.py` (in the same folder).
Making my own module isn't that difficult. Basically, you define some functions in a file, import them, and directly use them in your own code. The functions can be for different functions that you would like to perform.
'''

# CONTENTS OF my_utils.py (Create this file separately!)
# def greet(name):
#     return f"Hello, {name}!"

# def add(a, b):
#     return a + b

# Now using my custom module here

import my_utils  # Make sure this file exists in the same folder

print(my_utils.greet("Ayush"))
print("3 + 7 =", my_utils.add(3, 7))

# --- Creating a Package ---

# For now, I didn't go deep into creating packages, but these basics helped me understand how larger projects are organized.
