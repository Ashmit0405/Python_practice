import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamph=int(time.strftime('%H'))
print(timestamph)
timestampm=int(time.strftime('%M'))
print(timestampm)
timestamps=int(time.strftime('%S'))
print(timestamps)
if (timestamph>0 and timestamph<=12):
 print("Good morning")
elif timestamph>12 and timestamph<=16:
 print("Good afternoon")
elif timestamph>16 and timestamph<=20:
 print("Good evening")
else :
 print("Good night")