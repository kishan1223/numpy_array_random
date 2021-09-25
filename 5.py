#UFUNC FINDING LCM AND GCD
import numpy as np
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print("LCM of two numbers")
print(x)
print("\n")
print("LCM in arrays")
arr = np.array([3, 6, 9])
x1 = np.lcm.reduce(arr)
print(x1)
print("\n")
print("LCM of all of an array where the array contains all integers from 1 to 10")
arr1 = np.arange(1, 11)
x2 = np.lcm.reduce(arr1)
print(x2)
print("\n")
num1 = 6
num2 = 9
x3 = np.gcd(num1, num2)
print("GCD of two numbers")
print(x3)
print("\n")
print("GCD in arrays")
arr2 = np.array([20, 8, 32, 36, 16])
x4 = np.gcd.reduce(arr2)
print(x4)