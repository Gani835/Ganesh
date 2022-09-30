# Exception:-# An exception is an event, which occurs during the execution of a program that
                    # disrupts the normal flow of the program's instructions.

                    # When a Python script raises an exception, it must either handle the exception
                    # immediately otherwise it terminates and quits.

# Exception Handling:- # If you have some suspicious code that may raise an exception,
                                    # you can defend your program by placing the suspicious code in a try: block.
                                    # After the try: block, include an except: statement, followed by a block of code
                                    # which handles the problem as elegantly as possible.


#Here are few important points about the above-mentioned syntax −

# ----> A single try statement can have multiple except statements. This is useful when the try
        # block contains statements that may throw different types of exceptions.

# ----> You can also provide a generic except clause, which handles any exception.

# ---->After the except clause(s), you can include an else-clause. The code in the else-block executes
        # if the code in the try: block does not raise an exception.

# ----> The else-block is a good place for code that does not need the try: block's protection.

                                                 ### Exception Name & Description  ###

1. Exception:-               Base class for all exceptions.

2. StopIteration:-          Raised when the next() method of an iterator doesnor point to any object.

3. SystemExit:-             Raised by the sys.exit() function.

4. StandardError:-        Base class for all built-in exceptions except StopIteration and SystemExit.

5. ArithmeticError:-      Base class for all errors that  occur for numeric calculations.

6. OverflowError:-        Raised when a calculation exceeds maximum limit for a numeric type.

7. FloatingPointError:-  Raised when a floating point calculation fails.

8. ZeroDivisionError:-  Raised when division or modulo by zero takesplace for all numeric types.

9. AssertionError:-       Raised in case of failure of the Assert statement.

10. AttributeError:-      Raised in case of faliure of attribute reference or assignment.

11.EOFError:-               Raised when there is no input from either the raw_input() or input() function and the end of file is reached.

12. ImportError:-         Raised when an import statement fails.

13. KeyboardInterrupt:- Raised when the user interrupts program execution, usually by pressing ctrl+c.

14. LookupError:-        Base class for all lookup errors.

15. IndexError:-           Raised when an index is not found in a sequence.

16. KeyError:-              Raised when the specified key is not found in the dictionary.

17. NameError:-           Raised when an identifier is not found in the local or global namespace.

18. UnboundLocalErrror:- Raised when trying to access a local variable in a function or method but no value hasbeen assigned to it.

19. EnvironmentError:- Base class for all exceptions that occur outside the python environment.

20. IOError:-                Raised when an inout/output operation fails, such as the print statement or the open() function when trying to open a file that doesnot exist.

21. IOError:-                Raised for operating system-related errors.

22. SyntaxError:-          Raised when there is an error in python syntax.

23. IndentationError:-  Raised when indentation is not specified properly.

24. SystemError:-         Raised when the interpreter finds an internal problem, but when this error is encountered thepython interpreter does not exist.

25. SystemExit:-           Raised when python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.

26. TypeError:-            Raised when an operation or function is attempted that is invalid for the specified data type.

27. ValueError:-           Raised when  the built-in function for a data has the valid type of arguments, but the arguments have invalid values specified.

28. RuntimeError:-       Raised when a generated error does not fall into any category.

29. NotImplementedError:- Raised when an abstract method that needs to be implemented in an inherited class is not actuallyimplemented.
