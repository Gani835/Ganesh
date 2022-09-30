class Person:
    def __init__(self,name,age):                # __init__ is a constructor, which is used to assign the values to the object properties.
        self.name=name
        self.age=age

    def info(self):
        print(self.name,self.age)

    def show(self):
        print("I am a show from person class")


print(__name__)

if __name__ == "__main__":
    p2=Person("Ganesh",32)
    p2.info()
    p2.show()

    
