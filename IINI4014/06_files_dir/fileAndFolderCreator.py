"""

	Title:	fileAndFolderCreator.py
	Date:	11.10.2017
	Author:	Eskil Uhlving Larsen
	Desc:   Creates three folders with a subfolder.
	        Creates a file inside each subfolder. And writes to it.
	        
	        

"""

import os

run = input('Script will create a folder with some subfolders and textfiles.\n' +
            'Are you sure you want to continue? (y/n): ')
if not run == 'y':
    exit()
print()



# Sets our main_path to a random foldername. This asure all we do will only affect the content of this folder.
# This rootFolder and all other files we create will happen in the relative path where the script is run from.
# GOD this is bad london...
main_path = 'rootFolder'



# Foldernames
folder1 = 'folder1'
folder2 = 'folder2'
folder3 = 'folder3'
folders = ['folder1','folder2','folder3']

# Subfoldernames
subfolder1 = 'subfolder1'
subfolder2 = 'subfolder2'
subfolder3 = 'subfolder3'
subfolders = ['subfolder1','subfolder2','subfolder3']


# Creates the folders in a loop instead of one by one
'''
for i in range(0, len(folders)):
    os.makedirs(os.path.join(main_path, folders[i], subfolders[i]), exist_ok=True)

'''

# Creates the folders, if a folder exists, it will not be created again
# The 'exis_ok' parameter accepts a boolean and was introduced in python 3.2
os.makedirs(os.path.join(main_path, folder1, subfolder1), exist_ok=True)
os.makedirs(os.path.join(main_path, folder2, subfolder2), exist_ok=True)
os.makedirs(os.path.join(main_path, folder3, subfolder3), exist_ok=True)


# Make path to each file
subfile1_path = os.path.join(main_path, folder1, subfolder1, 'subfile1.txt')
subfile2_path = os.path.join(main_path, folder2, subfolder2, 'subfile2.txt')
subfile3_path = os.path.join(main_path, folder3, subfolder3, 'subfile3.txt')


# Make a file in currect location and write some lines to it
subfile1 = open(subfile1_path, 'w')
subfile1.write('This is subfile one\n')
subfile1.write('Here is the second line in subfile1\n')
subfile1.write('Subfile1 is ening now.\n')
subfile1.close()


# Using the 'with' structure
with open(subfile2_path, 'w') as sf2:
    sf2.write('This is subfile two\n')
    sf2.write('Here is the second line in subfile2\n')
    sf2.close() # No need to close file, since with opens and closes


subfile3 = open(subfile3_path, 'w')
subfile3.write('This is subfile three\n')
subfile3.write('Here is the second line in subfile3\n')
subfile3.write('This is gonna be subfile3\'s last line.\n')
subfile3.close()


# Reading all files and writing to a single file
# Create/open outputfile in write mode, replacing any old content
outputFile = open('output.txt','w')

# Walk main_path, and handle every file found
for root, dirs, files in os.walk(main_path):
    # Next four lines is for printing out a tree in console
    level = root.replace(main_path, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print('{}{}/'.format(indent, os.path.basename(root)))
    subindent = ' ' * 4 * (level + 1)
    
    for file in files:
        print('{}{}'.format(subindent, file)) # Prints out the file i tree
        # Only read .txt files
        if not file.endswith('txt'):
            break
        
        # Get the folder where file is located
        file_path = os.path.relpath(os.path.join(root, file))
        
        parent = os.path.basename(
            os.path.dirname(
                os.path.realpath(
                    os.path.join(root, file))))

        # print('File found: {}'.format(file_path))

        # Open the file found i read mode
        inputFile = open(os.path.join(root, file), 'r')
        # Write inputfile's filename and parentfolder
        outputFile.write(file_path + ':\n')
        # For each line in inputfile, write line to outputfile
        for line in inputFile:
            outputFile.write(line)
        inputFile.close()

        outputFile.write('\n') # Adds linebreak between files

outputFile.close()

input('\nWrote output.txt, press enter to continue ')


def cleanup():
    # Only import if run, would normally do all import on top
    from shutil import rmtree
    rmtree(main_path, ignore_errors=True)
    os.remove('output.txt')

response = ''
while response != 'y':
    response = input('\nDo you want to clean up? (y/n) ')
cleanup()



# Notes to self below
'''
os.mkdir('dirname')
os.rmdir('dirname')
os.listdir()
os.curdir()
os.rename('oldName', newName)
os.path.exists()
os.path.isdir()
curPath = os.path.realpath(__file__) # The path to where the script is run from
'''


# Two different ways to write path strings:
#main_path_doubble_slash = 'C:\\Users\\Myusername\\Downloads\\somefolder
#main_path = r'C:\Users\Myusername\Downloads\\somefolder



# -----------------------
# This way is for 2.7 ish
# -----------------------
# Tries to create folders in main_path
# Catches any error
# If the error occures because the folder already exists,
# The program will go on as usual
# Any other error will cause a stop
'''
import errno
try:
    #os.mkdir(os.path.join(main_path, folder1))
    os.mkdir(os.path.join(main_path, folder2))
    os.mkdir(os.path.join(main_path, folder3))
    print('Created folder {}, at {}\n\n{}'
        .format(folder1, main_path, os.path.join(main_path, folder1)))
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
'''
