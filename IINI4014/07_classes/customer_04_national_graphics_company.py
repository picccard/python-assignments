from Circle import Circle

bbd = 25.1
# c = Circle(bbd_to_radius(bbd))  # awkward to use a converter function, need for alternative constructor
c = Circle.from_bbd(bbd)    # Using the new constructor
print(f'A circle with a bbd of {bbd}')
print(f'has a radius of {c.radius}')
print(f'an area of {c.area()}')
