#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of {} is {} "
str2 = " "
if number < 0:
    number = -number
    last = number % 10
    number = -number
    last = -last
else:
    last = number % 10
if last == 0:
    str2 = "and is 0"
elif last > 5:
    str2 = "and is greater than 5"
else:
    str2 = "and is less than 6 and not 0"
print(str1.format(number, last) + str2)
