# def sum(a,b):
#     return a+b

# c=sum(2,3)
# print("The sum = ",c)

# def name(fname,mid="Kumar",lastname="Singh"):
#     print(fname,mid,lastname)

# name("Chandan")
def average(*num):
    print(type(num))
    sum=0
    for i in num:
        sum=sum+i
   
    return sum/len(num)

# avg=average(2,3,4,5)
# print("Average=",avg)
# marks=[23,46,55,79,34,68,13,90]
# print(marks)
# print(marks[:])
# print(marks[1:5])
l=[11,45,1,2,4,6,1,1]
print(l)
l.append(3)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(1))
m=[44,56,23]
# l.extend(m)
# print(l)
k=l+m
print(k)


# a=100
# b=1000
# # print(a) if a>b else print("Both are equal") if a==b else print(b)
# c=9 if a>b else 0
# print(c)

marks=[1,2,45,78,98,27,76,79]
for index,value in enumerate(marks):#enumerate is used to give the index for the respective value
    print(index,value)


marks=[1,2,45,78,98,27,76,79]
for index,value in enumerate(marks,start=1):#start changes the zero based indexing to whatever value we want
    print(index,value)