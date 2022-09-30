num=int(input("Enter a number:"))#153
bkp=num
rev=0
while num>0:        #153>0          15>0        1>0         0>0 (Program will be stopped here)
    t=num%10        #153%10=3       15%10=5     1%10=1
    rev=rev*10+t    #0*10+3=3       3*10+5=35   35*10+1=351
    num=num//10     #153//10=15     15//10=1    1//10=0
print(rev)
if bkp==num:
    print("The given number is a pallandrome")
else:
    print("The given number is not a pallandrome")
    
