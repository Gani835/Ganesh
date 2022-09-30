
                             ### Global & Local Variables ###

# Global and Local variables are just differ in their "Scoope".
# Global variables can be declared at any of the entire program.
# Local variables can be declared only in user-difined function.

a=20
def display():
    b=10
    print("inside the user defined function:",a)
display()
print("outside the user defined function:",a)
#print("b value can't be printed because it's not in user defined function.",b)

#Note:
        #Here variable a is declared above the user defined function. SO a acts as Global variable.


# If local and global variables are having same variable names, first prioroty is goes to local vriable value.


a=10 #(Global variable)
def display():
    a=20 #(Local Variable)
    print("a value is:",a)
display()


# If we want to print global variable value inside the funtion we have to use "global" keyword inside the function.

def display():
    global x
    x=20
    y=30
    print(x)
    print(y)

display()
print(x)


