"""

	Title:	02_anagram_solution2.py
	Date:	04.09.2017
	Author:	Eskil Uhlving Larsen

"""
import copy

def sortByKey(some_dict):
    return sorted(some_dict.items(), key = lambda t: t[0])


def runTest():
    if __name__ == '__main__':
        import timeit
        myWord = 'ABBA'
        yourWord = 'SAS'
        print(timeit.timeit("isAnagram('{}', '{}')".format(myWord, yourWord), setup="from __main__ import isAnagram", number=100000))
        print(timeit.timeit("getDiff('{}', '{}')".format(myWord, yourWord), setup="from __main__ import getDiff", number=100000))
        print(timeit.timeit("getDiffString('{}', '{}')".format(myWord, yourWord), setup="from __main__ import getDiffString", number=100))


def wordToCharDict(word):
    # Counting instances of each char in word
    word_count = {}
    for char in word.lower():  # ignore case
        word_count.setdefault(char, 0)
        word_count[char] = word_count[char] + 1
    return word_count


def isAnagram(word1, word2):
    # Dict with counted instances of a char
    word1_dict = wordToCharDict(word1)
    word2_dict = wordToCharDict(word2)

    # Checks for the actual anagram
    return word1_dict == word2_dict


def getDiff(word1, word2):
    #Create a dict to store differences
    diff = {}
    word1_dict = wordToCharDict(word1)
    word2_dict = wordToCharDict(word2)

    # Add all char from word1 to diff
    for char in word1_dict.keys():
        if not char in diff:
            diff[char] = word1_dict[char]
    # Add chars not in diff to diff
    # If char is in diff, subtract and get abs
    for char in word2_dict.keys():
        if not char in diff:
            diff[char] = word2_dict[char]
        else:
            diff[char] = abs(diff[char] - word2_dict[char])


    # Cleaning the dict for 0 values
    for key in list(diff.keys()):   # wraping in list() to make a copy of the list, we can now change the org list
        if diff[key] == 0:
            diff.pop(key)
    return diff


def getDiffString(word1, word2):
    # We make a dict from the word,
    # and makes a copy wich we can remove items from.
    # This way our copy shall only containt items not in the other word
    word1_dict_org = wordToCharDict(word1)
    word1_diff = copy.deepcopy(word1_dict_org)
    word2_dict_org = wordToCharDict(word2)
    word2_diff = copy.deepcopy(word2_dict_org)

    # Just in word1:
    for char in word2_dict_org.keys():
        if char in word1_diff.keys():
            the_sum = word1_diff[char] - word2_dict_org[char]
            if the_sum > 0:
                word1_diff[char] = the_sum
            else:
                word1_diff.pop(char) # Removes the char if the other word got more or the same amount

    # Just in word2
    for char in word1_dict_org.keys():
        if char in word2_diff.keys():
            the_sum = word2_diff[char] - word1_dict_org[char]
            if the_sum > 0:
                word2_diff[char] = the_sum
            else:
                word2_diff.pop(char) # Removes the char if the other word got more of the same amount

    return 'Just in A: {}\nJust in B: {}'.format(word1_diff, word2_diff)


    
if __name__ == '__main__':
    myWord = 'ABBA'
    yourWord = 'SAS'
    print('Result of anagram: {}\n'.format(isAnagram(myWord, yourWord)))
    print('Get diff: {}\n'.format(getDiff(myWord, yourWord)))
    print('DiffString:\n{}'.format(getDiffString(myWord, yourWord)))
