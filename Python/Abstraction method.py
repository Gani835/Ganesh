

# Data Abstraction method:- Hiding the data from outside the world.

'''class Animal:
    def sounds(self):
        pass
class Cat(Animal):
    
    def cat_sounds(self):
        print("meyam meyam")

class Dog(Animal):

    def dog_sounds(self):
        print("Bow Bow")

d=Dog()
d.dog_sounds()

c=Cat()
c.cat_sounds()'''


# NOTE:- For example if we create hundreds of animals as child classes
# then we create hundreds of method names. we have to confuse it.
# Thats why for simple calling an object we have to use Data Abstraction method.

# NOTE:- abc method means abstraction base control

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod

    def sounds(self):
        pass

class Cat(Animal):
    def sounds(self):
        print("meyam meyam")

class Dog(Animal):
    def sounds(self):
        print("Bow Bow")

d=Dog()
d.sounds()

c=Cat()
c.sounds()

