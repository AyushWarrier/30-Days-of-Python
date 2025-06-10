# Day 21: NumPy Basics

import numpy as np  # NumPy is usually imported as 'np'

# Creating Arrays
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Attributes
print("Shape of arr2:", arr2.shape)
print("Data type of arr1:", arr1.dtype)
print("Size (number of elements) in arr2:", arr2.size)

# Operations
print("Array + 2:", arr1 + 2)
print("Array * 3:", arr1 * 3)
print("Element-wise addition:", arr1 + np.array([10, 20, 30, 40, 50]))

# Functions
print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((3, 2)))
print("Random Numbers:\n", np.random.rand(2, 2))
print("Arange:", np.arange(0, 10, 2))  # Like range() but for arrays
print("Linspace:", np.linspace(0, 1, 5))  # 5 equally spaced numbers from 0 to 1

reshaped = arr2.reshape((3, 2))
print("Reshaped Array:\n", reshaped)

# Stats
data = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Standard Deviation:", np.std(data))
