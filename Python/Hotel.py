
                        ### Hotel Billing ###
print("Welcome to sri Sai family Restaurent. . . .")
print("")

idly={"Plain":20,"Ghee":30,"Sambar":40}
dosa={"Plain":30,"Onion":40,"Butter":40,"Egg":40,"Masala":50}
pesarattu={"Plain":30,"Ghee":40,"Onion":40,"Upma":50}
total=0
while True:
    
    tfn=input("Which tiffen do you want to eat?(idly,dosa,pesarattu):")

    if tfn=="idly":
        print("")
        print(idly.keys())
        print("")

        sel=input("Select which idly do you want?:")

        if sel=="Plain":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_1=idly["Plain"]*cnt
            print("")
            print("Total price of your items",cost_1)
                
        elif sel=="Ghee":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_2=idly["Ghee"]*cnt
            print("")
            print("Total price of your items",cost_2)

        elif sel=="Sambar":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_3=idly["Sambar"]*cnt
            print("")
            print("Total price of your items is:",cost_3)

    else:
        print("We dont have that items. . . . .")

    if tfn=="dosa":
        print("")
        print(dosa.keys())
        print("")

        sel=input("Select which dosa do you want?:")

        if sel=="Plain":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_4=dosa["Plain"]*cnt
            print("")
            print("Total price of your items is:",cost_4)
        
        elif sel=="Onion":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_5=dosa["Onion"]*cnt
            print("")
            print("Total price of your items is:",cost_5)
        
        elif sel=="Butter":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_6=dosa["Butter"]*cnt
            print("")
            print("Total price of your items is:",cost_6)
        
        elif sel=="Egg":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_7=dosa["Egg"]*cnt
            print("")
            print("Total price of your items is:",cost_7)
        
        elif sel=="Masala":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_8=dosa["Masala"]*cnt
            print("")
            print("Total price of your items is:",cost_8)
        
        else:
            print("Sorry! we don't have that item. . . . .")


    if tfn=="pesarattu":
        print("")
        print(pesarattu.keys())
        print("")

        sel=input("Select which pesarattu do you want?:")

        if sel=="Plain":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_9=pesarattu["Plain"]*cnt
            print("")
            print("Total price of your items is:",cost_9)
        
        elif sel=="Ghee":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_10=pesarattu["Ghee"]*cnt
            print("")
            print("Total price of your items is:",cost_10)
        
        elif sel=="Onion":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_11=pesarattu["Onion"]*cnt
            print("")
            print("Total price of your items is:",cost_11)
        
        elif sel=="Upma":
            print("")
            cnt=int(input("How many plates do you want?:"))
            cost_12=pesarattu["Upma"]*cnt
            print("")
            print("Total price of your items is:",cost_12)
        
        else:
            print("Sorry! we don't have that item. . . . .")

    print("")
    
    ch=input("Do you want anything else?:(yes/no)")
    print("")
    if ch=="no":
        break

print("Thank you for visit. Have a nice day. . . . . .")

            
            
