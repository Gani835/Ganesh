
# List of Arguments:- (* args)

def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum

res=add(10,20,30,40,50,60,70,80)
print("The sum of those values is:",res)


# Key word  Arguents or Dictionary of Arguments:-

def info(**kwargs):
    print(kwargs)

info(Name="Ganesh",Age=32,Location="Hyderabad",Salary=50000)

                    ## OR ##


def info(**kwargs):
    for items in kwargs.items():
        print(items)        # output in the form of (a,b)

info(Name="Ganesh",Age=32,Location="Hyderabad",Salary=50000)


# 
        
