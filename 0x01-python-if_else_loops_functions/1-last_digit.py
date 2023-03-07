#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number > 0):
    result = number % 10
elif (number < 0):
   result = (number % 10) - 10
else:
    result = 0
if (result == -10):
    result == 0
print("The last digit of", number, "is", result, "and is", end = " ")
if ((result) > 5):
    print("greater than 5")
elif ((result) == 0):
    print("0")
elif ((result) < 6 and (not (result) == 0)):
    print("less than 6 and not 0")
