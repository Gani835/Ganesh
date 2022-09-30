
                        ## G.S.T BILLING PROGRAM ##

print("Welcome to Jersy Parlour. . . . .")
print("")
milk=["Toned_Milk","Double_Toned_Milk","Full_Cream_Milk"]
curd_volume=[200,500]
milk_volume=[200,500]
milk_price=[28,32,35]
gst=5
net_price=0
while True:
    
    item=input("What do you want sir/madam?(milk/curd/lussy):")

    if item=="milk":
        print("")
        print("1.Toned_Milk")
        print("2.Double_Toned_Milk")
        print("3.Full_Cream_Milk")
        print("")
        ch=input("Which milk packet do you want?:")

        if ch=="1":
            print("")
            volume=int(input("How much volume(ml) of packet do you want? (200/500):"))

            if volume==200:
                print("")
                qty=int(input("How many packets do you want?:"))
                print("")
                price_1=qty*10
                sgst=((price_1)*gst)/100
                cgst=((price_1)*gst)/100
                tot_gst=int((sgst+cgst))
                total_1=price_1 + tot_gst

                print("*"*20)
                print(f"Please pay {total_1} rupees. . . .")
                print("*"*20)
                
            elif volume==500:
                print("")
                qty=int(input("How many packets do you want?:"))
                print("")
                price_2=qty*milk_price[0]
                sgst=((price_2)*gst)/100
                cgst=((price_2)*gst)/100
                tot_gst=int((sgst+cgst))
                total_2=price_2 + tot_gst

                print("*"*20)
                print(f"Please pay {total_2} rupees. . . .")
                print("*"*20)
                
        if ch=="2":
            print("")
            volume=int(input("How much volume(ml) of packet do you want?(200/500):"))

            if volume==200:
                print("")
                qty=int(input("How many packets do you want?:"))
                print("")
                price_3=qty*10
                sgst=((price_3)*gst)/100
                cgst=((price_3)*gst)/100
                tot_gst=int((sgst+cgst))
                total_3=price_3 + tot_gst

                print("*"*20)
                print(f"Please pay {total_3} rupees. . . .")
                print("*"*20)
                
            elif volume==500:
                print("")
                qty=int(input("How many packets do you want?:"))
                print("")
                price_4=qty*milk_price[1]
                sgst=((price_4)*gst)/100
                cgst=((price_4)*gst)/100
                tot_gst=int((sgst+cgst))
                total_4=price_4 + tot_gst

                print("*"*20)
                print(f"Please pay {total_4} rupees. . . .")
                print("*"*20)
                
        if ch=="3":
            print("")
            volume=int(input("How much volume(ml) of packet do you want?(200/500):"))
            print("")
            if volume==200:
                print("")
                qty=int(input("How many packets do you want?:"))
                print("")
                price_5=qty*10
                sgst=((price_5)*gst)/100
                cgst=((price_5)*gst)/100
                tot_gst=int((sgst+cgst))
                total_5=price_5 + tot_gst

                print("*"*20)
                print(f"Please pay {total_5} rupees. . . .")
                print("*"*20)
                
            elif volume==500:
                print("")
                qty=int(input("How many packets do you want?:"))
                print("")
                price_6=qty*milk_price[2]
                sgst=((price_6)*gst)//100
                cgst=((price_6)*gst)//100
                tot_gst=int((sgst+cgst))
                total_6=price_6 + tot_gst

                print("*"*20)
                print(f"Please pay {total_6} rupees. . . .")
                print("*"*20) 
    else:
        print("Sorry! We don,t have that item. . . . .")

    print("")
    opt=input("Do you want  anything else?(yes/no):")
    print("")
    if opt=="no":
        break
print("")
print("Thank you for visit. Have a nice day. . . ..")
    



            

    
