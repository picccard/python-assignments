"""

	Title:	01_var_print.py
	Date:	31.08.2017
	Author:	Eskil Uhlving Larsen

"""

# As a convention I find it helpful to use """ for docstrings
# and ''' for block comments.
# In this manner you can wrap ''' around your usual docstrings without conflict.

def converting():
    print('Choose integers.')
    varA = input('What does the first variable contain? ')
    varB = input('What does the second variable contain? ')

    varC = varA + varB
    print(varC)                     # This should print the the two integers as a joined string
                                    # Because the input-function returns a string

    varC = int(varA) + int(varB)
    print(varC)                     # Here the variables have been converted to integers
                                    # The third variable will also be a integer

    # print(varA*varB);             # This gives a TypeError because two strings cant be mutliplied
    print(int(varA) * int(varB))    # This converts both to integers and multiples them

    print(varA*int(varB))           # This is a much loved consept in python.
                                    # A string mutliplyed n times will repeat the string n times



def seperation():
    # Prints each word with X as seperation (sep='X')
    print('Have','a','nice','day',sep='')
    print('Have','a','nice','day',sep=' ')
    print('Have','a','nice','day',sep='->')
    print('Have','a','nice','day',sep='\t')
    print('Have','a','nice','day',sep='\n')
    print('Have','a','nice','day',sep='\n\n\n\n\n\n')


def moreFormat():
    # https://pyformat.info/
    print('{:^10}'.format('cent'))
    print('{:*<10}'.format('star'))
    print('{:>10}'.format('right'))
    print('{:10}'.format('left'))
    print('{:*^10}'.format('test'))


# https://goo.gl/5f43Gp
# The formula is (x*y)%5
'''
  0 1 2 3 4
0 0 0 0 0 0
1 0 1 2 3 4
2 0 2 4 1 3
3 0 3 1 4 2
4 0 4 3 2 1
'''
def multi5mod():
    print("{} {} {} {} {} {}".format(" ", "0", "1", "2", "3", "4"))
    for x in range(0, 5):
        line = ""
        for y in range(0, 5):
            line += str((x*y)%5) + " "
        print(str(x) + " " + line)

# The formula is (x*y)%6
'''
  0 1 2 3 4 5
0 0 0 0 0 0 0
1 0 1 2 3 4 5
2 0 2 4 0 2 4
3 0 3 0 3 0 3
4 0 4 2 0 4 2
5 0 5 4 3 2 1
'''
def multi6mod():
    print("{} {} {} {} {} {} {}".format(" ", "0", "1", "2", "3", "4", "5"))
    for x in range(0, 6):
        line = ""
        for y in range(0, 6):
            line += str((x*y)%6) + " "
        print(str(x) + " " + line)

def Main():
	converting()
	seperation()
	moreFormat()
	multi5mod()
	multi6mod()

if __name__ == "__main__":
	Main()
	input("Press enter to exit") # Pauses
