

# Recursion:- # A function can call itself is called Recursion.
              # It doesn't contains any looping statements.


# Example:-

def display():
    print("This is the Recursion topic. . . . .")
    display()

display()

# NOTE:- # If we run the above program, the content in the print method
         # will prints an infinite times.
         # In order to stop the infinite loop, we can use atleast one if statement.


# Base case:- # If the condition true, it terminates the infinite loop.
# Recursive Case: # It calling itself.


# Example:- # Its the perfect example to understanding the concept of Recursion.
            # Because till the condion becomes true, the function will repeats
            # and then stops the loop.

def factorial(n):
    
    if n==0 or n==1: # This is the Bace case.
        return 1      
    else:
        return n*factorial(n-1)  # This is the Recursive Case.

factorial(5)

# O/P is:- 120
