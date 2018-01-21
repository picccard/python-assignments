import sys
import string


def file_to_word_array(myFile):
    '''
    Reads a file and returns an array of the words.
    Tries to remove some of the punctuation
    '''
    try:
        with open(myFile, 'r') as f:
            return [word.translate(word.maketrans("", "", string.punctuation)).lower() for line in f for word in line.split()]
    except Exception as e:
        print(e)
        sys.exit(1)


def countWords(word_array):
    '''
    Takes an array of words as an argument.
    Goes through every index and adds every unique element to the dictionary's keys.
    Every key got it's own dictionary.
    For every index, we update the count of the following element in the array.
    '''
    book = {}
    for word in word_array:
        book.setdefault(word, 0)
        book[word] += 1

    return book
