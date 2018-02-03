from Circle import Circle

# Should have imported from Tire class. But keeping it here for educational purposes only
class Tire(Circle):
    'Tires are circles with a corrected perimeter'

    def perimeter(self):
        'Circumference corrected for the rubber'
        return Circle.perimeter(self) * 1.25


t = Tire(22)
print(f'A ture of radius {t.radius}')
print(f'has an inner area of {t.area()}')
print(f'and an odometer corrected perimeter of {t.perimeter()}')
print()
