
# Programs on OOPS Concept by different input methods:-

# 1)

'''class Student:

    def __init__(self,name,marks): # self--> Its a current object

        # Instance Variables. . . .
        self.name=name
        self.marks=marks                    

    def info(self):
        print(self.name,self.marks)


num=int(input("How many students do you want to be added:"))

std_obj=[]

for i in range(1,num+1):
    name=input(f"Enter the student {i} name:")
    marks=int(input(f"Enter student {i} marks:"))

    s=Student(name,marks)
    std_obj.append(s)


for obj in std_obj:
    obj.info()'''



# 2) Finding the student detailes (Count,Fee,etc):-

'''class Student:

    School_Name="V cube"
    Std_Cnt=0
    All_Fee=[]
    def __init__(self,name,age,fee):

        self.name=name
        self.age=age
        self.fee=fee
        Student.Std_Cnt+=1
        Student.All_Fee.append(fee)

    def info(self):
        print(self.name,self.age,Student.School_Name,self.fee)

s1=Student("Raju",35,6500)
s1.info()

s2=Student("Siva",34,7000)
s2.info()

s3=Student("Ramu",37,8000)
s3.info()

print("The total number of students are",Student.Std_Cnt)
print(Student.All_Fee)'''



# 3) Finding the total revenue from the students:-

class Student:

    School_Name=" V cube "
    Std_Cnt=0
    All_Fee=[]

    def __init__(self,name,age,fee):

        self.name=name
        self.age=age
        self.fee=fee
        Student.Std_Cnt+=1
        Student.All_Fee.append(fee)

    def info(self):

        print(self.name,self.age,Student.School_Name,self.fee)

Std_obj=[]

num=int(input("How many students do you have?:"))

for i in range(1,num+1):

    name=input(f"Enter the student {i} name:")
    age=int(input(f"Enter the student {i} age:"))
    fee=int(input(f"Enter the fee of student {i}:"))

    s=Student(name,age,fee)
    Std_obj.append(s)


for obj in Std_obj:
    obj.info()

@classmethod

def calcRevenue(cls):
    revenue=0

    for amt in cls.All_Fee:
        revenue+=amt
    return revenue

print(f"Total number of students are {Student.Std_Cnt}")
print(Student.All_Fee)

rev=Student.calcRevenue()
print(f"Total revenue generated from this batch is {rev}")





    



    










    
