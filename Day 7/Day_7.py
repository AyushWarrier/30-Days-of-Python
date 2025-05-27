# Day 7: Lists & Tuples

# Creating a List
fruits = ["apple", "banana", "cherry"]
print("My fruits list:", fruits)

# Accessing List Items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying List
fruits.append("mango")        # Add at end
fruits.insert(1, "orange")    # Add at specific index
print("After adding fruits:", fruits)

fruits[0] = "green apple"     # Update
print("After updating:", fruits)

# Removing from List
fruits.remove("banana")       # Remove by value
popped = fruits.pop()         # Remove last
print("After removal:", fruits)
print("Popped item:", popped)

# Looping Through a List
print("Looping through fruits:")
for fruit in fruits:
    print(fruit)

# List Length
print("Number of fruits:", len(fruits))

# Check if Item Exists
if "cherry" in fruits:
    print("Yes, cherry is in the list!")

# List Slicing
print("First two fruits:", fruits[:2])
print("Last two fruits:", fruits[-2:])

# Clear or Delete List
# fruits.clear()       # Uncomment to empty list
# del fruits           # Uncomment to delete entire list

# List Comprehension (Just saw this, looks cool!)
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]
print("Squares:", squared)

# -----------------------------
# Tuples — Immutable Lists
# -----------------------------

# Creating a Tuple
dimensions = (800, 600)
print("Dimensions:", dimensions)

# Accessing Tuple Elements
print("Width:", dimensions[0])
print("Height:", dimensions[1])

# Tuples are Immutable
# dimensions[0] = 1024  #Error!

# Single-item Tuple → needs a comma
single = ("one",)
print("Single-item tuple:", single)

# Looping Through a Tuple
print("Looping through tuple:")
for dim in dimensions:
    print(dim)

'''
Lists:
- Mutable (changeable)
- Created with square brackets []
- Can be modified (add/remove/update items)

Tuples:
- Immutable (unchangeable)
- Created with parentheses ()
- Faster and used when data shouldn't be changed
'''
