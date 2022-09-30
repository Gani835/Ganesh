# 1)
'''
num=int(input("Enter a number:"))
if num%2==0:
    print("The given number is Even Number. . .")
else:
    print("The given number is odd Number. . . .")

print('')
# 2)

num=int(input("Enter a number:"))
if num>0:
    print("The given number is positive. . .. ")
elif num<0:
    print("The given number is negative. . . .")
else:
    print("The given number is Zero. . . .")

print('')

#3)

import calendar
yy=int(input("Enter the year. . . ."))
mon=int(input("Enter the month. . .. "))
print(calendar.month(yy,mon))

print('')

#4)

str=input("Enter any string do you want?:")
print("Your entered string is:",str)

print('')

#5)

str1=input("Enter the first string. . . .")
str2=input("Enter the second string. .. . ")
str3=str1+str2
print("Your concatenated string is:",str3)                      #  Without a space in between two strings. . ..
print("Your concatenated string is:",str1+ ' ' +str2)     #  With a space in between two strings. . . .

print('')

#6)

list1=[10,25,53,45,78,68,36,48]
list2=["apple","ball","cat","dog","egg"]

item=int(input("Enter the checking number:"))

if item in list1:
    print(f" Yes, {item} was in the given list. . ..")
else:
    print(f"No, {item} was not in the given list. . . .")

item=int(input("Enter the checking word:"))

if item in list2:
    print(f" Yes, {item} was in the given list. . ..")
else:
    print(f"No, {item} was not in the given list. . . .")

print('')

#7)

list1=[10,30,50,70]
list2=[20,40,60,80]
print("The concatenated list is:",list1+list2)

list1=[10,20,30,40]
list2=["apple","ball","cat","dog"]
print("The concatenated list is:",list1+list2)

print('')

#8)

num=int(input("Enter a number:"))
cube=num*num*num
print("The cubic value of the given number is:",cube)

                    ## OR ##

import math
num=int(input("Enter a number:"))
cube=math.pow(num,3)
print("The cubic value of the given number is:",cube)

print('')

#9)

import math
num=int(input("Enter a number:"))
sqrt=math.pow(num,1/2)
print("The square root of the given number is:",sqrt)

##  OR  ##

import math
num=int(input("Enter a number:"))
x=math.sqrt(num)
print("The square root of the given number is:",x)

print('')

#10)

li=[5,10,15,20,25,30]
print([li[0],li[5]])

print('')

#11)

li=[1,1,2,3,5,8,13,21,34,55,89]
output=[]
for i in li:
    if i<5:
        output.append(i)
print(output)

print('')

#12)

li=[1,4,9,16,25,36,49,64,81,100]
output=[i for i in li if i%2==0 ]
print(output)

print('')

#13)

str=input("Enter a string:")
print("Te reverse order of the given string is:",str[-1::-1])
if str==str[-1::-1]:
    print("The string entered you is a pallandrome")
else:
    print("The string entered you is not a pallandrome")

           ##  OR  ##

a=input("Enter a string:")
c=a.casefold()                          # casefold() converts given string into lower case only.
b=reversed(c)
if list(c)==list(b):
    print("The string entered you is a pallandrome")
else:
    print("The string entered you is not a pallandrome")

                ##  OR  ##
    
a=input("Enter a string:")
b=list(reversed(a))
if a==b:
    print("The string entered you is a pallandrome")
else:
    print("The string entered you is not a pallandrome")

print('')

#14)

a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
output=[i for i in set(a) if i in set(b)]       # -----> For common elements in both lists.
print(output)

print('')

#15)

a={1,1,2,3,5,8,13,21,34,55,89}
b={1,2,3,4,5,6,7,8,9,10,11,12,13}
output={i for i in set(a) if i in set(b)}
print(output)
                                                                    # -----> For common elements in both sets.
                ##  OR  ##
a={1,1,2,3,5,8,13,21,34,55,89}
b={1,2,3,4,5,6,7,8,9,10,11,12,13}
print(a.intersection(b))
            ## OR  ##
print(a&b)

print('')

#16)

str=input("Enter a word:")
li=list(str)
print(li)

print('')

#17)

num=int(input("Enter a number:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)

print('')

#18)

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1>num2 and num1>num3:
    print("The biggest number is:",num1)
elif num2>num3 and num2>num1:
    print("The biggest number is:",num2)
else:
    print("The biggest number is:",num3)

print('')

#19)

num=int(input("Enter a number:"))
if num>0:
    print("The absolute value of the given number is:",num)
else:
    print("The absolute value of the given number is:",-num)

print('')

#20)

str=input("Enter a word:")
print("The length of the given string is:",len(str))

print('')

#21)

str=input("Enter a string:")
if str=="y":
    exit()                                      #  exit() is used to close the IDLE Tab.

print('')

#22)

num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(i)

print('')

#23)

N=int(input("Enter a number:"))
sum=0
for i in range(0,N+1):
    sum=sum+i
print("The sum of all the Natural numbers is:",sum)
avg=sum/N
print("The average of the Natural numbers is:",avg)

print('')

#24)

i=1
while i<=10:
    print("Python is an awesome lamguage")
    i=i+1
                ##  OR  ##
num=int(input("Enter a number:"))
for i in range(num):
    print("Python is an awesome lamguage")
    
print('')

# 25)

def mul(a,b):
    
    a=int(input("Enter a value:"))
    b=int(input("Enter a value:"))
    c=a*b
    return c
res=mul()
print(res)

print('')

#26)

list1=[4,5,6,7]
list2=[4,5]                                 # convert lists to sets and then substrate them.
print(list(set(list1)-set(list2)))

print('')

#27)

import random
list=["Apple","Ball","Cat","Dog","Egg"]
print(random.choice(list))      # Randomly take the value by the system by using choice() method.

print('')

#28)

for i in range(0,6):
    if i==2 or i==6:
        continue
    print(i)
    
print('')

#29)

str=input("Enter a word:")
print(str.upper())
print(str.lower())

print('')

#30)
str=input("Enter a sentense:")          # To check whether the given string should starts with the given characters or not.
print(str.startswith("The"))

print('')

#31)

num=int(input("Enter a number:"))
i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i=i+1

print('')

#32)

a=int(input("Enter the length of triangle side a:"))
b=int(input("Enter the length of triangle side b:"))
c=int(input("Enter the length of triangle side c:"))
if a==b==c:
    print("The given triangle is an Equilateral Triangle. . . .")
elif a==b or b==c or c==a:
    print("The given triangle is Isosceles Triangle. . . .")
else:
    print("The given triangle is Scalene Triangle. . . ")

print('')

#33)

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=a+b
if c>=15 and c<=20:             # OR #  if c in range(15,20):
    print(20)                                  #         print(20)
else:                                            #   else:
    print(c)                                    #         print(c)

print('')

#34)

import random
print(random.randint(1,10))

print('')

#35)

a=int(input("Enter the length of triangle side a:"))
b=int(input("Enter the length of triangle side b:"))
c=int(input("Enter the length of triangle side c:"))
semi_perimeter=(a+b+c)/2
print("The semi perimeter of the triangle is:",semi_perimeter)

print('')

#36)

li=[10,25,37,48,52,64,76,85,93]
for i in li:
    if i%2==0:
        print(i)

print('')

#37)

li=[1,3,5,7,9,2,4,6,8]
output=[]
for i in li:
    x=(i*5)
    output.append(x)
print(output)

import numpy                    # numpy model but not gives an output.
list=[1,2,3,4,5]
result=numpy.prod(list)     
print(result)

print('')

#38)

li=[1,3,5,7,9,2,4,6,8]
avg=sum(li)/len(li)
print("The average of numbers in the given list is:",avg)

print('')

#39)

import getpass                                          # Authentication process
pwd=getpass.getpass("Enter the Password:")
if pwd=="python":
    print('You are authenticated')
else:
    print("You are not authrnticated")

print('')

#40)

tel=int(input("Enter the marks in Telugu subject:"))
eng=int(input("Enter the marks in English subject:"))
mat=int(input("Enter the marks in Maths subject:"))
hin=int(input("Enter the marks in Hindi subject:"))
sci=int(input("Enter the marks in Science subject:"))
soc=int(input("Enter the marks in Social subject:"))
total_marks=(tel+eng+mat+hin+sci+soc)
print(total_marks)
avg=total_marks/6
if avg>=90:
    print("A GRADE")
elif avg>=80 and avg<90:
    print("B GRADE")
elif avg>=70 and avg<80:
    print("C GRADE")
elif avg>=60 and avg<70:
    print("D GRADE")
else:
    print("F GRADE")
    
print('')

#41)

num=int(input("Enter a number:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)

print('')
'''
#42)

num1=int(input("Enter first value:"))
num2=int(input("Enter second value"))
quotient=num2//num1
print(quotient)
remainder=num2%num1
print(remainder)
