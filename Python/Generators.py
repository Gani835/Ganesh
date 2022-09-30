
                                ## Short Notes On Generators ##
#Def:-
        # Generators are mainly used to returns the multiple values.
        # Generators are used the "yield" keyword to return a value.
        # If we want to streaming a data then we have to use a "Generator".
        # Generators are not returns multiple values in a single shot. It returns just value by value only.
        # Generators are also used to iterate the values. . . . .

#For Example. . . .        

def genExp():
    print("First step")
    yield 1
    print("Second step")
    yield 2
    print("Third step")
    yield 3

for i in genExp():
    print(i)

# Even Numbers finding by using Function. . . . . . .

def evennumbers(start,end):
    output=[]
    for i in range(start,end+1):
       if i%2==0:
           output.append(i)
    return output

res=evennumbers(1,1000)
print(res)

# Note:- # If we find the even numbers in the above way, we may consume so much of memory.
         # That is the memory utilisation management was failed.
         # Inorder to sort this issue, we have to use "Generator" like "yield" keyword.
    
def evenNumbers(start,end):
    for i in range(start,end+1):
        if i%2==0:
            yield i

for i in evenNumbers(1,1000):
    print(i)
