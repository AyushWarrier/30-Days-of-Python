# Day 4: Conditional Statements

# Simple if Statement
print("Simple if Statement:")
x = 10
if x > 5:
    print("x is greater than 5")  # This will run

# if-else Statement
print("\nif-else Statement:")
age = 17
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else Ladder
print("\nif-elif-else Ladder:")
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# Nested if
print("\nNested if:")
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")

# Boolean Variables in Conditions
print("\nBoolean Variables in Conditions:")
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")

# Short-Hand if and if-else
print("\nShort-Hand:")
x = 5
y = 10
if x < y: print("x is less than y")  # One-line if

# One-line if-else
print("Even" if x % 2 == 0 else "Odd")
