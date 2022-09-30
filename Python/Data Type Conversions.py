
                                            ## Data Type Conversions ##

# List to Tuple Conversion. . . .

            # 1) By Using tuple(). . . .

            li=[10,20,30,"ganesh",83.5]
            t=tuple(li)
            print(t)

            # 2) By Using * operator we can expand the list and can be placed in a parenthesis. . . . .

            li=[10,20,30,"ganesh",83.5]
            t=(*li,)
            print(t)


# List to Set Conversion. . . .

            # 1) By Using set() method. . . . .

            li=[10,83.5,"Ganesh",2+3j,True]
            s=set(li)
            print(s)

            # 2) By using Set Comprehension. . . . . .

            li=[10,83.5,"Pravallika",2+3j,False]
            s={i for i in li}
            print(s)

            # 3) By Using For Loop. . . . . . .

            li=[20,83.5,"Srikar",2+3j,True]
            s=set()
            for i in li:
                s.add(i)
            print(s)

            # 4) By Using dict.fromkeys() method. . . . . . .

            li=[60,83.5,"Ganesh",2+3j,False]
            x=list(dict.fromkeys(li))
            y=set(x)
            print(y)

# Set to Dictionary Conversion Methods. . . . .

            # 1) By Using Zip. . . . . .

            set1={"Name","Age","Gender","Location","Salary"}
            set2={"Ganesh",32,"Male","Hyderabad",50000}
            d=dict(zip(set1,set2))
            print(d)

            # 2) By Using .fromkeys(keys,value). . . . . .
            # Keys from set and value given one only.

            set1={"Name","Age","Gender","Location","Salary"}
            d=dict.fromkeys(set1,"No_Value")
            print(d)

            # 3) By using Dictoionary Comprehension. . . . .

            set1={"Name","Age","Gender","Location","Salary"}
            d={element:"No_value" for element in set1}
            print(d)



