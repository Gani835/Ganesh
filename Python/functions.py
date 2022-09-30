
# Function:- A function is nothing but a group of statements. or a block of code
# which runs only when it is called. you can pass the data in parenthesis
# known as parameters into a function. A function can return data as a result.

# A " parameter " is the variable listed inside the parentheses in the function definition.

# An " argument " is the value that is sent to the function when it is called.


# Simple Function Program. . . . . . .

def display():
    print("*"*20)
    print("welcome to Functions. . . .")
    print("*"*20)
display()
display()
display()
display()
display()

#NOTE:- In functions we can call functions anywhere and anytimes. . . . . .

print("")
print('')

# Addition program. . . . . . . .

def add(a,b):
    c=a+b
    print(c)
add(10,20)

print('')
print('')

# Addition and Subtraction program. . . . . . .
    
def add(a,b):
    c=a+b
    print(f'addition of {a} and {b} is {c}')
    
def subs(a,b):
    d=b-a
    print(f'Subtraction of {b} and {a} is {d}')
    add(a,b)

add(20,50)
subs(20,50)

print('')
print('')

# Addition and Subtraction program by using return concept. . . . . .

def add(a,b):
    c=a+b
    return c
def subs(a,b):
    d=b-a
    return d

res=add(10,30)
print(res)

res=subs(20,70)
print(res)

print('')
print('')

# Even Numbers finding by using Function. . . . . . .

def  evennumbers(start,end):
    for i in range(start,end+1):
        if i%2==0:
            print(i)


evennumbers(1,10)

                    ## OR ##

def evennumbers(start,end):
    output=[]
    for i in range(start,end+1):
        if i%2==0:
            output.append(i)
    return output

res=evennumbers(1,100)
print(res)

print('')
print('')

# Prime number program by using function. . . . . . .

def isprime(num):
    i=1
    cnt=0
    while i<=num:
        if num%i==0:
            cnt=cnt+1
        i=i+1
    if cnt==2:
        return True
    else:
        return False

res=isprime(7)
if res:
    print("prime")
else:
    print("not prime")

print('')
print('')

                    ## OR ##

        
for i in range(1,101):
    if i%2==1:
        if isprime(i):
            print(i)

# Arbitrary Arguments:- If you do not know how many arguments that will be
# passed into your function, add a * before the parameter name in the function definition.

def family(*names):
    print("My family members names are",names)

family("Ganesh","Pravallika","Srikar","Seetharatnam")

# O/P is My family members names are ('Ganesh', 'Pravallika', 'Srikar', 'Seetharatnam')

# Keyword Arguments:- You can also send arguments with the " key = value " syntax.
                    # In this way the order of the arguments does not matter.

def personDetailes(**detailes):
    print(detailes)

personDetailes(name="Ganesh",age=32,location="Hyderabad",salary=50000)

# O/P is {'name': 'Ganesh', 'age': 32, 'location': 'Hyderabad', 'salary': 50000}
