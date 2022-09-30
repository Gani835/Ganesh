num=int(input("Enter a number:"))       #153
sum=0
bkp=num
while num>0:                            #153>0
    digit=num%10                        #153%10=3
    sum=sum+(digit**3)                  #sum=0+3**3=27
    num=num//10                         #num=153//10=15
print(sum)

if bkp==num:
    print("given number is Amstrong")
else:
    print("given number is not an Amstrong")
    
    

