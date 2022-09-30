                                ##### Tuple #####

tup=(10,"Ganesh",83.5,"Pravallika")
tup2=(10,30,70,60,40,50,20)
tup3=(10,20,30,(40,50,60),70,80) # (Nested Tuple)

# NOTE:-

# Packing:- Creating a tuple from a set of values is called Packing.
# and its reverse that is creating individual value from tuples elements is called Unpacking.

t1=(100,200,300,400)
a,b,c,d=t1
print(a)    # O/P ---> 100
print(b)    # O/P ---> 200
print(c)    # O/P ---> 300
print(d)    # O/P ---> 400

# Type Convertions:-

# String to Tuple. . . . 

t=tuple("python")
print(t)            # O/P ---> ('p','y','t','h','o','n')

# List to Tuple. . . .

li=[10,"Ganesh",83.5]
t=tuple(li)
print(t)            # O/P ---> (10,'Ganesh',83.5)

# Dictionary to tuple. . . .

tup=tuple({1:"name",2:"age"})
print(tup)          # O/P ---> (1,2)  It returns only key values from dictionary

#NOTE:-

    # Tuples are immutable data types.
    # We can't add or remove an element in tuple.
    # We can do slicing and indexing only in Tuple Methods:



# Comparing the tuples:-

a=(10,20,30)
b=(30,40,20)
print(a==b)            # O/P ---> False

# Indexing of a tuple

print(tup.index("Ganesh"))
print(tup[0])
print(tup[-1])


# Slicing of a tuple

print(tup[1:4])
print(tup[1:])
print(tup[:4])

# Reversing of elements in tuple

print(tup[-1::-1])

# Length of tuple

print(len(tup2))

# Maximum value of a tuple

print(max(tup2))

# Minimum value of a tuple

print(min(tup2))

# Sum of elements in a tuple

print(sum(tup2))

# Sorting of elements in a tuple

print(sorted(tup2))

li=[50,60]
tup=(10,20,[30,40])
print(type(tup))

# Count Method

print(tup.count(10))

# length of tuple:-

t=(10,"Ganesh",83.5)
print(len(t))        # O/P ---> 3

# Operators in tuple:-

t1=(10,20,30)
t2=('a','b','c')
t3=t1+t2
print(t3)            # O/P ---> (10,20,30,'a','b','c')

t1=("DO","IT","FAST")
print(t1*3)          # O/P ---> ('DO','IT','FAST','DO','IT','FAST','DO','IT','FAST')     


'''
