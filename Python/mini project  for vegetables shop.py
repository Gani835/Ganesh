print("Welcome to Sai vegetables Shop. . .")
print("")
veg=["onions","tomatoes","brinjals"]
qty=[40,30,20]
price=[25,40,30]
cost=0
while True:
    item=input("What do you want sir/madem?:")
    print("")
    if item in veg:
        idx=veg.index(item)
        quantity=int(input("How many kg's do you want?:"))
        print("")
        if quantity<=qty[idx]:
            total=quantity*price[idx]
            cost=cost+total
            print("please pay the total amount of rupees:",cost )
            
        else:
            print("Sorry, we don't have those many kg's. . .")
    
    else:
        print(f"Sorry, {item} was in out of stock. . .")
        
    print("")
    ch=input("Do you want anything else?(yes/no):")
    print("")
    if ch=="no":

        if cost>=1000:
            disc=(cost*10)/100
            cost=cost-disc
            print("You got 10% discount on total purchase value. So you will pay just",cost)
                
        else:
            print("Sorry! You didn't get any discount on total purchase value. . . . ")
        
        break
    print("")

    qty[idx]=qty[idx]-quantity
    if quantity<qty[idx]:
        continue
print("")     
print("Thank you for visit.Have a nice day. . . .")
        
