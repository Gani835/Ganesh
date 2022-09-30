                              #### Dictionaries ####

#Def:-

        # Dictionary is a collection of different types of elements as "key:value" pairs.
        # Dictionary doesn't allows duplicate values.
        # We can create a dictionary by using built-in function "dict".
        # Dictionary is a "Mutable" data type. So we can add or delete or modify the key:value pairs.


dict1={"Name":"Gani","Age":32}
dict2={"Gender":"Male"}

# Reading a value from dictionary

print(dict1["Name"])

        #or#

# By using .get() Method

print(dict1.get("Age"))

# dict.get(key[,default]) method:-

dict={'a':54,'b':36,'c':86,'d':69}
value=dict.get('f',0)
print(value)                # It returns default value "0" as we given.

# Adding a new key:value pair

dict1["Wife"]="Pravallika"
print(dict1)

# Replacing/Updating of an key:value pair

dict1["Name"]="Ganesh"
print(dict1)

        # OR #

dict1={'a':54,'b':36,'c':86,'d':69}
dict2={'a':48,'b':72,'c':56,'d':79}
dict1.update(dict2)
print(dict1)            # Values will be changed in dict1 with the values of dict2.

# Deleting of a key:value pair

dict1.pop('Age')        # It removes the key:value pair.
print(dict1)

dict1.popitem()         # It removes the last key:value pair and returns it.
print(dict1)

# clear() method:-

dict={1:"one",2:"two"}
dict.clear()
print(dict)             # It returns an empty dictionary.

# copy() method:-

dict1={1:"one",2:"two"}
dict2=dict1.copy()
print(dict2)            # It copies the key:value paires into dict2.

# dict.keys() method:-

dict={'a':54,'b':36,'c':86,'d':69}
print(dict.keys())          # It returns output like dict_keys in the list form (['a','b','c','d'])

for key in dict.keys():
    print(key)               # It returns only keys. (a,b,c,d in vertically)

# dict.values() method:-

dict={'a':54,'b':36,'c':86,'d':69}
print(dict.values())    # It returns output like dict_values in the list form ([54,36,86,69])

for value in dict.values():
    print(value)        # It returns only values. (54,36,86,69 in vertically)

# dict.fromkeys(sequence[,value]) method:

dictionary=dict.fromkeys(['a','b','c','d'],0)
print(dictionary)       # It returns a dictionary like {'a':0,'b':0,'c':0,'d':0}

# dict.pop(key[,default]) method:-

dict = {'a': 54, 'b': 87, 'c': 61}
value=dict.pop('f',0)
print(value)
print(dict)             # It doesn't throws an error and it returns 0 as output. dictionary doesn't changed

# dict.setdefault(key[,default]) method:-

dict = {'a': 54, 'b': 87, 'c': 61}
value=dict.setdefault('g',36)
print(value)            # It doesn't throws an error and it returns 36 as output. dictionary was change.

print(dict)             # dict = {'a': 54, 'b': 87, 'c': 61,'g':36}

# dict.items() method:-

dict={'a':54,'b':36,'c':86,'d':69}
print(dict.items())     # It returns output like dict_items in the list form ([('a',54),('b',36),('c',86),('d',69)])

for item in dict.items():
    print(item)         # It returns both key and values in a parenthesis individually




    
    



#printing of keys and values

print(dict1.keys())

print(dict1.values())

print(len(dict1))

print(dict1)

#Printing of keys and values by using for loop

for i in dict1.keys():
    print(i)

for i in dict1.values():
    print(i)

for item in dict1.items():
    print(item)
    
    
#print squares of integers between range values in dictionary

output={i:i**2 for i in range(1,11)}
print(output)

#print squares if num is even or cube if num is odd in dictionary

output={i:i**2 if i%2==0 else i**3 for i in range(1,6)}
print(output)













 
