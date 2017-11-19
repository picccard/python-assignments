"""

	Title:	textAnalysis.py 
	Date:	05.11.2017
	Author:	Eskil Uhlving Larsen
	Notes:  Had some problems with special characters.
	        Had some problems with (print) in windows console
	        Needs python3.6 to run in windows console, because of PEP528, PEP529.
		When implementing sorting, the JSON formatter I used in chrome un-sorted the JSON. When i looked at the raw json it was all sorted.


	Usage: assignment-8.py data_file -w/-l
	-w: get word result, -l: get letter result, needs min and max 1 of the flags
	-o SOME_FILE_NAME.json, this will save the result to a file named SOME_FILE_NAME.json.
		SOME_FILE_NAME will automaticly be given .json ending if not given
		if no filename given or filename not just letters, output.json will be given.
	-s sorts result alfabetically.
	-f toggles off the auto-filtering.
	-q toggles off printing result to console.
	-c makes console print compact


	TODO: add_argument -s --search to search with wikipedia-api and get text-data from article instead of file
		  add_argument -f --file to get text-data from a file
		  make required group(-s | -f)

		  better way to filter out illegal_chars

		  update SOURCES

		  optimize / monitor mem-usage & speed

                  might use s.translate(None, string.punctuation) ? any difference?
"""

import sys
import pprint
import operator
import string
import argparse
import json
from collections import OrderedDict

# illegal_chars = ["–", "‘", "’", "“", "”"]


def file_to_word_array(myFile):
    '''
    Reads a file and returns an array of the words.
    '''
    try:
        # myFile must be ANSI, if use:
        # with open(myFile, 'r', utf-8, encoding='utf-8') as f:
        with open(myFile, 'r') as f:
            # Adds word to array, for each line in f, for each word in line.split()
            # for each line in f, do line.split() on the line and add each word in the line.split()-resault to the array
            return [word.translate(word.maketrans("", "", string.punctuation)).lower() for line in f for word in line.split()]
            # return [word.lower() for line in f for word in line.split()]
    except Exception as e:
        print(e)
        sys.exit(1)


def file_to_letter_array(myFile):
    '''
    Reads a file and returns an array of the letters.
    '''
    try:
        # myFile must be ANSI, if use:
        # with open(myFile, 'r', utf-8, encoding='utf-8') as f:
        with open(myFile, 'r') as f:
            # adds letter to array, for each line in f, for each word in line.lower().split() for each letter in list(word)
            # for line in f, make it lower case and split on every whitespace,
            # make a list of letters from each word and add the letters to the array
            return [letter for line in f for word in line.translate(line.maketrans("", "", string.punctuation)).lower().split() for letter in list(word)]
            # return [letter for line in f for word in line.lower().split() for letter in list(word)]
            # ['?', '.', ',', '-'] all of these char's gets its own index.
            # Could use replace('?', ''), but i dont feel its necessary
            # Should use a regex-expresion to split at any (?.-,!_) non [a-z] char
            # https://stackoverflow.com/a/1059596
    except Exception as e:
        print(e)
        sys.exit(1)


def getAutocompleteDict(word_array):
    '''
    Takes an array of words or letters as an argument.
    Goes through every index and adds every unique element to the dictionary's keys.
    Every key got it's own dictionary.
    For every index, we update the count of the following element in the array.
    '''
    book = {}
    counter = -1  # Starts at -1 and goes to 0 at first loop-through
    for word in word_array:
        counter += 1
        if counter >= len(word_array) - 1:
            break  # this is the last word and got no following word
        if word in book.keys():  # Word already in book
            if word_array[counter + 1] in book[word].keys():  # following word is not new
                book[word][word_array[counter + 1]] += 1  # just update counter
                continue
            book[word][word_array[counter + 1]] = 1  # Word in book, following word is new
            continue
        book[word] = {word_array[counter + 1]: 1}  # New main word

    return book


def getSortedBook(book, do_filter):
    '''
    Sort every key in the dictionary, and sort every keys dict by value(count)
    If do_filter is True, key's whitch is not a digit/word/letter will be removed.
    '''
    sortedBook = OrderedDict()
    for key in iter(sorted(book)):
        if (do_filter) and not (key.isdigit() or key.isalpha()):
            # And key not in illegal_chars:
            break
        sortedBook[key] = OrderedDict()
        # Returns a list of tupels, tupelformat is (followingLetter, count)
        for letter in iter(sorted(book[key].items(), key=operator.itemgetter(1), reverse=True)):
            sortedBook[key][letter[0]] = letter[1]
    return sortedBook


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze some text data ' +
                                     'and create an autocomplete-' +
                                     'dictionary containing words or letters.')
    parser.add_argument('data_file', type=str,
                        help='The data file to read, in txt format.', )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-w', '--words', action='store_true',
                       help='Get word data.')
    group.add_argument('-l', '--letters', action='store_true',
                       help='Get letter data.')
    parser.add_argument('-o', '--output', action='store', type=str,
                        help='Save result to JSON file.')
    parser.add_argument('-s', '--sort', action='store_true',
                        help='Sort the result.')
    parser.add_argument('-f', '--filter', action='store_false',
                        help='Opt out from filtering the result.')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Doesn\'t print the result.')
    parser.add_argument('-c', '--compact', action='store_true',
                        help='Makes the console-output compact.')
    args = parser.parse_args()
    if args.words:
        array_from_text = file_to_word_array(args.data_file)
    elif args.letters:
        array_from_text = file_to_letter_array(args.data_file)

    # Dict with a dict for each letter
    # with a counting dict for each following letter, book_setup.txt for format
    book = getAutocompleteDict(array_from_text)

    if args.sort:
        book = getSortedBook(book, args.filter)

    if not args.quiet:
        pprint.pprint(book, compact=args.compact)

    if args.output:  # Default is None
        if args.output.endswith('.json'):
            with open(args.output, 'w') as output_file:
                output_file.write(json.dumps(book))
        elif args.output.isalpha():
            with open((args.output + '.json'), 'w') as output_file:
                output_file.write(json.dumps(book))
        else:
            with open('output.json', 'w') as output_file:
                output_file.write(json.dumps(book))

# SOURCES NB. not updated
'''
isalpha() or isdigit()    https://stackoverflow.com/a/40097699
Remove non-alpha-numeric  https://stackoverflow.com/a/34294398
'''
