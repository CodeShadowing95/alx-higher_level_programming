#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    nbr = -1 * number
    nbr = -1 * (nbr % 10)
else:
    nbr = number % 10

if nbr > 5:
    print(f"Last digit of {number:d} is {nbr:d} and is greater than 5")
if nbr == 0:
    print(f"Last digit of {number:d} is {nbr:d} and is 0")
if nbr < 6 and nbr != 0:
    print(f"Last digit of {number:d} is {nbr:d} and is less than 6 and not 0")
