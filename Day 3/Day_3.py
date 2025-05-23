# Day 3: Operators & Expressions

# Today I'm learning about different types of operators in Python.

# Arithmetic Operators
print("Arithmetic Operators:")
print("10 + 5 =", 10 + 5)   # Addition
print("10 - 5 =", 10 - 5)   # Subtraction
print("10 * 5 =", 10 * 5)   # Multiplication
print("10 / 5 =", 10 / 5)   # Division (float)
print("10 // 3 =", 10 // 3) # Floor Division
print("10 % 3 =", 10 % 3)   # Modulus
print("2 ** 3 =", 2 ** 3)   # Power

# Assignment Operators
print("\nAssignment Operators:")
x = 5
print("x =", x)
x += 3  # Same as x = x + 3
print("x += 3 →", x)
x *= 2  # Same as x = x * 2
print("x *= 2 →", x)

# Comparison Operators
a = 10
b = 20
print("a == b:", a == b)  
print("a != b:", a != b)  
print("a > b:", a > b)    
print("a < b:", a < b)    
print("a >= b:", a >= b)  
print("a <= b:", a <= b)  

# Logical Operators
print("\nLogical Operators:")
is_sunny = True
is_weekend = False
print("is_sunny and is_weekend:", is_sunny and is_weekend)
print("is_sunny or is_weekend:", is_sunny or is_weekend)
print("not is_sunny:", not is_sunny)

# Identity & Membership Operators
print("\nIdentity Operators:")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)      # True (same object)
print("a is c:", a is c)      # False (different objects)
print("a == c:", a == c)      # True (same content)

print("\nMembership Operators:")
print("2 in [1, 2, 3]:", 2 in [1, 2, 3])
print("4 not in [1, 2, 3]:", 4 not in [1, 2, 3])
