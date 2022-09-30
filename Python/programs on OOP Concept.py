# programs on OOPS Concept:-

# 1) To write a program on detailes and marks of the students. .. . . .


class Student:

    SCHOOL_NAME = "V CUBE" 
    
    def __init__(self,name,age,eng_marks,math_marks,tel_marks,hin_marks,sci_marks,soc_marks):

        self.Name=name
        self.Age=age
        self.Eng_Marks=eng_marks
        self.Math_Marks=math_marks
        self.Tel_Marks=tel_marks
        self.Hin_Marks=hin_marks
        self.Sci_Marks=sci_marks
        self.Soc_Marks=soc_marks

    def totalMarks(self):

        return self.Eng_Marks+self.Math_Marks+self.Tel_Marks+self.Hin_Marks+self.Sci_Marks+self.Soc_Marks
    
    def info(self):
        
        print(self.Name,self.Age)

# Object-1

std1=Student("Raju",15,36,43,45,38,49,47)

std1.info()

scl_name=std1.SCHOOL_NAME
print("Name of the school is",scl_name)

tot_marks=std1.totalMarks()
print(f"Total marks obtained by {std1.Name} out of 300 marks are:",tot_marks)

print("")

# Object-2

std2=Student("Siva",14,38,49,42,36,45,48)

std2.info()

scl_name=std2.SCHOOL_NAME
print("Name of the school is",scl_name)

tot_marks=std2.totalMarks()
print(f"Total marks obtained by {std2.Name} out of 300 marks are:",tot_marks)

print("")

# Object-3

std3=Student("Ramu",15,32,46,49,38,41,45)

std3.info()

scl_name=std3.SCHOOL_NAME
print("Name of the school is",scl_name)

tot_marks=std3.totalMarks()
print(f"Total marks obtained by {std1.Name} out of 300 marks are:",tot_marks)




# 2) Finding volume of Cubes. . . . ..  .

class Cube:

    def __init__(self,l,w,h):

        self.length=l           # self.__lenght=l
        self.__width=w            # self.__width=w
        self.height=h           # self.__height=h

    def getvolume(self): 

        volume= self.length*self.__width*self.height
        return volume

# Object-1

obj1=Cube(10,20,25)
vol=obj1.getvolume()
print("The volume of the first cube is:",vol)

# Object-2

obj2=Cube(15,25,30)

obj2.width=20           # NOTE:- instance variables can be modified by anyone at outside
                                 # the object. So we have to give private security to that
                                 # Variables by giving "__" infront of the variable name.
                                 # Like shown above.

vol=obj2.getvolume()    
print("The volume of the second cube is:",vol)








