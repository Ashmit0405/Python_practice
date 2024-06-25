import pandas as pd
import numpy as np

# a=pd.DataFrame({'A':[1,2,3]})#used to generate a list with heading in what is in the single quotes and the under that column we get a list of the array we have passed 
# print(a)
# s=pd.Series([1,2,3,4,np.nan,90])#used to generate a series 
# print(s)
# dates =pd.date_range('20240101',periods=7)
# print(dates)
# s=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
# df=pd.DataFrame(s,index=dates,columns=list("ABCD"))

data = "Books_small_10000.json"
df = pd.read_json(data, lines=True)
# print(df.head())
# print(df.head())
# print(df.to_numpy())
print(df)
# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo",
#     }
# )
# print(df2)

data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
d=pd.DataFrame(data)
print(d)
# d.insert(2,'Age',[21,23,34,56],True)
# d2=d.assign(age=[21,34,25,30])
# print(d2)
age=[21,34,25,30]
address=['Delhi','Mumbai','Chennai','Kolkata']
new_data={'Age':age,'Address':address}
d2=d.assign(**new_data)
print(d2)
d2.drop(['Age','Address'],axis=1,inplace=True)
print(d2)
da=pd.DataFrame(df)
print(da)