# Day 5: Loops & Iteration

# The while Loop
print("while Loop:")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Infinite Loop Example (be careful!)
'''
while True:
    print("This will run forever unless there's a break.")
'''

# Using break and continue
print("\nUsing break and continue:")
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  # Skips 5
    if i == 8:
        break  # Stops the loop when i is 8
    print(i)

# The for Loop (much cleaner!)
print("\nfor Loop with range():")
for num in range(1, 6):
    print("Number:", num)

# range(start, stop, step)
print("\nfor Loop with step:")
for num in range(0, 10, 2):
    print(num)

# Looping through a List
print("\nLooping through a List:")
colors = ["red", "green", "blue"]
for color in colors:
    print("Color:", color)

# Looping through a String
print("\nLooping through a String:")
word = "Python"
for char in word:
    print(char)

# Nested Loops
print("\nNested Loops:")
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")

# Using else with Loops
print("\nelse with for loop:")
for n in range(3):
    print("Number:", n)
else:
    print("Loop finished!")
