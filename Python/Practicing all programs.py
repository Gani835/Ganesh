
                        ###  Practicing all Programs ###

# 1) Factorial Program:-

'''num=int(input("Enter a number:"))
fact=1
while num>0:
    fact=fact*num
    num=num-1
print(fact)

print("")'''

# 2) Fibonacci Series:-

'''x=0
y=1
print(x,y,end="")
i=1
while i<=10:
    z=x+y
    print(z,end="")
    x=y
    y=z
    i=i+1'''


# 3) FizzBuzz Program:-

'''num=int(input("Enter a number:"))

if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("Invalid Number")'''

# 4) Amstrong Number:- 

'''num=int(input("Enter a number:"))
sum=0
bkp=num
while num>0:
    t=num%10
    sum=sum+t**3
    num=num//10
print(sum)
if bkp==sum:
    print("Its a Amstrong number")
else:
    print("Its not an Amstrong number")'''


# 5) L.C.M of two numbers:-

'''num1=int(input("Enter the first number:"))
num2=int(input("Enter the second nimber:"))
div=2
while div<=num1:
    if num1%div==0 and num2%div==0:
        print(div)
    div=div+1'''

# 6) Swapping of two numbers:-

'''x=int(input("Enter the x value:"))
y=int(input("Enter the y value:"))

# x,y=y,x
#print(x,y)

print("x vlaue is",y)
print("y value is",x)'''


# 7) Reversing a number:-(Pallandrome or not)

'''num=int(input("Enter a number:"))
rev=0
bkp=num
while num>0:
    t=num%10
    rev=rev*10+t
    num=num//10
print(rev)
if bkp==rev:
    print("Its a pallandrome number")
else:
    print("Its not a Pallandrome number")'''
    

# 8) Sum of digits in a number:-

'''num=int(input("Enter a number:"))
sum=0
while num>0:
    t=num%10
    sum=sum+t
    num=num//10
print(sum)'''

# 9) No.of digits in a number:-

'''num=int(input("Enter a number:"))
cnt=0
while num>0:
    cnt=cnt+1
    num=num//10
print(cnt)'''

# 10) Guessing Number Game:-

'''import random
while True:
    fix=random.randint(1,10)

    i=1
    while i<=3:
        guess=int(input("Enter the guess number:"))

        if guess==fix:
            print("You  won the game. . . .")
            break
        else:
            print("Wrong guess. . ..")
            i=i+1
    else:
        print("You lost the game. . . . ")

    ch=input("Do you want to play again?(yes/no):")
    if ch=="no":
        break
print("Game over. . . .")'''


# 11) Prime Number:-

# Even numbers are nor prime numbers.

'''num=int(input("Enter a number:"))

if num%2==0:
    print("Not a prime number")
else:
    i=1
    cnt=0
    while i<=num:
        if num%i==0:
            cnt=cnt+1
            print(i)
        i=i+1

    if cnt==2:
        print("prime number. . . . .")
    else:
        print("Not a Prime number. . . .")'''
              

# 12) While Loop:-

'''i=1
while i<=10:
    print("Python is Awesome.")
    print("But some times its tricky. . . .")
    i=i+1'''

# 13) Multiplication Table:-
'''num=int(input("Enter a number:"))
i=1
while i<=10:
    print(i,"*",num,"=",num*i)
    print(f"{num}*{i}=",num*i)
    i=i+1'''

            ## or ##

'''num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
    i=i+1'''

# 14) List indexing and Slicing:-

'''li=[10,30,50,70,90,110]
for idx in range(0,len(li)):
    print(idx)
    print(idx,li[idx])

print(li[-1:-4:-2])
print(li[1:4:2])'''


'''name=input("Enter the name:")
mid=len(name)//2
print(name[:mid+1])
print(name[-1::-1])'''


# 15) Suffling program:-

'''import random
li=[1,2,3,4,5]

output=[]
indexes=[]
for i in range(0,1000):
    idx=random.randint(0,len(li)-1)
    if idx not in indexes:
        output.append(li[idx])
        indexes.append(idx)

    if len(li)==len(output):
        break

print(output)
print(indexes)'''


# 16) Car Game:-

'''Start=0
while True:
    
    print("1.START")
    print("2.STOP")
    print("3.EXIT")

    ch=int(input("Choose an option:"))

    if ch==1:
        if Start==0:
            print("Car Started. . . . ")
            Start=1
        else:
            print("Car is already started. . . .")

    elif ch==2:
        if Start==1:
            print("Car is Stopped. . . . .")
            Start=0
        else:
            print("Car is already stopped. . . . .")

    elif ch==3:
        print("Exiting. . . .")
        break
    else:
        print("Choose correct option. . . .")'''



# 17) Generators:-

'''def evenNumbers(start,end):
    for i in range(start,end+1):
        if i%2==0:
            yield i
        

for j in evenNumbers(1,1000):
    print(j)'''

            ## Without Generator ##

'''def evenNumbers(start,end):
    output=[]
    for i in range(start,end+1):
        if i%2==0:
            output.append(i)

    return output

res=evenNumbers(1,1000)
print(res)'''
            



    
        



    
