import numpy as np

arr=np.array([1,2,3,4])
arr2=arr+10
print(arr2)

arr1=np.array([10,20,30,40])
arr2=np.array([50,60,70,80])
arr=arr1+arr2
print(arr)

# NOTE:- An array takes less memory than a list. . . . .
# Itemsize means memory taken by an array
# size means number of elements in ana array.

arr=np.array([30,40,50,60,70,80])
print(arr.itemsize)
print(arr.size)
print(arr.itemsize*arr.size)

arr=np.array(([1,2],[3,4],[5,6]))
print(arr)

# NOTE:- List takes more memory than Array. . . .

import sys
x=[10,20,30,40]
memory=sys.getsizeof(x)
print(memory)

# Time checking with arrays and lists. . . . 
# arrange helps to take number of values.

import time
start=time.time()
arr1=np.arange(1000)
arr2=np.arange(1000)
output=arr1+arr2
print(output)
end=time.time()
print('Time taken by sum of 2 arrays is',end-start)

'''import time
start=time.time()
list1=[i for i in range(1000)]
list2=[i for i in range(1000)]

for j in range(0,1000):
    print(list1.j[i]+list2.j[i])
end=time.time()
print('Time taken by sum of 2 lists is',end-start)'''

# Matrix Operations in arrays. . . . . .
# T means Transposing means rows to columns and columns to rows.
# reshape helps to convert into desired matrix size.

arr=np.array([10,20,30,40,50,60])
output=(arr.reshape(2,3))
print(output)
print(output.T)

# Row sum(axis=1) and Column Sum(axis=0). . . .

print(output.sum(axis=0))
print(output.sum(axis=1))

# .dot is used for matrix multiplication . . . .

arr1=np.array(([1,2],[3,4]))
arr2=np.array(([3,4],[5,6]))
output=arr1.dot(arr2)
print(output)

