"""

	Title:	bubbleSort.py
	Date:	22.09.2017
	Author:	Eskil Uhlving Larsen

"""
'''
	myBubbleSort() sorts a single list.
	myBubbleSort2() sorts two lists as if they were one.
	Every index is checked if it's in the list1, if its the last item in list1 of in list2
'''

def myBubbleSort(list1):
	for passnr in range(len(list1)-1, 0, -1):				# Goes throught the list n-1 times,
															# each time the last item is sorted and doesnt need to be checked
		for i in range(passnr):								# For every unsorted item in the list:
			if list1[i] > list1[i+1]:						# Check is the current item and the next should be swapped
				list1[i], list1[i+1] = list1[i+1], list1[i]	# Swaps the two values




				# haha, this is probably the most spagetti i ever made @ 22.09.2017 - 02:09
def myBubbleSort2(list1, list2):
	for passnr in range(len(list1)+len(list2)-1, 0, -1):			# Goes through every index in both lists, each time the last index is sorted and will not be checked the next passnr
		noChanges = True
		for i in range(passnr):
			if i < len(list1)-1:									# if index is lower than the last index in list1
				if list1[i] > list1[i+1]:							# Compare current index to the next index
					list1[i], list1[i+1] = list1[i+1], list1[i]		# Swap the two values
					noChanges = False

			if i == len(list1)-1:									# if index is the last in list1
				if list1[i] > list2[i-len(list1)+1]:				# Compare current index to the first index in list2
					list1[i], list2[i-len(list1)+1] = list2[i-len(list1)+1], list1[i]	# Swap the two values
					noChanges = False

			if i > len(list1)-1:									# if index is inside list2
				if list2[i-len(list1)] > list2[i-len(list1)+1]:		# Compare current index to the first index in list2
					list2[i-len(list1)], list2[i-len(list1)+1] = list2[i-len(list1)+1], list2[i-len(list1)]	# Swap the two values
					noChanges = False

		if noChanges:	# if no swapping done, exit loop
			break


def Main():
	myList = [14, 4, 8, 7, 5]
	myList2 = [15, 2, 1]

	print('Before bubblesort:')
	print(myList)
	print(myList2)

	myBubbleSort2(myList, myList2)
	print('\nAfter bubblesort:')
	print(myList)
	print(myList2)

	input()


if __name__ == '__main__':
	Main()
