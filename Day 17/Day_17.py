# Day 17: Lambda Functions & Comprehensions

# --- Lambda Functions ---

'''
Lambda functions are like one-liners, throwaway functions. They are often used when you need a function temporarily.
Syntax: lambda arguments: expression
'''

# Traditional function
def square(x):
    return x * x

# Lambda equivalent
square_lambda = lambda x: x * x

print(square(5))         # Output: 25
print(square_lambda(5))  # Output: 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7

# Using lambda with `sorted()`
people = [("Ayush", 20), ("Raj", 25), ("Mira", 22)]
# Sort by age
people_sorted = sorted(people, key=lambda x: x[1])
print(people_sorted)

# --- List Comprehensions ---

'''
Instead of writing a loop to build a list, we can use list comprehensions.
Syntax: [expression for item in iterable if condition]
'''

# Traditional way
squares = []
for i in range(5):
    squares.append(i**2)
print(squares)

# List comprehension
squares_comp = [i**2 for i in range(5)]
print(squares_comp)

# Filtering even numbers
evens = [i for i in range(10) if i % 2 == 0]
print(evens)

# --- Set Comprehensions ---

nums = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in nums}
print(unique_squares)

# --- Dictionary Comprehensions ---

names = ["Alice", "Bob", "Charlie"]
lengths = {name: len(name) for name in names}
print(lengths)
