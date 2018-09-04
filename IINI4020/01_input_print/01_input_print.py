"""

	Title:	01_input_print.py
	Date:	02.02.2018
	Author:	Eskil Uhlving Larsen

"""

# As a convention I find it helpful to use """ for docstrings
# and ''' for block comments.
# In this manner you can wrap ''' around your usual docstrings without conflict.


# Task 1
print('Hello World!')
print('Hello Eskil')
name = input('What is your name? ')
# python3.1
print('Hello {}'.format(name))
# The new f-string in python3.6
print(f'Hello {name}')


# Task 2
sumA = 1 + 3 * 3
sumB = 1 + (5 * 3)
sumC = (1 + 4) * 3
import math
radius = 8
#  PI * r ** 2
# float()
sumD_area = math.pi * (radius ** 2)
# 2 * PI * r
sumD_circumference = 2 * math.pi * radius

print('A: {}'.format(sumA))
print('B: {}'.format(sumB))
print('C: {}'.format(sumC))
print('Area: {}'.format(round(sumD_area, 2)))
print('Circumference: {}'.format(round(sumD_circumference, 2)))


# Task 3
number1 = float(input('Number1: '))
number2 = float(input('Number2: '))
print('{0} + {1} = {2}'.format(number1, number2, (number1 + number2)))
