
                        ### Simple Calculator by using function. . . . ###

print("Welcome to the Simple Calculator. . . .")
print("")
while True:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))

    ch=input("Select an operator(+,-,*,/):")
    if ch=="+":
        def add(num1,num2):
            x=num1+num2
            return x
        res=add(num1,num2)
        print(f"Addition of {num1} and {num2} is",res)
    elif ch=="-":
        def sub(num1,num2):
            x=num2-num1
            return x
        res=sub(num1,num2)
        print(f"Subtraction of {num1} and {num2} is",res)
    elif ch=="*":
        def sub(num1,num2):
            x=num2*num1
            return x
        res=sub(num1,num2)
        print(f"Multiplication of {num1} and {num2} is",res)
    elif ch=="/":
        def sub(num1,num2):
            x=num2/num1
            return x
        res=sub(num1,num2)
        print(f"Division of {num1} and {num2} is",int(res))
    else:
        print("Wrong operator was entered by you. Please check it. . . . .")
    opt=input("Do you want to calculate again(yes/no):")
    if opt=="no":
        break
print("Closing the calculator. . . . .")

