
class OperatorOverloading:

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def add(self):
        print(self.a+self.b)

    def sub(self):
        print(self.b-self.a)
    
    def mul(self):
        print(self.a*self.b)

    def div(self):
        print(self.b/self.a)

obj=OperatorOverloading(10,20)
obj.add()
obj.sub()
obj.mul()
obj.div()
