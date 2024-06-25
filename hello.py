print("Hello World")
names="Hello I aM A student..........."
print(len(names))#len is to claculate length
print(names[0:-2])#negative sign if there is then it is replaced by lengthofstring-absolutevalueofnegvalue
print(names[-1:0])#this does not make any sense as as substring from 20 to 0 index is not possible
print(names.split(" "))#split function just takes all the individual elements divided by the parameter inside it
print(names.lower())
print(names.upper())
print(names.rstrip("."))
print(names.replace('H','i'))
print(names.capitalize())
for i in names:
    print(i,end=' ')

print('\n')
for k in range(1,5,3):
    print(k)

i=0
while(i<4):
    print(i)
    i=i+1

    for i in range(1,20,3):
        print(i)

name="Amit"
country="India"
print(f"I am {name} and I am from {country}.")#this is an f-string 
price=99.239623122
print(f"Only {price:.2f} Rs")#it rounds off to 2 decimal points
print(type(f"Only {price:.2f} Rs"))