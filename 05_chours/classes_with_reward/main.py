"""

	Title:	main.py
	Date:	30.09.2017
	Author:	Eskil Uhlving Larsen

"""
'''
    Uses the person and task classes.
    Got a list with tasks to be done.
    Can add new tasks to this list.
    Can add persons. A person can take task from the list and mark it as done.
    The person with the lowest score can be alerted. 
'''
# sys.maxsize
# https://stackoverflow.com/questions/13795758/what-is-sys-maxint-in-python-3

# Imports classes and modules from other files
from person import Person
from task import Task
import sys
MAX_INT = sys.maxsize

# Adds some default tasks for anybody to complete
taskList = [
    Task('wash', 4),
    Task('cook', 2),
    Task('shop')
]

# Empty array for all users in the program
userList = []


def addTask(desc, reward):
    # Creates a task and adds it to the list with uncomplete tasks
    taskList.append(Task(desc, reward))
    return True


def completeTask(user, taskDesc):
    # Checks if there exists a task with spesified taskDesc
    for task in taskList:
        if task.desc == taskDesc.lower():
            # If it exists, add it to the users done-tasks
            # and remove it from uncomplete tasks
            user.doTask(task)
            taskList.remove(task)
            return True
    # Task was not found, returning false
    return False


def addUser(name):
    # Create a person instance
    # and add it to the list over active users
    tempPerson = Person(name)
    userList.append(tempPerson)
    # Return the person object
    return tempPerson


def getLoser():
    # Creates some temporary valiables
    currentLoser = None
    userScores = []
    loserScore = MAX_INT
    # Checks every user and adds their score the the userScores-list
    # if they got the lowest score
    # they gets assigned as the currentLoser
    for user in userList:
        userScores.append(user.getScore())
        if user.getScore() < loserScore:
            currentLoser = user
            loserScore = currentLoser.getScore()
    # If there are multiple instances of the lowest score,
    # there aint a uniqe looser, we return None
    if userScores.count(min(userScores)) > 1:
        return None
    return currentLoser


def alertLoser():
    # If getLoser returns an object, we print out info about the loser
    # If we get no object, there isn't a uniqe loser or lowScore
    loser = getLoser()
    if loser:
        print('{} is loosing with just {} points'
              .format(loser.name, loser.getScore()))
        return None
    print('Can\'t get loser, two or more users' +
          ' are sharing last place')


def endChallenge():
    pass


def main():
    emma = addUser('Emma')
    john = addUser('John')
    print(addTask('clean', 3))
    print(completeTask(emma, 'Wash'))
    print(completeTask(john, 'cook'))
    print(completeTask(john, 'clean'))
    print(completeTask(emma, 'nothing'))

    alertLoser()


main()


# class Challenge:
#     player1 = None
#     player2 = None
#     taskList = None
#     pass
#
# Challenge.completeTask(player1, 'wash')
