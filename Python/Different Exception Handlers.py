# Exception and Exception Handlers:-
# else: You can use the else keyword to define a block of code to be executed if
# no errors were raised:

#1 ZeroDivisionError:-
'''
try:
    num=int(input("Enter numerator value:"))
    den=int(input("Enter denominator value:"))
    div=num//den
    print(div)

except ZeroDivisionError:
    print("Denominator should not be Zero. . . .")

except Exception:                                           # Base class or Generic Exception Handler for all Errors.
    print("Something went wrong. . . .")


#2) ValueError:-                                                #  invalid literal for int() with base 10: 'Raju

try:
    num=int(input("Enter numerator value:"))
    den=int(input("Enter denominator value:"))
    div=num//den
    print(div)

except ZeroDivisionError:   # It's not working if we use ZeroDivisionError handler for ValueError.
    print("Denominator should not be zero. . . . .")

except ValueError:
    print("Value should be an integer. . . .")

except Exception:
    print("Something went wrong. . . . .")


#3) NameError:-                     # The try block will generate a NameError, because x is not defined
try:
    print(x)
except NameError:
    print("Variable x is not defined. . . . .")
except:
    print('Something else went wrong. . . .')


#4) TypeError:-

try:
    x="Hello"
    y=835
    print(x+y)
except NameError:
    print("checking it as a NameError or not. . . .")
except TypeError:
    print("Checking it as a TypeError or not. . . .")           # Its throws an  TypeError . . . .
'''

