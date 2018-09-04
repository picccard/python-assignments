"""

	Title:	02_math_list_format.py
	Date:	02.02.2018
	Author:	Eskil Uhlving Larsen

"""

# Task 1
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in days:
    print(day)
print('Lenth of {} is: {}'.format(days, len(days)))
days.sort() # Sorts the list
# sorted(days) # This return the list sorted, but doesn't change the orginal list
print('{} is now sorted'.format(days))


# Task 2
import math
squard_pi = math.sqrt(math.pi)
print(round(squard_pi, 3))
print(round(squard_pi, 6))


# Task 2d
print('X    sin(x)  cos(x)')
for x in range(-100, 101, 5): # int(start), int(stop), int(step)
    '''
    Put x/10 instead of x * 0.1
    Some numbers in there will be more precise,
    e.g.
    3*0.1 you get 0.30000000000000004,
    3/10 you get 0.3
    '''
    x /= 100
    sinX = round(math.sin(x), 4)
    cosX = round(math.cos(x), 4)
    print('{}   {}  {}'.format(x, sinX, cosX))


# Task 3
def celciusToFar(deg):
    return round(deg * (9/5) + 32, 2)

celc = int(input('How hot is it? '))
print(celciusToFar(celc))


# Task 4
number1 = float(input('Number1: '))
number2 = float(input('Number2: '))

operations = {
    1: 'add',
    2: 'subtract',
    3: 'multiply',
    4: 'devide'
}
for nr, opt in operations.items():
    print('{}: {}'.format(nr, opt))

while True:
    opt_to_use = input('Chose your operation: ')
    opt_to_use_ok = True
    if opt_to_use == '1' or opt_to_use == operations[1]:
        print(number1 + number2)
    elif opt_to_use == '2' or opt_to_use == operations[2]:
        print(number1 - number2)
    elif opt_to_use == '3' or opt_to_use == operations[3]:
        print(number1 * number2)
    elif opt_to_use == '4' or opt_to_use == operations[4]:
        print(number1 / number2)
    else:
        print('Operation not found, try again.')
        opt_to_use_ok = False
    if opt_to_use_ok:
        break
