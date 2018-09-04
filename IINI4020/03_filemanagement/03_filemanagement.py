"""

	Title:	03_filemanagement.py
	Date:	04.09.2018
	Author:	Eskil Uhlving Larsen

"""

import os
import sys
def clear():
    os.system('cls' if os.name=='nt' else 'clear')


# Task 1
'''
Write to file
'''
try:
    with open("file_from_task1.txt", 'w') as f:
        f.write('Hallo\nSkriver en linje til\nHer kommer enda en linje')
except Exception as e:
    print(e)
    sys.exit(1)

'''
Read from file
'''
try:
    with open("file_from_task1.txt", 'r') as f:
        for i, line in enumerate(f):
            # Makes sure you dont read mye than you need.
            # Doesn't read all text and hugs up more ram than needed.
            if i == 1:
                print(f'Line {i+1}: {line}')
                break
except Exception as e:
    print(e)
    sys.exit(1)


'''
Read first 10 letters and print them.
'''
try:
    with open("file_from_task1.txt", 'r') as f:
        chars_left = 10
        for i, line in enumerate(f):
            for char in line:
                if (chars_left > 0 and char.isalpha()):
                    print(char + " ")
                    chars_left -= 1
                else:
                    break
            # We must also stop reading the lines
            if (chars_left <= 0):
                break
except Exception as e:
    print(e)
    sys.exit(1)

input('Enter to coninue')
clear()

# Task 2
'''
Reads the number of lines and words in a file
'''
def fileStat(filename):
    with open(filename, 'r', encoding="utf8") as f:
        total_lines = 0
        total_words = 0
        for line in f:
        # for i, line in enumerate(f):
            total_lines += 1
            total_words += len(line.split())
        return (filename, total_words, total_lines)

'''
Prints the number of lines and words of all files in a directory
'''
def printFileStat(directory='.'):
    print("File\t\t\tWords\tLines")
    print("_______________________________________")

    for root, dirs, files in os.walk(directory):
        # to delete print(root, dirs, files)
        for file in files:
            stats = fileStat(file)
            print("{}\t{}\t{}".format(stats[0], stats[1], stats[2]))

        break # Only want to walk through top level
printFileStat()

input('Enter to coninue')
clear()

# Task 3
'''
Counts the nr of bytes inside a file
'''
def countContentBytes(filename):
    with open(filename, 'r', encoding="utf8") as f:
        bytes = 0
        for line in f:
            bytes += len(line) # Whitespace is also counted
        return bytes
nrOfBytes = countContentBytes('file_from_task1.txt')
print(nrOfBytes)
