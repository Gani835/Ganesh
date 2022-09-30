
                                        ## Inheritance ##

#Def:- ---> The aquiring of properties of one class(Child class)
            # from another class(Parent class) is called Inheritance.

        # ---> The process of obtaining properties and characterstics
            # (variables and methods) of another class.

# Child class(Sub Class/):- The class which inherits the another class is called child classs.          
# Parent class(Super class/Base class):- Except child class the other class is called parent class.

# Single Inheritance:-
# This type of inheritance enables a subclass or derived class to inherit properties
# and characteristics of the parent class, this avoids duplication of code and improves code reusability.
'''class A:
    def __init__(slef,b):
        self.b=b
        print("I am a constructor from class A")
    def display(self):
        print("I am a display from class A",self.b)

class B(A):
    def __init__(self,a):
        self.a=a
        print("I am a constructor from class B")
        super().__init__(a)
    def display(self):
        print("I am a display from class B",self.a)

b=B(20) 
b.display()
'''


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def pinfo(self):
        print(self.name,self.age)

class Employee(Person):
    def __init__(self,name,age,empno,salary):
        super().__init__(name,age)
        self.empno=empno
        self.salary=salary

    def einfo(self):
        print(self.empno,self.salary)

obj=Employee("Ganesh",32,835,50000)
obj.pinfo()
obj.einfo()

class Farmer(Person):
    def __init__(self,name,age,village):
        super().__init__(name,age)
        self.village=village

    def finfo(self):
        print(self.village)
obj=Farmer("Ganesh",32,"Koyyalagudem")
obj.finfo()


