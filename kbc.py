questions=["What is full form of iiit?","Who is pm of india?","Who won the olympic gold medal in javelin?"]

answers=["Indian Institute of Information Technology","Narendra Modi","Neeraj Chopra"]
amount=[1000,5000,10000]
c=0
for i in questions:
    print(i)
    ans=input("Answer: ")

    if(ans==answers[c]):
        print(f"You have won {amount[c]} rupees")
    else:
        print("Better luck next time.")
        break
    c=c+1