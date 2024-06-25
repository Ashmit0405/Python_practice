dic={
    "Name": "Ashmit",
    "Age": 3,
    "Roll no.": "2023KUCP1014"
}

print(dic["Age"])

dic1={
    "list1": [1,2,3],
    "list2": [8,9,10],
    "list3": [11,12,13]
}
print(dic1["list1"])
dic.update(dic1)
print(dic)
dic1.clear()
print(dic1)
print(dic)
dic.pop("Name")
print(dic)
dic.popitem()
print(dic)
del dic1
try:
    print(dic1)

except Exception as e:
    print(e)

print("Code is running fine")