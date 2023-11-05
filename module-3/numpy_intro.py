# Import the NumPy library
import numpy as np

# Create NumPy arrays with different data types and dimensions
arr1 = np.array([1, 2, 3, 4, 5])  # 1D array of integers
arr2 = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])  # 2D array of floats

# Perform array arithmetic operations
result_add = arr1 + arr1  # Addition
result_sub = arr2 - arr2  # Subtraction
result_mul = arr1 * 2      # Multiplication
result_div = arr2 / 2      # Division

# Calculate statistics using NumPy functions
mean = np.mean(arr1)      # Calculate mean
median = np.median(arr2)  # Calculate median
std_dev = np.std(arr1)    # Calculate standard deviation

# Display the results
print("Array 1:", arr1)
print("Array 2:")
print(arr2)

print("\nArray Addition:")
print(result_add)

print("\nArray Subtraction:")
print(result_sub)

print("\nArray Multiplication:")
print(result_mul)

print("\nArray Division:")
print(result_div)

print("\nMean of Array 1:", mean)
print("Median of Array 2:", median)
print("Standard Deviation of Array 1:", std_dev)
