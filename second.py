# def square(n):
#     '''squares a number and returns the output'''
#     return n*n

# def fib(n):
#     if n==1 or n==0:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)

# print(fib(6))

s={1,2,3,"Naman",1,19.0}#set prints no repeated elements
print(s)
print(type(s))
k={}
print(k)
print(type(k))
em=set()
print(em)
print(type(em))

# for i in s:
#     print(i)    #to print elements in the sets

s1={1,2,4,5}
s2={2,4,7,8}
print(s1.union(s2))#to find union of two sets
print(s1)
s2.update(s1)#used to update the union set in either of the two sets
print(s2)

if 2 in s2:
    print("2 is present.")
else:
    print("2 is not present.")

