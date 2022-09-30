num=int(input("Enter a number:"))       #123
sum=0
while num>0:                            #123>0          12>0        1>0         0>0(Program will be stopped here)
    t=num%10                            #123%10=3       12%10=2     1%10=1
    sum=sum+t                           #sum=0+3=3      sum=3+2=5   sum=5+1=6
    num=num//10                         #123//10=12     12//10=1    1//10=0
print(sum)
    
