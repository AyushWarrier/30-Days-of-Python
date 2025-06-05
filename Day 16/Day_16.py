# Day 16: Decorators & Generators

# --- Decorators ---

'''
A decorator is just a function that takes another function as input, adds some extra behavior, and returns a new function.
'''

# Basic decorator example
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

say_hello()

'''
Here, `say_hello()` is wrapped by `my_decorator`. 
When I call `say_hello()`, it actually calls the `wrapper()` function.
'''

# Decorator with arguments
def greet_decorator(func):
    def wrapper(name):
        print("Getting ready to greet...")
        func(name)
        print("Finished greeting!\n")
    return wrapper

@greet_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Ayush")
greet("World")

# --- Generators ---

'''
A generator is a function that returns an iterator using the `yield` keyword.
Unlike regular functions that return a value and exit, generators maintain their state.
'''

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
for number in countdown(5):
    print(number)

'''
This doesn't store all values in memory like a list. It yields them one by one — (super efficient)
'''

# Generator expression (similar to list comprehension)
squares = (x**2 for x in range(5))

for s in squares:
    print(f"Square: {s}")

''' 
Generators are great when working with large datasets or infinite sequences.
'''
