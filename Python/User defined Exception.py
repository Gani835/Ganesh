# User_defined Exception:- Here we have to create our own exception by raising the exception.

class NotAllowed(Exception):

    def __init__(self,msg):
        self.msg=msg
try:
    name=input("Enter the name of the student who entered into your class:")
    if name=="Ganesh":
        raise NotAllowed("You are not allowed into the class. . . .")
    else:
        print(f"Hi {name}, How are you?")

except NotAllowed:
    print("You are not allowed into the class. . . .")
