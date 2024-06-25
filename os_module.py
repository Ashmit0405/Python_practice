import os
import shutil
if(not os.path.exists("New")):
    os.mkdir("New")

for i in range(1,101):
    os.mkdir(f"New/Day{i}")

l=os.listdir("New")
print(l)
for i in l:
    print(i)
    print(os.listdir(f"New/{i}"))

for i in range(1,101):
    os.rename(f"New/Day{i}",f"New/Program{i}")

for i in range(16,101):
    shutil.rmtree(f"New/Program{i}")
print(os.getcwd())
os.chdir("/home/ashmit/python_programming/New")
print(os.getcwd())
os.chdir("/home/ashmit/python_programming")
print(os.getcwd())
