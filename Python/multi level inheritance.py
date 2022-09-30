
                    ##  Multi level Inheritance  ##

# Def:- In multilevel inheritance, the transfer of the properties of
# characteristics is done to more than one class hierarchically.
'''class Person:

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def info(self):
        print(self.name,self.age)

class Employee(Person):

    def __init__(self,name,age,empno,salary,location):
        super().__init__(name,age)
        self.empno=empno
        self.salary=salary
        self.location=location

    def einfo(self):
        print(self.empno,self.salary,self.location)

class Manager(Employee):

    def __init__(self,name,age,empno,salary,location,rights):
        super().__init__(name,age,empno,salary,location)
        self.rights=rights

    def minfo(self):
        print(self.rights)

p=Person("Raju",32)
p.info()

e=Employee("Siva",35,835,50000,"Hyderabad")
e.info()
e.einfo()

m=Manager("Ravi",36,786,45000,"Bangalore","Special")
m.info()
m.einfo()
m.minfo()
'''


# Simple calculator program by using Multilevel Inheritance. . . .

class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def addition(self):
        return (self.a+self.b)

class Calc_1(Calc):
    def substraction(self):
        return self.b-self.a

class Calc_2(Calc_1):
    def division(self):
        return self.b/self.a

class Calc_3(Calc_2):
    def multiplication(self):
        return self.a*self.b


c=Calc_3(20,30)
res=c.addition()
print("The addition of a and b is:",res)
res=c.substraction()
print("The substraction of a and b is:",res)
res=c.division()
print("The division of a and b is:",res)
res=c.multiplication()
print("The multiplication of a and b is:",res)

