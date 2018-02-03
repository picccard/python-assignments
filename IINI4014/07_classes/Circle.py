
"""

	Title:	Circle.py
	Date:	21.10.2017
	Author:	Raymond Hettinger @ PyCon US 2013
	Recreated by: Eskil Uhlving Larsen

"""

''' Circuitous, LLS -
    An Advanced Circle Analytics Company
'''

import math


class Circle:
    'An advanced circle analytic toolkit'

    # flyweight design pattern suppresses
    # the instance dictionary
    __slots__ = ['diameter']
    version = '0.7'

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):   # Convert dotted access to method calls
        'Radius of a circle'
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    def area(self):
        'Perform quadrature on a shape of uniform radius'
        p = self.__perimeter()
        r = p / math.pi / 2
        return math.pi * r ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter  # Local reference: keep a spare copy

    @classmethod        # Alternative constructor
    def from_bbd(cls, bbd):
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)  # Use cls instead of Circle, makes the method usable for subclasses

    @staticmethod       # Attach function to classes
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0


'''
## Summary ##

1.  Inherit from object(), not needed on python3 and onwards.
2.  Instance varibles for information unique to an instance.
3.  Class variables for data shared among all instances.
4.  Regular methods need "self" to operate on instance data.
5.  Class methods implement alternative constructors.
    They need "cls" so they can create subclass instances as well.
6.  Static methods attach functions to classes. They don't need either "self" og "cls".
    Static methods improve discoverability and require context to be specified.
7.  A property() lets getter and setter methods be invoked automatically by attribute access.
    This allows Python classes to freely expose thir instance variables.
8.  The "__slots__" variable implemets the Flyweight Design Pattern by suppressing instance dictionaries.
'''
