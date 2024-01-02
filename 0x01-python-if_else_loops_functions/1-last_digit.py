#!/usr/bin/python3
import random

def last_digit_analysis(num):
    last_digit = int(str(num)[-1])
    output = "The string Last digit of, followed by " + str(num) + " is " + str(last_digit)

    if last_digit > 5:
        output += " and is greater than 5"
    elif last_digit == 0:
        output += " and is 0"
    else:
        output += " and is less than 6 and not 0"

    return output

number = random.randint(-10000, 10000)
print(last_digit_analysis(number))
