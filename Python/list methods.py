list=[10,"Ganesh",83.5,"Pravallika"]
list2=[10,50,30,70,60,20,40]
list3=[10,20,30,[40,50,60],70,80] # Nested List


                       #List Methods. . . .

# List Comaparisions:-

print(list2==list3)     # O/P ---> False
print(list2<list3)      # o/p ---> False

# Joining lists:-

l1=["apple","banana"]
l2=["Carrot","Mango"]
print(l1+l2)            # O/P ---> ['apple','banana','carrot','mango']]

# List operations:-

li=["Hi"]
print(li*3)             # O/P ---> ['Hi','Hi','Hi']

l1=[10,20]
l2=[30,40]
print(l1+l2)            # O/P ---> [10,20,30,40]

#Adding of an lement (append() method used for adding only one element at once at last position.)

list.append("Srikar")
print(list)

#Inserting of an element (insert() method used to add an element at required position.)

list.insert(2,"Baby")
print(list)

# Updating a list:-

li=[10,20,30,40]
li[3]=100
print(li)               # O/P ---> [10,20,30,100]

# Deleting elements in a list:-

li=[10,30,50,70,90,20,40,60,80]
del li[2]
print[li]               # O/P ---> [10,30,70,90,20,40,60,80]   

del li[2:6]
print(li)               # O/P ---> [10,30,40,60,80]

#Remove an element      (Deleteing an element by using value)

list.remove("Baby")
print(list)

#Popping of an element (Delete an element by using the index position)

li=[10,20,30,40,50]
li.pop()              # By using pop with empty arguments last value in the list will be deleted
print(li)             # O/P ---> [10,20,30,40]

li.pop(2)             # O/P ---> 30 pop will remove the item and returns it.
print(li)

# List Functions and Methods :-
# (index(),append(),extend(),insert(),pop(),remove(),clear(),count(),
# reverse(),sort(),max(),min())

#Indexing of an element

print(list.index("Ganesh"))

#Count of an element    (It gives a value how many times it repeated.)

list.count("Ganesh")

#Sorting of elements in assending oreder.   (arrange the elements in assending order)

list2.sort()
print(list2)

#Reversing of a list    (reverse the order of elements)

list2.reverse()
print(list2)

#Copying of a list

list2.copy()
print(list2)

#Concatenating of two lists

list.append(list2)
print(list)

#Extension of list:-  (extend() method used for adding multiple items into a list)

list.extend("Srikar")
print(list)

#Deleting/Clear the list

list.clear()
print(list)

#Replacing/ Updating of an element

list2[6]=80
print(list2)

#Sum of elements in a list

print(sum(list2))

#printing of maximum value

print(max(list2))

#Printing of a minimum value

print(min(list2))

#Length of a list

print(len(list2))


                                #### Nested List ####


l1=[10,20,[30,40],50,60,[70,80]]
print(type(l1))
print(l1[2][1])



                                    #List Slicing. . .

#Slicing of elements in a list

print(list[1:4])
print(list2)

#Reversing of a list by using slicing

print(list2[-1::-1])


