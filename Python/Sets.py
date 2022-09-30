                            #### Sets ####

#Def:-
        # Sets are the "unordered" collection of different types of values.
        # Sets dont follows the order.
        # Sets dont allows the "Indexing".
        # Sets are "Mutable" that means we can modify the elements.
        # Sets dont allows multiple values.
        
family1={"Ganesh","Pravallika"}
family2={"Srikar","Seetaratnam"}

#Adding an element

family1.add("Srikar")
print(family1)

#Updating of a Set

family1.update(family2)
print(family1)

#Length of a set

print(len(family1))

#Remove of an element from a set

family1.remove("Ganesh")
print(family1)

# discard() method:-

s={20,83.5,"Ganesh"}
s.discard(20)
print(s)            # It removes 20 from the set.
# IF
s.discard("Valli")
print(s)            # It doesn't throw any error even the value not there in the set.


#Popping of a set

family1.pop()       # In sets pop() without an argument, it removes the first value in set.
print(family1)

#Copying of a set

family1.copy()
print(family1)

# Clear method:-

set={10,20,50}
set.clear()
print(set)          # Empty set returns. . . 

####  Set Operations ####

set1={10,20,30,40,10}
set2={20,40,50,60,30}

#Union operation                    # It returns combined values without duplicates.    

print(set1.union(set2))

#Intersection Operation             # It returns only common values in both sets.

print(set1.intersection(set2))

# intersection_update() method:-

s={10,20,30,40,50,60}
s.intersection_update({30,40,70})
print(s)            # O/P ---> {30,40}
                    # it means it compares and returns the common elements.

# Difference Operation

print(set1.difference(set2))        # set1=set1-set2
print(set2.difference(set1))        # set2=set2-set1

# Symmetric_difference() method:- It returns elements without common values

print(set1.symmetric_difference(set2))

# symmetric_diffrence_update() method:- It is as same as symmetric_difference() method.

print(set1.symmetric_difference_update(set2))

# difference_update({iter}):-

s={10,30,50,70}
s.difference_update({10,30})
print(s)     # It removes the parameters we have entered if those are common and
                # returns remaining values in the set.

# isdisjoint() method:-

s1={10,20,30}
s2={40,50,60}
print(s2.isdisjoint(s1))    # It returns "True" when there is no common element in both sets.
                                     # It returns "False" when there is common element is ppresent.
# issubset() method:-

s1={10,20,30}
s2={40,50,60}
print(s2.issubset(s1))  # It returns True is s2 set elements are in s1 set
                                  # It returns False when s2 set elements are not in s1 set.
# issuperset() method:-

s1={10,20,30}
s2={40,50,60}
print(s1.issubset(s2))  # It returns True is s1 set elements are in s2 set
                                  # It returns False when s1 set elements are not in s2 set.

                        
                                ### Type Convertions ###

li=[10,20,30,40,50,10,30,60,"raju",83.5,3+4j]
s=set(li)
print(s)




















