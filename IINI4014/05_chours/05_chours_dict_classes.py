"""

	Title:	05_chours_dict_classes.py
	Date:	30.09.2017
	Author:	Eskil Uhlving Larsen

"""

class Person:
    def __init__(self, name):
        self.name = name
        self.tasksDone = []

    def doTask(self, taskDesc):
        if len(taskList) == 0:
            print('No tasks left')
            return None
        if not isinstance(taskDesc, str):
            return None
        foundTask = None
        for task in taskList:
            if task.desc == taskDesc.lower():
                foundTask = task
                break
        if not foundTask:
            print('Cound not find task')
            return None
        self.tasksDone.append(foundTask)
        print('{} have done task: {}'.format(self.name, foundTask))
        taskList.remove(foundTask)
        task.isDone = True
        if len(taskList) == 0:
            print('No tasks left to')

    def getPoints(self):
        return len(self.tasksDone)


class Task:
    def __init__(self, desc):
        # Makes sure all Task.desc is non-capitalized
        self.desc = desc.lower()
        self.isDone = False

    def __str__(self):
        return str(self.desc)

class Challenge:
    def __init__(self, player1, player2, taskList):
        self.taskList = taskList

        self.player1 = player1
        self.player2 = player2
        self.taskList.extend([
            Task('Wash'),
            Task('Fold'),
            Task('Shop')])
        
    def addTask(self, taskDesc):
    # Checks if there already is a task with the same desc
        for task in self.taskList:
            if task.desc == taskDesc.lower():
                print('Task already exist')
                return False
        # Creates a new Task in taskList
        self.taskList.append(Task(taskDesc))
        print('Added new task for {}'.format(taskDesc))

    def checkLooser(self):
        pl1 = self.player1.getPoints()
        pl2 = self.player2.getPoints()
        print('{} got {} points\n'.format(self.player1.name, pl1) +
              '{} got {} points'.format(self.player2.name, pl2))
        if pl1 != pl2:
            print('_________________')
            if min(pl1, pl2) == pl1:
                print('{} is loosing!\n'.format(self.player1.name))
                return self.player2.name
            if min(pl1, pl2) == pl2:
                print('{} is loosing!\n'.format(self.player2.name))
                return self.player1.name
        else:
            # print('Same score')
            return 0

# We need to create to Persons to participate in the clallenge
# We need a list of Tasks for us to do
# With Persons and a list of Tasks, we can create a Challenge
# Not elegant, but works 
taskList = []
ole = Person('Ole')
per = Person('Per')

cl = Challenge(ole, per, taskList)

cl.addTask('suppe')
ole.doTask('suppe')
ole.doTask('wash')
ole.doTask('noTask')
ole.doTask('shop')
ole.doTask('fold')
ole.doTask('noTask')
#print(cl.checkLooser())
