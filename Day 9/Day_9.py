# Day 9: Strings & String Manipulation

# ------------------------------------
# String Basics
# ------------------------------------
greeting = "Hello"
name = "Ayush"

# Concatenation
message = greeting + " " + name
print("Concatenated:", message)

# f-strings (Recommended way)
age = 20
intro = f"My name is {name} and I am {age} years old."
print("Using f-string:", intro)

# String Length
print("Length of name:", len(name))

# ------------------------------------
# Common String Methods
# ------------------------------------
sample = "  python is FUN  "

print("Original:", sample)

# Stripping whitespace
print("Stripped:", sample.strip())

# Lowercase & Uppercase
print("Lower:", sample.lower())
print("Upper:", sample.upper())

# Title Case & Capitalize
print("Title Case:", sample.title())
print("Capitalize:", sample.capitalize())

# Replace & Split
print("Replace 'FUN' with 'awesome':", sample.replace("FUN", "awesome"))
print("Split by space:", sample.strip().split(" "))

# Finding substrings
print("Does it start with 'python'? ->", sample.strip().startswith("python"))
print("Index of 'is':", sample.find("is"))  # returns -1 if not found

# ------------------------------------
# String Checks (Very Useful)
# ------------------------------------
test_str = "Python123"

print("Is alphanumeric?", test_str.isalnum())
print("Is alphabetic?", test_str.isalpha())
print("Is digit only?", "1234".isdigit())
print("Is lowercase?", test_str.islower())

# ------------------------------------
# Multi-line Strings
# ------------------------------------
multiline = """This is a
multi-line string in Python."""
print("Multiline:\n", multiline)

# ------------------------------------
