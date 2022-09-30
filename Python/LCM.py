num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
div=2
while div<=num1:
    if num1%div==0 and num2%div==0:
        print(div)
        break
    div+=1
