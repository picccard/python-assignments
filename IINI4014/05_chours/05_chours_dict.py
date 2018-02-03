"""

	Title:	05_chours_dict.py
	Date:	27.09.2017
	Author:	Eskil Uhlving Larsen

"""

# -------------------- SOURCE -------------------- #

# https://stackoverflow.com/questions/960733/python-creating-a-dictionary-of-lists

# dict.update()
# https://stackoverflow.com/questions/39680317/append-nested-dictionaries

# dict.get(key, 0), 0 is returned if not found
# https://automatetheboringstuff.com/chapter5/

# remove key from dict
# https://stackoverflow.com/questions/5844672/delete-an-item-from-a-dictionary

# split string and code over multiple lines
# https://stackoverflow.com/questions/3346230/wrap-long-lines-in-python

# max(value1, value2...)
# https://stackoverflow.com/questions/3357369/maximum-of-2-numbers

# isinstance(var, type)
# https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
# -------------------- PROGRAM -------------------- #

import pprint

chores = {
    # User: {'Task-desc': rewardedPoints}
    'him': {},
    'her': {},
    'notDone': {}
}

def addChore(task, value):
    # adds new chore to the notDone dict
    # Check parameters
    #if not (isinstance(task, str)) or not isinstance(value, int):
        #print('Error task must be string and value an integer')
        #return None
    if not isinstance(task, str):
        print('task must be str')
        return True
    try:
        chores['notDone'].update({
            task:   value
        })
        print('Added new chore: {},  {}'.format(task, value))
    except TypeError as error:
        print('Noe gikk galt i addChore: {}'.format(error.args))
        return False

def doneChore(user, task):
    # Check parameters
    try:
        # Adds chore and reward to user-dict and removes entry from notDone
        # Get the reward value for the task
        reward = chores['notDone'].get(task, 0)
        # Add the chore to the users dict
        chores[user].update({
            task:   reward
        })
        # Remove chore from notDone
        chores['notDone'].pop(task)
        print(('{} has has done task: {}, and was rewarded {} points')
            .format(user, task, reward))
        checkLooser()   # Prints a msg to the looser (Alerts the user)
        return True
    except (TypeError, KeyError) as error:
        print('Noe gikk galt i doneChore: {}'.format(error.args))
        return False

def printDict(someDict):
    # Help-func: Prints the user and they chores
    for key in someDict.keys():
        print('{}: {}'.format(key, someDict[key]))

def checkPoints(user):
    # Help func: returns the total points user have earned
    myPoints = 0
    for key, value in chores[user].items():
        myPoints += value
    # print('{} got {} points'.format(user, myPoints))
    return myPoints

def checkLooser():
    # Help-func, Returns the user with the least points
    him = checkPoints('him')
    her = checkPoints('her')
    # left = checkPoints('notDone')

    if him != her:
        if min(him, her) == him:
            print('\'Him\' got less points and is loosing!')
            return 'him'
        if min(him, her) == her:
               print('\'Her\' got less points and is loosing!')
               return 'her'
    else:
        # print('Same score')
        return 0

def endChallenge():
    looser = checkLooser()
    print('--------------------------')
    print('CHALLENEGE ENDED')
    print('--------------------------')
    print('\'{}\' recived divorcepapers from partner.'.format(looser))

def Main():
    # Add chores
    addChore('make food', 1)
    addChore('cook', 2)
    addChore('eat', 1)
    addChore('wash clothes', 1)
    addChore('grocery shopping', 3)
    # Complete task
    doneChore('him', 'cook')
    doneChore('her', 'eat')
    doneChore('her', 'make food')
    doneChore('her', 'grocery shopping')
    endChallenge()


    # Validation
    print('-------------------------------')
    addChore(2, 3)
    addChore('wash', 'she')
    doneChore('her', 2)
    doneChore('her', 'wash')
    doneChore('noUser', 2)
    doneChore('noUser', 'taskValue')


# -------------------- TESTING -------------------- #

Main()
input()

# -------------------- TO DO -------------------- #

# What if trying to add task to user not found? exception handling
# What if trying to do task not found?
# What if
# Alternatively set chore-boolean DONE to False at creation and True after completion
# Also removing the nessesary to delete it from the notDone dict

# instead of a reward system, we could count how many times they did the task
# e.g. 'cook': 3 would indicate that cooking had been done 3 times by user


# Alternative assignment for future self:
# make class 'Choure', with: desc,reward,owner,doneBoolean
# make a choure array, choureArray.append(new Choure(args))
