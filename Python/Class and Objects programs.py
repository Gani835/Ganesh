
# Displaying output by using Class & Object:-

'''class First():
    def display(self):
        print("I am a display function. . .. . ")


obj=First()
obj.display()'''

# Addition program by using Class :-

class First():
    def __init__(self,a,b):

        self.n1=a
        self.n2=b

    def add(self):
        print(self.n1+self.n2)


obj1=First(10,20)
obj1.add()

# Creating another class. . . .

'''class Second():
    def __init__(self,a,b):

        self.n1=a
        self.n2=b

    def sub(self):
        print(self.n2-self.n1)

obj1=Second(40,60)
obj1.sub()'''

# Get output of first class in second class. . . . .

obj1=First(100,300)
obj1.add()

# Factorial of a number by using class:-

class Factorial():
    def __init__(n):
        def fact(self):
            print(n*fact(n-1))

obj=Factorial(5)
obj.fact()

