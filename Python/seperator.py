
class Student:

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def info(self):

        print(f"Student name is {self.name} and age is {self.age}")

    @classmethod

    def CreateObj(cls,S_data):
        name,age=S_data.split('-')
        return cls(name,age)

std_data=input("Enter the detailes:")
s=Student.CreateObj(std_data)
s.info()
        
