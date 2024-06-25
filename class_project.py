class Person:
    def __init__(self,n,o):#this is a constructor in python
        self.name=n
        self.education=o 
    def info(self):
        print(f"{self.name} is currently studying {self.education}")

a=Person("Ashmit","Btech")
a.info()
b=Person("Aysuh","Acting")
b.info()

#decorators
def greet(fx):
    def mfx(*args,**kwargs):#the *args is used to take all arguments in form of tuple and **kwargs takes arguments in form of dictionary
        print("Good Morning")
        fx(*args,**kwargs)
        print("Good Bye")
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print(a+b)

hello()
add(2,3)