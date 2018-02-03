"""

	Title:	Tire.py
	Date:	21.10.2017
	Author:	Raymond Hettinger @ PyCon US 2013
	Recreated by: Eskil Uhlving Larsen

"""

from Circle import Circle

class Tire(Circle):
    'Tires are circles with a corrected perimeter'

    def perimeter(self):
        'Circumference corrected for the rubber'
        return Circle.perimeter(self) * 1.25
