
                        ## Multiple Inheritance ##

# Def:- This inheritance enables a child class to inherit from
      # more than one parent class.

'''# EXAMPLE:- 1

class A:

    def display(self):
        print("I am a display function from claa A")

    def show(self):
        print("I am a show function from class A")

class B:

    def display(self):
        print("I am a display function from class B")    

    def show(self):
        print("I am a show function from class B")


class C(A,B):
    def info(self):
        print("I am a info from class C")

    #pass   # If we give parameters as (A,B) class A display and show functions will printed out.
            # If we give parameters as (B,A) class B display and show functions will printed out.
    
c1=C()
c1.display()
c1.show()
c1.info()

# EXAMPLE:- 2

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def display(self):
        print("I am a display function from class A")

    def info(self):
        print("I am a info function from classs A")

class B:
    def show(self):
        print("I am a show function from class B")

    def display(self):
        print("I am a display function from class B")


class C(A,B):   # If we give parameters as (A,B) class A display and show functions will printed out.
                # If we give parameters as (B,A) class B display and show functions will printed out.

    
    def __init__ (self,d):
        self.d=d

    def info(self):
        print("I am a info function from classs C")

    def display(self):
        print("I am a display function from class c")


c1=C(20)
c1.display()
c1.show()
c1.info()
print(C.mro())

# mro() function gives the priority to this order

# If class=C(A,B)------>
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

# If class=C(B,A)------->
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]'''


# Calling of parent class functions in child class by using A.__init__(self,c) and B.__init__(self,c) keyword without using super().__init__() keyword:-


class A:
    def __init__(self,a):
        self.a=a
    def info(self):
        print(self.a)

class B:
    def __init__(self,b):
        self.b=b
    def show(self):
        print(self.b)

class C(A,B):
    def __init__(self,c):
        self.c=c
        A.__init__(self,c)
        B.__init__(self,c)

    def display(self):
        print(self.c)

c1=C(10)
c1.display()
c1.show()
c1.info()


        

























        
