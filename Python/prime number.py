num=int(input("Enter a number:"))
i=1
count=0
while i<=num:
    if num%i==0:
        print(i)
    i+=1
    count=count+1
if count==2:
    print("Its a prime number")
elif count>2:
    print("Its not a prime number")
    

# Prime Numbers between Range. . ..

min=int(input('Enter the minimum value:'))
max=int(input('Enter the maximum value:'))
li=[]
for num in range(min,max+1):   
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
        li.append(num)
print(li)


