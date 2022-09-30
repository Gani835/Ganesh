
class MethodOverloading:

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.b-self.a
    
    def mul(self):
        return self.a*self.b

    def div(self):
        return self.b/self.a

obj=MethodOverloading(10,30)
obj.add()
obj.sub()
obj.mul()
obj.div()

