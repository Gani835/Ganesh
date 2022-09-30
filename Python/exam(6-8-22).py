
# Question No-4:- Find words which are greater than the given length k=4?
'''
li=["Python","Apple","ant","Ravi"]

k=int(input("Enter the length you want:"))

for i in li:
    if k<=len(i):
        print(i)

#  or  #

li=["Python","Apple","ant","Ravi"]

for i in li:
    if len(i)>4:
        print(i)

# Question No-5:- Counting the frequencies in a list by using Dictionary in python?

li=[1,2,1,2,1,1,3,4,3,4,3,6]
output={}

for i in li:
    output[i]=li.count(i)

print(output)               # O/P---> {1:4, 2:2, 3:3, 4:2, 6:1}


# Question-2:- Write a program to find the fibonacci series by using recursive function?

def febFun(a,b):
    c=a+b
    print(c,end=' ')

    if c>100:
        return

    a=b
    b=c
    febFun(a,b)

x=0
y=1
print(x,y,end=' ')
febFun(x,y)'''

# Question-1:- Find the second largest number from the given list without using built-in functions.

li=[10,4,0,15,5,14]

def maxValue(list1):
    big=list[0]
    for val in list1:
        if big < val:
            big=val
    return big

def findIndex(list1,val):
    for i in range(0,len(list1)):
        if val==list1[i]:
            return i
    return -1


for i in range(0,len(li)):
    max_val=maxValue(li[i:])
    idx=findIndex(li,max_value)
    li[i],li[idx]=li[idx],li[i]

print(li)
print(li[1])


    
        













