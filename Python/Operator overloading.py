
# Operator Overloading:- # Giving some extra power to the operator to adding the objects.

                         # Operator Overloading means giving extended meaning beyond
                         # their predefined operational meaning. For example operator +
                         # is used to add two integers as well as join two strings and merge
                         # two lists. It is achievable because '+' operator is overloaded by
                         # "int class" and "str class".

# Method Overloading:- # Method overriding in Python is when you have two methods with the
                       # same name that each perform different tasks. This is an important
                       # feature of inheritance in Python. In method overriding, the child
                       # class can change its functions that are defined by its ancestral classes.


class Quantity:

    def __init__(self,qty):
        self.qty=qty

    def __add__(self,other):
        return self.qty+other.qty

    def __gt__(self,other):

        if self.qty>other.qty:
            return True
        else:
            return False

    def __str__(self):
        return str(self.qty)

q1=Quantity(10)
q2=Quantity(20)

print(q1)
print(q2)
print(q1+q2)
print(q1>q2)





