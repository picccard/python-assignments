"""

	Title:	05_chours_dict_classes.py
	Date:	30.09.2017
	Author:	Eskil Uhlving Larsen

"""
'''
    A person object. A person got a name and a list with tasks that is done.
    A person can do a task. A person can give its score from the done tasks.
'''
class Person:
    def __init__(self, name):
        self.name = name
        self.tasksDone = []

    def doTask(self, task):
        self.tasksDone.append(task)
        task.isDone = True
        return True

    def getScore(self):
        score = 0
        for task in self.tasksDone:
            score += task.reward
        return score

    def __str__(self):
        return '{}: {}'.format(self.name, self.getScore())
