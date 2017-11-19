from Circle import Circle
import random

n = 1_000_000   # Python 3.6: visual space in large numbers in source

seed(8675309)
print(f'Using Circuituous(tm) version {Circle.version}')

circles = [Circle(random()) for i in range(n)]  # list comprehension
print(f'The average area of {n} random circles')
avg = sum([c.area() for c in circles]) / n
# f-string with format spec: https://docs.python.org/2/library/string.html#format-specification-mini-language
print(f'is {avg:.1f}')
