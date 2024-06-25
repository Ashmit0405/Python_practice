import numpy as np
# a=np.array([1,2,3])#used to create an array
# print(a)
# print(a.ndim)#gives the dimensions of the array
# b=np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]],dtype='int32')#we can change the data type size using the dtype parameter in the array function of numpy
# print(b)
# print(b.ndim)
# print(b.shape)#gives the number of rows,number of columns
# print(b.dtype)#gives the data type size of the array default: int64 and float64
# print(b.itemsize)
# print(b[1,2])#gives a specific element based on zero indexing
# print(b[1,:])#to print a specific row 
# print(b[:,2])#to print a specific column
# #a little better way to make
# print(b[0,1:6:2]);#it means on the 0th row we start from index 1 to index 6 with a stepsize of 2
# #get 3d array
# d3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(d3)
# print(d3.ndim)
# print(d3[0,0,1])
# print(d3[:,1,:])#it means access all the 2d arrays with 1 index row and all its elements
# a=np.zeros((2,3,3,4,5),dtype='int32')#gives the array of zeros with the specified dimensions
# print(a)
# print(a.ndim)
# b=np.ones((3,4),dtype='int32')
# print(b)
# c=np.full((2,3),4)#to generate a matrix with all the elements filled with a specified number it would have 2 parameters first is the dimensions and second is the number to be filled in the array
# print(c)
# c=np.full(d3.shape,4)#in full we have to give the shape of the array as parameter
# c=np.full_like(d3,4)#to fill an array we have already generated here in full_like we can just pass the array name as parameter
# c=np.random.rand(4,2)#gives an array of specified value filed with radoom numbers form 0 to 1
# c=np.random.randint(1,4,size=(3,3))
# c=np.identity(5,dtype='int32')#gives an identity matrix of specifies dimension\
# arr=np.array([[1,2,3]])
# c=np.repeat(arr,3,axis=0)#used to repeat an array
# print(c)
# '''1 1 1 1 1
#    1 0 0 0 1
#    1 0 9 0 1
#    1 0 0 0 1
#    1 1 1 1 1 '''
# arr=np.ones((5,5),dtype='int32')
# z=np.zeros((3,3),dtype='int32')
# z[1,1]=9
# arr[1:4,1:4]=z
# print(arr)



###maths
# d=np.array([1,2,3,4])
# d=d**2#finds each element raised to power 2
# print(d)
# print(d+2)
# print(np.cos(d))#finds cos of each element
# print(np.sin(d))#finds sin of ech element



###linear algebra
# a=np.ones((2,3),dtype='int32')
# b=np.full((3,2),2)
# print(a)
# print(b)
# c=np.matmul(a,b)#used to multiply 2 matrices
# print(c)
# d=int(np.linalg.det(c))#used to find the determinant
# print(d)


###stats
# stats=np.array([[1,2,3],[4,5,6]])
# small=np.min(stats)#finds the mininmun value
# print(small)
# large=np.max(stats)#finds the maximum value
# print(large)
# add=np.sum(stats)#finds the sum of all elements
# print(add)


####matrix reorganize
# b=np.array([[1,2,3,4],[5,6,7,8]])
# print(b)
# a=b.reshape((1,8))#used to  reshape a matrix into a given dimension if number of elements remain same
# print(a)
# a=np.array([1,2,3,4])
# print(a)
# b=np.array([5,6,7,8])
# print(b)
# c=np.vstack([a,b])
# print(c)
# d=np.hstack([a,b])
# print(d)


####load data from a file
# e=np.genfromtxt("data.txt",delimiter=",",dtype='int32')
# print(e)


# ###boolean masking and advanced indexing
print(e>50)#this gives true and false 
print(e[e>50])#this is used to give values

# ####we can pass index as a list
a=np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,3,4]])