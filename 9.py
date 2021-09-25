#NUMPY ARRAY SLICING
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Slice elements from index 1 to index 5")
print(arr[1:5]) 

print("\n")

print("Slice elements from index 4 to the end of the array")
print(arr[4:]) 

print("\n")

print("Slice elements from the beginning to index 4")
print(arr[:4])

print("\n")

#2d array slicing
print("From the second element, slice elements from index 1 to index 4")
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr1[1, 1:4])

print("\n")

print("From both elements, return index 2")
print(arr1[0:2, 2])

print("\n")
print("From both elements, slice index 1 to index 4")
print(arr1[0:2, 1:4])