"""

	Title:	02_anagram_solution1.py
	Date:	04.09.2017
	Author:	Eskil Uhlving Larsen

"""
def rmWhiteSpace(s):
	return ''.join(s.split())

def isAnagram(list1, list2):
	list1.sort()
	list2.sort()
	# The sort() functions is usually O(n log n)
	if (list1 == list2):
		return True

def getDifference(list1, list2):
	# Converts the lists to sets
	# Sets can't contain duplicates and doesn't care about order
	# e.g. if we compare "abba" and "sas" uniqeChar will only contain {'b', 's'}

	# Speed: (I asume using sets gives the best performance)
	# https://wiki.python.org/moin/TimeComplexity
	# https://stackoverflow.com/questions/3462143/get-difference-between-two-lists
	
	s1_set = set(list1)
	s2_set = set(list2)

	# Usage:
	# https://www.programiz.com/python-programming/methods/set/symmetric_difference
	uniqeChar = s1_set.symmetric_difference(s2_set)
	return uniqeChar

def getDifference2(list1, list2):
	# Bulids an array with non-matching chars
	# If we compare "abba" and "sas", we get duplicates and notMatch will contain ['b', 'b', 's', 's']
	notMatch = []
	for i in range(0, (len(list1))):
		if list1[i] not in list2:
			notMatch.append(list1[i])
	for i in range(0, (len(list2))):
		if list2[i] not in list1:
			notMatch.append(list2[i])
	return notMatch

def Main():
	# Asks user for input and makes the string lowercase
	# Removes any whitespace and converts string to a list of char
	s1 = list(rmWhiteSpace(input("String: ").lower()))
	s2 = list(rmWhiteSpace(input("String: ").lower()))

	

	if isAnagram(s1, s2):
		print("\nFound anagram")
		input("") # Pauses before quiting
		exit()

	print('\n')
	print('Non-matching using sets: ' + str(getDifference(s1, s2)))
	print('Non-matching using lists: ' + str(getDifference2(s1, s2)))


	input("") # Pauses before quiting

if __name__ == '__main__':
	Main()
