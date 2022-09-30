
# Finding average of the numbers in a given list:-

'''a=[]
n=int(input("Enter n value:"))
for i in range(1,n+1):
    elem=int(input("Enter element:"))
    a.append(elem)
avg=sum(a)/n
print(avg)'''

# Swaping of numbers without using a Temporary variable.. . . .

'''x=int(input("Enter x value:"))
y=int(input("Enter y value:"))

x=x+y
y=x-y
x=x-y

print("x value is:",x)
print("y value is:",y)'''


# print Even and odd numbers within a given range:-

'''a=[]
b=[]
for i in range(1,11):
    if i%2==0:
        a.append(i)
    
    elif i%2!=0:
        b.append(i)

print(a)
print(b)'''

# Printing all numbers in a range divisible by a given number:

'''num=int(input("Enter a number:"))
a=[]
for i in range(1,50):

    if i%num==0:
        a.append(i)

print(a)'''


# Finding the smallest divisor of an integer. . . . .

'''num=int(input("Enter a number:"))
li=[]
for i in range(2,num+1):
    if num%i==0:
        li.append(i)

print(li[0])'''


# Python program to print an identity matrix. . . . . 

'''num=int(input("Enter a number:"))
for i in range(0,num):
    for j in range(0,num):
        if i==j:
            print("1",sep='',end=" ")
        else:
            print("0",sep='',end=" ")
            
    print()'''
        
# Python program to print a unit matrix . . . . . .

'''num=int(input("Enter a number:"))
for i in range(0,num):
    for j in range(0,num):
        if i==j:
            print("1",sep='',end=" ")
        else:
            print("1",sep='',end=" ")
            
    print()'''

# Star pattens. . . . .
'''
num=int(input("Enter no.of rows:"))
for i in range(num,0,-1):
    print((num-i)* " " +i*"*")

num=int(input("Enter no.of rows:"))
for i in range(1,num+1):
    print("*"*i)

num=int(input("Enter no.of rows:"))
for i in range(num,0,-1):
    print(i*"*"+(num-i)*" ")

num=int(input("Enter no.of rows:"))
for i in range(1,num):
    print((num-i)*" " + i*"*")
'''


# Finding simple interest .. . . . .
'''
p=int(input("Enter the principle amount:"))
t=int(input("Enter the no.of years:"))
r=int(input("Enter the rate of interest:"))

simple_interest=(p*t*r)/100

print("The simle interest is", simple_interest)'''


# To check the Leap year or not. . . . .

'''year=int(input("Enter the year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"is the Leap year")

else:
    print(year,"is not a Leap year")'''


# Unit conversions. . . . .

# centimeters to inches and feets. . . . .

'''height=float(input("Enter your height in centimeters:"))

#1_inch=2.54cm
#1_cm=1_inch/2.54=0.394 inches
#1_feet=0.394/12=0.0328

print("your height in inches is",height*0.394)

print("Your height in feets is",(height*0.394)/12)'''


# Celcius to fahrenheit . . . . . .

'''temp=float(input("Enyer the temperature in celcius:"))

# F=(Celcius*1.8)+32

print("The temperature in fahrenheits is",(temp*1.8)+32)'''


# Mathematical Table. . . . . .

'''num=int(input("Enter a number:"))

for i in range(1,11):
    print(num,"*",i,"=",num*i)
    i=i+1'''


# Program for to find Perfect number. . . .

# Def:- The sum of the divisors is equal to the number is called perfect number.
# Ex:- 1+2+3=6, here 1,2,3 are the divisors of 6.        

'''num=int(input("Enter a number:"))
sum=0
bkp=num
for i in range(1,num):
    if num%i==0:
        print(i)
        sum=sum+i
    i=i+1
if bkp==sum:
    print("Its a perfect number")
else:
    print("Its not a perfect number")'''


# Program for to find strong number. . . .

# Def:- Strong number is a special number whose sum of the factorial of digits
# is equal to the original number. For Example: 145 is strong number.
# Since, 1! + 4! + 5! = 145.

    
'''num=int(input("Enter a number:"))
sum=0
bkp=num
while num>0:
    fact=1
    i=1
    t=num%10
    while i<=t:
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10

if bkp==sum:
    print("Its a strong number")
else:
    print("Its not a strong number")'''


# Finding G.C.D of a number. . . .

'''import fractions
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print("G.C.D value of a & b is",fractions.gcd(a,b))'''


# Finding area of a Triangle. . . .. 

import math

'''a=int(input("Enter the side value of a:"))
b=int(input("Enter the side value of b:"))
c=int(input("Enter the side value of c:"))

s=(a+b+c)/2
print(s)

area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of triangle is:",round(area,2))'''


# finding sum of "n" Natural numbers. . . .    
    
'''num=int(input("Enter a number:"))
sum=0
i=1
while i<=num:
    sum=sum+i
    i=i+1
print(f"The sum of first (num} natural numbers is:",sum)'''


# Replacing a letter in a string. . . . . 

'''string=raw_input("Enter a string:")
string=string.replace("a","&")
string=string.replace("e","@")

print(string)'''


# Python program to detect if two strings are Anagrams or not. . . . .

'''str1=input("Enter the first string:")
str2=input("Enter the second string:")

if sorted(str1)==sorted(str2):
    print("The two strings are Anagrams. . .. ")
else:
    print("The two strings are not Anagrams. . . . .")'''


# Counting the number of vowels in a string. . .. .

'''str=input("Enter a string:")
count=0
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E'
       or i=='I' or i=='O' or i=='U'):
        count=count+1

print("The number of vowels in a given string are:",count)'''


# Replacing a space in a string with any seperator. . . . . .

str=input("Enter a string:")
str=str.replace(" ","-")
print(str)


# Counting of digits in a string. . . . .

str=input("Enter a string:")
count1=0
count2=0
for i in str:
    if (i.isdigit()):
        count1=count1+1
    count2=count2+1

print("The number of digits in a string are:",)
print("")



        




    


