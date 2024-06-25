msg=input("Enter the string: ")
words=msg.split(" ")
nstr=[]
i=input("Do you want to decode or encode (1 for encode 0 for decode): ")
if(i==1):
    for word in words:
        if(len(word)>=3):
            firststr="abc"
            secstr="xyz"
            word=firststr+word[1:]+word[0]+secstr
            nstr.append(word)
        else:
            nstr.append(word[::-1])
    print(" ".join(nstr))
else:
    decode=[]
    for word in words:
        if(len(word)>=3):
            word=word[len(word)-4]+word[3:len(word)-4]
            decode.append(word)
        else:
            decode.append(word[::-1])
    print(" ".join(decode))
