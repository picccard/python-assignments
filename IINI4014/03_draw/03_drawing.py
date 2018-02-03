"""

	Title:	03_drawing.py
	Date:	13.09.2017
	Author:	Eskil Uhlving Larsen

"""
'''
	Asks the user for a number of points, multiplier and speed.
	Draws a sircle with n number of points on it and lines between some points
'''

import turtle

def createTimesTable(points, multiplier, speed, pen):
	# Allows the user to skip a specific input-value
	if speed == '':
		speed = 0
	if multiplier == '':
		multiplier = 2
	if points == '':
		points = 200
	# Tries to convert the given values to integers
	try:
		points = int(points)
		multiplier = int(multiplier)
		speed = int(speed)
	# If one of the values causes a ValueError all values is set to default. To prevent gibberish
	except ValueError:
		print('Caught an error with some of the given values, all values is set to default')
		print('Press enter to start')
		# If you want to customize just one setting you will also have to customize the others too
		# Is there a way to set default speed if input-value is equal to '' ?
		speed = 0
		points = 200
		multiplier = 2
		input()
	
	# Default values
	pen.speed(speed)
	radius = 300
	degPP = 360 / points
	posXY = [0] * points # pos[xValue][yValue]
	
	# Moves the pen to the starting pos at the bottom of the sircle
	# This should maybe be changed so the start is to the left on the sircle
	pen.penup()
	pen.setpos(0, -radius)
	pen.pendown()
	
	# Draws some of the sircle and puts down a point, continues this all around the sircle
	for i in range(0, points):
		pen.circle(radius, degPP)
		pen.dot(7, 'blue')
		posXY[i] = [pen.xcor(), pen.ycor()]
		print('({}, {})'.format(str(posXY[i][0]), str(posXY[i][1])))	# Prints point to console
	
	# Draws a line between each point acording to the multiplier and number of points
	for i in range(0, points):
		pen.penup()
		pen.goto(posXY[i][0], posXY[i][1])
		pen.pendown()
	
		x = (i * multiplier) % points
		
		pen.goto(posXY[x][0], posXY[x][1])

def Main():
	# User input
	myPoints = input('How many points? ')
	myMulti = input('What multiplier? ')
	print('\nSpeeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning.')
	print('0 is the fastes mode')
	mySpeed = input('\nWhat speed? ')
	
	wd = turtle.Screen()		# Creates the canvas
	pen = turtle.Turtle()		# Creates our 'turtle' aka pen
	createTimesTable(myPoints, myMulti, mySpeed, pen)
	wd.exitonclick()
	
if __name__ == '__main__':
    Main()
