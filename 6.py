#RANDOM INTRO USING RANDOM MODULE
from numpy import random
x = random.randint(100)
print("To generate any random integer from 0 to 100")
print(x)
print("\n")
x2=random.randint(100, size=(5))
print("To generate a random array")
print(x2)
print("\n")
x3 = random.randint(100, size=(3, 5))
print("To generate a random 2-D array")
print(x3)
