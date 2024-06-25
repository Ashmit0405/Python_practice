def appl(fx,value):
    return 234+fx(value)


cube=lambda x: x**4
# print(cube(3))

print(appl(cube,3))