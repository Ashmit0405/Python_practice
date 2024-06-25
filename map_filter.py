#map function
# def cube(x):
#     return x*x*x

l=[1,2,3,4,5]
m=list(map(lambda x: x*x*x,l))
print(m)
 
#filter function
def compare(a):
    return a>=2

l=[2,3,4,5,6]
m=list(filter(compare,l))
print(m)

#reduce function
from functools import reduce
l=[1,2,3,4,5]
m=reduce(lambda x,y: x + y,l)
print(m)