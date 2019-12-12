#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = 0
str1 = "Last digit of {} is {} "
str2 = " "
if number < 0:
    number2 = -number
mod = number2 % 10
if mod == 0:
    str2 = "and is 0"
elif mod > 5:
    str2 = "and is greater than 5"
elif mod < 6:
    str2 = "and is less than 6 and not 0"
print(str1.format(number, mod) + str2)
