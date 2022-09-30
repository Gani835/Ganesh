
                                    ###  Types of Arguments  ###

#1. Required Arguments:-

def display(a,b):
    print(a,b)
display(10,20)

#2. Keyword Arguments:-

def display(a,b):
    print(a,b)
display(b=30,a=20)

#3. Default Arguments:-

def display(name,course="B.Tech"):
    print(name)
    print(course)
display(name="abc",course="M.Tech")
display(name="pqr")

#4. Variable length Arguments:-

def display(*courses):
    print(courses)
display("B.Tech","M.Tech","M.C.A","M.B.A")



                                        ###  Examples ###

# 1) Required Arguments:-

def add(x,y):
    z=x+y
    print(z)

add(10,20)

# 2) Default Arguments:-

def info(name,age,gender):
    print(f"Name={name} Age={age} Gender={gender}")
info("Ganesh",32,"M")

                    ## OR ##

# We can also do the above program like this. . .. .

def info(name,age,gender):
    print(f"Name={name} Age={age} Gender={gender}")
info(age=32,name="Ganesh",gender="M")


# If we enter the arguments not in the order of parameters. Following happens. . . . .

def info(name,age,gender):
    print(f"Name={name} Age={age} Gender={gender}")
info(32,"ganesh","M")

# In the following, we didn't gave gender argument, but it takes the default gender value from parameters. . . 

def info(name,age,gender="M"):
    print(f"Name={name} Age={age} Gender={gender}")
info("Ganesh",32)

# In the following program we specify the gender in arguments so it doesnot follows the default value in parameters. . . . 

def info(name,age,gender="M"):
    print(f"Name={name} Age={age} Gender={gender}")
info("Ganesh",32,gender="F")

# 3) List type argument or Variable length argument:-
# Here we can give "n" no.of input values and get the output value. . . .

def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
res=add(10,20,30,50,60,70)
print(res)

# 4) Dictionary type argument or Keyword argument:

def info(**kwargs):
    print(kwargs)
    
info(Name="Ganesh",Age=32,Gender="Male",Location="hyderabad",Salary=50000)

                                ## OR ##

def info(**kwargs):
    for items in kwargs.items():
        print(items)

info(Name="Ganesh",Age=32,Gender="Male",Location="Hyderabad",Salary=50000)




