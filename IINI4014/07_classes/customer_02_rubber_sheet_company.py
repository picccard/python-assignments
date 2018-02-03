from Circle import Circle

cuts = [0.1, 0.7, 0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
    print(f'A circlet with a radius of {c.radius}')
    print(f'has a perimeter of {c.perimeter()}')
    print(f'and a cold area of {c.area()}')
    c.radius *= 1.1
    print(f'and a warm area of {c.area()}')
    print()
