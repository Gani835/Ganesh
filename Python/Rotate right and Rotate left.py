
# Rotation right( Clock Wise ):-


li=[1,2,3,4,5,6]
output=[]
num=int(input("Enter index value from which you want to rotate:"))
if num in li:
    idx=li.index(num)
    output.extend(li[idx+1:])
    output.extend(li[:idx+1])
else:
    print("can't rotate")
print(output)



# Rotation Left ( Anti Clock Wise ):
li=[1,2,3,4,5,6]
output=[]
num=int(input("Enter index value from which you want to rotate:"))
if num in li:
    idx=li.index(num)
    output.extend(li[(idx-1)::-1])
    output.extend(li[-1:(idx-1):-1])

else:
    print("Cant rotate")

print(output)


