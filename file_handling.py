# f1=open('f1.txt','r')
# i=0
# while True :
#     i=i+1
#     line=f1.readline()#this is used to read a full line from a file
#     if not line:
#         break
#     print(line)
# f1.close()

# f2=open('f2.txt','w')
# lines=['This is line 1\n','This is line2\n','This is line3\n']
# f2.writelines(lines)#this is used to write lines in a file
# f2.close()

# f1=open('f1.txt','r')
# f1.seek(10)#advances 10 characters forward before reading
# t=f1.tell()#gives us upto which character we have seeked
# print(t)
# data=f1.read(5)#starts reading the next 5 characters in the file
# print(data)
# f1.close()

f2=open('f1.txt','w')
f2.write('1 2 3 4 5 6 7 8 9 d')
f2.truncate(17)#truncates the file upto the given number no. of characters
f2.close()

with open('f1.txt','r') as f1:
    print(f1.read())