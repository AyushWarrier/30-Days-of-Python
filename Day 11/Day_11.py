# Day 11: File & Exception Handling

# --- File Handling ---

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is my first file in Python!\n")
    file.write("Writing to files is surprisingly easy.\n")

# Appending to the same file
with open("sample.txt", "a") as file:
    file.write("This line was added later using append mode.\n")

# Reading from a file
print("Reading contents from 'sample.txt':\n")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("Reading line by line:")
with open("sample.txt", "r") as file:
    for line in file:
        print("->", line.strip())

'''
The `with` keyword handles closing the file automatically, so I don't have to call file.close().
'''

# --- Exception Handling ---

print("Now trying exception handling:")

try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("That wasn't a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print(f"Some unexpected error occurred: {e}")
finally:
    print("Try-Except block finished.\n")

'''
The try-except block is useful to catch and handle potential errors during runtime.
Using multiple except blocks lets me handle specific types of exceptions.
The finally block always runs, no matter what.
'''

# Checking if a file exists before reading
import os

filename = "sample.txt"
if os.path.exists(filename):
    print(f"Yes, '{filename}' exists!")
else:
    print(f"File '{filename}' not found.")
