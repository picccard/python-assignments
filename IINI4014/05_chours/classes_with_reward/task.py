"""

	Title:	05_chours_dict_classes.py
	Date:	30.09.2017
	Author:	Eskil Uhlving Larsen

"""
'''
    A task object. A task got a description, status and a reward.
'''
class Task:
    # When we initiate a task
    # we can optionally give it a spesific reward
    # default reward is set to 1
    def __init__(self, desc, reward=1):
        self.desc = desc.lower()
        self.isDone = False
        self.reward = reward

    def __str__(self):
        return '{}: {}'.format(self.desc, self.reward)
