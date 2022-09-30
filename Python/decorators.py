

                            ### Decorators Concept ####

#Def:-
        # Python has an additional and interesting feature called Decorators
        #to add functionality to an existing code.
        # This is also called "meta programmig" as a part of the program tries
        #to modify another part of the program at compile time.
        # Decorator is a function that takes another function
        #as an argument and add some kinds of functionalities and returns function.
        #
        
# 1) Example:-

def decorate(func):
    def inner_function():
        print("I got decorated")
        func()
    return inner_function
@decorate  
def simple_function():
    print("Iam a simple function")
simple_function()

             ## Or ##

def decorate(func):
    def inner_function():
        print("I got decorated")
        func()
    return inner_function

def simple_function():
    print("Iam a simple function")

decor=decorate(simple_function)
decor()

print("")

# 2) Example:-
def div(func):
    def inner_func(x,y):
        print("I am dividing",x,"and",y)
        if y==0:
            print("Oops! division by zero is illegal. . . .")
            return
        return func(x,y)
    return inner_func
@div

def divide(a,b):
    return a/b

print(divide(20,2))
print(divide(20,0))
    
        

