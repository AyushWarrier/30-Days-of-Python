# Day 8: Dictionaries & Sets

# -----------------------------
# Dictionaries
# -----------------------------

# Creating a Dictionary
student = {
    "name": "Ayush",
    "age": 20,
    "course": "Python",
    "is_enrolled": True
}
print("Student Dictionary:", student)

# Accessing Values
print("Name:", student["name"])
print("Age:", student.get("age"))  # get() avoids errors if key doesn't exist

# Adding or Updating Values
student["grade"] = "A"
student["age"] = 21
print("Updated Student Dictionary:", student)

# Removing Items
student.pop("course")        # Removes by key
print("After removing 'course':", student)

# Looping Through Dictionary
print("All key-value pairs:")
for key, value in student.items():
    print(key, ":", value)

# Checking for Key
if "name" in student:
    print("Yes, 'name' exists in the dictionary.")

# 📏 Length of Dictionary
print("Total keys:", len(student))

# Clearing Dictionary
# student.clear()  # Uncomment to empty the dictionary

# -----------------------------
# Sets
# -----------------------------

# Creating a Set
unique_numbers = {1, 2, 3, 4, 4, 5, 5}
print("Unique numbers set:", unique_numbers)  # duplicates removed automatically

# Adding Items
unique_numbers.add(6)
print("After adding 6:", unique_numbers)

# Removing Items
unique_numbers.remove(3)  # Will give error if item not found
unique_numbers.discard(10)  # Safer, doesn't give error
print("After removals:", unique_numbers)

# Looping Through a Set
print("Looping through set:")
for num in unique_numbers:
    print(num)

# Set Operations
odds = {1, 3, 5, 7}
evens = {2, 4, 6, 8}
print("Union:", odds.union(evens))
print("Intersection:", odds.intersection({1, 2, 3}))
print("Difference:", odds.difference(evens))
