
                            ## Anagrams in Strings ##

# Def:- # An anagram of a string is another string that contains same characters,
        # only the order of characters can be different.

def anagram(str1,str2):
    if sorted(str1)==sorted(str2):
        print(" Both strings are Anagram")
    else:
        print("Both strings are not Anagram")
str1="silent"

str2="listen"

anagram(str1,str2)

