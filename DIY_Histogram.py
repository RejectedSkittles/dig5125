import numpy as np

#Create a 2D array
array_2d = np.array([[1,2,3], [4,5,6]])

# Use ravel to flatten the 2D array to a 1D array
array_1d = array_2d.ravel()

print("Original 2D array: ")
print(array_2d)

print("Flattened 1D array:")
print(array_1d)