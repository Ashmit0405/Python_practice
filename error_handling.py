# def func1():
#     try:
#         l=[1,2,3]
#         i=int(input("Enter a number: "))
#         print(l[i])
#         return 1

#     except:
#         print("Error")
#         return 0
    
#     finally:
#         print("Always executed")


# x=func1()
# print(x)
a=int(input("Enter the number: "))

if(a<5 or a>9):
    raise ValueError("The entered value is not within range")