# Day 23: Matplotlib for Data Visualization

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 7]

plt.plot(x, y, marker='o')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# Bar Chart
students = ['Alice', 'Bob', 'Charlie', 'David']
scores = [85, 90, 75, 88]

plt.bar(students, scores, color='skyblue')
plt.title("Student Scores")
plt.xlabel("Name")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.show()

# Pie Chart
activities = ['Study', 'Sleep', 'Play', 'Others']
hours = [8, 7, 6, 3]

plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)
plt.title("Daily Time Distribution")
plt.axis('equal')  #Equal aspect ratio to make the pie chart circular
plt.show()
