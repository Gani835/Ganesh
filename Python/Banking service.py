
'''# Banking Services:-
sav_acc=[]
class SavingsAccount:

    def savings_account(self,name,age,branch,place,accno,balance):

        self.name=name
        self.age=age
        self.branch=branch
        self.place=place
        self.__accno=accno
        self.__balance=balance

    def sav_display(self):
        print(self.name,self.age,self.branch,self.place,self.__accno,self.__balance)
curr_acc=[]
class CurrentAccount:

    def current_account(self,name,age,branch,place,accno,balance,):
        super().__init__(name,age,branch,place,accno,balance)

    def curr_display(self):
        print(self.name,self.age,self.branch,self.place,self.__accno,self.__balance)



obj=CurrentAccount("")

'''

class SbiBankingServices:      # Parent Class

    def __init__(self,name,age,branch,acctype,accno,balance):

        self.name=name
        self.age=age
        self.branch=branch
        self.acctype=acctype
        self.accno=accno
        self.balance=balance

    def customer(self):
        print(self.name,self.age,self.branch,self.acctype,self.accno,self.balance)

class SavingsAccount(SbiBankingServices):       # Child Class-1

    def __init__(self,name,age,branch,acctype,accno,balance):
        super().__init__(name,age,branch,acctype,accno,balance)

    def sav_display(self):
        print(self.name,self.age,self.branch,self.acctype,self.accno,self.balance)

class CurrentAccount(SbiBankingServices):       # Child Class-2

    def __init__(self,name,age,branch,acctype,accno,balance):
        super().__init__(name,age,branch,acctype,accno,balance)

    def curr_display(self):
        print(self.name,self.age,self.branch,self.acctype,self.accno,self.balance)


obj=CurrentAccount("Raju",34,"Madhapur Branch","Current_Acc",63001432561,150000)
obj.curr_display()

print("*"*20)

obj=CurrentAccount("Siva",36,"Lingampally Branch","Current_Acc",63004568736,58000)
obj.curr_display()

print("*"*20)

obj=SavingsAccount("Hari",39,"Kukkatpally Branch","Savings_Acc",63004578546,67500)
obj.sav_display()

print("*"*20)

obj=SavingsAccount("Siva",36,"Ameerpet Branch","Savings_Acc",63004557866,93000)
obj.sav_display()


        
